# DEEP RESEARCH COMMISSION

## Research Question
Which open-source LLM plays chess best as of mid-2026 — ranked by gameplay Elo, puzzle-solving accuracy, chess understanding, and cost-efficiency?

## Purpose & Context
This research aims to determine the single best open-source/ open-weight large language model for playing chess, evaluated across multiple dimensions: full-game play (Elo vs engines), tactical puzzle solving, chess knowledge understanding, instruction-following (legal move rates, game completion), and cost-efficiency. The answer matters to AI researchers using chess as a reasoning benchmark, hobbyists who want the strongest self-hosted chess LLM, and developers evaluating open-source models for agentic planning tasks where chess serves as a proxy.

The open-source LLM landscape in 2026 has narrowed the gap with proprietary models to 3-5 months [1]. Models like GLM-5.2, DeepSeek V4 Pro, Qwen 3.5, and Llama 4 Maverick now rival GPT-5 and Claude Opus on general benchmarks. But chess-specific data is sparse — most chess LLM benchmarks (LLM CHESS [2], Dubesor AI Chess [3], Chess AI Bench [4]) primarily tested proprietary models. This research must extract every available chess-specific datapoint for open-weight models and triangulate with general reasoning benchmarks to produce a definitive ranking.

### Audience
- Primary: Technical AI/ML practitioners evaluating open-source models for reasoning benchmarks. Expert level.
- Secondary: Chess enthusiasts curious about AI chess play. Intermediate.
- Tone: Precise, data-driven, authoritative.
- Complexity: Technical depth expected, with ELI5 [imagine: explain-like-I'm-5] inline explanations for chess-specific and ML-specific jargon.
- Child-reader adaptivity: Every technical term must have an inline [imagine: ...] explanation.

### Decision Context
- What decision will this research inform? Which open-weight model to download/self-host for chess play, or which to use as a chess-proxy benchmark for evaluating general reasoning.
- What are the stakes? Picking the wrong model wastes GPU hours and delivers weak chess play. The benchmark also has implications for which open-source architecture best handles long-horizon planning (a core AI capability).
- What would change if the answer is X vs Y? If a small model (e.g., DeepSeek R1 distill) wins, it suggests efficiency over brute scale. If a giant MoE wins, it suggests scale continues to matter.

## Research Scope

### In Scope
1. Open-source/open-weight LLMs only (Apache 2.0, MIT, Llama License, CC-BY-NC, etc.)
2. Chess gameplay Elo ratings from standardized benchmarks (LLM CHESS, Dubesor AI Chess, Chess AI Bench, Benedict Brady benchmark)
3. Chess puzzle-solving accuracy and Elo (Lichess-derived puzzle sets)
4. Chess understanding/knowledge metrics (ChessQA-based evaluations)
5. Full-game play: win rates vs random players, vs engine opponents
6. Move legality rates and game completion rates (instruction-following dimension)
7. Cost per game / cost per Elo point for open-source models
8. General reasoning benchmarks (GPQA, AIME, MMLU-Pro, SWE-bench) as chess-ability proxies
9. Open-source models capable of being run locally (self-hosting)

### Out of Scope
1. Proprietary/closed-source models (GPT-5, Claude Opus/Fable, Gemini 3) — mentioned only as baselines
2. Traditional chess engines (Stockfish, Leela Chess Zero, Komodo Dragon) — they are not LLMs
3. Chess engines built on RL/MCTS that are not LLMs (AlphaZero derivatives)
4. Fine-tuning approaches to improve LLM chess play (methodology, not raw ranking)
5. Hardware benchmarks beyond what's needed to run models locally

### Timeframe
2024–2026, with emphasis on 2025–2026. The LLM CHESS paper is Dec 2025. Dubesor leaderboard updated March 2026. Latest open-source model releases through June 2026.

### Geographic Focus
Global — models from US (Meta, Mistral, Google), China (DeepSeek, Alibaba/Qwen, Zhipu/GLM, Moonshot/Kimi, Xiaomi/MiMo), and others.

## Required Dimensions of Investigation

Each dimension must be investigated from multiple angles and reported with specific evidence:

1. **Technical/Mechanistic Exploration**
   - What chess-specific architectures or prompting strategies do LLMs use when playing chess? (tool-use agentic loop vs raw continuation)
   - How do reasoning models (o-series, DeepSeek R1, Kimi K2 Thinking) differ from non-reasoning models in chess play?
   - What is the relationship between chain-of-thought/thinking tokens and chess Elo?
   - How does the agentic framework (tool-calling for board state vs PGN continuation) affect chess performance?

2. **Historical Context & Evolution**
   - How did LLM chess ability evolve from 2024 (early models barely beat random) to 2026 (some reach ~1900 Elo)?
   - What were the key milestones? (Saplin's 2024 chaos monkey tests, LLM CHESS arXiv Dec 2025, Benedict Brady's Mar 2026 benchmark)
   - How does the trajectory of LLM chess skill compare to the trajectory of traditional chess engines?

3. **Current State-of-Art**
   - What are the exact top open-source LLM chess rankings from ALL available leaderboards?
   - What are the best open-source models for: (a) full games vs engines, (b) puzzle solving, (c) chess understanding?
   - How do open-source models compare to proprietary baselines in chess?
   - What are the latest results (as of June 2026) for open-source models in chess?

4. **Quantitative Evidence**
   - Chess Elo ratings for every open-source model tested (LLM CHESS, Dubesor, Benedict Brady, Chess AI Bench)
   - Puzzle Elo (Glicko-2) ratings from Lichess-based tests
   - Win/loss/draw rates vs random and vs engine opponents
   - Move legality rates and game completion rates
   - Accuracy on ChessQA-style chess knowledge questions
   - Tokens per move and cost per game
   - Cost per 1000 Elo points (cost efficiency)
   - General benchmark scores (GPQA, AIME, MMLU-Pro, SWE-bench) for chess-tested models

5. **Stakeholder Analysis**
   - Which companies/labs produce the best open-source chess-playing LLMs? (DeepSeek, Alibaba/Qwen, Zhipu/GLM, Meta/Llama, Moonshot/Kimi, Mistral, Google/Gemma)
   - Who are the key researchers in LLM chess benchmarking? (Maxim Saplin, Sai Kolasani, Kyle Montgomery, Benedict Brady)
   - What is the relationship between the LLM CHESS project and the Dubesor leaderboard?
   - Which open-source models are most actively tested for chess?

6. **Competing Approaches Comparison**
   - Head-to-head comparison of top open-source models' chess performance
   - Agentic tool-use (LLM CHESS framework) vs PGN continuation (Dubesor approach) vs raw FEN-to-move (puzzle benchmarks)
   - Reasoning (thinking) vs non-reasoning models for chess
   - Large MoE (e.g., DeepSeek R1 671B) vs efficient dense models (e.g., Qwen 3.5 27B)

7. **Criticisms & Limitations**
   - Is chess a good benchmark for LLM reasoning, or is it too narrow? (LLM CHESS paper argues it prevents overfitting and memorization)
   - Can LLMs truly play chess or are they pattern-matching memorized games? (Apple GSM-Symbolic-style critique)
   - Contamination risk: are chess positions memorized from training data?
   - The 200-move limit in LLM CHESS: does it mask poor endgame play?
   - Small sample sizes in current chess benchmarks

8. **Contrarian & Heterodox Perspectives**
   - Skeptic view: LLMs don't "reason" about chess — they pattern-match. Evidence from illegal move rates and blunders.
   - Alternative view: Standard benchmarks (MMLU, GPQA) are saturated and chess is a harder, more dynamic test [2]
   - Is the best chess LLM actually the best reasoning model, or are chess-specific abilities orthogonal?
   - Could a smaller open-source model specialized for chess beat a frontier general model?

9. **Future Trajectories & Predictions**
   - Will LLMs reach Grandmaster level (2500+ Elo) in chess? Timeline?
   - Will open-source models close the chess gap with proprietary models as they have on general benchmarks?
   - What innovations (test-time compute, RL fine-tuning on chess games, specialized chess datasets) could improve LLM chess play?
   - Will chess benchmarks become saturated like MMLU?

10. **Regulatory, Legal & Ethical Dimensions**
    - Licensing implications for using open-source models for chess (Apache 2.0 vs Llama License vs CC-BY-NC restrictions)
    - Ethical concerns: LLMs playing chess against humans without disclosure
    - Should chess be used as an AI capability benchmark given its cultural significance?

11. **Geographic & Geopolitical Variation**
    - US open-source models (Llama, Gemma) vs Chinese models (DeepSeek, Qwen, GLM, Kimi) in chess performance
    - European models (Mistral) positioning
    - Which regions invest most in open-source chess AI?

12. **Practical Applications & Case Studies**
    - Real-world use: LLMs as chess opponents in apps, websites, training tools
    - Case studies of open-source LLMs deployed as chess AI in production
    - How to self-host the best chess LLM (hardware requirements, setup)
    - Using chess as a benchmark for evaluating agentic LLM deployments

## Source Requirements

### Source Types Required (ALL must be represented)
- Academic/peer-reviewed research (arXiv papers, ICLR submissions): LLM CHESS paper, PGN2FEN, PuzzlePlex, ChessQA
- Industry analysis (leaderboards, benchmarks): LLM Stats, BenchLM, Artificial Analysis, Vellum
- Technical documentation (GitHub repos, framework docs): llm_chess repo, Dubesor repo, chess-bench.com
- News/current events: blog posts announcing new model chess capabilities
- Primary sources: Raw leaderboard data from LLM CHESS, Dubesor, Chess AI Bench, Benedict Brady
- Expert commentary: Maxim Saplin's blog posts, Benedict Brady's analysis
- Contrarian/critical sources: Skeptical takes on LLM chess reasoning (Apple GSM-Symbolic parallels)

### Minimum Source Count: 216+ — Level 1 initial sources should target >=216. Multi-level BFS expansion (following links/references from each source to generate further sources, iteratively) is used only when Level 1 falls short.

### Source Diversity Requirements
- At least 4 different source types
- Mix of recent (2025-2026) and foundational (pre-2025)
- Both proponents AND critics of LLM chess ability
- Geographic diversity (US, China, EU sources)
- If a source type is unavailable, document the gap

## Output Requirements

### Report Structure
1. Executive Summary (800-1500 words) — synthesize ALL major findings: the top open-source chess LLM, how it compares to proprietary, cost-efficiency, and implications for AI reasoning research
2. Introduction — scope, methodology, assumptions, key terms (chess notation, Elo, MoE, reasoning models, agentic framework) defined with ELI5
3. Main Analysis (4-8 findings, 600-2000 words each, with inline evidence)
   - Finding 1: The chess LLM benchmark landscape — what tests exist, what they measure
   - Finding 2: Open-source LLM chess gameplay rankings (Elo, win rates, completion)
   - Finding 3: Chess puzzle solving and knowledge understanding rankings
   - Finding 4: Instruction-following dimension (legal move rates, hallucination)
   - Finding 5: Cost-efficiency analysis — best chess per dollar
   - Finding 6: Why reasoning models dominate chess (and which open-source reasoning model wins)
   - Finding 7: General benchmarks as chess-ability predictors
   - Finding 8: Contrarian view — do LLMs actually play chess or just pattern-match?
4. Synthesis & Insights — cross-cutting patterns, the open-source chess LLM hierarchy
5. Limitations & Caveats — data gaps (few open-source models tested in chess), small sample sizes, benchmark methodology differences
6. Recommendations — best open-source LLM for chess by category (best overall, best free, best for self-hosting, best for puzzles)
7. Complete Bibliography — every citation [1]-[N], no placeholders
8. Methodology Appendix — research process, verification, confidence levels, data sources

### Quality Mandates
- EVERY factual claim followed by [N] citation in the same sentence
- No vague attributions ("research shows", "experts believe", "studies suggest")
- Distinguish facts FROM sources vs. your own synthesis explicitly
- For speculative content, label as "This suggests..." not "Research shows..."
- Minimum 3 independent sources per major claim
- Prose >=80%, bullets sparingly (only for distinct lists)
- No placeholder text, no "content continues", no ranges in bibliography
- Admit uncertainty: "No sources found for X" rather than fabricating
- ELI5 [imagine: ...] explanations throughout for technical terms

### Bias Safeguards
- Actively seek sources that contradict the finding that "LLMs can play chess"
- Flag when sources have financial interests (e.g., model providers)
- Note when chess research is sparse — don't fill gaps with speculation
- Distinguish correlation (high general benchmark = good chess) from causation
- Mark predictions (e.g., "LLMs will reach GM level by 2028") as [SPECULATION]

## Seed Keywords

### Core Terms
open-source LLM chess, LLM chess Elo, LLM chess benchmark, open-weight model chess, LLM chess leaderboard

### Benchmark Names
LLM CHESS benchmark, Dubesor AI Chess, Chess AI Bench, ChessQA, PGN2FEN, chess-bench.com, PuzzlePlex, Benedict Brady chess benchmark

### Open-Source Model Keywords
DeepSeek R1 chess, DeepSeek V3 chess, DeepSeek V4 Pro chess, Qwen 3 chess, Qwen 3.5 chess, GLM-5 chess, GLM-5.2 chess, Llama 4 Maverick chess, Llama 4 Scout chess, Kimi K2 chess, Kimi K2.5 chess, Mistral Large chess, Mistral chess, Gemma 4 chess, Phi-4 chess, MiMo chess, MiniMax chess, Nemotron chess

### Proprietary Model Baselines
GPT-5 chess Elo, Claude Opus 4.6 chess, Gemini 3.1 Pro chess Elo, o3 chess, o4-mini chess, Grok chess

### Technical Keywords
agentic chess LLM, tool-use chess, reasoning model chess, chain-of-thought chess, FEN, PGN, UCI, Stockfish analysis depth, Komodo Dragon, illegal move rate LLM, hallucinated move LLM, game completion rate, tokens per move

### Comparative Keywords
open source vs proprietary chess LLM, best free chess LLM, cheapest chess LLM, self-hosted chess AI, local LLM chess

### Contrarian Keywords
LLM cannot play chess, LLM chess memorization, LLM chess pattern matching, chess benchmark contamination, LLM chess failure modes

### Time-Specific
2026 LLM chess, 2025 LLM chess, latest chess LLM benchmark, June 2026 open-source LLM

## Mode
Deep Research (8-phase pipeline, multi-level BFS expansion, 216+ sources)
