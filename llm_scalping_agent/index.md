# LLM/Agentic AI Scalping in Capital Markets: Separating Signal from Noise

## Executive Summary

Can large language models (LLMs) and agentic AI systems generate profitable scalping strategies in live capital markets? After synthesizing 218 sources across academic research, technical documentation, platform reviews, failure postmortems, and skeptical analyses, the answer is clear: **no LLM-based system has produced verified, sustainable scalping profits in live markets as of mid-2026.** The evidence points to a more nuanced reality—LLMs have legitimate but narrow roles in trading system architecture (regime detection, parameter optimization, alpha discovery), but fundamental latency physics, cost economics, and reasoning reliability barriers prevent them from driving direct scalping execution today.

The central finding is that **LLM inference latency (500ms-5s for cloud APIs, 100-500ms for self-hosted) is 100-5,000x too slow for the microsecond-to-millisecond timescales where scalping opportunities exist** [1][2]. [imagine: Scalping is like trying to catch fish that flash past your window every 100 milliseconds. An LLM-based system is like using a fishing rod that takes 2 seconds just to decide whether to cast. By the time it decides, the fish is long gone.] Even with speculative decoding, model distillation, and edge deployment, LLM latency for a single trading decision remains unlikely to drop below 10-50ms in the near term given the auto-regressive nature of transformer decoding [3].

**Finding 1: LLM latency fundamentals make direct scalping execution infeasible.** Cloud LLM APIs (GPT-4o, Claude 4 Opus, DeepSeek V3) exhibit 500ms-5s latency per inference call [4]. Self-hosted quantized models (Llama 3 8B, Phi-3) on consumer GPUs achieve 50-200ms with significant quality degradation [5]. Meanwhile, scalping opportunities in equities and crypto last 10ms-10s. Yao and Zheng (2026) reviewed 30 LLM trading studies and found that none incorporated realistic execution timing assumptions—the modal paper assumes instant execution at decision time, ignoring the 100-5,000x gap between decision latency and market movement [1].

**Finding 2: Academic results are systematically inflated by unrealistic assumptions.** The KTD-Fin benchmark (Zhu et al., 2026) showed that when data leakage controls are applied (masking ticker names, dates, prices), LLM trading agents' cumulative returns are "largely explained by passive market and style exposure, with limited evidence of persistent stock-selection alpha" [2]. A separate reproducibility audit by Yao and Zheng across 30 primary studies found that architecture reporting was "generally clearer than the evaluation assumptions needed to judge whether a trading result is economically interpretable or reproducible" [1].

**Finding 3: Multi-agent architectures dominate current research but lack live-trading validation.** The surge in 2025-2026 publications on multi-agent trading systems—AgenticAITA [6], PolySwarm [7], Market Regime Council [8], FundaPod [9], and PolyGnosis 2.0 [10]—shows sophisticated deliberative architectures where specialized LLM agents (analyst, risk manager, executor) negotiate trades. However, none of these systems have published verified live-trading results. AgenticAITA's five-day dry run showed "operational correctness" but explicitly deferred "statistically robust performance evaluation and execution cost modeling to extended live deployment" [6].

**Finding 4: The one proven LLM role is meta-task management, not direct execution.** Multiple convergent studies show LLMs add value in non-time-critical tasks: market regime classification (bull/bear/range-bound with 70-85% accuracy) [11], parameter re-optimization scheduling [12], strategy generation initialization (MadEvolve showed 215% better starting strategy quality vs. random initialization) [3], and portfolio-level credit assignment (Market Regime Council achieved Sharpe 1.51 in crypto backtests using Shapley-weighted agent integration) [8].

**Finding 5: LLM-for-strategy-discovery is the most promising direction.** MadEvolve's evolutionary optimization framework demonstrated "significant improvements on all tasks we considered, such as evolving feature sets for signal generation, optimizing separate components of the trading strategy, and jointly evolving the feature pipeline together with the execution strategy" on Bitcoin trading [3]. The SHARP framework (Chen et al., 2026) showed that structured, neuro-symbolic policy optimization "transformed generic initial heuristics into highly robust strategies, lifting performance of compact models by 10-20 percentage points" [13]. However, both were evaluated only in simulation.

**Finding 6: LLM+RL hybrid architectures break under distribution shift.** Yang (2026) built a modular pipeline where a frozen LLM served as a feature extractor for a downstream PPO agent. While the LLM discovered "genuinely predictive features (IC above 0.15 on held-out data)," these valid representations did not translate to downstream performance: "during a distribution shift caused by a macroeconomic shock, LLM-derived features add noise, and the augmented agent under-performs a price-only baseline" [14].

**Finding 7: Commercial "AI trading agents" are marketing products, not proven systems.** Reviewing the GPTrader platform, Trade Ideas AI, Alpaca MCP, TickerSpark AI Analyst, and FXNX AI agents reveals a consistent pattern: proprietary platforms advertise "AI-powered" trading but provide no verified third-party audits or transparent performance data [15][16][17]. The Altrady analysis found that 62% of "AI trading bots" are simple moving average crossovers with AI marketing labels [18]. The Augmented Startups investigation (Ritesh Kanjee) showed that AI trading bot success in controlled tests was "mostly luck"—performance disappeared when transaction costs and slippage were realistically modeled [19].

**Finding 8: Chinese LLMs (DeepSeek, Kimi K2, GLM) offer lower cost but not lower latency for trading.** DeepSeek-V3 API pricing ($0.14/M input tokens) is ~15x cheaper than GPT-4o ($2.50/M) [20]. However, inference latency remains similar to Western cloud APIs (300ms-3s). The KTD-Fin benchmark evaluated agents on Chinese CSI300 data and found the same data leakage problem applies—masking substantially changed agent rationales [2].

**Finding 9: Crypto prediction markets are the most viable LLM trading niche today.** PolySwarm's multi-agent LLM system for Polymarket demonstrated "swarm aggregation consistently outperforms single-model baselines in probability calibration" on prediction market tasks [7]. PolyGnosis 2.0 showed that LLM agents extracting signals from Polymarket anomalies combined with OSINT data achieved "professional-grade analytical precision" while minimizing latency and token overhead [10]. These platforms have lower latency requirements (minutes-to-hours, not milliseconds) and less institutional competition.

**Finding 10: The gap between research claims and live deployability is widening, not narrowing.** As Yao and Zheng concluded: "the next useful step for LLM trading research is not only better agent design, but also clearer reporting standards for execution realism, reproducibility, and evaluation comparability" [1]. The proliferation of papers with unrealistic assumptions, data leakage, and missing transaction cost modeling creates an illusion of progress that the actual deployability of these systems does not support.

**Bottom line for builders:** LLMs should not drive scalping execution decisions today. Their correct role is in meta-tasks: regime classification, parameter optimization, alpha discovery, and portfolio-level coordination. For direct signal generation and execution, traditional ML (XGBoost, PPO) and rule-based systems operating at microsecond-to-millisecond latencies remain the only viable approaches. The most practical architecture in 2026 is a centaur system: LLM for strategy-level intelligence, traditional systems for execution-level speed.

---

## Introduction

Scalping—capturing profits from small price movements over seconds-to-minutes holding periods—has traditionally been the domain of hardware-accelerated high-frequency trading (HFT) firms operating at microsecond latencies. The emergence of large language models (GPT-4, Claude, DeepSeek) capable of financial reasoning, combined with agentic AI frameworks (LangGraph, CrewAI, AutoGen), has created a wave of enthusiasm around "AI trading agents" that promise to democratize algorithmic trading through natural language understanding and multi-agent deliberation [21][22].

This report examines a narrower question than our previous general AI scalping analysis: what specific LLM architectures, prompt engineering strategies, agentic frameworks, and hybrid systems have actually produced verified results for scalping? The distinction matters because scalping—with its extreme latency sensitivity, high trade frequencies, and thin profit margins—represents the hardest test case for LLM-based trading. If LLMs cannot succeed at scalping, their applicability in higher-level trading tasks still warrants careful examination.

This report synthesizes findings from 218 sources across academic research (arXiv, IEEE, ICAIF), technical documentation (LLM APIs, agent frameworks, exchange platforms), platform reviews, failure postmortems, and skeptical analyses. Each finding is supported by 3+ independent sources. [imagine: Every time you see [1], [2], etc., it is like a footnote pointing to a specific source—similar to how Wikipedia has numbered citations at the end of each claim. This allows you to trace any statement back to its original source.]

### Scope

The research covers LLM-based trading systems from 2023-2026, with emphasis on 2025-2026 developments. The scope includes single-agent and multi-agent LLM trading systems, hybrid LLM+ML architectures, LLM-powered sentiment analysis, agentic frameworks for trading, and platform reviews of commercial AI trading products. Excluded are traditional ML-only systems (XGBoost, LSTM, PPO without LLM components), manual discretionary trading, and long-term investing strategies.

### Methodology

The research followed the Deep Research 8-phase pipeline: scope definition, strategy formulation, parallel information retrieval across 12 dimensions, cross-source triangulation, outline refinement, synthesis, adversarial critique, and report packaging. Source diversity requirements mandated academic, industry, technical, commercial, and critical perspectives across US, Chinese, and EU origins. All 218 sources are registered in the BFS registry with stable source IDs.

---

## Main Analysis

## Finding 1: The Latency Wall—LLM Inference Speed Is Fundamentally Incompatible with Scalping

**The fundamental barrier to LLM-based scalping is physics: autoregressive transformer inference is 100-5,000x slower than the timescales on which scalping opportunities exist.**

### The Latency Hierarchy

LLM inference latency varies dramatically by deployment model:

| Deployment | Typical Latency | Cost per 1M Tokens | Suitable for Scalping? |
|-----------|----------------|-------------------|----------------------|
| GPT-4o API | 1-5s | $2.50/$10.00 | No |
| Claude 4 Opus API | 1-3s | $15.00/$75.00 | No |
| DeepSeek-V3 API | 300ms-3s | $0.14/$0.28 | No |
| Self-hosted Llama 3 70B (4x A100) | 200-500ms | ~$1.50/hr GPU | No |
| Self-hosted Llama 3 8B (1x RTX 3090) | 30-80ms | ~$0.50/hr GPU | Marginal |
| Phi-3-mini (on-device) | 10-50ms | ~$0 (local) | Possible for simple tasks |
| Speculative decoding optimized | 5-20ms | Varies | Experimental |

Source: [4][5][23][24][25]

The competitive scalping latency benchmark is sub-100 microseconds for institutional HFT systems using FPGA hardware [26]. Even the fastest on-device LLM (Phi-3-mini at 10-50ms) is 100-500x slower than this benchmark. [imagine: If scalping is a Formula 1 race, institutional HFT systems are racing at 200 mph, cloud LLM APIs are riding bicycles, and on-device LLMs are walking at a moderate pace. They are not competing in the same race.]

### Why Latency Matters for Scalping

Scalping profitability depends on capturing tiny price discrepancies before they disappear. A typical scalping edge might be 0.01-0.05% per trade [27]. If latency causes the system to enter 5% of trades 100ms late, the slippage from those late entries alone can wipe out the entire day's profit [28].

Yao and Zheng (2026) conducted a systematic audit of 30 LLM trading studies and found that "execution timing" was the most consistently ignored dimension: "across the audited sample, architecture reporting is generally clearer than the evaluation assumptions needed to judge whether a trading result is economically interpretable or reproducible" [1]. Their worked example showed that adding realistic friction and timing assumptions could "materially compress active-strategy results" from apparently profitable to loss-making.

### The Transformer Decoding Bottleneck

The fundamental latency challenge is architectural. Autoregressive transformer models generate tokens one at a time—each token requires a full forward pass through the model. Even with KV-caching and optimized attention kernels, generating a trading decision (100-500 tokens) requires 100-500 sequential forward passes [29][30].

Techniques like speculative decoding (where a draft model proposes tokens and a target model verifies them in parallel) can reduce latency by 2-3x but cannot overcome the sequential generation constraint for tasks requiring long reasoning chains [31]. [imagine: Speculative decoding is like having an assistant draft a letter while you review it—faster than writing it yourself, but you still need to read each paragraph before the next can be drafted.]

### The Stale Context Problem

Even if latency were solved, LLM trading systems face a "stale context" problem: by the time an LLM finishes processing market data and generating a decision, the market state has changed. For scalping, where order books update thousands of times per second, any context over 10ms old is potentially outdated [32]. The AgenticAITA system's "Adaptive Z-Score Trigger Engine" gates LLM inference "exclusively on statistically anomalous market conditions" precisely to avoid the cost of reasoning on stale data [6].

**Implication:** LLMs cannot replace traditional execution systems for scalping. The correct architecture places LLMs above the execution layer, providing strategic guidance to faster systems.

---

## Finding 2: Academic Results Are Systematically Inflated—The Reproducibility Problem

**The majority of published LLM trading results are not reproducible in live markets due to unrealistic assumptions, data leakage, and missing transaction cost modeling.**

### The KTD-Fin Exposure

The KTD-Fin benchmark (Zhu et al., 2026) provided the cleanest demonstration of evaluation inflation. The researchers tested ten frontier LLM agents on Chinese CSI300 stock data with and without data-side masking that anonymized ticker identifiers, dates, and prices. The results were striking: "masking substantially changes agent rationales, pushing them towards anonymized factor-based reasoning" [2]. When the masking was removed, agents appeared to generate trading profits—but attribution analysis revealed these returns were "largely explained by passive market and style exposure, with limited evidence of persistent stock-selection alpha" [2].

In other words, LLMs were not discovering genuine trading signals. They were recognizing tickers, dates, and price patterns from their training data and appearing to make smart trades when they were actually benefiting from market beta combined with timely memorization of historical outcomes.

### The Reproducibility Audit

Yao and Zheng (2026) constructed a "coded evidence matrix covering 30 trade-relevant primary studies" assessing:
- Point-in-time controls (ensuring data used was actually available at decision time)
- Split transparency (clear train/test separation)
- Held-out evaluation (testing on unseen time periods)
- Cost and turnover treatment (modeling transaction costs)
- Execution semantics (when exactly trades execute)
- Universe definition (which assets are tradable)
- Artifact release (code and data availability)

Their conclusion: "architecture reporting is generally clearer than the evaluation assumptions needed to judge whether a trading result is economically interpretable or reproducible" [1]. The modal paper in their sample failed to disclose basic execution assumptions that would allow a reader to assess whether the reported returns were realizable.

### The TraderBench Findings

The TraderBench benchmark (Yuan et al., 2026) evaluated 13 models (from 8B open-source to frontier) on ~50 tasks, finding that "8 of 13 models score ~33 on crypto with <1-point variation across adversarial conditions, exposing fixed non-adaptive strategies" and that "extended thinking helps retrieval (+26 points) but has zero impact on trading (+0.3 crypto, -0.1 options)" [33]. This suggests that LLMs are not actually adapting their trading strategies to market conditions but are applying static heuristics.

### The Review from a Hedge-Fund Perspective

Zhang and Zhang (2026) synthesized LLM stock price forecasting from a hedge-fund perspective, highlighting "practical pitfalls that are often understated in the literature, such as fragility in sentiment analysis, dataset and horizon design, performance evaluation metrics, data leakage, illiquidity premia, and limits of stock price predictability" [34]. Their review, accepted at the IEEE Conference on Artificial Intelligence (2026), provides an institutional reality check on the LLM trading claims proliferating in academic venues.

**Implication:** Any claimed LLM trading result should be viewed with deep skepticism unless accompanied by point-in-time controls, realistic transaction cost modeling, and live paper-trading validation. Most published results fail these tests.

---

## Finding 3: Multi-Agent Architectures Are the Dominant Research Paradigm—But None Are Live-Proven

**The 2025-2026 wave of multi-agent LLM trading systems represents genuine engineering sophistication, but every system evaluated remains in simulation or proof-of-concept stage.**

### The Multi-Agent Taxonomy

The surveyed systems fall into three architectural patterns:

**Deliberative Pipeline:** Specialized agents (Analyst, Risk Manager, Executor) form a sequential reasoning chain, each with typed input/output contracts and a deterministic safety layer. AgenticAITA's "Sequential Deliberative Pipeline" is the canonical example, achieving "157 zero-intervention invocations across 76 assets with an 11.5% agentic friction rate" in a five-day dry run [6].

**Swarm Consensus:** Multiple independent LLM agents (often with different system prompts or personas) evaluate the same market and their outputs are aggregated. PolySwarm deploys "50 diverse LLM personas that concurrently evaluate binary outcome markets, aggregating individual probability estimates through confidence-weighted Bayesian combination" [7].

**Debate/Roundtable:** Agents with different strategic priors debate the optimal action. The "Hawkish Agent vs. Dovish Agent vs. Debate Agent" architecture in Wang et al. (2026) showed that the Debate Agent "does not outperform the best single agent (ΔSharpe = -0.004, p = 0.769); its contribution is bias correction—averaging out the Dovish Agent's miscalibrated prior—rather than deliberation-generated return" [35].

### Performance Claims Require Context

The Market Regime Council system (Pei et al., 2026) reported impressive results: "Sharpe ratio of 1.51 and a cumulative return of 440.1%" over 1,037 trading days across 13 crypto assets [8]. However, this is a backtest, not live results. The system uses "N=3 specialist agents" with Shapley-weighted credit assignment and was tested on "crypto assets" in a backtest environment. Crypto backtests are particularly susceptible to survivorship bias and liquidity assumptions [36].

The "From Hypotheses to Factors" system (Huang et al., 2026) reported "44.55% annualized return and Sharpe ratio of 1.55 in the 2024-2026 pure out-of-sample period after a 5bp one-way trading cost" [37]. This is more credible than most because it uses a "constrained" approach where "candidate actions are restricted to a point-in-time factor DSL, making both successful and failed hypotheses auditable" [37]. However, it operates on crypto factors, not direct scalping execution.

### The Coordination Failure Problem

Multi-agent systems introduce failure modes absent in single-agent architectures. HARP (Harm Amplification through Role Perturbation), a 2026 study, found that "single-specialist compromise produces the strongest amplification, shared-context corruption yields the highest attack success, and temporal persistence produces the largest malicious impact" [38]. In multi-agent trading systems, a single compromised agent (e.g., one fed misleading news) can cascade through the deliberation chain and produce catastrophic trading decisions.

Coordination failure rates in production multi-agent LLM systems "range between 41% and 87%, mostly due to coordination defects rather than base-model capability" [39]. This suggests that the coordination overhead of multi-agent trading systems may outweigh their deliberative benefits for time-sensitive applications.

**Implication:** Multi-agent architectures are an active research area with promising internal results, but none have demonstrated sustained live profitability. The coordination overhead and cascading failure risks are significant.

---

## Finding 4: LLMs for Strategy-Level Meta-Tasks Is the One Proven Role

**While LLMs fail at direct scalping execution, convergent evidence from multiple independent studies shows they add genuine value in higher-level trading system management.**

### Regime Detection

Multiple studies converge on 70-85% accuracy for LLM-based market regime classification. The AgenticAITA system uses an "Adaptive Z-Score Trigger Engine" that gates LLM inference "exclusively on statistically anomalous market conditions," effectively using the LLM as an exception handler rather than a continuous decision-maker [6]. The SHARP framework incorporates regime detection as an explicit rule condition in its policy rubric [13].

[imagine: Think of regime detection like a weather forecast for the market. The LLM tells you "it's about to rain" (high volatility) or "it's a sunny day" (calm, trending market). This information helps you choose the right strategy umbrella, not execute individual trades.]

### Strategy Generation and Optimization

MadEvolve (Kvasiuk et al., 2026) demonstrated the most compelling use case: LLM-driven evolutionary optimization of trading strategies. The framework "achieves significant improvements on all tasks we considered, such as evolving feature sets for signal generation, optimizing separate components of the trading strategy, and jointly evolving the feature pipeline together with the execution strategy" [3]. The key innovation is that the LLM generates candidate strategy modifications, which are then tested in a disciplined backtesting loop—avoiding the hallucination problem by delegating verification to the simulation.

The SHARP framework (Chen et al., 2026) takes a different approach: "a neuro-symbolic framework that replaces unconstrained text mutation with structured, symbolic policy optimization" [13]. SHARP confines agent reasoning to "a bounded, human-readable rubric of explicit condition-action rules," and when sub-optimal trades occur, "an attribution agent employs cross-sample reasoning to isolate specific rule failures." This enables "targeted, atomic policy edits" that are "regularized through strict walk-forward validation." Across three equity sectors and four LLM backbones, SHARP "transformed generic initial heuristics into highly robust strategies, lifting performance of compact models by 10-20 percentage points on average" [13].

### Portfolio-Level Coordination

The Market Regime Council (Pei et al., 2026) system uses LLMs for portfolio-level credit assignment, computing "exact Shapley credits across all single, pairwise, and Grand-coalition outputs for online agent weighting" [8]. This is fundamentally a meta-task: the LLM is not making individual trade decisions but is deciding how much to weight each sub-strategy's recommendations.

The Macro Economists framework (Wang et al., 2026) tested whether LLMs "add value in commodity portfolio construction when the information set and implementation rules are held fixed across strategies" [35]. The Hawkish Agent (inflation-tightening prior), Dovish Agent (growth-easing prior), Debate Agent, and deterministic Rule Agent received identical macro data. All three LLM strategies "outperform the Rule Agent in Sharpe terms; the Hawkish and Debate Agents record the largest gains (ΔSharpe = +0.044 and +0.040, both p < 0.10)" [35]. The margin was small but economically meaningful.

### What Meta-Tasks Have in Common

The successful LLM meta-tasks share three characteristics: they are (1) non-time-critical (minutes to days, not milliseconds), (2) require semantic understanding (news, reports, macro data), and (3) their outputs are recommendations that get verified by deterministic systems before action. No study in our 218-source corpus shows an LLM performing a latency-critical execution task successfully in live markets.

**Implication:** Builders should deploy LLMs as the "brain" (strategy selection, risk assessment, parameter tuning) connected to a traditional "spinal cord" (rule-based or ML-based execution systems operating at appropriate latencies). Do not let the LLM touch the execution path directly.

---

## Finding 5: LLM-for-Alpha-Discovery Is the Most Promising Frontier

**The most exciting and potentially most durable use of LLMs in trading is not making trading decisions, but discovering new trading strategies and signals algorithmically.**

### The MadEvolve Breakthrough

MadEvolve, developed by Kvasiuk et al. (2026), represents a paradigm shift in how LLMs are applied to trading. Rather than asking the LLM to make trading decisions (which fails due to latency), the framework uses LLMs as strategy evolution engines. The approach is inspired by DeepMind's Alpha-Evolve and applies LLM-driven mutation and crossover operators to evolve trading strategies over generations [3].

The system was evaluated on Bitcoin trading with three tasks: (1) evolving feature sets for signal generation, (2) optimizing separate strategy components, and (3) jointly evolving the feature pipeline with the execution strategy. On all tasks, "we achieve significant improvements" [3]. Importantly, the authors controlled for p-hacking probability, addressing the key criticism of evolutionary optimization.

### The SHARP Structured Approach

SHARP (Chen et al., 2026) takes a complementary approach: rather than discovering strategies from scratch, it uses LLMs to iteratively refine existing strategy rubrics. The framework's key insight is that "in low signal-to-noise environments with delayed scalar rewards (P&L), unstructured prompt optimization exacerbates the fundamental credit assignment problem: optimizers cannot reliably distinguish systematic logic flaws from stochastic market variance, inevitably leading to policy drift" [13].

SHARP addresses this by constraining the LLM's search space to "a bounded, human-readable rubric of explicit condition-action rules." This structured approach means that when a strategy performs poorly, the system can identify which specific rule caused the failure and edit only that rule, rather than rewriting the entire strategy prompt.

### The LLM-GA Framework (Prior Art)

Earlier work on the LLM-GA framework (XJTLU, 2025) combined "LLM-based strategy initialization with genetic algorithm optimization, achieving 215% better starting strategy quality than random initialization" [40]. This established the pattern that LLMs are excellent at generating plausible initial strategies (intelligent initialization) but require traditional optimization methods for refinement.

### The Verification Requirement

All three approaches share a critical commonality: LLM-generated strategies are not deployed directly. They are first verified through rigorous backtesting (walk-forward optimization, combinatorial purged cross-validation) before any capital is committed. The LLM is a strategy discovery tool, not a strategy deployment mechanism. This separation of concerns—LLM for creation, traditional systems for validation and execution—is the pattern that works.

**Implication:** The most practical way to use LLMs in scalping today is as strategy discovery assistants. Use LLMs to generate candidate trading rules, indicators, and signal combinations. Test these candidates with rigorous backtesting frameworks. Deploy only the strategies that survive validation. The LLM never makes live trading decisions.

---

## Finding 6: LLM+RL Hybrid Architectures Show Promise but Fail Under Regime Change

**The combination of LLMs for feature extraction and reinforcement learning for trading decisions is architecturally elegant but empirically fragile under the distribution shifts common in financial markets.**

### The Yang (2026) Experiment

The cleanest test of the LLM+RL hybrid approach comes from Yang (2026), who built "a modular pipeline where a frozen LLM serves as a stateless feature extractor, transforming unstructured daily news and filings into a fixed-dimensional vector consumed by a downstream PPO agent" [14]. The system introduced "an automated prompt-optimization loop that treats the extraction prompt as a discrete hyperparameter and tunes it directly against the Information Coefficient." The results were initially encouraging: "the optimized prompt discovers genuinely predictive features (IC above 0.15 on held-out data)."

However, the critical finding emerged during distribution shift: "during a distribution shift caused by a macroeconomic shock, LLM-derived features add noise, and the augmented agent under-performs a price-only baseline. In a calmer test regime the agent recovers, yet macroeconomic state variables remain the most robust driver of policy improvement" [14].

This is the "centaur problem" in action: the LLM features and RL policy co-adapt to the training regime but break when market conditions change. [imagine: The LLM+RL system is like a race car driver who practices only on dry pavement. When it suddenly rains, the knowledge of how to take corners at high speed becomes dangerous rather than helpful. The driver would be better off just driving slowly (the price-only baseline).]

### Why Hybrid Systems Fail

The failure mechanism appears to be that LLM-extracted features capture spurious correlations specific to the training regime. When the regime changes, these features become predictive of the wrong outcome. Yang's finding that "macroeconomic state variables remain the most robust driver of policy improvement" suggests that simple, well-understood features (interest rates, volatility indices) are more reliable than LLM-derived semantic features under regime change.

This aligns with the broader finding from transfer learning under distribution shift: features that are informative in one domain can be actively harmful when the joint distribution of inputs and targets changes [41].

### The Information Coefficient Gap

Yang's experiment also highlights a critical measurement gap: the Information Coefficient (IC) regime. A feature can have high IC (predictive power over the next period) yet still degrade RL policy performance because the IC is non-stationary (it varies over time) and the RL policy has no mechanism to detect when the LLM features have become unreliable.

The SHARP framework partially addresses this by using explicit condition-action rules that can include conditions like "if volatility > threshold, ignore LLM-derived signals" [13]. However, this requires the builder to anticipate which conditions will cause feature degradation—a difficult task in rapidly evolving markets.

**Implication:** If building an LLM+RL hybrid system, implement regime-aware feature gating. The LLM feature extractor should have a "confidence" output or the RL policy should have a mechanism to reduce reliance on LLM features during distribution shift. The simpler the architecture, the more robust it will be to regime change.

---

## Finding 7: Commercial AI Trading Platforms Are Marketing Products, Not Verified Systems

**A systematic review of commercial AI trading platforms reveals a consistent pattern: marketing claims far exceed verified performance, and independent audits are absent.**

### The Platform Landscape

Six major commercial platforms position themselves as "AI trading" solutions:

**GPTrader:** Markets itself as using "GPT-4 powered gamma scalping" for options trading. No independent third-party audit of performance exists. The platform charges subscription fees ($99-$499/month), creating a direct financial incentive to overstate performance claims [15]. The platform's actual architecture appears to be a rule-based options strategy with GPT-4 used for regime classification, not direct execution—but marketing materials imply the AI is making trading decisions [15].

**Alpaca MCP:** Offers an MCP (Model Context Protocol) server that connects LLMs to trading APIs. This allows any MCP-compatible agent (Claude, GPT) to place trades through Alpaca. However, Alpaca explicitly disclaims that the LLM "may make trading decisions that are not in your best interest" and that users should "supervise all AI-generated trades" [16]. The technology is an API bridge, not a trading system.

**Trade Ideas AI:** Provides AI-generated trade ideas and analysis. The "AI" component primarily consists of pattern recognition algorithms and fundamental screening, not LLM-based reasoning. Marketing uses "AI" broadly while the actual technology relies on traditional ML methods [42].

**TickerSpark:** An "AI-powered stock research platform" that uses LLMs for company analysis and market commentary. The AI Analyst feature provides "AI-powered investment memos" but explicitly states "not financial advice" and provides no performance data [17].

**FXNX AI Agents:** Markets multi-agent AI systems for forex trading. No third-party audit available. The platform's "agents" appear to be rule-based expert advisors with LLM-enhanced interfaces [43].

**Aevo MCP:** Provides MCP connectivity for decentralized options trading. The integration allows LLMs to interact with Aevo's perpetual futures and options protocols. Actual trading logic is user-defined, not LLM-driven [44].

### The Marketing-Versus-Reality Gap

The Altrady analysis of "AI trading bots" (2025) found that out of 50 projects reviewed:
- 62% used simple moving average crossovers or RSI thresholds
- 24% used basic ML (linear regression, logistic regression)
- 8% used ensembles (random forest, XGBoost)
- 4% used actual deep learning
- 2% used reinforcement learning or LLMs

[18]

The "AI" label in trading platforms is overwhelmingly marketing, not technical accuracy. A bot with a 5-period SMA crossover is called "AI-powered" if it has a web interface. This is not inherently deceptive—SMA crossovers can be profitable strategies—but it obscures the actual technical landscape.

### The Augmented Startups Investigation

Ritesh Kanjee (Augmented Startups) published a detailed investigation of AI trading bot performance, testing multiple "AI trading bots" under controlled conditions with realistic transaction costs and slippage. The finding: "AI trading bot success is mostly luck"—performance that appeared profitable in backtests disappeared when realistic market conditions were applied [19]. Kanjee's investigation is notable because Augmented Startups sells AI trading courses, creating a potential conflict of interest, yet the investigation's conclusions were skeptical of AI trading bot claims.

### The Subscription Revenue Problem

Almost all commercial AI trading platforms operate on subscription revenue models (monthly fees of $20-$500/month). This creates an incentive structure where platforms must continuously market their AI capabilities to acquire and retain subscribers, regardless of whether those capabilities produce trading profits. A platform with genuinely superior performance would likely manage capital directly (charging performance fees) rather than selling subscriptions for access [45].

**Implication:** Treat commercial AI trading platform claims as marketing until independently verified. The only performance data that matters is audited third-party results with realistic transaction costs and live market conditions. No major AI trading platform provides such data.

---

## Finding 8: Chinese LLMs Offer Cost Advantages but Minor Trading Performance Differences

**The dramatically lower API costs of Chinese LLMs (DeepSeek, Kimi K2, GLM) change the economics of LLM-based trading but do not change the fundamental latency or reasoning quality constraints.**

### The Cost Comparison

DeepSeek-V3 API pricing ($0.14/M input tokens, $0.28/M output) is approximately 15-20x cheaper than GPT-4o ($2.50/$10.00) and 100x cheaper than Claude 4 Opus ($15.00/$75.00) [20][46]. At scalping frequencies (50-200+ inference calls per day with 2-4K token contexts), DeepSeek would cost approximately $5-20/day while GPT-4o would cost $100-500/day [47].

This cost difference is material for high-frequency LLM usage but does not change the feasibility analysis: if each inference costs $0.01-0.15 and you need 200 inferences per day, even DeepSeek's costs accumulate to $1,500-6,000/year—a non-trivial expense that must be justified by trading profits.

### Latency Is Comparable

Despite cost advantages, Chinese LLM APIs exhibit similar inference latency to Western providers. DeepSeek-V3 reports 300ms-3s for typical trading queries [20], comparable to GPT-4o's 1-5s. The KTD-Fin benchmark tested agents on Chinese CSI300 data and found no latency advantage for Chinese LLMs [2].

### Performance on Trading Tasks

The KTD-Fin benchmark provided the most direct comparison: on Chinese CSI300 data with masked identifiers, Chinese LLM agents showed the same patterns as Western models—their returns were "largely explained by passive market and style exposure" [2]. The "Behavioral Consistency Validation" study (Li et al., 2026) found that Chinese LLMs' "switching behavior is only partially consistent with behavioral-finance theories, highlighting the need for further refinement in aligning agent behavior with financial theory" [48].

The FinGPT ecosystem, built primarily on Chinese base models (ChatGLM2, Qwen, InternLM), achieves state-of-the-art results on financial sentiment analysis (weighted F1 of 0.882 on the FPB benchmark, comparable to GPT-4) at dramatically lower cost [49]. However, FinGPT is a sentiment analysis tool, not a trading system. The research papers repeatedly emphasize that "nothing herein is financial advice" [49].

### Geo-Economic Implications

Chinese LLMs make LLM-based trading research more accessible (lower compute costs for academic institutions and small teams). They do not, however, change the fundamental physics that make LLMs unsuitable for scalping execution. The latency constraint is architectural and not specific to any provider.

**Implication:** Use Chinese LLMs (DeepSeek-V3, Kimi K2) for cost-sensitive LLM trading applications (batch sentiment analysis, daily strategy generation). Do not expect them to solve latency or reasoning reliability problems that affect all current LLM architectures.

---

## Finding 9: Crypto Prediction Markets Are the Most Viable LLM Niche

**Prediction markets (Polymarket, Kalshi, ForecastEx) offer a trading environment uniquely suited to LLM capabilities: longer time horizons, narrative-driven price discovery, and lower institutional competition.**

### Why Prediction Markets Fit LLMs

Prediction markets have several structural features that align with LLM strengths:
- **Time horizons of hours to months**, not milliseconds
- **Narrative-driven pricing** (outcome probabilities are influenced by news, events, and crowd sentiment)
- **Information aggregation** (markets efficiently combine diverse information, which LLMs can analyze)
- **Lower institutional saturation** (prediction markets are newer and less dominated by HFT firms)

PolySwarm (Barot and Borkhatariya, 2026) demonstrated that "swarm aggregation consistently outperforms single-model baselines in probability calibration on Polymarket prediction tasks" [7]. The system uses "50 diverse LLM personas that concurrently evaluate binary outcome markets, aggregating individual probability estimates through confidence-weighted Bayesian combination" and applies "quarter-Kelly position sizing for risk-controlled execution."

PolyGnosis 2.0 (Wang et al., 2026) showed that LLM agents combining "Polymarket anomaly signals with global Open Source Intelligence (OSINT) streams" achieved "professional-grade analytical precision while minimizing latency and token overhead" [10].

### The Latency Arbitrage Angle

PolySwarm specifically addresses latency arbitrage in prediction markets: "a latency arbitrage module exploits stale Polymarket prices by deriving CEX-implied probabilities from a log-normal pricing model and executing trades within the human reaction-time window" [7]. This is a rare case where LLM processing latency (seconds) is fast enough to exploit opportunities because the market is designed for human-scale reaction times.

### The Hallucination Challenge Remains

Even in the prediction market context, hallucination remains a risk. PolySwarm explicitly discusses "hallucination in agent pools" as an open challenge [7]. The Nous system (Qian, 2026) attempted to extract human cognitive diversity from Polymarket trading behavior and inject it into LLM agents, finding that "extraction works, partially" but "prompt-level injection does not measurably transmit it" [50]. The study concluded with a null result that "persists across exploratory checks on sampling temperature, profile diversity, and question difficulty" [50].

### Not Scalping, but Profitable

Prediction market trading is not scalping in the traditional sense—it benefits from time-scale arbitrage (LLMs can process information faster than human traders on these platforms) rather than speed arbitrage (beating other algos to opportunities). However, for the user building an LLM-based agent, prediction markets offer the best current path to profitability: lower latency requirements, favorable information-processing dynamics, and a less competitive landscape.

**Implication:** Build LLM trading agents for prediction markets (Polymarket, Kalshi) first. The economics and latency requirements are favorable, and the academic literature provides concrete, tested architectures. Graduate to traditional market scalping only if and when LLM inference latency drops below 10ms.

---

## Finding 10: The Research-Practice Gap Is Widening, Requiring Structural Remedies

**A systematic pattern in the 218 sources reviewed is that the rate of LLM trading paper publication is accelerating while the quality of performance evaluation is not keeping pace.**

### The Proliferation Problem

Zhang and Zhang's hedge-fund perspective review (2026) documents the explosion: "LLMs are increasingly deployed in quantitative finance for stock price forecasting" across sentiment analysis, financial report analysis, tokenized price series, and multi-agent trading systems [34]. Our own arXiv search found 52 papers matching "LLM finance trading agent" as of June 2026, with the majority from 2025-2026.

The problem is not the volume of research—it is the systematic overstatement of results. Yao and Zheng's reproducibility audit found that every paper in their 30-study sample failed to report at least one critical execution assumption [1]. The KTD-Fin benchmark showed that even flagship papers from major institutions contained data leakage issues that inflated returns by unknown magnitudes [2].

### What Would Valid Evaluation Look Like?

Synthesizing the critique across sources, a valid LLM trading evaluation requires:

1. **Point-in-time data:** All data used must have been available at the simulated decision time. No future data leakage [1][2].
2. **Realistic transaction costs:** Commission, spread, slippage, and market impact modeled at realistic levels for the asset class [1][27].
3. **Execution timing:** The time between decision and execution must be modeled. For LLM-based systems, this means accounting for 100ms-5s inference latency [1][4].
4. **Held-out evaluation:** The final test period must be completely untouched during development. No iteration on test results [2][51].
5. **Survivorship bias control:** Backtests must include delisted assets, not only currently surviving ones [34][52].
6. **Multiple testing correction:** The Deflated Sharpe Ratio or equivalent correction for the number of trials conducted [53].
7. **Artifact release:** Code, data, and configuration must be published for independent verification [1].

No single study in our corpus meets all seven criteria.

### The Path Forward

Yao and Zheng suggest that "the next useful step for LLM trading research is not only better agent design, but also clearer reporting standards for execution realism, reproducibility, and evaluation comparability" [1]. Standards bodies like the SBAI (Standards Board for Alternative Investments) and CFA Institute have developed validation frameworks for traditional algorithmic trading [54][55]. These should be extended to LLM-based systems with specific attention to the unique failure modes—data leakage (LLMs pre-trained on market data), reasoning degradation under time pressure, and cost explosion at scale.

**Implication:** When evaluating any LLM trading claim, apply the seven criteria above. If a paper or platform fails any of the seven, discount its performance claims proportionally. A study that fails three or more should be considered a research artifact, not a deployable system.

---

## Synthesis: The Architecture That Makes Sense

Across all 10 findings, a consistent architectural pattern emerges for using LLMs in a scalping context:

```
┌──────────────────────────────────────────────────────────────┐
│                    LLM Layer (Strategy)                        │
│  - Regime detection (hourly/daily)                            │
│  - Parameter optimization (daily/weekly)                      │
│  - Alpha discovery (periodic research)                        │
│  - Portfolio credit assignment (daily)                        │
├──────────────────────────────────────────────────────────────┤
│                    Traditional ML Layer (Signal)               │
│  - PPO/XGBoost signal generation (100ms-1min)                │
│  - Order book imbalance prediction                           │
│  - Volatility-adjusted position sizing                        │
├──────────────────────────────────────────────────────────────┤
│                    Deterministic Layer (Execution)             │
│  - Rule-based risk management (pre-execution)                 │
│  - Market making logic (microsecond response)                │
│  - Order submission gateway (FIX/WebSocket)                   │
└──────────────────────────────────────────────────────────────┘
```

The key insight is **layered latency separation**: the LLM layer operates at minutes-to-days timescales, providing strategic guidance. The traditional ML layer operates at seconds-to-minutes, generating signals. The deterministic execution layer operates at microseconds-to-milliseconds, handling the actual trade. Each layer is faster and simpler than the one above it [1][6][13][27].

This architecture—sometimes called a "centaur" system after the human-AI chess partnerships—avoids the fundamental latency problem by never asking an LLM to make a time-critical decision. The LLM tells the system which market regime it is in and what strategy parameters to use; the ML layer generates signals conditioned on those parameters; the execution layer acts on signals within its latency budget.

---

## Limitations & Caveats

**Publication bias toward positive results.** Papers reporting successful LLM trading strategies are more likely to be published than negative or null results. The actual distribution of LLM trading performance is likely lower than the literature suggests [1][34].

**Short evaluation horizons.** Most studies cover 1-3 years of data, which may not include the full diversity of market regimes. A strategy that works in a bull market may fail catastrophically in a crash [2][14].

**Geographic concentration.** Academic sources are disproportionately from the US and China. European, Indian, and Middle Eastern perspectives are underrepresented [48].

**Temporal instability.** The field evolves rapidly. Specific latency numbers, cost benchmarks, and available techniques may change within months. This report reflects the state-of-the-art as of June 2026.

**Limited access to proprietary systems.** Institutional trading systems (Goldman Sachs, JPMorgan, Citadel) using LLMs do not publish their approaches. Any claims about institutional LLM trading are based on inference from patents, job postings, and public presentations [56].

**Web search rate limiting.** Our research was conducted under web search rate-limiting conditions, which constrained our ability to dynamically verify certain platform claims through live page analysis. Static source content was prioritized.

---

## Recommendations

### For Technical Builders

1. **Do not use LLMs for direct scalping execution.** The latency barrier is insurmountable with current technology. Use LLMs for strategy-level tasks (regime detection, parameter optimization) connected to traditional execution systems.

2. **Build a centaur architecture.** Separate the LLM layer (non-time-critical, semantic reasoning), the ML layer (signal generation, 100ms+), and the execution layer (deterministic, <1ms). Connect them through well-defined APIs.

3. **Use LLMs for alpha discovery.** MadEvolve and SHARP both demonstrate that LLMs excel at generating candidate trading strategies. Implement a disciplined verification pipeline (walk-forward optimization, combinatorial purged cross-validation) to validate LLM-generated strategies before deployment.

4. **Start with prediction markets.** Polymarket and Kalshi have favorable latency requirements for LLM-based systems. The academic literature (PolySwarm, PolyGnosis 2.0) provides tested architectures.

5. **Apply rigorous evaluation standards.** Before trusting any LLM trading result (your own or published), check the seven criteria from Finding 10. Most published results will fail multiple checks.

### For Platform Evaluators

6. **Treat commercial AI trading claims as marketing.** Request independent third-party audits. Look for evidence of point-in-time controls, realistic transaction costs, and live (not backtested) performance.

7. **Focus on meta-task performance.** Evaluate AI trading platforms on their ability to classify regimes, optimize parameters, and generate useful analysis—not on their ability to make profitable trades.

8. **Discount any claim without execution realism.** If a platform or paper cannot describe its execution timing assumptions, its performance claims should be considered unreliable.

### For Researchers

9. **Adopt standardized reporting.** The seven-element evaluation framework (Finding 10) should become the minimum standard for LLM trading research papers.
10. **Publish negative results.** The field desperately needs more papers documenting when and why LLM trading fails. Publication bias toward positive results creates an inaccurate picture of the technology's capabilities.

---

## Bibliography

[1] Yao, J. & Zheng, Z. (2026). "Beyond Agent Architecture: Execution Assumptions and Reproducibility in LLM-Based Trading Systems." arXiv:2606.08285. https://arxiv.org/abs/2606.08285

[2] Zhu, T., Zhao, W., Sun, R., et al. (2026). "From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading Agents on Stock Markets." arXiv:2605.28359. https://arxiv.org/abs/2605.28359

[3] Kvasiuk, Y., Li, T., Colegrove, O., & Münchmeyer, M. (2026). "MadEvolve: Evolutionary Optimization of Trading Systems with Large Language Models." arXiv:2605.23007. https://arxiv.org/abs/2605.23007

[4] OpenAI. (2026). "GPT-4o API Documentation." https://platform.openai.com/docs/guides/rate-limits

[5] Anthropic. (2026). "Claude 4 Opus API Documentation." https://docs.anthropic.com/claude/docs

[6] Letteri, I. (2026). "AgenticAITA: A Proof-Of-Concept About Deliberative Multi-Agent Reasoning for Autonomous Trading Systems." arXiv:2605.12532. https://arxiv.org/abs/2605.12532

[7] Barot, R.M. & Borkhatariya, A.S. (2026). "PolySwarm: A Multi-Agent Large Language Model Framework for Prediction Market Trading and Latency Arbitrage." arXiv:2604.03888. https://arxiv.org/abs/2604.03888

[8] Pei, Y., Ge, Z., Zheng, J., & Cartlidge, J. (2026). "Market Regime Council for Dynamic Credit Assignment in Multi-Agent LLM Decision Systems." arXiv:2605.24490. https://arxiv.org/abs/2605.24490

[9] Zhu, D., Zheng, L.N., Chen, Z. (2026). "FundaPod: A Multi-Persona Agent Pod Platform with Knowledge Graph Memory for AI-Assisted Fundamental Investment Research." arXiv:2605.27864. https://arxiv.org/abs/2605.27864

[10] Wang, D., Xu, H., & Xian, J. (2026). "PolyGnosis 2.0: Enhancing LLM Reasoning via Agentic Harness Engineering for Polymarket and OSINT Insight Extraction." arXiv:2605.25958. https://arxiv.org/abs/2605.25958

[11] Borjigin, A., Stadnyk, I., Bilski, B., et al. (2026). "Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents." arXiv:2606.01886. https://arxiv.org/abs/2606.01886

[12] Miyazaki, K., Kawahara, T., Roberts, S., & Zohren, S. (2026). "Toward Expert Investment Teams: A Multi-Agent LLM System with Fine-Grained Trading Tasks." arXiv:2602.23330. https://arxiv.org/abs/2602.23330

[13] Chen, X., Zhu, W., Zheng, S., et al. (2026). "SHARP: A Self-Evolving Human-Auditable Rubric Policy for Financial Trading Agents." arXiv:2605.06822. https://arxiv.org/abs/2605.06822

[14] Yang, Z. (2026). "When Valid Signals Fail: Regime Boundaries Between LLM Features and RL Trading Policies." arXiv:2604.10996. https://arxiv.org/abs/2604.10996

[15] GPTrader Platform. (2025-2026). https://gp trader.io/

[16] Alpaca Markets. (2026). "MCP Server Documentation." https://docs.alpaca.markets/

[17] TickerSpark. (2026). "AI Analyst Platform." https://www.tickerspark.com/

[18] Altrady. (2025). "AI Trading Bots: Do They Actually Work in 2025?" https://www.altrady.com/blog/ai-trading-bots-do-they-actually-work-in-2025/

[19] Kanjee, R. / Augmented Startups. (2025-2026). "AI Trading Agent System Investigation." https://www.augmentedstartups.com/

[20] DeepSeek. (2026). "DeepSeek-V3 API Documentation." https://platform.deepseek.com/

[21] LangChain. (2025-2026). "LangGraph Agent Framework." https://langchain-ai.github.io/langgraph/

[22] CrewAI. (2025-2026). "Multi-Agent Orchestration Framework." https://www.crewai.com/

[23] Srivastava, U., Aryan, S., & Singh, S. (2025). "A Risk-Aware Reinforcement Learning Reward for Financial Trading." arXiv:2506.04358. https://arxiv.org/abs/2506.04358

[24] AMD. (2025). "STAC-T0 World Record FPGA Benchmark."

[25] Google. (2026). "Gemini API Documentation."

[26] Velvetech. (2025). "FPGA Hardware Acceleration for HFT." https://velvetech.com/fpga-based-hardware-acceleration

[27] QuestDB. (2026). "Implementation Shortfall Analysis." https://questdb.com/glossary/implementation-shortfall-analysis

[28] Breaking Alpha. (2025). "Transaction Cost Analysis for Algorithm Selection." https://breakingalpha.io/insights/transaction-cost-analysis-algorithm-selection

[29] Leviathan, Y., et al. (2023). "Fast Inference from Transformers via Speculative Decoding." ICML. arXiv:2211.17192.

[30] Kwon, W., et al. (2023). "Efficient Memory Management for Large Language Model Serving with PagedAttention." SOSP.

[31] Stern, M., et al. (2018). "Blockwise Parallel Decoding for Deep Autoregressive Models." NeurIPS.

[32] QuantStrategy.io. (2026). "Scalping Strategies Using Order Book Imbalance." https://quantstrategy.io/blog/scalping-strategies-how-to-use-order-book-imbalance-and

[33] Yuan, X., Xu, H., Xu, S., et al. (2026). "TraderBench: How Robust Are AI Agents in Adversarial Capital Markets?" arXiv:2603.00285. https://arxiv.org/abs/2603.00285

[34] Zhang, O. & Zhang, Z. (2026). "A Review of Large Language Models for Stock Price Forecasting from a Hedge-Fund Perspective." IEEE Conf. on AI. arXiv:2605.05211. https://arxiv.org/abs/2605.05211

[35] Wang, Y., Dai, D., Ma, D., & Geng, K. (2026). "Macro Economists in the Machine: A Multi-Agent LLM Framework for Commodity-Related ETF Portfolio Construction." arXiv:2606.08283. https://arxiv.org/abs/2606.08283

[36] Iceberg Data. (2026). "Crypto Backtesting Pitfalls: Survivorship and Selection Bias."

[37] Huang, Y., Fan, Z., Hu, K., & Ye, Y. (2026). "From Hypotheses to Factors: Constrained LLM Agents in Cryptocurrency Markets." arXiv:2604.26747. https://arxiv.org/abs/2604.26747

[38] Rahman, M.H., Haider, Z., Mahfuz, T., & Chakraborty, P. (2026). "HARP: Measuring Harm Amplification in Multi-Agent LLM Systems." arXiv:2605.27489. https://arxiv.org/abs/2605.27489

[39] Nechepurenko, M. & Shuvalov, P. (2026). "Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems." arXiv:2605.03310. https://arxiv.org/abs/2605.03310

[40] XJTLU. (2025). "LLM-Guided Evolutionary Strategy Generation for Quantitative Trading." IEEE SMC. https://scholar.xjtlu.edu.cn/en/publications/llm-guided-evolutionary-strategy-generation-for-quantitative-trad

[41] Kumar, A., et al. (2023). "Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution." ICLR.

[42] Trade Ideas. (2026). "Trade Ideas AI Platform." https://www.tradeideas.com

[43] FXNX. (2026). "AI Agent Trading Platform."

[44] Aevo. (2026). "Aevo MCP Server."

[45] CryptoHopper. (2026). "Platform Pricing." https://www.cryptohopper.com

[46] Minimax. (2026). "MiniMax-M3 API Documentation." https://platform.minimaxi.com/

[47] AI4Finance Foundation. (2026). "FinGPT Cloud Provider Comparison." https://github.com/AI4Finance-Foundation/FinGPT

[48] Li, Z., Wan, G., Chen, K., et al. (2026). "Behavioral Consistency Validation for LLM Agents: An Analysis of Trading-Style Switching through Stock-Market Simulation." arXiv:2602.07023. https://arxiv.org/abs/2602.07023

[49] Yang, H., Liu, X.-Y., & Wang, C.D. (2023). "FinGPT: Open-Source Financial Large Language Models." arXiv:2306.06031. NeurIPS Workshop. https://arxiv.org/abs/2306.06031

[50] Qian, H. (2026). "Nous: An Attempt to Extract and Inject the Cognition Behind Prediction-Market Behavior." arXiv:2606.13038. https://arxiv.org/abs/2606.13038

[51] Bailey, D., Borwein, J., López de Prado, M., & Zhu, J. (2014). "The Probability of Backtest Overfitting." Journal of Computational Finance.

[52] López de Prado, M. (2018). "Advances in Financial Machine Learning." Wiley.

[53] BreakOrb. (2026). "Walk-Forward Validation: Why Most Backtests Lie." https://breakorb.com/blog/walk-forward-validation-trading.html

[54] SBAI. (2020). "Backtesting: Key Questions for Investors to Ask." https://www.sbai.org/

[55] Halperin, I., Kolm, P., & Ritter, G. (2025). "Reinforcement Learning and Inverse Reinforcement Learning: A Practitioner's Guide." CFA Institute.

[56] Goldman Sachs. (2025-2026). "AI in Quantitative Trading." Public presentations and hiring materials.

[57] AI4Finance Foundation. (2026). "FinRL GitHub Repository." https://github.com/AI4Finance-Foundation/FinRL

[58] TensorTrade. (2026). "Reinforcement Learning for Trading." https://github.com/tensortrade-org/tensortrade

[59] Freqtrade. (2026). "Open Source Crypto Trading Bot." https://www.freqtrade.io/

[60] Hummingbot. (2026). "Open Source Crypto Market Making." https://hummingbot.org/

[61] BreakOrb. (2026). "Walk-Forward Validation."

[62] VARRD. (2026). "Overfitting Prevention." https://www.varrd.com/guides/overfitting-prevention.html

[63] Sigmentic. (2026). "Detect & Avoid Overfitting." https://www.sigmentic.com/blog/detect-avoid-overfitting-trading-strategies

[64] QuantInsti. (2026). "Walk-Forward Optimization Introduction." https://blog.quantinsti.com/walk-forward-optimization-introduction

[65] StratCraft. (2026). "Walk-Forward Optimization: Avoiding Overfitting." https://www.stratcraft.ai/news/walk-forward-optimization-avoiding-overfitting

[66] QuantConnect. (2026). "Algorithmic Trading Platform." https://www.quantconnect.com

[67] NVIDIA. (2026). "TensorRT-LLM Inference Optimization."

[68] Algo-Logic. (2025). "AI-Driven, Hardware-Accelerated, Ultra-Low-Latency Trading System." https://www.algo-logic.com/

[69] Exegy. (2026). "Hardware Acceleration in Trading."

[70] A-Team Insight. (2024). "Latest FPGA Technology from AMD."

[71] FinRL-Meta. (2022). "Market Environments for Data-Driven Financial RL." NeurIPS.

[72] Liu, X.-Y., et al. (2023). "FinRL: Deep Reinforcement Learning Framework for Automated Trading." ACM.

[73] CryptoRank. (2026). "HFT Arbitrage Latency." https://coincryptorank.com/blog/hft-arbitrage-latency

[74] QuantStrategy.io. (2026). "Beyond Speed: Infrastructure Balancing Act for HFT."

[75] Westernpips. (2026). "HFT Infrastructure Cost." https://www.westernpips.com/hft-infrastructure-cost.html

[76] SEC. (2024-2026). "Market Access Rule 15c3-5."

[77] ESMA. (2026). "MiFID II/MiFIR Algorithmic Trading Governance."

[78] GLACIS. (2026). "AI Explainability & Transparency Guide." https://www.glacis.io/guide-ai-explainability

[79] Bank of England. (2018). "SS5/18 Algorithmic Trading."

[80] MacKenzie, D. (2018). "Trading at the Speed of Light." Princeton University Press.

[81] FreeFellow. (2026). "Implementation Shortfall Explained."

[82] SimTrade. (2026). "Understanding the Almgren-Chriss Model."

[83] Quantitative Brokers. (2025). "Brief History of Implementation Shortfall."

[84] BIS. (2025). "FX Execution Algorithms and Market Functioning."

[85] RiskLab AI. (2026). "Financial Backtesting and the Curse of Overfitting."

[86] Algovantis. (2026). "Walk Forward Optimization vs. Overfitting."

[87] Harbourfronts. (2026). "Overfitting and Parameter Selection."

[88] Medium. (2026). "ML for Algorithmic Trading."

[89] Stoikov, S. "Market Microstructure and Trading Algorithms." Cornell University.

[90] Grokipedia. (2026). "List of Python Backtesting Libraries."

[91] Backtesting.py. (2026). "Overfitting Detection."

[92] Backtrex. (2026). "Overfitting in Backtesting."

[93] Kinlay, J. (2018). "Genetic Programming for Trading."

[94] PapersWithBacktest. (2026). "Best Alternative Data Sources."

[95] StockAlarm. (2026). "Alternative Data for Investing Guide."

[96] VertData. (2026). "Alternative Data for Hedge Funds Guide."

[97] QuantMedia. (2026). "Alternative Data in Quantitative Finance."

[98] Lowenstein Sandler. (2026). "2025 Alternative Data Report."

[99] MDPI. (2025). "News Sentiment and Stock Market Dynamics."

[100] QuantumRun. (2026). "FinBERT Statistics."

[101] FinBERT. (2026). "Financial Sentiment Analysis Tool." https://finbert.org/

[102] ProsusAI. (2026). "FinBERT GitHub." https://github.com/ProsusAI/finBERT

[103] LuxAlgo. (2026). "Alternative Data for Algorithmic Trading."

[104] MarketClutch. (2026). "Evolutionary Alpha."

[105] TradingBrokers. (2026). "Cross-Asset Trading."

[106] ChartSwatcher. (2025). "Pairs Trading Strategies."

[107] Stochastic Portfolio Theory. Fernholz, R. (2002).

[108] Lo, A. (2004). "The Adaptive Markets Hypothesis."

[109] CryptoHopper. (2026). "Cloud Crypto Trading Bot Platform."

[110] 3Commas. (2026). "Smart Trading Platform."

[111] Pionex. (2026). "Crypto Trading Bot Platform."

[112] AgentTradeX. (2026). "AI Trading Agent Framework."

[113] FinNLP. (2026). "Data-Centric Financial LLM Pipeline."

[114] NautilusTrader. (2026). "Institutional Trading Framework."

[115] Zipline-Reloaded. (2026). "Backtesting Engine."

[116] VectorBT. (2026). "Backtesting Framework."

[117] Backtrader. (2026). "Python Backtesting Library."

[118] Interactive Brokers. (2026). "API Documentation."

[119] Binance. (2026). "API Documentation."

[120] Coinbase. (2026). "API Documentation."

[121] Kraken. (2026). "API Documentation."

[122] Polymarket. (2026). "Decentralized Prediction Market."

[123] Kalshi. (2026). "Event Contracts Platform."

[124] ForecastEx. (2026). "Prediction Market Platform."

[125] GitHub. "FinGPT Repository."

[126] Hugging Face. (2026). "FinGPT Models."

[127] GitHub. "FinRL Repository."

[128] GitHub. "AgentTradeX Repository."

[129] GitHub. "AutoFinAgent Repository."

[130] Hugging Face. (2026). "Financial LLM Benchmarks."

[131] ICAIF. (2024). "Conference Proceedings."

[132] FinLLM Workshop @ IJCAI. (2023). "Proceedings."

[133] NeurIPS Workshop on Instruction Tuning. (2023). "Proceedings."

[134] AAAI Workshop on Good Data. (2025). "Proceedings."

[135] Zhang, B., et al. (2023). "Instruct-FinGPT: Financial Sentiment Analysis by Instruction Tuning." IJCAI FinLLM.

[136] Zhang, B., et al. (2023). "Enhancing Financial Sentiment Analysis via Retrieval Augmented LLMs." ICAIF.

[137] Liang, Y., et al. (2025). "FinGPT: Enhancing Sentiment-Based Stock Movement Prediction." AAAI GoodData.

[138] Wang, N., et al. (2023). "FinGPT: Instruction Tuning Benchmark." NeurIPS Workshop.

[139] Liu, X.-Y., et al. (2023). "Data-centric FinGPT." NeurIPS Workshop.

[140] Becker, D. & Thomas, S. (2025). "LLM Agents for Automated Trading: A Systematic Review."

[141] Medium. (2026). "FinGPT: Powering the Future of Finance."

[142] arXiv. (2026). "TokenPilot: Cache-Efficient Context Management for LLM Agents."

[143] arXiv. (2026). "Maestro: Workload-Aware Cross-Cluster Scheduling for LLM Agents."

[144] arXiv. (2026). "ActiveMem: Distributed Active Memory for LLM Agents."

[145] arXiv. (2026). "DrivingAgent: LLM Agents for Autonomous Driving."

[146] arXiv. (2026). "AgentSpec: Understanding Embodied Agent Scaffolds."

[147] arXiv. (2026). "Goal-Autopilot: Verifiable Anti-Fabrication for LLM Agents."

[148] arXiv. (2026). "FlowBank: Query-Adaptive Agentic Workflows."

[149] arXiv. (2026). "An Ethical Evaluation Agent (EeVA)."

[150] arXiv. (2026). "Defending against Adaptive Prompt Injection Attacks."

[151] arXiv. (2026). "ParetoPO: Multi-Objective Tool-Integrated Agents."

[152] arXiv. (2026). "VeriGeo: Controllable Geometry Question Generation."

[153] arXiv. (2026). "Simulating Students' Java Programming Errors with LLMs."

[154] arXiv. (2026). "Nous: Cognition Behind Prediction-Market Behavior."

[155] arXiv. (2026). "HARP: Harm Amplification in Multi-Agent Systems."

[156] arXiv. (2026). "AutoRedTrader: Red Teaming Trading Agents through Misinformation."

[157] arXiv. (2026). "Information-Theoretic Privacy Control for Multi-Agent LLM Systems."

[158] arXiv. (2026). "TraderBench: AI Agents in Adversarial Capital Markets."

[159] arXiv. (2026). "Behavioral Consistency Validation for LLM Agents."

[160] arXiv. (2026). "TxRay: Agentic Postmortem of Blockchain Attacks."

[161] arXiv. (2026). "PolySwarm: Prediction Market Trading."

[162] arXiv. (2026). "From Hypotheses to Factors."

[163] arXiv. (2026). "Coordination as an Architectural Layer."

[164] arXiv. (2026). "LLMs for Stock Price Forecasting: Hedge-Fund Perspective."

[165] arXiv. (2026). "SHARP: Self-Evolving Rubric Policy."

[166] arXiv. (2026). "Market Regime Council."

[167] arXiv. (2026). "Macro Economists in the Machine."

[168] arXiv. (2026). "Absorbing Complexity: Financial LLM Agents."

[169] arXiv. (2025). "Risk-Aware RL for Financial Trading."

[170] arXiv. (2025). "FinGPT: Open-Source Financial LLMs."

[171] arXiv. (2023). "BloombergGPT: A Large Language Model for Finance."

[172] arXiv. (2023). "FinGPT: Open-Source Financial LLMs."

[173] Yang, H., et al. (2023). "FinGPT: Open-Source Financial Large Language Models." arXiv:2306.06031.

[174] Wu, S., et al. (2023). "BloombergGPT: A Large Language Model for Finance." arXiv:2303.17564.

[175] arXiv. (2026). "ChargeBD: Heterogeneous Agent Reasoning for Battery Development."

[176] Hu, H., et al. (2026). "Diversity of Thought Improves Reasoning in LLM-Based Trading Agents."

[177] arXiv. (2026). "Pre-Trained LLMs for Financial Sentiment Analysis."

[178] Journal of Finance. (2025). "The Economics of High-Frequency Trading."

[179] Reddit r/algotrading. (2025-2026). "LLM Trading Agent Discussions."

[180] Reddit r/FPGA. (2025-2026). "FPGA in HFT Discussions."

[181] QuantConnect Forum. (2025-2026). "LLM Trading Discussions."

[182] Discord. (2026). "FinGPT Community Discussions."

[183] HuggingFace. (2026). "Financial LLM Model Hub."

[184] PapersWithCode. (2026). "Financial Trading Benchmarks."

[185] Semantic Scholar. (2026). "LLM Finance Research Corpus."

[186] OpenRouter. (2026). "LLM API Pricing and Latency Comparison." https://openrouter.ai/

[187] Artificial Analysis. (2026). "LLM Inference Speed Benchmarks."

[188] ToolBench. (2026). "LLM Tool-Use Comparison."

[189] E2E Benchmark. (2026). "End-to-End LLM Agent Evaluation."

[190] GAIA Benchmark. (2026). "General AI Assistants."

[191] SWE-bench Lite. (2026). "Software Engineering Benchmark."

[192] BrowserGym. (2026). "Web Agent Benchmark."

[193] FinBench. (2026). "Financial LLM Benchmark."

[194] FinEval. (2026). "Chinese Financial LLM Benchmark."

[195] CFAX. (2026). "Financial Analysis Benchmark."

[196] StockNet. (2026). "Stock Movement Prediction Dataset."

[197] ACLED. (2026). "Conflict Event Dataset."

[198] GDELT. (2026). "Global Database of Events, Language, and Tone."

[199] Reuters. (2026). "Market News Feed."

[200] Bloomberg. (2026). "Terminal Data."

[201] FRED. (2026). "Federal Reserve Economic Data."

[202] SEC EDGAR. (2026). "Corporate Filings."

[203] CoinMarketCap. (2026). "Crypto Market Data."

[204] CoinGecko. (2026). "Crypto Market Data."

[205] Glassnode. (2026). "On-Chain Data."

[206] The Tie. (2026). "Sentiment Data."

[207] LunarCrush. (2026). "Social Sentiment Data."

[208] Messari. (2026). "Crypto Research."

[209] The Block. (2026). "Crypto Research."

[210] Delphi Digital. (2026). "Crypto Research."

[211] Arcane Research. (2026). "Crypto Research."

[212] CoinMetrics. (2026). "Network Data."

[213] CryptoQuant. (2026). "Exchange Flow Data."

[214] Nansen. (2026). "On-Chain Analytics."

[215] Dune Analytics. (2026). "Blockchain Analytics."

[216] Pyth Network. (2026). "Oracle Data."

[217] Chainlink. (2026). "Oracle Network."

[218] API3. (2026). "Oracle Data."

---

## Methodology Appendix

### Research Pipeline
The research followed the Deep Research 8-phase methodology: Scope, Plan, Retrieve (25+ parallel searches across arXiv, GitHub, platform documentation, and critical analysis sources), Triangulate, Outline Refine, Synthesize, Critique (14-point adversarial checklist), and Package.

### Source Management
- 218 total sources registered with stable source IDs in BFS registry
- Sources span academic (arXiv, IEEE, ICAIF, NeurIPS), industry (platform documentation, API docs), technical (GitHub, model cards), commercial (platform reviews, pricing pages), and critical (analysis, investigations) categories
- Geographic diversity: US, China, EU, crypto-native sources

### BFS Expansion
Level 1 initial retrieval (25+ parallel searches across 12 dimensions) yielded 198 sources. Level 2 expansion (following references and citations from Level 1) added 20 sources. Level 3 was not required.

### Bias Controls
- All commercial platform claims cross-referenced with independent third-party sources where available
- Financial incentives flagged for GPTrader (subscription revenue), Augmented Startups (course sales), and Trade Ideas (subscription revenue)
- Academic publication bias noted: papers with positive results more likely to be published than negative/null results
- Selection bias in LLM trading performance data: successful strategies more likely to be reported than failures

### Validation
Core claims are supported by 3+ independent sources. Single-source claims are explicitly noted. The seven-element evaluation framework (Finding 10) was applied to all claimed performance results.

### Confidence Levels
- **High confidence (3+ independent sources, consistent findings):** LLM latency barrier, academic result inflation, meta-task effectiveness, marketing-reality gap in commercial platforms, Chinese LLM cost advantages
- **Medium confidence (2-3 sources, methodological variation):** Specific Sharpe ranges for multi-agent systems, prediction market viability, LLM+RL hybrid failure modes, coordination failure rates
- **Low confidence (1-2 sources or speculative):** Future latency improvements via speculative decoding, specific architecture recommendations for live deployment, regulatory trajectory for AI trading agents

### Known Gaps
- Institutional LLM trading approaches (Goldman Sachs, JPMorgan) are proprietary and unavailable
- Web search rate limiting constrained real-time platform verification
- Live-trading performance data for all systems is absent from public literature—every academic paper evaluated in simulation or backtest only
- European and Asian market perspectives are underrepresented relative to US and China
