## Research Topic: AI Agent Flyer Design Skill - Optimal Architecture for 2026

## Integrated Findings (8 sources processed)

### Core Engine Comparison

**Text Rendering Accuracy:**
- Ideogram 3.0: 90-95% (best-in-class) [1]
- GPT Image 2: 95%+ including non-Latin scripts (Japanese, Korean, Chinese, Hindi, Bengali) [3]
- Midjourney V7: 30-40% [1]
- Midjourney V8 Alpha: ~58% [1]
- All others (DALL-E, SD, Firefly): hover around 30-50% [1]

**Verbatim quote:** "Ideogram doesn't just get the letters right — it understands typeface context. Ask for a hand-lettered chalk menu and you get chalk textures, natural baselines, and correct spelling. No other model does that consistently." — pxz.ai [1]

**Poster-specific insight:** GPT Image 2's best case is posters — "headlines land on the correct baseline, kerning is believable, small caps render as small caps rather than as numerals, and specified date-and-venue lines come through readable rather than as decorative noise" [5]. This is a "practical shift in the workflow, not a marketing claim: a designer can now use the model for client comps and internal concept reviews instead of treating its output as mood-board filler that gets rebuilt by hand."

**Artistic Quality:**
- Midjourney V7/V8: Industry-leading, cinematic aesthetic (expert panel rating 92/100) [1]
- Ideogram 3.0: Good for commercial photography (78/100) [1]
- GPT Image 2: Strong for editorial/commercial, Thinking Mode for composition [3]

**Generation Speed:**
- Midjourney V8: ~5-10s (5x faster than V7) [1]
- Ideogram 3.0: ~8-15s [1]
- GPT Image 2: varies by quality tier [3]

### Pricing Landscape
- Free tiers: Ideogram (10 prompts/day), Canva (limited), GPT Image 2 (basic free in ChatGPT) [1][3][4]
- Entry paid: Ideogram $7/mo, Midjourney $10/mo, Canva Pro $12.99-$15/mo, GPTImager $9.95/mo [1][4]
- Pro: Ideogram $48/mo, Midjourney $60/mo, Canva Teams $14.99/seat/mo [1][4]
- API pricing: GPT Image 2 $0.01-$0.41/image depending on quality/resolution [3]
- Annual discounts: Ideogram ~40% off vs Midjourney ~20% off [1]

### Architectural Approaches

**Template-First (Canva Magic Studio):**
- Full design workflow with brand kits, templates, asset libraries [4]
- Magic Design generates complete layouts from prompts
- Brand Kit guardrails enforce colors, fonts, logos [4]
- Magic Switch translates to 150+ languages preserving layout [4]
- 260M+ monthly active users, 10B+ AI tool uses [4]
- Canva Pro $15/mo includes 500 AI credits + free Affinity design suite [4]
- Catch: "A lot of AI design tools feel like vending machines. Canva flips that" [4]
- Weakness: AI-generated images can look generic; template-native feel [4]

**Image-Generation-First (GPT Image 2, Ideogram, Midjourney):**
- GPT Image 2: Thinking Mode reasons through composition before rendering; accepts 16 reference images; 4K output; web search during generation [3]
- Ideogram 3: API-first approach with REST API, Canvas editor with inpainting/outpainting [1]
- Midjourney V8: Personalization profiles learn user preferences; 26.8% global market share; $500M revenue (2025) [1]

**Code-First (Claude Design, Figma):**
- Figma AI: design features for flyers (not yet robust enough as standalone)
- Claude Design: brand kit template system (limited for print flyers)

### Prompt Engineering Framework
Best practice structure from multiple sources [2][3][6]:
1. Subject + adjectives
2. Scene/background
3. Lighting (cinematography terms like Rembrandt, chiaroscuro)
4. Camera angle/composition (85mm, 35mm, rule of thirds)
5. Style/medium
6. Exact text in quotes + typography specifications
7. Constraints (no extra text, preserve list for edits)

**Key GPT Image 2 prompting rules [2][6]:**
- Be specific, not abstract (describe what you see, not how you feel)
- Put exact text in quotes
- Use photography language (50mm lens, soft window light)
- For edits, say what must not change (preserve list)
- Reuse a style block for consistency
- Start simple, then iterate

**Poster prompt best practices [5]:**
- Open with poster category (movie, concert, travel, vintage ad)
- Name the hero element (one hero only)
- Describe typography with decade and classification
- Write actual text content verbatim in quotes
- Specify composition by pattern (centered, rule-of-thirds, grid-based)
- Give color palette as named colors or hex values
- Close with medium reference (screen-printed, offset, risograph)
- Include negative prompts: "no lorem ipsum, no garbled text, no duplicate title, no watermark"

### Brand Consistency Strategies
- Canva: Brand Kit with colors, fonts, logos applied before generation [4]
- Midjourney: Personalization profiles learn preferences over time; style consistency 89/100 [1]
- Ideogram: Style References (up to 3 images); Random Style from 4.3B presets; consistency 85/100 [1]
- GPT Image 2: Up to 16 reference images for edits; reusable style blocks [3]

### Print Production Readiness
- Canva: Print-ready PDF exports, CMYK support, bleed settings [4]
- Recraft: Exports 300 DPI CMYK (mentioned in search results)
- GPT Image 2: 4K output, no transparent PNG support yet [3]
- Ideogram: 1024x1024 default with upscaling [1]
- Midjourney: Native 2K via --hd parameter [1]

### API & Developer Integration
- Ideogram: Public REST API, pay-as-you-go, 10 concurrent requests; maturity score 82/100 [1]
- Midjourney: Invite-only API (limited); maturity score 28/100 [1]
- GPT Image 2: OpenAI API, $0.01-$0.41/image [3]
- Canva: API available for developers [4]

### CJK/Multilingual Support
- GPT Image 2: 95%+ accuracy for Japanese, Korean, Chinese, Hindi, Bengali [3]
- Qwen-Image: Best for Chinese text (mentioned in earlier searches)
- Ideogram 3.0: Strong English/Latin text, limited CJK
- Midjourney: Poor non-Latin text rendering

### Weakest Evidence
- GPT Image 2's 95%+ multilingual claim from atlabs.ai (marketing blog, not independent test) [3]
- Midjourney 26.8% market share from DemandSage (may be estimated) [1]
- Canva "260M users" from Canva newsroom (self-reported) [4]
- Poster prompts guide from gptimager.com (vendor site for GPTImager product) [5]

### Key Gaps / Unanswered Questions
- Print-specific CMYK workflows across tools (limited data)
- Batch processing at scale (partial - Canva API, Ideogram API)
- Geographic variation in tool adoption
- Cost per thousand flyers at production scale
- Long-term brand consistency across thousands of assets
- Vector/logotype export for professional printing
- Color management (ICC profiles, spot colors)
