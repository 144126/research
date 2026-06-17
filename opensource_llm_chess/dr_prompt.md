# DEEP RESEARCH COMMISSION

## Research Question
Which open-source (open-weight) large language model performs best at playing chess, and what specific capabilities, architectures, and reasoning mechanisms enable strong chess performance in LLMs?

## Purpose & Context
There is growing interest in whether LLMs can play chess as a proxy for evaluating reasoning, planning, instruction-following, and state-tracking abilities. Unlike traditional chess engines (Stockfish, Leela Chess Zero) that use specialized search algorithms, LLMs must reason about chess positions purely through natural language interaction and generated text. The LLM Chess benchmark (Kolasani et al., accepted at ICLR 2026) and the LLM Chess Leaderboard (maxim-saplin.github.io/llm_chess/) have begun systematically evaluating models. However, no definitive answer exists for which open-source model is best specifically at chess. This research serves developers, AI researchers, and hobbyists who want to run chess-playing LLMs locally or understand the relationship between general reasoning capability and chess performance.

### Audience
- Primary: AI/ML engineers and researchers evaluating open-source LLMs for reasoning-intensive tasks
- Secondary: Chess enthusiasts interested in LLM-based chess play
- Tone: Precise, data-driven, technical but accessible
- Complexity: Academic-level depth with inline ELI5 explanations for difficult concepts
- Child-reader adaptivity: Yes — every hard concept must have an inline [imagine: ...] explanation

### Decision Context
- Which open-weight model to self-host for chess analysis/play
- Understanding whether chess performance correlates with general reasoning benchmarks
- Evaluating whether reasoning models (DeepSeek-R1, Kimi K2 Thinking, QwQ) actually outperform standard instruction-tuned models at chess
- Determining the practical utility of LLMs vs. traditional chess engines

## Research Scope

### In Scope
1. All open-weight/open-source LLMs tested on chess-related benchmarks (LLM Chess, PGN2FEN, custom evaluations)
2. Chess played through natural language/agentic interaction (text-based moves, UCI notation)
3. Traditional chess engines (Stockfish, Lc0) only as baseline comparison points, NOT as primary subjects
4. Reasoning models vs. non-reasoning models — head-to-head chess comparisons
5. Correlation between chess Elo and standard reasoning benchmarks (AIME, GPQA, MATH)
6. Technical analysis of WHY certain models perform better at chess (architecture, training data, reasoning mechanisms)
7. Hardware requirements to run chess-capable open-source models locally

### Out of Scope
1. Proprietary/closed models (GPT, Claude, Gemini) except as benchmark reference points
2. Traditional chess engines as primary subject
3. Chess puzzle generation or chess notation conversion as primary focus (PGN2FEN is secondary)
4. Fine-tuning LLMs specifically for chess
5. Reinforcement learning from self-play (AlphaZero-style approaches)

### Timeframe
2024-2026, with emphasis on 2025-2026 (reasoning models era). Foundational work (LLM Chess benchmark 2024, early GPT-4o/Claude testing 2024) included for context.

### Geographic Focus
Global — open-source models from US (Meta Llama, Mistral, Google Gemma), China (DeepSeek, Alibaba Qwen, Zhipu GLM, Moonshot Kimi), and others.

## Required Dimensions of Investigation

1. **Technical/Mechanistic Exploration**
2. **Historical Context & Evolution**
3. **Current State-of-Art**
4. **Quantitative Evidence**
5. **Stakeholder Analysis**
6. **Competing Approaches Comparison**
7. **Criticisms & Limitations**
8. **Contrarian & Heterodox Perspectives**
9. **Future Trajectories & Predictions**
10. **Regulatory, Legal & Ethical Dimensions**
11. **Geographic & Geopolitical Variation**
12. **Practical Applications & Case Studies**

## Source Requirements
- Source Types Required (ALL must be represented): Academic, Industry, Technical, News, Primary, Expert, Contrarian, Chess-specific
- Minimum Source Count: 216+
- Multi-level BFS expansion: Level 1 (200-300) from seed queries, Level 2+ (600-1500+) from references

## Output Requirements

### Report Structure
1. Executive Summary (800-1500 words)
2. Introduction — scope, methodology, assumptions, key terms with ELI5
3. Main Analysis (4-8 findings)
4. Synthesis & Insights
5. Limitations & Caveats
6. Recommendations
7. Complete Bibliography
8. Methodology Appendix

### Quality Mandates
- EVERY factual claim followed by [N] citation
- Distinguish facts FROM sources vs. synthesis explicitly
- Label speculative content as [SPECULATION]
- Minimum 3 independent sources per major claim
- Prose >=80%, bullets sparingly
- Inline ELI5 explanations [imagine: ...] for every hard concept

## Seed Keywords

Core terms: LLM chess, open-source LLM chess, language model chess, chess-playing LLM, LLM Chess Leaderboard, LLM CHESS benchmark, ICLR 2026 chess

Reasoning models: DeepSeek-R1 chess, Kimi K2 chess, Kimi K2.5 chess, Kimi K2 Thinking chess, QwQ chess, GLM-5 chess, Qwen chess, Llama chess, Gemma chess, Mistral chess

Benchmarks: LLM Chess Elo, random player LLM chess, Komodo Dragon LLM chess, PGN2FEN benchmark, AIME GPQA correlation chess, SWE-bench chess correlation

Technical: chain-of-thought chess, LLM chess hallucination, move legality LLM, instruction following chess, agentic chess, board state tracking LLM

People: Maxim Saplin LLM chess, Sai Kolasani LLM CHESS, Nicholas Crispino, Jared Quincy Davis, Matei Zaharia, Chi Wang

Evaluation: win rate vs random, game duration LLM chess, tokens per move chess, cost per Elo LLM, LLM Elo rating chess

Deployment: Ollama chess LLM, llama.cpp chess, vLLM chess, quantized chess LLM, self-hosted chess AI, local LLM chess

Contrarian: LLM not reasoning chess, gpt-3.5-turbo-instruct chess, LLM pattern matching chess, training data contamination chess, LLM chess skepticism
