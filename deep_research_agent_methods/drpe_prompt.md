# DEEP RESEARCH COMMISSION

## Research Question
What is the complete landscape of methods — from academic research, industry labs, and individual practitioners — for building AI deep research agents that maximize information discovery, source coverage, objective truth-finding, and citation-verified synthesis, including every known technique as of mid-2026?

## Purpose & Context
This research aims to produce an exhaustive reference of every method, technique, training strategy, architecture pattern, verification approach, and inference-time scaling strategy that has been empirically shown to improve the performance of AI deep research agents. The audience is a developer building a next-generation open-source deep research agent and wants to know every known technique from every source — Google, OpenAI, Anthropic, DeepMind, Microsoft, Meta, academic labs (Tsinghua, PKU, ETH, Stanford, MIT, CMU, etc.), individual researchers, and small labs — regardless of provenance, as long as it yields measurable improvements on benchmarks like BrowseComp, GAIA, HLE, DeepSearchQA, XBench, DeepResearch Bench, and others.

### Audience
- Primary: AI engineer/researcher building an open-source deep research agent; deep technical expertise; wants exhaustive enumeration of methods
- Secondary: Academic researchers studying LLM agent architectures
- Tone: Technical, precise, data-driven, comprehensive
- Complexity: PhD-level depth in methodology sections, with inline ELI5 bracketed explanations when introducing any concept, term, or idea that may be unfamiliar to a lay reader
- Child-reader adaptivity: Every time a hard term is introduced, immediately follow with [imagine: like...] explanation

### Decision Context
- What decisions will this research inform? Which training strategies, architecture choices, verification mechanisms, and inference-time scaling approaches to implement in a production deep research agent
- Stakes: Missing a key method means building an agent that underperforms SOTA by significant margins
- What would change if the answer is X vs Y? If verification-centric methods prove most impactful, focus resources on verifier design. If RL-based training is key, invest in RL infrastructure. If test-time scaling strategies dominate, focus on compute-optimal orchestration.

## Research Scope

### In Scope
1. All training methodologies for deep research agents (SFT, RL, multi-turn RL, curriculum RL, progressive RL, hierarchical RL, GRPO variants)
2. All verification approaches (chain-of-verification, self-verification, fine-grained verification, formal verification, neuro-symbolic verification, verifier-guided test-time scaling)
3. All architecture patterns (single-agent, multi-agent, hierarchical, planner-executor, recursive, graph-based exploration, multi-agent debate)
4. All inference-time/test-time scaling methods (budget forcing, parallel scaling, best-of-N, beam search, tree search, confidence-aware scaling, compute-optimal allocation, iterative refinement)
5. All data synthesis methods for training (graph-based QA, shortcut-resistant synthesis, multi-agent self-play, iterative injection, reverse construction, verified QA synthesis)
6. All context management strategies (sliding window, recursive trajectory compression, dynamic context, structured state representations, memory folding)
7. All benchmarks and evaluation frameworks (BrowseComp, BrowseComp-ZH, BrowseComp-Plus, GAIA, HLE, DeepSearchQA, XBench, DeepResearch Bench, WebArena, etc.)
8. All open-source implementations and codebases that demonstrate these methods

### Out of Scope
1. General LLM training methods not specific to search/agentic tasks
2. Prompt-engineering-only approaches (focus is on trainable agents)
3. Single-turn RAG systems without multi-step search
4. Non-AI information retrieval methods
5. Domain-specific applications (e.g., only medical or only legal) unless methods generalize

### Timeframe
2023–mid-2026, with strong emphasis on 2025–2026 (where ~90% of advances occurred). Foundational works (CoVe, ReAct, Reflexion, GRPO) from 2023–2024 included as precursors.

### Geographic Focus
Global — US (OpenAI, Google, Anthropic, Stanford, MIT, CMU, Berkeley, NVIDIA), China (Tsinghua, PKU, Zhipu, Alibaba, DeepSeek, Moonshot AI, Baidu), UK (DeepMind, Oxford, Cambridge), Switzerland (ETH), Germany (TU Munich), individual/open-source contributors worldwide.

## Required Dimensions of Investigation

Each dimension must be exhaustively investigated with specific methods, paper citations, and comparative results:

### 1. Technical/Mechanistic Exploration
- What are the core architectural patterns for deep research agents? (ReAct, single-model, multi-agent orchestration, hierarchical planner-executor, recursive/iterative, MDP-inspired)
- How do different methods implement planning? (step-back prompting, graph-based dynamic planning, anchor-plan-first, state-conditioned planning)
- How do search and reasoning interact? (sequential ReAct vs parallel search-first vs hybrid parallel+sequential)
- What is the "Asymmetry of Verification" principle and how is it exploited across different systems?
- [imagine: the Asymmetry of Verification is the idea that it's much easier to CHECK if an answer is right than to GENERATE the right answer in the first place]

### 2. Historical Context & Evolution
- Timeline of key milestones: ReAct (2023) → CoVe (2024) → BrowseComp release → OpenAI Deep Research (Feb 2025) → Google Deep Research (Dec 2024–Apr 2026) → GRPO adaptation for agents → verification-centric era (2025–2026)
- How did each major lab's approach evolve? (OpenAI: end-to-end RL on browsing tasks; Google: planning + synthesis + iterative refinement; DeepSeek: search+R1 integration; Anthropic: computer-use + deep research)
- What were the key benchmark creations and how did they drive progress? (BrowseComp, GAIA, DeepSearchQA, HLE, BrowseComp-Plus)

### 3. Current State-of-Art (mid-2026)
- What are the current SOTA systems and their benchmark scores? (OpenAI Deep Research, Gemini Deep Research/Max, Kimi Researcher, Grok ResearchSearch, and all open-source: DeepDive-32B, WebAnchor-30B, Re-TRAC-30B, DeepMiner-32B, ASearcher, Marco DeepResearch-8B, LiteResearcher-4B, DR-Venus-4B, HybridDeepSearcher, SMTL, BrowseMaster)
- What are the top benchmark scores as of mid-2026? (BrowseComp, BrowseComp-ZH, GAIA, HLE, DeepSearchQA, XBench-DeepSearch, DeepResearch Bench I+II)
- What capabilities are frontier systems showing? (MCP support, native chart generation, collaborative planning, multi-modal search, 200+ tool calls, 2048+ interaction scaling)

### 4. Quantitative Evidence
- Benchmark scores: exhaustive table of every reported result on every benchmark for every system
- Compute requirements: training cost, inference cost per query, model sizes (4B to frontier)
- Scaling laws: how performance scales with model size, context length, number of tool calls, number of RL rollouts, parallel samples
- Efficiency metrics: token usage per task, wall-clock time, cost vs accuracy tradeoffs
- Improvement percentages: how much each technique adds (e.g., Anchor-GRPO +X% on BrowseComp, verification +Y% on GAIA)
- [imagine: think of benchmark scores like test scores in school — each benchmark tests different skills like finding hidden information or answering very hard questions]

### 5. Stakeholder Analysis
- Major corporate labs and their strategies: Google (Deep Research & Max with MCP/charts), OpenAI (deep research in ChatGPT powered by o-series reasoning models), Anthropic (Claude with computer use), DeepSeek (R1 variants + search), Microsoft (research agents, AutoGen), Meta (open-source agent frameworks), Baidu (Chinese search optimization), Moonshot AI (Kimi-Researcher)
- Major academic labs and contributions: Tsinghua (DeepDive, WebAnchor, BrowseMaster), PKU (DeepAgent, FORT-Searcher), ETH Zurich (CoVe foundation), UC Berkeley (Gorilla, tool-use), CMU (STV, self-verification)
- Open-source communities and individual contributors: wandabwa2004 (deep_research_agent), thtskaran (claude-researcher), B143KC47 (deep-research-skill), 2imi9 (LocalPilot), Jason Liang (Caesar)
- Funding and incentive structures: who benefits from open vs closed, who is driving benchmark creation

### 6. Competing Approaches Comparison
- Single-agent end-to-end vs multi-agent orchestration: tradeoffs in reliability, cost, latency, modularity
- RL-based training vs SFT-only vs prompting-only: which methods work at which scales
- Verification-centric design vs generation-centric design: Marco DeepResearch vs standard ReAct agents
- Verification types: meta-verification, tool-based adaptive verification, formal/neuro-symbolic verification, self-verification, reference-conditioned verification — when does each work best?
- Training data synthesis approaches: graph-based (DeepDive, FORT) vs agent-based (REDSearcher) vs reverse construction (DeepMiner) vs multi-agent self-play (Fathom-DeepResearch)
- Context management: vanilla ReAct vs sliding window (DeepMiner) vs recursive state compression (Re-TRAC) vs memory folding (DeepAgent) vs structured state (IterResearch)
- Test-time scaling strategies: uniform budget forcing vs confidence-aware (CATTS) vs agent-orchestrated (ATLAS, AgentTTS) vs fine-grained verification (FineVerify)
- [imagine: this is like comparing different ways to build a car — some focus on making one perfect engine, others use multiple smaller engines working together]

### 7. Criticisms & Limitations
- What failure modes are known? (context suffocation, plan anchoring errors, error cascades from early mistakes, shortcut collapse in training data, premature stopping, hedging behaviors)
- What are the reliability issues with current verification approaches? (fake verification where the model appears to check but doesn't actually change answers; correlated failure patterns in multi-sample consensus)
- What are the scalability bottlenecks? (training with 100+ turn trajectories is unstable; context window limits; reward sparsity in long-horizon RL; cost of running real web searches during training)
- What bias concerns exist? (search engines returning non-representative results; training data leakage; benchmark contamination)
- What are the reproducibility issues? (dependence on live web APIs, non-static benchmarks, closed-source models used as teachers)
- What do critics say? Are these agents actually useful in production or mostly benchmark-chasing? What are the real-world failure rates?

### 8. Contrarian & Heterodox Perspectives
- Is the deep research benchmark race producing genuine capability advances or just overfitting to benchmark characteristics? (BrowseComp-Plus was created specifically because original BrowseComp was vulnerable to retrieval shortcuts)
- The "Search More, Think Less" (SMTL) argument: maybe deep research agents should minimize reasoning and maximize parallel search rather than the current trend toward more reasoning
- Do we need verification at all? The asymmetry of verification is well-established but some argue that better generators negate the need for verifiers
- Is the multi-agent approach over-engineered? Single-model end-to-end RL (ASearcher approach) achieves competitive results without complex multi-agent orchestration
- Are small models the future of deep research? DR-Venus (4B) and LiteResearcher (4B) match or exceed 30B+ models — does scale matter less than data quality and training recipe?
- Decentralized/individual approaches vs industrial labs: can individual researchers meaningfully contribute or does deep research require Google-scale resources?
- [imagine: contrarian views are like someone saying "actually, I think everyone else is wrong about this" — they might not be right, but they help us question our assumptions]

### 9. Future Trajectories & Predictions
- Will deep research agents converge on a standard architecture (like transformers did for NLP) or remain fragmented?
- What is the trajectory of test-time compute scaling? Will agents routinely use 1000+ tool calls per query?
- Will MCP and standardized tool protocols make deep research agents composable building blocks?
- Multi-modal deep research: agents that search images, video, audio, code repositories, databases simultaneously
- The "agentic scientist" trajectory: Caesar, LocalPilot, Sibyl, Arbor, AgentLabX — autonomous research agents that not only search but run experiments
- Will edge-scale (4B) deep research agents running on devices become viable? DR-Venus and LiteResearcher suggest yes
- What disruptive technologies could change the landscape? (significantly cheaper inference, 1M+ context windows as standard, native agent capabilities in foundation models)

### 10. Regulatory, Legal & Ethical Dimensions
- Copyright implications of deep research agents scraping and synthesizing web content
- Bias in search results propagating through agent research
- Hallucination and liability: who is responsible when a research agent produces incorrect information used for decisions?
- Open vs closed: should deep research capabilities be openly available or restricted?
- Academic integrity: agents writing research reports raises questions about plagiarism and attribution
- Existing and emerging regulations (EU AI Act implications for autonomous research agents)

### 11. Geographic & Geopolitical Variation
- US dominance in frontier model development vs Chinese dominance in open-source agent ecosystem
- How does search ecosystem vary? Google search API (US) vs Baidu (China) — how agents adapt to different underlying search infrastructures
- Access to compute: differences in training infrastructure availability
- Language-specific benchmarks and optimization (BrowseComp-ZH, Chinese-specific challenges)
- Government AI strategies influencing research direction (UK DeepMind lab, China state-backed AI initiatives)

### 12. Practical Applications & Case Studies
- Real-world deployments of deep research agents in finance (due diligence, market research), life sciences (literature review, drug discovery), enterprise (competitive intelligence, report generation)
- Open-source case studies: how builders are using open-source deep research agents (wandabwa2004's multi-agent research assistant, thtskaran's claude-researcher with 127 sources per report, the RAGFlow Multi-Agent Deep Research system)
- Academic reproducibility case studies: KLong system that reproduces research papers, Sibyl generating conference-quality papers
- Individual practitioner use cases: how independent developers are integrating deep research into their workflows (e.g., per-query costs, latency expectations, quality)
- The DuMate-DeepResearch practical evaluation: real multi-indicator evaluation frameworks with AHP-entropy weighting

## Source Requirements

### Source Types Required (ALL must be represented)
- Academic/peer-reviewed research: arXiv papers, ACL/NeurIPS/ICML/EMNLP proceedings (minimum 50 papers, covering all major methods)
- Industry analysis: blog posts, technical reports from Google, OpenAI, Anthropic, DeepSeek, Microsoft (minimum 20)
- Technical documentation: API docs, GitHub READMEs, architecture docs (minimum 20)
- News/current events: reporting on releases and announcements (TechCrunch, VentureBeat, The Verge) (minimum 10)
- Open-source codebases: GitHub repositories with implementations (minimum 30)
- Benchmark sources: Kaggle leaderboards, benchmark papers, evaluation frameworks (minimum 10)
- Contrarian/critical sources: failure postmortems, critical blog posts, rebuttals (minimum 5)

### Minimum Source Count
1440+ sources — Level 1 initial sources should themselves aim for >=1440. Multi-level BFS expansion follows references, links, and citations to reach 1440+.

### Source Diversity Requirements
- At least 6 different source types represented
- Mix of recent (2025-2026) and foundational (pre-2025)
- Both proponents AND critics cited
- Geographic diversity: US, China, UK, Switzerland, individual contributors
- Every major method paper must be cited
- If a source type is unavailable, document the gap explicitly

## Output Requirements

### Report Structure
1. Executive Summary (1000-1500 words) — synthesize ALL major findings, patterns, implications, and recommendations upfront; this is the most important section
2. Introduction — scope, methodology, key terms defined with ELI5 explanations, assumptions
3. Main Analysis (findings organized into 6-10 sections, 800-2000 words each):
   - Finding 1: Training Methodologies (comprehensive taxonomy of every training approach)
   - Finding 2: Verification & Factuality (all verification methods compared)
   - Finding 3: Architecture Patterns (all architectures with tradeoffs)
   - Finding 4: Test-Time & Inference Scaling (all scaling strategies)
   - Finding 5: Data Synthesis & Benchmarking (training data and evaluation approaches)
   - Finding 6: Open-Source Implementations (ecosystem survey)
   - Finding 7: Quantitative Comparison (benchmark leaderboard with methodology used)
   - Finding 8: Future Directions & Remaining Challenges
4. Synthesis & Insights — cross-cutting patterns, which methods are complementary, which are rivals, recommendations for building a SOTA agent
5. Limitations & Caveats — gaps in the literature, uncertainties, contradictory evidence, reproducibility concerns
6. Recommendations — actionable guidance for building a next-generation deep research agent based on evidence
7. Complete Bibliography — every citation [1]-[N], no placeholders, no ranges
8. Methodology Appendix — research process, BFS expansion details, verification procedures, confidence levels

### Quality Mandates
- EVERY factual claim followed by [N] citation in the same sentence
- No vague attributions ("research shows", "experts believe", "studies suggest") — always [PaperName, Year] or [Source, URL]
- Distinguish facts FROM sources vs. your own synthesis explicitly: "Source X reports 46.0% on BrowseComp [1]. This suggests that..." — the "suggests" is your synthesis, the "46.0%" is the source's fact
- For speculative content, label as "This suggests..." not "Research shows..."
- Minimum 3 independent sources per major claim
- Prose >=80%, bullets sparingly (only for distinct lists like benchmark tables or comparison matrices)
- No placeholder text, no "content continues", no ranges in bibliography
- Admit uncertainty: "No sources found for X" rather than fabricating
- ELI5 inline bracketed explanations for every hard concept, every time

### Bias Safeguards
- Actively seek sources that contradict initial findings — for every method's claimed improvement, find at least one source showing its limitations or failure cases
- Flag when sources have financial or ideological interests (e.g., a Google blog post about Google's product)
- Note when research is sparse — don't fill gaps with speculation; explicitly say "We found limited independent evaluation of Y beyond Z's own reporting"
- Distinguish correlation from causation (e.g., "Models that use method A achieve higher scores on BrowseComp" vs "Method A causes higher BrowseComp scores")
- Mark predictions/forecasts as [SPECULATION] not [FACT]

## Seed Keywords

### Core Terms
deep research agent, deep search agent, autonomous research, agentic search, web agent, browse agent, information-seeking agent, long-horizon reasoning agent

### Training Methods
reinforcement learning agent, GRPO, multi-turn RL, Anchor-GRPO, HGPO, IGPO, curriculum RL, progressive RL, hierarchical RL, ToolPO, EAPO, rejection sampling, SFT long-horizon, trajectory-splitting SFT, stepwise policy optimization, RLVR, VPR (Verifiable Process Reward), RLOO, stepwise GRPO

### Verification Methods
chain-of-verification, CoVe, self-verification, fine-grained verification, FineVerify, DeepVerifier, meta-verification, tool-based adaptive verification, formal verification, FormalJudge, neuro-symbolic, SMT solver, Dafny, STV, self-trained verification, SAVeR, verifier-guided test-time scaling, Counterfactual Self-Questioning, CSQ, rubric-guided verification, DeepVerifier, Co-Sight, CAMV, TRSF, CRITIC

### Architecture
ReAct, multi-agent orchestration, planner-executor, hierarchical agent, recursive agent, graph-based exploration, Generator-Verifier loop, multi-agent debate, memory folding, structured state representation, recursive trajectory compression

### Test-Time Scaling
budget forcing, parallel scaling, best-of-N, beam search, tree search, self-consistency, confidence-aware scaling, CATTS, ATLAS, AgentTTS, compute-optimal, sequential scaling, hybrid scaling, verifier-guided scaling

### Data Synthesis
shortcut-resistant, FORT-Searcher, graph-based QA, reverse construction, DeepMiner, multi-agent self-play, DUETQA, verified QA synthesis, iterative injection, REDSearcher, BrowseMaster-QA, HDS-QA

### Context Management
context suffocation, sliding window, dynamic context window, recursive trajectory compression, Re-TRAC, structured state, memory folding, DeepAgent, IterResearch workspace

### Key Systems
Marco DeepResearch, IterResearch, DeepDive, WebAnchor, Re-TRAC, DeepMiner, SMTL, ASearcher, DeepAgent, HybridDeepSearcher, LiteResearcher, DR-Venus, BrowseMaster, VSearcher, DuMate-DeepResearch, Yunque DeepResearch, Fathom-DeepResearch, KLong, BrowseMaster, DeepVerifier, Search-o1, WebThinker, WebDancer, WebSailor, MiroThinker, Tongyi DeepResearch, Cao Shen DeepResearch

### Benchmarks
BrowseComp, BrowseComp-ZH, BrowseComp-Plus, GAIA, HLE, DeepSearchQA, XBench-DeepSearch, DeepResearch Bench, DeepResearch Bench II, SimpleQA, FRAMES, WebWalker, SeAL0, MuSiQue, WebArena, WebShop, ALFWorld, ToolBench, API-Bank

### Key Papers
BrowseComp paper, DeepSearchQA paper, HLE paper, Marco DeepResearch paper, IterResearch paper, FORT-Searcher paper, DeepDive paper, WebAnchor paper, Re-TRAC paper, DeepMiner paper, SMTL paper, ASearcher paper, LiteResearcher paper, DR-Venus paper, Fathom-DeepResearch paper, Yunque DeepResearch paper, DuMate-DeepResearch paper, KLong paper, DeepAgent paper, HGPO paper, HiPER paper, ProAct paper, FineVerify paper, Co-Sight paper, FormalJudge paper, DeepVerifier paper, STV paper, VPR paper, SAVeR paper, CSQ paper, AgentTTS paper, ATLAS paper, CATTS paper, BrowseMaster paper, VSearcher paper, Search More Think Less paper

### Open-Source Repos
deep_research_agent (wandabwa2004), claude-researcher (thtskaran), deep-research-skill (B143KC47), LocalPilot (2imi9), Caesar (jasonzliang), RAGFlow multi-agent deep research, scholar-deep-research (Agents365), ARIA Research Agent, Arbor (sid77ai), AgentLabX, Sibyl, AutoResearch, Fathom-DeepResearch, DR-Venus, LiteResearcher, DeepDive, ASearcher, DeepMiner, Marco DeepResearch, Re-TRAC

## Mode
Deep Research (8-phase pipeline, multi-level BFS expansion, 1440+ sources)
