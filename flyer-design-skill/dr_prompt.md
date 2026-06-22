# DEEP RESEARCH COMMISSION

## Research Question
What constitutes the single best "AI agent flyer design skill" — meaning the optimal combination of AI tools, prompt engineering frameworks, design knowledge, and workflow patterns that produce professional-quality flyers when executed by an AI agent in 2026?

## Purpose & Context
This research aims to define the ideal specification for an AI agent skill (comparable to the opencode skill system) that enables an AI coding agent to design and generate high-quality flyers autonomously. The skill must cover: which AI image generation model to use, what prompt engineering structure yields consistent results, what design principles (typography, layout, color, hierarchy) the agent must encode, what print/digital technical specs matter, and how to handle brand consistency across outputs.

The distinction this research must answer: is the best "skill" a GPT Image 2 prompt library, a Canva API integration, a Midjourney workflow, an HTML/CSS flyer generation approach (like Claude Design), or a hybrid strategy? What does the winning architecture look like?

### Audience
- **Primary**: AI agent developers and prompt engineers building specialized agent skills for visual content creation. They need actionable specifications, not theory.
- **Secondary**: Marketers and non-designers who want AI agents to produce professional flyers for them. They need to understand what's possible and what to demand.
- **Tone**: Technical and precise where needed, but always grounded in practical application. Expert-level vocabulary with inline child-level explanations for design concepts.
- **Complexity**: Moderate — assumes familiarity with AI image generation but no formal design background.
- **Child-reader adaptivity**: Every design term (hierarchy, kerning, bleed, etc.) gets an inline [imagine: ...] explanation.

### Decision Context
- What tool/approach should be the CORE engine of an AI agent flyer design skill?
- What prompt engineering framework produces the most reliable results?
- What design knowledge must the skill embed vs. offload to the model?
- What validation/QA process ensures the output is actually usable?
- This research will directly determine the architecture of a flyer-design skill for the opencode agent ecosystem.

## Research Scope

### In Scope
1. All major AI image generation models usable for flyer design in 2026 — GPT Image 2, Midjourney V6/V7, DALL-E 3, Adobe Firefly, Stable Diffusion, Ideogram
2. AI-powered design platforms with APIs — Canva AI, Adobe Express, Claude Design, Figma AI, Kodo
3. Prompt engineering frameworks specific to flyer/poster/brochure generation
4. Design knowledge requirements: layout, typography, color theory, visual hierarchy, branding, CTA placement
5. Print vs. digital flyer technical specifications (DPI, bleed, margins, color spaces)
6. Evaluation criteria: How to judge whether a flyer design is "good"
7. Integration patterns: How an AI agent would invoke these tools programmatically
8. Real user sentiment: What actual users (not companies) say works best for them

### Out of Scope
1. Video or animation flyers (digital motion graphics)
2. Hand-coding flyers from scratch in HTML/CSS as primary approach (only as comparison point)
3. Traditional design software without AI features (Photoshop/Illustrator manual workflows)
4. Flyer distribution/printing logistics
5. AI logo/brand identity generation as standalone topic (only as part of flyer creation)
6. 3D or VR flyer formats

### Timeframe
2024-2026 with emphasis on April-June 2026 (post-GPT Image 2, post-Canva AI 2.0, post-Claude Design launches)

### Geographic Focus
Global perspective with attention to regional differences in tool availability (US, EU, Asia)

## Required Dimensions of Investigation

Each dimension must be investigated from multiple angles and reported with specific evidence:

1. **Technical/Mechanistic Exploration**
   - How does GPT Image 2's reasoning-before-generation architecture enable multi-constraint flyer prompting? What are its actual limitations in text rendering for different languages?
   - How do Midjourney V7's prompt fidelity improvements affect flyer-specific generation?
   - What are the API capabilities of Canva AI vs Adobe Express vs Claude Design for programmatic flyer creation?
   - How does Ideogram's text rendering compare to GPT Image 2 for flyer use cases?
   - What is the actual resolution/output quality ceiling of each tool for print-ready flyers?

2. **Historical Context & Evolution**
   - How did AI flyer design evolve from 2023 (DALL-E 2 era, unusable text) to 2026 (GPT Image 2 with near-perfect text)?
   - What were the key breakthroughs: reasoning models, text rendering, multi-constraint handling?
   - How did Canva's transition from template-only to AI-native (Magic Studio, Canva AI 2.0) change the landscape?
   - When did "the brief is the design" paradigm emerge and what drove it?

3. **Current State-of-Art (June 2026)**
   - What are the leading AI flyer generation approaches RIGHT NOW, ranked by output quality?
   - What is Claude Design's approach (reads brand codebase, returns live HTML) and how does it compare to image-based approaches?
   - What launched recently (Figma AI Design Agent May 2026, Canva AI 2.0, Claude Design)?
   - Which approach yields the best flyer output for an AI agent to produce autonomously?

4. **Quantitative Evidence**
   - Comparative benchmark data: tool speed, output resolution, text accuracy, brand consistency
   - Pricing comparison: API costs per 1000 flyers for each approach
   - Market share/adoption: which platforms have the most users for flyer design
   - Quality scores: user ratings on G2/Capterra/Trustpilot for each tool in "flyer creation" use case
   - Failure rates: how often does each tool produce unusable text or broken layouts

5. **Stakeholder Analysis**
   - OpenAI (GPT Image 2) — what are their priorities, API terms, commercial usage rights
   - Canva — their agentic OS strategy, Brand Intelligence, API availability
   - Adobe — Firefly commercial safety argument, Creative Cloud lock-in
   - Anthropic (Claude Design) — differentiator: reads codebase, returns HTML, not images
   - Midjourney — independent, Discord-first, highest image quality
   - Figma — beta AI Design Agent, native design environment
   - Open-source community — Stable Diffusion fine-tunes for flyers

6. **Competing Approaches Comparison**
   - Image-generation-first (GPT Image 2 prompt → flyer image) vs. template-first (Canva API → template customization) vs. code-first (Claude Design → HTML flyer)
   - Single-model approach vs. hybrid pipeline (Midjourney for background + GPT for text overlay)
   - Cloud API approach vs. local inference (Stable Diffusion)
   - Prompt library approach vs. structured API approach

7. **Criticisms & Limitations**
   - What do actual users complain about with each tool for flyer creation? (Reddit, HN, Trustpilot, G2)
   - Text rendering failures: which tools still struggle, for which languages, in which contexts
   - Commercial use concerns: copyright, training data, IP indemnification
   - Consistency problems: maintaining brand identity across multiple flyers
   - Print-readiness issues: resolution, color space, bleed handling
   - Cost barriers for high-volume production

8. **Contrarian & Heterodox Perspectives**
   - Are AI-generated flyers actually effective for marketing, or do they all look the same? What evidence exists?
   - Is the "prompt-to-flyer" paradigm a dead end? Would a different interface (constraint-based, like CSS) produce better results?
   - Are dedicated AI flyer tools (Pixazo, Flyerwiz) actually worse than general-purpose AI image generators for flyers?
   - Does the Claude Design HTML approach produce more usable output than image generation? What are real user testimonials?

9. **Future Trajectories & Predictions**
   - Where is AI flyer generation heading in 2027-2028: real-time 3D flyers, video flyers, interactive HTML?
   - Will text rendering become a solved problem for all models?
   - Will brand consistency and design systems become automated (AI understands your brand and never deviates)?
   - What happens when AI agents can directly manipulate Figma/Canva files programmatically?
   - Will prompt engineering become obsolete as models improve, or will "prompt literacy" become a lasting skill?

10. **Regulatory, Legal & Ethical Dimensions**
    - Copyright status of AI-generated flyers: US Copyright Office rulings, what can/cannot be copyrighted
    - Commercial use licensing: which tools offer IP indemnification, which don't
    - Training data ethics: which models trained on designer work without consent
    - Impact on graphic designers: job displacement vs. productivity enhancement
    - Accessibility requirements: WCAG compliance for digital flyers

11. **Geographic & Geopolitical Variation**
    - Tool availability by region: Canva blocked in China, local alternatives
    - Language support: which tools handle non-Latin scripts (CJK, Arabic, Devanagari) for flyer text
    - Pricing differences: tool cost by region (e.g., Canva Pro in India at ₹3,999/year vs $119.99/year US)
    - Regional design aesthetic preferences: East Asian vs European vs North American flyer conventions

12. **Practical Applications & Case Studies**
    - AI agent flyer generation in practice: startups using Kodo for design, Canva API for bulk marketing, etc.
    - Real-world examples of AI-generated flyers that actually drove results (conversion rates, engagement)
    - How agencies are incorporating AI flyer tools into their workflows
    - Implementation patterns: what does a production AI flyer pipeline look like end-to-end

13. **Public Opinion, User Sentiment & Social Proof**
    - What do real users (not companies) say on Reddit/Hacker News/X/YouTube about each tool for flyer design?
    - What do users report as working best, what they like most, and what they commonly complain about?
    - What does the general public seem to prefer or recommend across different communities?
    - What is the consensus vs. divergence: which tool wins for which use case, according to actual users?

## Source Requirements

### Source Types Required (ALL must be represented)
- Academic/peer-reviewed research (design theory, HCI, AI image generation papers)
- Industry analysis (Gartner, Forrester reports on AI creative tools)
- Technical documentation (OpenAI API docs, Canva API docs, Adobe Firefly docs, Anthropic Claude Design docs)
- News/current events (TechCrunch, The Verge coverage of 2026 AI design tool launches)
- Primary sources (official product announcements, changelogs, API reference)
- Expert commentary (design blogs, AI newsletters, practitioner analyses)
- Contrarian/critical sources (failure postmortems, critical takes on AI design quality)
- Personal & user-reported sources (Reddit r/advertising, r/Design, r/graphic_design, r/ChatGPT, Hacker News discussions, X/Twitter threads, G2 reviews, Capterra reviews, Trustpilot reviews, YouTube reviews/tutorials)

### Minimum Source Count: 216+
Level 1 initial sources should aim for >=216 relentlessly. Multi-level BFS expansion (following links/references/ideas from each source to generate further sources, iteratively) is used only when Level 1 falls short.

### Source Diversity Requirements
- At least 4 different source types must be represented
- Mix of recent (2025-2026) and foundational (pre-2025) sources
- Both proponents AND critics must be cited
- Geographic diversity (not US-only)
- If a source type is unavailable, document the gap

## Output Requirements

### Report Structure
1. Executive Summary (1000-1500 words) — synthesize ALL major findings, patterns, implications, and recommendations upfront. This is the most important section.
2. Introduction — scope, methodology, assumptions, key terms defined with ELI5 explanations
3. Main Analysis (6-10 findings, 600-2,000 words each, with evidence)
   - Finding 1: The AI Flyer Design Tool Landscape (June 2026)
   - Finding 2: GPT Image 2 vs. Midjourney vs. Firefly vs. Claude Design — Head-to-Head for Flyers
   - Finding 3: The Prompt Engineering Framework for Reliable Flyer Generation
   - Finding 4: Design Knowledge Encoding — What the Agent Must Know
   - Finding 5: Print vs. Digital — Technical Specifications That Matter
   - Finding 6: Commercial, Legal & Ethical Considerations
   - Finding 7: User Sentiment & Real-World Results
   - Finding 8: The Optimal AI Agent Flyer Design Skill Architecture
4. Synthesis & Insights — cross-cutting patterns, novel connections
5. Recommendations — actionable guidance for building an AI agent flyer design skill
6. Complete Bibliography — every citation [1]-[N], no placeholders
7. Methodology Appendix — research process, verification, confidence levels
8. Weakest Evidence — 3 claims least well-supported, with explanation

### Quality Mandates
- EVERY factual claim followed by [N] citation in the same sentence
- No vague attributions ("research shows", "experts believe", "studies suggest")
- Distinguish facts FROM sources vs. your own synthesis explicitly
- For speculative content, label as "This suggests..." not "Research shows..."
- Minimum 3 independent sources per major claim
- Prose >=80%, bullets sparingly (only for distinct lists)
- No placeholder text, no "content continues", no ranges in bibliography
- Admit uncertainty: "No sources found for X" rather than fabricating
- **Distinguish evidence classes explicitly**: label every claim as one of 'vendor-sourced' (marketing, press releases, company statements), 'user-reported' (reviews, forum posts, social media, testimonials, surveys, interviews), or 'expert/third-party' (analyst reports, academic research, independent journalism). Never blend vendor claims with independent evidence without flagging.
- **End with a "Weakest Evidence" section** listing the 3 claims least well-supported by the source base. This forces a self-audit and tells the reader exactly what to verify by hand.

### Bias Safeguards
- Actively seek sources that contradict initial findings
- Flag when sources have financial or ideological interests
- Note when research is sparse — don't fill gaps with speculation
- Distinguish correlation from causation
- Mark predictions/forecasts as [SPECULATION] not [FACT]

### Child-Reader Adaptivity (Gate 4)
- Every design term (visual hierarchy, kerning, bleed, DPI, CMYK, color space, typographic contrast, brand kit, call-to-action, etc.) must have an inline [imagine: ...] explanation
- Example: "visual hierarchy [imagine: arranging information so your eye knows what to look at first, like a headline being big and bold, then smaller details below]"
- Example: "bleed [imagine: printing extends past the edge where the paper will be cut, so there's no white border]"

## Seed Keywords

**Core terms**: AI flyer design, AI poster generator, AI agent design skill, AI flyer maker, prompt-to-flyer

**Model-specific**: GPT Image 2, gpt-image-2, ChatGPT Images 2.0, Midjourney V7, DALL-E 3, Adobe Firefly, Stable Diffusion, Ideogram, Flux

**Platform-specific**: Canva AI 2.0, Canva Magic Studio, Canva Brand Intelligence, Adobe Express, Adobe Firefly AI Assistant, Claude Design, Figma AI Design Agent, Kodo AI design, Pixazo, Venngage, Visme, PosterMyWall, Piktochart, VistaCreate, Kittl, Flyerwiz

**Technical terms**: text-to-image prompt engineering, multi-constraint prompting, reasoning-before-generation, brand kit integration, auto-resize, print-ready export, 300 DPI, CMYK, bleed, safe margins

**Prompt engineering**: flyer prompt template, ChatGPT image prompting guide 2026, AI flyer prompt structure, "the brief is the design"

**Design concepts**: visual hierarchy, typographic contrast, color palette, layout composition, call-to-action placement, white space, brand consistency

**User sentiment**: Reddit AI flyer design, Hacker News AI poster tool, G2 AI design tools, Trustpilot Canva AI, Capterra Adobe Express

**Comparisons**: Canva AI vs Midjourney vs Adobe Firefly, GPT Image 2 vs Ideogram text rendering, Claude Design vs image-based flyer generation, Canva API vs direct image generation

**Contrarian**: AI flyers all look the same, AI design slop, AI flyer design criticism, AI replaces graphic designers, prompt-to-flyer limitations

## Mode
Deep Research (8-phase pipeline, multi-level BFS expansion, 216+ sources)
