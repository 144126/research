# DEEP RESEARCH COMMISSION

## Research Question
Which LLM API provider delivers the fastest time-to-first-token (TTFT) as of mid-2026, and what are the architectural, geographic, workload-specific, and cost trade-offs that determine the right choice for different use cases?

## Purpose & Context
Time-to-first-token (TTFT) — the latency between submitting a prompt and receiving the first response token — is the single most impactful metric for user-facing AI applications. A 13x gap exists between the fastest and slowest providers (45ms vs 2,000ms+), which is the difference between an app that feels "instant" and one users abandon.

This research serves technical decision-makers (CTOs, ML engineers, product leads) evaluating inference providers for latency-sensitive workloads: real-time chat, voice AI agents, copilots, agentic loops, and interactive streaming applications. The stakes are high — choosing the wrong provider means either broken UX from high latency or unnecessary cost/complexity from over-provisioning.

The key tension: the fastest providers (Groq LPU, Cerebras WSE-3) use specialized inference silicon with narrow model catalogs, while GPU-based providers (OpenAI, Anthropic, Google) offer broader model selection but 5-20x slower TTFT. This research must surface the decision framework for navigating this trade-off.

### Audience
- Primary: Technical decision-makers evaluating LLM API providers for production deployment
- Secondary: ML researchers, infrastructure engineers, voice AI product builders
- Tone: Formal, precise, data-driven with actionable recommendations
- Complexity: Deep technical depth on inference architecture; accessible framing for business stakeholders
- Child-reader adaptivity: Every technical term (TTFT, LPU, WSE, KV cache, SRAM, speculative decoding) must have an inline [imagine: ...] explanation in plain language

### Decision Context
- What decision will this research inform? Which provider(s) to route production traffic through for latency-critical LLM workloads
- What are the stakes? User retention, product viability for real-time AI features, infrastructure cost optimization
- What would change if the answer is X vs Y? If specialty silicon providers win on TTFT, the recommendation is to adopt a multi-provider architecture (fast for interactive, cheap for batch). If GPU providers close the gap, single-provider strategies become viable.

## Research Scope

### In Scope
1. Quantitative TTFT benchmarks (p50, p95, p99) across all major LLM API providers as of Q2 2026
2. Architectural analysis of why TTFT varies (LPU vs WSE vs GPU vs TPU inference stacks)
3. Cold start vs warm start TTFT differences and mitigation strategies
4. Geographic/regional TTFT variance (US, EU, Asia)
5. Workload-specific TTFT requirements: voice AI (<100ms), chat (<500ms), agents (<300ms per hop), batch (no constraint)
6. Cost vs TTFT trade-off analysis across providers
7. Multi-provider routing strategies for optimizing TTFT
8. Emerging providers and technologies that could shift the TTFT landscape

### Out of Scope
- Model quality/benchmark scores (MMLU, HumanEval, etc.) — only referenced where relevant to provider choice
- Training infrastructure or fine-tuning platforms
- Self-hosted/on-premise inference optimization
- TTFT for image/video/multimodal models (text-only focus)
- Long-term (>12 month) predictions

### Timeframe
Primary emphasis on 2025-2026 data, with foundational context (architecture evolution, historical TTFT improvements) from 2023-2024

### Geographic Focus
Global coverage with specific attention to US, EU, and Asia-Pacific regional differences

## Required Dimensions of Investigation

Each dimension must be investigated from multiple angles and reported with specific evidence:

1. **Technical/Mechanistic Exploration**
   - Why does Cerebras WSE-3 achieve sub-100ms TTFT? How does wafer-scale on-chip SRAM eliminate the memory bandwidth bottleneck?
   - How does Groq's LPU achieve deterministic sub-100ms TTFT? What is the architectural advantage of compilation-level scheduling vs GPU runtime scheduling?
   - What is SambaNova's RDU approach and how does it compare?
   - How do GPU-based providers (OpenAI, Anthropic, Google) achieve their TTFT on commodity hardware? What optimization techniques do they use (speculative decoding, prompt caching, KV cache management)?
   - What is the cold start penalty for each architecture type? How does model loading, kernel JIT compilation, and KV cache initialization contribute?

2. **Historical Context & Evolution**
   - How has TTFT improved from 2023 to 2026 across provider categories?
   - What were the key architectural breakthroughs (FlashAttention, speculative decoding, prompt caching, LPU introduction)?
   - How did the entry of Cerebras and Groq change the competitive landscape?
   - Timeline of TTFT milestones: what was the fastest API at each point?

3. **Current State-of-Art**
   - Ranked TTFT leaderboard (p50 and p95) for all major providers as of June 2026
   - Categorize by: specialty silicon (Cerebras, Groq, SambaNova), cloud GPU (OpenAI, Anthropic, Google, Together, Fireworks, DeepInfra), emerging (StepFun, Qwen, MiniMax), and reasoning (DeepSeek-R1, o-series)
   - Which providers have the best p95/p99 tail latency (not just p50)?
   - How does TTFT vary by model size within the same provider?
   - What is the impact of prompt length on TTFT?

4. **Quantitative Evidence**
   - Compile TTFT data from at least 5 independent benchmark sources (Artificial Analysis, VerticalAPI, TokenMix, Digital Applied, lmspeed.net, etc.)
   - Price per 1M tokens (input/output) alongside TTFT for each provider-model pair
   - Tokens-per-second throughput alongside TTFT
   - Regional TTFT variance: US-East vs EU-West vs Asia-Pacific
   - Cold vs warm TTFT ratios
   - Free tier TTFT vs paid tier TTFT

5. **Stakeholder Analysis**
   - Cerebras: strategy, model catalog (Llama, Qwen, GPT-OSS), pricing, enterprise traction
   - Groq: strategy, model catalog (Llama, Mixtral, Gemma, Whisper), free tier, rate limits
   - SambaNova: strategy, RDU hardware, model catalog, enterprise focus
   - OpenAI: TTFT posture, GPT-4.1 mini/nano, GPT-5.4, prompt caching, Realtime API
   - Google DeepMind: Gemini Flash/Flash Lite, TPU infrastructure, AI Studio
   - Anthropic: Claude Haiku/Sonnet/Opus, prompt caching strategy, speed modes
   - DeepSeek: V4 Flash, Chinese infrastructure, regional advantages
   - StepFun, Qwen (Alibaba), MiniMax, Zhipu: Chinese providers gaining global distribution
   - Together AI, Fireworks AI, DeepInfra: open-weight hosts with competitive TTFT

6. **Competing Approaches Comparison**
   - Specialty silicon (Cerebras/Groq/SambaNova) vs GPU cloud (OpenAI/Anthropic/Google) vs TPU (Google)
   - Single-provider vs multi-provider routing strategy
   - Open-weight (Llama, Qwen on Groq/Cerebras) vs proprietary (GPT, Claude, Gemini)
   - Streaming vs batch: when does TTFT matter vs throughput?
   - Speculative decoding vs standard decoding for TTFT

7. **Criticisms & Limitations**
   - Narrow model catalogs of Groq/Cerebras: what models are unavailable?
   - Groq rate limits: does speed become a rate-limit trap?
   - Cold start TTFT variance: how much does first-request latency differ from benchmarks?
   - Queue depth sensitivity: how does TTFT degrade under concurrent load?
   - Provider lock-in risk with specialty silicon
   - Free tier reliability: rate limits, deprecation patterns

8. **Contrarian & Heterodox Perspectives**
   - Is TTFT overrated? When does throughput matter more than first-token latency?
   - Are Groq/Cerebras actually worth the premium for most workloads?
   - Do users actually perceive the difference between 100ms and 500ms TTFT?
   - Is the multi-provider routing approach over-engineered? Would a single competent provider suffice?
   - Are Chinese providers (DeepSeek, Qwen, StepFun) actually competitive on TTFT despite geographic latency?

9. **Future Trajectories & Predictions**
   - Will Groq/Cerebras expand their model catalogs and become full-platform providers?
   - Will GPU-based providers close the TTFT gap through software optimization?
   - Impact of NVIDIA's next-generation inference hardware on TTFT
   - Will voice AI demand drive further TTFT specialization?
   - Emerging inference technologies: speculative decoding 2.0, CRIU snapshots for cold start elimination

10. **Regulatory, Legal & Ethical Dimensions**
    - Data residency requirements: how does GDPR, China data law affect TTFT via regional routing?
    - Are there ethical concerns with ultra-low-latency voice AI (e.g., real-time voice cloning, deepfake risk)?
    - Export controls on specialized AI chips (WSE-3, LPU) — geopolitical implications

11. **Geographic & Geopolitical Variation**
    - US vs EU vs Asia TTFT comparison for each major provider
    - Chinese provider landscape (DeepSeek, Qwen, StepFun, ByteDance, Zhipu) — how do they compare on TTFT?
    - How does the US-China chip export ban affect access to Cerebras/Groq-class hardware?
    - Regional inference infrastructure: where are the compute clusters located?

12. **Practical Applications & Case Studies**
    - Voice AI production deployments: what TTFT do teams actually achieve with Groq/Cerebras?
    - Agentic AI pipelines: how does multi-step TTFT compounding affect architecture decisions?
    - Real-time coding copilots: which providers do JetBrains, GitHub Copilot, Cursor use and why?
    - Chat UX: case study of a provider migration driven by TTFT improvement

## Source Requirements

### Source Types Required (ALL must be represented)
- Academic/peer-reviewed research (MLSys 2026, IBM Research on vLLM cold start)
- Industry analysis (VerticalAPI benchmark, TokenMix comparison, Digital Applied quarterly report)
- Technical documentation (Groq/Cerebras architecture docs, OpenAI/Anthropic/Google API docs)
- News/current events reporting (vendor announcements, product launches)
- Primary sources (independent benchmarks, user-reported production data from forums/communities)
- Expert commentary/analysis (tech blogs, conference talks, engineering postmortems)
- Contrarian/critical sources (skeptical takes on TTFT importance, failure postmortems)
- Practitioner testimonials (LiveKit community, production case studies)

### Minimum Source Count: 270+ — Level 1 initial sources should themselves aim for >=270 relentlessly. Multi-level BFS expansion (following links/references/ideas from each source to generate further sources, iteratively) is used only when Level 1 falls short.

### Source Diversity Requirements
- At least 5 different source types must be represented
- Mix of recent (2025-2026) and foundational (pre-2025) sources
- Both proponents AND critics must be cited
- Geographic diversity: US, EU, and Chinese provider coverage
- If a source type is unavailable, document the gap explicitly

## Output Requirements

### Report Structure
1. Executive Summary (1000-1500 words) — synthesize ALL major findings: the absolute TTFT champion, the best value choice, the voice AI pick, the agentic workload pick, geographic considerations, and actionable routing strategy. Every claim cited.
2. Introduction — scope, methodology, assumptions, key terms defined with ELI5 [imagine: ...] explanations for: TTFT, LPU, WSE, KV cache, SRAM, speculative decoding, prompt caching, cold start
3. Main Analysis (6-8 findings, 600-2000 words each)
   - Finding 1: The TTFT Leaderboard — ranked providers by TTFT with architectural explanations
   - Finding 2: Why TTFT Varies — deep technical analysis of inference architectures
   - Finding 3: Cold Start — the hidden TTFT tax and mitigation strategies
   - Finding 4: Workload-Specific TTFT Requirements — voice, chat, agents, batch
   - Finding 5: Cost-Performance Trade-offs — TTFT vs price analysis
   - Finding 6: Geographic Variance — regional TTFT comparison
   - Finding 7: Multi-Provider Routing — production patterns for TTFT optimization
   - Finding 8: Emerging Players & Future Outlook — Chinese providers, next-gen hardware
4. Synthesis & Insights — cross-cutting patterns: the model catalog bottleneck, the voice AI tail wagging the inference dog, multi-provider as the new normal
5. Limitations & Caveats — benchmark methodology differences, temporal variance, sample size issues
6. Recommendations — actionable, prioritized guidance by use case
7. Complete Bibliography — every citation [1]-[N], no placeholders
8. Methodology Appendix — research process, verification approach, confidence levels

### Quality Mandates
- EVERY factual claim followed by [N] citation in the same sentence
- No vague attributions ("research shows", "experts believe", "studies suggest") — cite the specific source
- Distinguish facts FROM sources vs. your own synthesis explicitly
- For speculative content, label as "This suggests..." not "Research shows..."
- Minimum 3 independent sources per major claim
- Prose >=80%, bullets sparingly (only for distinct lists)
- No placeholder text, no "content continues", no ranges in bibliography
- Admit uncertainty: "No sources found for X" rather than fabricating
- ELI5 inline [imagine: ...] for every technical term

### Bias Safeguards
- Actively seek sources that contradict initial findings (e.g., sources arguing TTFT is overrated)
- Flag when sources have financial or ideological interests (Cerebras vs Groq marketing claims)
- Note when research is sparse — don't fill gaps with speculation
- Distinguish correlation from causation (e.g., model size vs TTFT correlation isn't deterministic)
- Mark predictions/forecasts as [SPECULATION] not [FACT]
- Distinguish vendor-published benchmarks from independent verification

## Seed Keywords

### Core Terms
time to first token, TTFT, LLM latency, inference latency, first token latency

### Provider Names
Groq, Cerebras, SambaNova, OpenAI, Anthropic, Google Gemini, DeepSeek, Together AI, Fireworks AI, DeepInfra, StepFun, Qwen, MiniMax, Mistral, xAI Grok, Cohere, Replicate, Perplexity, OpenRouter, Azure OpenAI, AWS Bedrock

### Model Names
Llama 3.3 70B, Llama 4, Qwen 3, GPT-4.1 mini, GPT-4.1 nano, GPT-5.4, Gemini 2.0 Flash, Gemini 2.5 Flash, Flash Lite, Claude Haiku 4.5, Claude Sonnet 4, DeepSeek V4 Flash, Step-3.5-Flash, MiMo-V2.5

### Architecture Terms
LPU, WSE-3, wafer-scale, RDU, TPU v5e, H100, H200, B200, SRAM, KV cache, speculative decoding, prompt caching, FlashAttention, FireAttention

### Benchmark Sources
Artificial Analysis, VerticalAPI, TokenMix, Digital Applied, lmspeed.net, easy-benchmarks.com, llmversus.com, global-apis.com

### Use Cases
voice AI TTFT, real-time chat latency, agentic AI TTFT, copilot latency, streaming inference

### Region-Specific
TTFT US vs EU vs Asia, China LLM API latency, DeepSeek region routing, cloud inference latency by region

### Contrarian
is TTFT overrated, tokens per second vs TTFT, perceived latency vs actual latency, user psychology response time

### Cold Start
cold start TTFT, warm vs cold inference, GPU cold start, LLM container startup, inference engine initialization

## Mode
Deep Research (8-phase pipeline, multi-level BFS expansion, 270+ sources)
