# Adversarial Critique: AI Scalping Agent Research

## Overview
14-point critique of `index.md` following Phase 6 methodology. Each issue rated Severity 1-5 (5=critical).

---

## Findings

### 1. Over-reliance on HFT/Latency Frame [Severity 4]
The report frames scalping almost exclusively through the HFT lens — FPGA, colocation, kernel bypass. A genuine scalping agent for retail/mid-frequency traders would emphasize pattern recognition, risk management, execution quality, and broker API nuances. The institutional HFT focus risks alienating the actual target audience. **Missing: mid-frequency scalping strategies (1-60 min holding), retail broker API performance, pattern day trading rules.**

### 2. Absence of Counterevidence Register [Severity 3]
The validator flagged missing Counterevidence and Claims-Evidence sections. There is no dedicated space documenting contradictory findings or studies that challenge the report's thesis (e.g., academic papers showing retail scalping is unprofitable net of fees, or evidence that ML-based scalping underperforms simple mean-reversion). **Missing: at least one counterexample per finding.**

### 3. Slippage and Transaction Cost Understatement [Severity 4]
Citations mention latency costs (~$100M/ms for HFT) but do not adequately address **slippage** for a $10K-$100K retail account, which dominates costs at lower frequencies. Bid-ask spread, market impact, commission structure, and SEC Section 31 fees are mentioned in passing but never quantified. **Missing: realistic P&L model showing slippage impact at various account sizes.**

### 4. Overclaiming on ML Predictive Power [Severity 3]
Finding 3 claims microstructure + sentiment + TA yields "actionable alpha" with FinBERT and XGBoost. The literature is mixed: most academic studies show ML signal decays rapidly post-publication. The report should caveat that public-domain ML signals are likely arbitraged away. **Missing: decay curve data, publication bias discussion.**

### 5. Regulatory Analysis is U.S.-Centric [Severity 3]
MiFID II tick-size regimes and the EU's 500ms quote-hold are mentioned but never applied to system design. The report gives the impression that the U.S. regulatory framework (SEC, FINRA) is the default. A global scalping agent must handle radically different market structures (e.g., China's T+1 settlement, India's STT, Europe's dark pool caps). **Missing: regulatory feature matrix for top 5 markets.**

### 6. Backtesting Claims Need Qualification [Severity 4]
Finding 6 compares backtesting frameworks but does not address survivorship bias, look-ahead bias, or overfitting at any depth. Walk-forward validation and out-of-sample tests are mentioned in one paragraph. Given that 90%+ of backtested scalping strategies fail live, this deserves a dedicated subsection. **Missing: overfitting detection protocol, out-of-sample methodology.**

### 7. Cost Estimates Are Superficial [Severity 3]
Finding 6's cost comparison ($500-$5M) is too wide to be actionable. No breakdown of: cloud compute vs colocation, data feed costs (OPRA, direct exchange), regulatory/compliance staffing, legal entity setup, or ongoing maintenance. **Missing: tiered budget table (lean/standard/enterprise).**

### 8. Alternative Data Section Lacks ROI Data [Severity 3]
Finding 5 catalogs alt-data types but never answers the question: *Does alt-data generate net positive alpha for a scalping agent, after accounting for acquisition, processing, and signal decay costs?* The literature suggests most alt-data has negative ROI for short-horizon strategies. **Missing: ROI analysis per alt-data category.**

### 9. No Discussion of Sequence/Timing of Build [Severity 3]
The report presents components independently but never provides a build sequence. What should be built first? What is the MVP? The implied timeline (12-36 months) is stated without a phased roadmap. **Missing: build roadmap with milestones.**

### 10. Persona Bias: Institutional Trader Default [Severity 2]
The report implicitly addresses a quant at a prop shop or hedge fund. Language like "co-location agreement," "direct market access," "FPGA team" assumes organizational resources. The user's background suggests a solo/small-team context. **Missing: solo-dev adaptation guide.**

### 11. Evidence JSONL Is Empty [Severity 4]
Per schema requirements, each cited claim should trace to evidence entries. Currently `evidence.jsonl` is empty. Without evidence traces, claim verification is manual and non-reproducible. **Action: populate evidence.jsonl with entries matching cited claims.**

### 12. Persona Critique: Skeptical Practitioner
*"I've done this for 10 years. Your Finding 3 makes ML sound like a silver bullet. Show me one real strategy that beats a simple 20-tick chart with VWAP bands. Your cost numbers are 2-5x too low for a real setup, and 2-5x too high for a hobbyist. Pick a lane."*
**Implication:** The report tries to cover too broad a spectrum (hobbyist to institution). Better to explicitly target one archetype.

### 13. Persona Critique: Adversarial Reviewer
*"Citation [88] and [89] appear to be blog posts, not peer-reviewed sources. Finding 4 mixes original research and secondary reporting without distinction. The 2023-2026 range is thin for a field that changes yearly. Several claims lack a supporting citation entirely."*
**Implication:** Need to distinguish primary/secondary sources and add recent (2025-2026) academic references.

### 14. Persona Critique: Implementation Engineer
*"You mention Kafka as a 'backbone' but don't address Kafka operational complexity (ZooKeeper/KRaft, partitioning strategy, exactly-once semantics). PGVector is listed as a vector DB but has terrible performance at scale. The architecture diagram has no network topology, no security boundaries, no disaster recovery."*
**Implication:** Architecture section needs operational detail or a disclaimer that detailed deployment is out of scope.

---

## Priority Fixes (Phase 7)
1. Populate `evidence.jsonl` (Severity 4)
2. Add Counterevidence paragraph per finding (Severity 3)
3. Add realistic slippage/cost quantification (Severity 4)
4. Add overfitting/backtesting integrity subsection (Severity 4)
5. Add build roadmap + solo-dev adaptation (Severity 3)
6. Distinguish primary vs secondary sources (Severity 2)
