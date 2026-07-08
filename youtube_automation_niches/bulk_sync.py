#!/usr/bin/env python3
"""Bulk register missing sources & populate evidence from index.md"""
import json, os, re, sys, hashlib
from datetime import datetime, timezone
from pathlib import Path

DIR = Path("/home/ed/research/youtube_automation_niches")
REPORT = DIR / "index.md"
SOURCES = DIR / "sources.jsonl"
EVIDENCE = DIR / "evidence.jsonl"

def canonicalize_url(raw):
    from urllib.parse import urlparse, urlunparse
    TRACKING = frozenset(['utm_source','utm_medium','utm_campaign','utm_term','utm_content','ref','source','fbclid','gclid','mc_cid','mc_eid'])
    parsed = urlparse(raw)
    scheme = (parsed.scheme or 'https').lower()
    host = (parsed.hostname or '').lower()
    path = parsed.path.rstrip('/')
    if parsed.query:
        pairs = []
        for part in parsed.query.split('&'):
            kv = part.split('=',1)
            if kv[0].lower() not in TRACKING:
                pairs.append(part)
        query = '&'.join(sorted(pairs))
    else:
        query = ''
    return urlunparse((scheme, host, path, '', query, ''))

def source_id(canonical):
    return hashlib.sha256(canonical.encode('utf-8')).hexdigest()[:16]

def read_jsonl(path):
    rows = []
    if path.exists():
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line: rows.append(json.loads(line))
    return rows

def append_jsonl(path, obj):
    with open(path, 'a') as f:
        f.write(json.dumps(obj, ensure_ascii=False) + '\n')

def main():
    # 1. Parse bibliography from report
    content = REPORT.read_text()
    bib_match = re.search(r'## Bibliography(.*?)(?=##|\Z)', content, re.DOTALL)
    if not bib_match:
        print("ERROR: No Bibliography section")
        sys.exit(1)
    
    bib_text = bib_match.group(1)
    
    entries = []
    for m in re.finditer(r'^\[(\d+)\]\s+(.+?)$', bib_text, re.MULTILINE):
        num = int(m.group(1))
        rest = m.group(2)
        # Extract URL
        url_m = re.search(r'https?://[^\s\)\]]+', rest)
        # Extract title
        title_m = re.search(r'"([^"]+)"', rest)
        # Extract year
        year_m = re.search(r'\((\d{4})\)', rest)
        entries.append({
            'num': num,
            'raw': rest,
            'url': url_m.group(0) if url_m else '',
            'title': title_m.group(1) if title_m else rest[:80],
            'year': int(year_m.group(1)) if year_m else 2026
        })
    
    print(f"Found {len(entries)} bibliography entries")
    
    # 2. Load existing sources
    existing = read_jsonl(SOURCES)
    existing_ids = {s['source_id'] for s in existing}
    existing_urls = {s['canonical_locator'] for s in existing}
    
    # 3. Register missing sources
    registered = 0
    skipped = 0
    for e in entries:
        if not e['url']:
            skipped += 1
            continue
        canonical = canonicalize_url(e['url'])
        sid = source_id(canonical)
        if sid in existing_ids or canonical in existing_urls:
            skipped += 1
            continue
        
        source_type = 'industry_blog'
        if 'youtube.com' in e['url'] or 'youtu.be' in e['url']:
            source_type = 'video'
        elif 'support.google.com' in e['url'] or 'support.google' in e['url']:
            source_type = 'official_documentation'
        elif 'techcrunch.com' in e['url'] or 'mashable.com' in e['url'] or 'thenextweb.com' in e['url']:
            source_type = 'news_article'
        elif 'air.io' in e['url']:
            source_type = 'industry_analysis'
        elif 'tubevertex.com' in e['url']:
            source_type = 'vendor_blog'
        elif 'medium.com' in e['url']:
            source_type = 'community_post'
        elif 'businessinsider.com' in e['url']:
            source_type = 'news_article'
        
        row = {
            'source_id': sid,
            'canonical_locator': canonical,
            'raw_url': e['url'],
            'title': e['title'],
            'authors': None,
            'year': e['year'],
            'source_type': source_type,
            'metadata_status': 'unverified',
            'registered_at': datetime.now(timezone.utc).isoformat()
        }
        append_jsonl(SOURCES, row)
        existing_ids.add(sid)
        existing_urls.add(canonical)
        registered += 1
    
    print(f"Registered {registered} new sources, skipped {skipped} (duplicates or no URL)")
    
    # 4. Populate evidence.jsonl from key claims
    evidence_rows = read_jsonl(EVIDENCE)
    existing_evidence_ids = {r['evidence_id'] for r in evidence_rows}
    
    # Extract findings with citations
    claims = []
    for m in re.finditer(r'^(\d+)\.\s+(.+?)(?:\n|$)', content, re.MULTILINE):
        num = int(m.group(1))
        text = m.group(2).strip()
        # Extract citation numbers
        cites = re.findall(r'\[(\d+)\]', text)
        if cites and num <= 148:
            claims.append({'num': num, 'text': text, 'cites': cites})
    
    print(f"Found {len(claims)} numbered claims with citations")
    
    evidence_added = 0
    for c in claims:
        # Map claim citations to source_ids
        for cite_num in c['cites'][:3]:  # Use first 3 citations max
            # Find entry with this bib number
            entry = next((e for e in entries if e['num'] == int(cite_num)), None)
            if not entry or not entry['url']:
                continue
            canonical = canonicalize_url(entry['url'])
            sid = source_id(canonical)
            if sid not in existing_ids:
                continue
            
            # Compute evidence_id
            quote = c['text'][:200]
            normalized = re.sub(r'\s+', ' ', quote.strip()).lower()
            payload = sid + normalized + f"finding_{c['num']}"
            eid = hashlib.sha256(payload.encode('utf-8')).hexdigest()[:16]
            
            if eid in existing_evidence_ids:
                continue
            
            row = {
                'evidence_id': eid,
                'source_id': sid,
                'retrieval_query': f"YouTube automation niche finding {c['num']}",
                'locator': f"finding_{c['num']}",
                'quote': c['text'],
                'evidence_type': 'paraphrase',
                'captured_at': datetime.now(timezone.utc).isoformat()
            }
            append_jsonl(EVIDENCE, row)
            existing_evidence_ids.add(eid)
            evidence_added += 1
    
    print(f"Added {evidence_added} evidence entries")
    print(f"Total sources: {len(existing_ids)}, Total evidence: {len(existing_evidence_ids) + evidence_added}")

if __name__ == '__main__':
    main()
