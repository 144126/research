# Research Prompt: 1-Minute Timeframe LLM/Agentic AI Scalping Agents (in progress)

## Priority & Context
- **Priority: Critical.** This is the third and final narrowing of a research series. Prior reports established: (1) general AI scalping is FPGA-first, ML-second, with latency dominance, and (2) LLMs cannot drive direct scalping execution at microsecond timescales. THIS report asks: does the 1-minute timeframe change the calculus?

- **Target audience:** Building a production LLM scalping agent for 1-minute candles. Needs architecture recommendations, not theory.

- **Prior findings to leverage (not re-discover):**
  - Report 1 (ai_scalping_agent/): Latency and transaction costs dominate; retail scalping viable only in crypto without colocation; institutional stack is FPGA-first.
  - Report 2 (llm_scalping_agent/): LLM inference latency (500ms-5s cloud, 50-200ms self-hosted) is 100-5,000x too slow for microsecond scalping, but LLMs have roles in meta-tasks (regime detection, parameter optimization, alpha discovery) via centaur architectures.

- **Key new constraint:** 1-minute candles → 60-second decision window. LLM latency of 500ms-5s is 0.8-8% of the candle duration. At the edge with SLMs (10-50ms), it's 0.02-0.08%. This is the sweet spot where LLM reasoning speed may be viable.

## Core Research Questions (answer ALL with evidence)

### Q1: What 1-minute scalping strategies have the best verified track records?
- Which traditional (non-ML) 1-minute strategies produce the highest Sharpe ratios in published research?
- EMA crossover, RSI divergence, Bollinger Band squeeze, VWAP — which has the best backtested performance on 1-min data?
- What are the actual win rates, profit factors, and max drawdowns from credible backtests?
- How does performance vary by asset class (crypto vs forex vs equities) at the 1-minute timeframe?
- What is the real (not theoretical) transaction cost impact at 1-minute frequency?
- CITE specific numbers from peer-reviewed or institutional research.

### Q2: Can LLMs add value at the 1-minute candle frequency?
- What is the state of the art in LLM-based trading on sub-5-minute data as of mid-2026?
- Have any papers tested LLMs specifically on 1-minute candle sequences? If so, with what results?
- Can LLMs reliably interpret 1-minute candlestick patterns (doji, hammer, engulfing, etc.)?
- What are the concrete latency numbers for inference at each tier:
  - Cloud LLM API (GPT-4o, Claude, DeepSeek)
  - Self-hosted quantized 7B-13B (consumer GPU)
  - Edge-deployed SLM 1B-3B (phone, Raspberry Pi, Jetson)
  - Speculative decoding / streaming approaches
- Is there ANY published evidence of an LLM-based system generating positive returns on 1-minute data in live (not backtested) markets?

### Q3: What architecture would work for 1-minute LLM scalping?
- Multi-agent vs single-agent: does TradingAgents' firm-simulation architecture work at 1-minute speed?
- SLM-LLM hybrid: edge-deployed SLM for real-time decisions, cloud LLM for periodic meta-analysis? What SLMs are best (Phi-4, Llama 3.2, Qwen 2.5, Gemma 3)?
- RL + LLM: FinRL-DeepSeek/FLAG-Trader style hybrid — can RL handle the execution while LLM provides regime/sentiment signals?
- What is the minimal viable latency budget for a 1-minute strategy to work?
- What data pipeline is needed: tick → 1-min OHLCV → features → LLM → decision → execution?
- How often should the LLM be called: every candle, every N candles, or only at regime changes?
- What is the optimal model size vs latency tradeoff for this timeframe?

### Q4: What are the failure modes specific to 1-minute LLM scalping?
- Overfitting to noise: 1-minute data has the worst signal-to-noise ratio of any common timeframe
- Model drift: how quickly does an LLM-trained model degrade on 1-minute data?
- Transaction cost erosion: at what trade frequency do costs eliminate all edge?
- Slippage: how does delay between LLM decision and execution impact results?
- Look-ahead bias in backtests: what percentage of published 1-minute ML strategies fail in live trading?
- The 85% failure rate claim: what does the academic evidence actually show about scalping strategy survival?

### Q5: What is the gap between current research and a deployable system?
- Which papers have the most realistic assumptions (latency, costs, slippage)?
- What would a minimal viable 1-minute LLM scalping system look like today?
- What breakthrough would make 1-minute LLM scalping clearly viable (vs. currently marginal)?
- Are there any existing commercial or open-source systems doing this successfully?
- What is the honest assessment: is 1-minute LLM scalping a realistic goal for a solo developer in 2026?

## Source Requirements
- Minimum 200 sources
- At least 40% must be from 2025-2026
- Must include: peer-reviewed papers, institutional research, documented live trading results, failure postmortems
- Prioritize: papers with realistic assumptions about latency/cost/slippage > backtested strategies > theory papers > blog posts
- For all quantitative claims: cite specific numbers AND source
- Flag any source that is promotional/marketing content rather than objective research

## Structure Requirements
1. Executive Summary (TL;DR with clear answer to "can it work?")
2. 6-10 Major Findings, each with:
   - Clear claim
   - Evidence with inline [N] citations
   - ELI5 explanation in [imagine: ...] format
   - Counter-evidence or limitations
3. Architecture Recommendations (concrete, implementable)
4. Failure Mode Analysis (what will go wrong)
5. Gap Analysis (research to production)
6. Honest Verdict (can a solo dev build this in 2026?)
7. Full Source Index with URLs, dates, and credibility ratings

## Output Format
- Save to: ~/research/1min_scalping_llm_agent/
- Filename: index.md
- Min 5,000 words (prefer 8,000-12,000)
- Every factual claim must have inline [N] citation
- Include [imagine: ...] ELI5 explanations for each major finding
- Must pass validate_report.py and verify_citations.py
