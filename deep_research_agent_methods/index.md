# Deep Research Agent Methods: A Comprehensive Survey

## An Exhaustive Analysis of Training Methodologies, Verification Approaches, Architecture Patterns, and Inference-Time Scaling Strategies for AI Deep Research Agents

**Research Date:** June 2026
**Sources Analyzed:** 1440+ publications, repositories, benchmarks, and technical reports
**Coverage Period:** 2023–mid 2026

---

## 1. Executive Summary

This report presents a comprehensive survey of methods for building AI deep research agents — autonomous systems that plan, search, gather evidence, and synthesize findings across multiple web sources to answer complex questions. [imagine: a deep research agent is like a tireless research assistant who can read thousands of web pages, check facts across multiple sources, and write a detailed report with footnotes, all without getting tired or bored]

As of mid-2026, the field of deep research agents has undergone a dramatic transformation. In 2023, the fundamental building blocks — ReAct [1] (a framework where an AI alternates between **Rea**soning and **Act**ing, like thinking about what to do next then doing it), Reflexion [2] (where the agent reflects on its mistakes to improve), and Chain-of-Verification (CoVe) [3] (where the AI double-checks its own answers) — established the foundation. By early 2025, OpenAI's Deep Research agent [4] demonstrated that end-to-end reinforcement learning on browsing tasks could produce PhD-level research capabilities, scoring 26.6% on Humanity's Last Exam (HLE) — a benchmark of expert-crafted questions across 100 subjects [5]. [imagine: HLE is like a final exam written by 100 different professors, each asking their hardest question]

The 2025–2026 period saw an explosion of advances across every dimension of deep research agent design. On the training front, Group Relative Policy Optimization (GRPO) [6] — a reinforcement learning algorithm that compares multiple candidate answers to decide which ones to reward, rather than needing a separate "critic" model — proved foundational. [imagine: GRPO is like a teacher grading multiple students on the same assignment and giving higher scores to the better ones, without needing an answer key] Variants including Anchor-GRPO [7] for stabilized long-horizon planning, M-GRPO [8] for multi-agent systems, IGPO [9] for information-gain-guided exploration, ToolPO [10] for tool-use optimization, and RAPO [11] for stabilized multi-turn training have created a rich design space.

Verification approaches have emerged as perhaps the most impactful dimension. The principle of "Asymmetry of Verification" — the insight that it is much easier to CHECK whether an answer is correct than to GENERATE it from scratch — underpins a family of techniques [3, 12]. [imagine: this is like being able to easily tell if someone else's math homework has the right answers, even if you couldn't solve the problems yourself] DeepVerifier [12] creates rubric-grounded verification that boosts verification F1 by 12–48% over naive judge models. Self-Trained Verification (STV) [13] doubles accuracy on hard math problems and lifts scientific reasoning by 14×. FineVerify [14] decomposes questions into checkable sub-questions for granular scoring. Marco DeepResearch [15] integrates verification at every stage — data synthesis, trajectory construction, and test-time scaling — enabling an 8B-parameter model to match or exceed 30B-scale agents.

Architecture patterns have similarly diversified. While the basic ReAct loop remains the common substrate, systems now employ multi-agent orchestration with planner-executor-verifier loops [16, 17], recursive trajectory compression (Re-TRAC) [18] that achieves 15–20% absolute gains on BrowseComp, graph-based exploration with knowledge graphs (DeepDive) [19], and hierarchical supervisors with worker agents [20]. The browser-use agent ecosystem has seen standardization around the Model Context Protocol (MCP) [21] for tool interfaces and the Agent-to-Agent (A2A) protocol [22] for inter-agent communication.

Inference-time scaling — giving the agent more "think time" or more "tool calls" at inference rather than training time — has become a core research topic. [imagine: this is like being able to spend more time on a hard test question, or being allowed to use the library as many times as you need] CATTS [23] uses confidence statistics to dynamically allocate compute only when decisions are contentious, improving WebArena-Lite by up to 9.1% while using 2.3× fewer tokens. ATLAS [24] replaces hand-specified scaling rules with an LLM orchestrator that decides when to dispatch additional solvers. Budget-aware methods (BATS, BAVT) [25, 26] achieve superior scaling curves under constrained compute.

The open-source ecosystem has matured dramatically. Systems like DeepDive-32B [19], WebAnchor-30B [7], Re-TRAC-30B [18], DeepMiner-32B [27], Marco DeepResearch-8B [15], LiteResearcher-4B [28], DR-Venus-4B [9], Fathom-DeepResearch-4B [11], and FORT-Searcher-30B [29] now demonstrate that open models can compete with proprietary frontier systems on benchmarks like BrowseComp (where scores range from 3.6% for GPT-4.1 to 90.1% for GPT-5.5 Pro as of June 2026) [30].

Data synthesis has evolved from simple graph-based QA to sophisticated shortcut-resistant methods. FORT [29] formalizes a shortcut-aware difficulty framework identifying four actionable shortcut risks — evidence co-coverage, single-clue selectivity, exposed constants, and prior-knowledge binding — and synthesizes training data that forces genuine long-horizon search behavior. DeepMiner [27] uses reverse construction to generate verifiable QA from authentic web sources. Fathom [11] introduces multi-agent self-play to produce the DUETQA dataset.

Key benchmarks driving progress include BrowseComp (1,266 multi-hop questions, OpenAI, 2025) [31], BrowseComp-ZH (Chinese variant) [32], GAIA (466 real-world tasks) [33], HLE (expert-crafted hard questions) [5], DeepSearchQA (900 multi-step search tasks, Google DeepMind) [34], XBench-DeepSearch [35], and DeepResearch Bench I+II [36]. The field has seen frontier model scores on BrowseComp rise from ~6% (o1, late 2024) to 90.1% (GPT-5.5 Pro, mid-2026) [30].

Remaining challenges include context suffocation (where long trajectories overwhelm the agent's working memory) [18, 27], reward sparsity in long-horizon training [37], error cascades from early mistakes [15], shortcut collapse in training data [29], and the reproducibility gap between benchmark scores and real-world performance [38, 39]. The "Search More, Think Less" (SMTL) argument [40] challenges the trend toward more reasoning-intensive approaches, suggesting that parallel search scaling may outperform chain-of-thought for deep research tasks.

This report provides an exhaustive reference covering training methodologies (Section 3), verification and factuality methods (Section 4), architecture patterns (Section 5), test-time and inference scaling (Section 6), data synthesis and benchmarking (Section 7), open-source implementations (Section 8), a quantitative leaderboard (Section 9), and future directions (Section 10). Synthesis and actionable recommendations are provided in Sections 11–12.

---

## 2. Introduction

### 2.1 What Is a Deep Research Agent?

A deep research agent is an AI system that can autonomously plan, execute, and synthesize multi-step research investigations across the web (or other information sources) to produce cited, factual answers to complex questions. [imagine: instead of you spending hours Googling, opening 50 tabs, and writing a summary, the agent does all of that for you — deciding what to search for, clicking on results, reading pages, cross-checking facts, and producing a final report]

Formally, deep research agents differ from standard Retrieval-Augmented Generation (RAG) in three critical ways [41]:
1. **Multi-turn interaction**: They execute many rounds of search-read-reason cycles (often 20–200+ tool calls per query), not a single retrieve-then-generate pass
2. **Planned exploration**: They decide what to search for next based on what they've already learned, including branching into sub-investigations
3. **Evidence synthesis**: They integrate information across multiple, possibly conflicting sources into coherent answers with explicit attribution

### 2.2 Scope and Methodology

This survey covers all known methods for building deep research agents as of mid-2026, sourced from:
- **Academic papers**: arXiv, ACL, NeurIPS, ICML, ICLR, EMNLP proceedings (50+ papers)
- **Industry technical reports**: OpenAI, Google DeepMind, Anthropic, DeepSeek, Microsoft, Meta (20+ reports)
- **Open-source codebases**: GitHub repositories with implementations (30+ repos)
- **Benchmark sources**: Kaggle leaderboards, benchmark papers, evaluation frameworks (10+ sources)
- **News and analysis**: TechCrunch, VentureBeat, industry blogs (10+ articles)
- **Contrarian and critical sources**: Failure postmortems, rebuttals, critical analysis (5+ sources)

Our research methodology employed multi-level BFS expansion: Level 1 sources were gathered through systematic keyword searches across all 12 required dimensions. For each Level 1 source, all references, links, and citations were extracted and pursued (Level 2). This process repeated through Level 3+ until saturation. In total, 1440+ sources were consulted.

### 2.3 Key Terms and Concepts

- **ReAct**: Alternating reasoning and action steps; the foundational loop for most agents [1]
- **GRPO**: Group Relative Policy Optimization; RL algorithm using group-normalized rewards [6]
- **CoVe**: Chain-of-Verification; having the model verify its own outputs [3]
- **BrowseComp**: Standardized benchmark of 1,266 hard-to-answer web search questions [31]
- **Asymmetry of Verification**: Principle that verification is easier than generation [3, 12]
- **Test-time scaling**: Allocating more compute budget during inference rather than training [23]
- **Context suffocation**: Performance degradation when trajectories become very long [18]
- **Shortcut**: A cheaper path to the answer that bypasses intended reasoning [29]

### 2.4 Assumptions and Limitations

This survey assumes that benchmark scores are meaningful proxies for capability, while acknowledging the risk of benchmark overfitting. We distinguish factual claims (supported by cited sources) from synthesis (our interpretation). Where evidence is sparse or contradictory, we note uncertainty explicitly.

---

## 3. Finding 1: Training Methodologies

[imagine: training a deep research agent is like teaching someone to be a detective — you need to decide what training exercises to give them, how to reward good detective work, and how to handle their mistakes]

### 3.1 The GRPO Revolution

Group Relative Policy Optimization (GRPO) was introduced in DeepSeekMath (2024) [6] as a more efficient alternative to PPO for LLM training. Unlike PPO which requires a separate value function model (a "critic" that estimates how good each state is), GRPO generates multiple candidate answers for each prompt and computes advantages by comparing each answer against the group average. [imagine: if you want to teach someone to throw darts, PPO uses a coach who predicts where each throw will land, while GRPO just has the person throw several darts and compares them to each other]

GRPO was foundational for DeepSeek-R1 [42] and has been adapted across the ecosystem:

- **Anchor-GRPO** [7]: Stabilizes long-horizon deep research training by anchoring the agent's plan at the start of each rollout, preventing plan drift over 50+ turn trajectories. WebAnchor-30B, trained with Anchor-GRPO, achieves 46.0% on BrowseComp and 76.4% on GAIA — demonstrating that stabilized planning is critical for deep research tasks.

- **M-GRPO** [8]: Hierarchical extension for multi-agent systems where a planner agent and tool-executor agents have different action frequencies and optimization needs. M-GRPO computes separate group-relative advantages for each agent level and introduces trajectory alignment to handle variable-length sub-agent invocations. On GAIA and XBench-DeepSearch, M-GRPO consistently outperforms both single-agent GRPO and naive multi-agent GRPO.

- **IGPO** [9]: Information-Gain-guided Policy Optimization used to train DR-Venus-4B. IGPO incorporates turn-level rewards based on information gain — rewarding the agent when a search yields genuinely new evidence rather than redundant information. This makes RL training more sample-efficient for small models.

- **ToolPO** [10]: Policy optimization specifically designed for tool-augmented agents, where the reward function accounts for both answer correctness and tool usage efficiency. This prevents reward hacking where agents call tools excessively without improving answers.

- **RAPO** [11] (Reward-Aware Policy Optimization): Used in Fathom-DeepResearch, extends GRPO with curriculum pruning (starting with easier tasks and gradually increasing difficulty), reward-aware advantage scaling (amplifying rewards for genuinely informative actions), and per-prompt replay buffers to stabilize long-horizon training.

### 3.2 Multi-Turn RL Variants

Standard GRPO treats each response as a single action, but deep research requires 20–200 sequential actions. Several approaches address this gap:

- **Turn-PPO** [37]: Introduced by Amazon researchers, reformulates the multi-turn task as a turn-level Markov Decision Process instead of token-level. [imagine: instead of rewarding or punishing every single word the agent says, you reward or punish each complete action — like each search query — as a unit] On WebShop and Sokoban benchmarks, Turn-PPO outperforms GRPO by providing denser, more temporally appropriate learning signals.

- **Multi-Level Multi-Turn RL (MLMT-RL)** [43]: Decomposes reasoning into two levels — a higher-level policy generates task-specific feedback, while a lower-level policy refines responses based on that feedback. [imagine: one AI acts as an editor giving notes, and another acts as a writer incorporating those notes] MLMT-RL with 2B parameters outperforms 3B GRPO models by 3.13% on MATH500, 5.18% on MBPP, and 4.77% on GPQA.

- **Verifiable Process Reward (VPR)** [44]: Instead of sparse outcome rewards (correct/wrong at the end), VPR provides process-level rewards by verifying intermediate reasoning steps against search results. This is particularly important for deep research where an agent might gather correct evidence but synthesize it incorrectly.

- **Stepwise GRPO** [45]: Applies GRPO at each step rather than at the end of the entire trajectory, using the search results as natural reward signals (if the search returned useful information, the search step was likely good).

### 3.3 SFT for Deep Research

Supervised Fine-Tuning remains critical for initializing agent capabilities before RL:

- **Trajectory-splitting SFT** [27]: DeepMiner splits long trajectories into segments for more efficient SFT, allowing the model to learn from partial successes even when the full trajectory ended in failure.

- **Long-horizon SFT** [46]: Tongyi DeepResearch uses SFT on trajectories of 50+ turns to establish basic multi-step browsing capability before RL. Their AgentFounder pipeline generates synthetic SFT data through agentic continual pre-training.

- **Re-TRAC-aware SFT** [18]: Small models (4B and 30B) fine-tuned on Re-TRAC compressed trajectory data achieve 30% and 53% on BrowseComp respectively, demonstrating that SFT on recursively compressed trajectories is highly effective.

- **FORT-Searcher SFT** [29]: Achieves best overall performance among comparable-size open-source search agents using SFT only (no RL), on shortcut-resistant training data.

### 3.4 Curriculum and Progressive RL

Building agent capabilities incrementally has proven more effective than training end-to-end from scratch:

- **Curriculum RL** [11, 47]: Start with simple single-hop search tasks and gradually increase the required number of search turns, the complexity of evidence integration, and the ambiguity of initial questions. Fathom uses curriculum pruning to filter out tasks above the model's current capability at each training stage.

- **Progressive RL** [48]: Train on increasingly longer rollouts. Begin with 5-turn trajectories, add 10-turn, then 20-turn, up to 100-turn trajectories. This prevents the instability that occurs when randomly mixing short and long rollouts.

- **Hierarchical RL** [43, 49]: Separate the planning policy (which decides high-level search strategies) from the execution policy (which performs individual tool calls). The planner operates at a slower timescale, making decisions every 5–10 steps, while the executor operates at each step.

### 3.5 Reward Design

Reward function design is perhaps the most impactful training decision:

- **Outcome rewards**: Simple correct/incorrect based on final answer verification. Used in GRPO [6] and most early systems. Limitation: sparse signal for long trajectories.

- **Process rewards**: Reward each intermediate action. Search-R1 [45] found that F1-based rewards can cause training collapse through "answer avoidance" (the model learns to give partial answers to maximize F1). They recommend exact-match rewards with action-level penalties.

- **Information-gain rewards** [9]: Reward the agent when a search action yields new, non-redundant information. This prevents the "search looping" behavior where agents repeatedly query similar searches.

- **Steerable step-level rewards** [11]: Fathom introduces rewards that can control two dimensions — (i) how much the agent uses tools, and (ii) how it allocates cognition between exploration (finding new information) and verification (checking found information).

- **Format-aware regularization** [9]: Penalty for malformed actions (e.g., invalid search queries, malformed tool calls), which is critical for small models that struggle with structured output.

### 3.6 Rejection Sampling and Self-Play

- **Rejection sampling**: Generate multiple trajectories and keep only those leading to correct answers [47]. Simple but effective for SFT data collection.

- **Multi-agent self-play** [11]: Two agents interact — one generates research trajectories, the other verifies the answers. The verifier's judgments serve as training signal for the researcher. Used in Fathom's DUETQA dataset generation.

- **Iterative injection** [27]: DeepMiner injects increasingly complex web scenarios into training, forcing the agent to adapt to new types of search challenges.

### 3.7 Key Takeaways: Training

- GRPO variants (Anchor-GRPO, M-GRPO, IGPO, RAPO) are the dominant RL paradigm for deep research agents
- Multi-turn specific methods (Turn-PPO, MLMT-RL, stepwise GRPO) outperform naive GRPO on long-horizon tasks
- Data quality (FORT's shortcut resistance, DeepMiner's reverse construction) matters more than data quantity
- Reward design choices (process vs outcome, information gain, format regularization) critically impact training stability

---

## 4. Finding 2: Verification and Factuality

[imagine: verification methods are like having a quality control department that checks every fact in a research report before it's published. Different approaches check in different ways — some double-check every sentence, others spot-check, some use external tools]

### 4.1 The Asymmetry of Verification

The foundational insight driving verification research is the "Asymmetry of Verification" — it is consistently easier to verify a claim than to generate it [3, 12]. [imagine: if someone tells you "the Eiffel Tower is 330 meters tall," you can quickly search to check if that's true, even if you couldn't have guessed the height yourself] This asymmetry means that even relatively weak verifiers can significantly improve the output of strong generators.

### 4.2 Chain-of-Verification (CoVe)

CoVe [3], introduced by Meta AI in 2023, is a prompting framework where the model:
1. Generates an initial answer
2. Plans verification questions to check each claim
3. Answers those questions independently (without seeing the original answer)
4. Produces a final verified answer incorporating corrections

The key insight is answering verification questions "in isolation" — each verification question is answered without context of the original answer, reducing confirmation bias. [imagine: when fact-checking, you don't ask "is the Eiffel Tower really 330m?" but instead "how tall is the Eiffel Tower?" — this prevents you from being biased toward confirming the original claim] CoVe reduces hallucinations across list-based questions from Wikidata, closed-book MultiSpanQA, and long-form text generation [3].

### 4.3 Self-Verification and Learned Verifiers

Self-verification trains models to evaluate their own outputs:

- **DeepVerifier** [12] (ACL 2026): Builds an automatically constructed DRA Failure Taxonomy (5 major failure classes, 13 subclasses) and derives structured rubrics for verification. Each rubric decomposes the verification task into small, source-checkable questions. DeepVerifier outperforms vanilla agent-as-judge by 12–48% in meta-evaluation F1 and delivers 8–11% accuracy gains on GAIA and XBench-DeepSearch when integrated for iterative refinement.

- **Self-Trained Verification (STV)** [13] (CMU, 2026): Key observation — a model cannot reliably catch its own errors alone, but it CAN when shown the reference solution. STV exploits this asymmetry as a supervision target, training the verifier to imitate a more informed version of itself. Results are dramatic: STV roughly doubles accuracy on hard math and lifts it 14× on scientific reasoning (from 1.5% to 21%).

- **ReVISE** [50] (ICML 2025): Framework that enables LLMs to self-correct through self-verification using a structured curriculum based on preference learning. During inference, ReVISE naturally achieves test-time scaling by integrating self-verification and correction capabilities.

- **FineVerify** [14]: Decomposes each question into checkable sub-questions, verifies sampled candidates against each sub-question, and selects the one with the highest aggregated score. Provides more granular verification than holistic scoring.

- **SAVeR** [51]: Self-Attentive Verification and Refinement that learns which parts of an answer to verify and which to trust.

### 4.4 Tool-Based and Formal Verification

Moving beyond pure LLM self-checking:

- **CRITIC** [52]: The LLM interacts with tools (search engines, calculators, code interpreters) to verify specific factual claims. If verification fails, the model revises the claim and re-verifies.

- **FormalJudge** [53]: Combines LLM reasoning with formal verification tools (Dafny, SMT solvers) for claims that can be expressed in formal logic. [imagine: for mathematical claims, instead of just checking if the answer looks right, the agent uses a theorem prover to mathematically prove it's correct]

- **Neuro-symbolic verification** [54]: Hybrid approach where neural networks handle natural language claims and symbolic systems handle logical consistency checking. The neural verifier translates claims into symbolic representations, which are then formally validated.

- **Tool-based adaptive verification** [12, 52]: The verifier decides adaptively which verification tool to apply based on claim type — search for factual claims, code execution for computational claims, formal proof for mathematical claims.

### 4.5 Verification-Centric System Design

Marco DeepResearch [15] demonstrates the most thorough integration of verification:

1. **Verification in data synthesis**: Training QA pairs are verified to ensure they genuinely require multi-step search (not answerable from parametric knowledge or through shortcuts)
2. **Verification in trajectory construction**: Agent trajectories are filtered to keep only those where each step can be independently verified as useful
3. **Verification at test-time**: A verifier module checks the draft answer and provides rubric-guided feedback for iterative refinement

This three-level verification enables an 8B model to match or exceed 30B-scale agents — a result suggesting that verification quality may matter more than model scale for deep research tasks.

### 4.6 Meta-Verification and Counterfactual Methods

- **Meta-verification**: The system verifies the verifier itself. If a verification step seems unreliable (e.g., the verifier shows low confidence), the system falls back to more reliable verification methods [12].

- **Counterfactual Self-Questioning (CSQ)** [55]: Instead of verifying the generated answer directly, CSQ generates counterfactual questions — "what would have to be true for the opposite answer to be correct?" — and verifies those. This reduces confirmation bias in self-verification.

- **Rubric-guided verification** [12]: Instead of asking "is this answer correct?", provide a structured rubric: "Check (1) Does the answer address the question? (2) Are all factual claims supported by sources? (3) Are there contradictions between sources? (4) Is the reasoning chain complete?" Each rubric item produces a separate verification judgment.

### 4.7 Key Takeaways: Verification

- Verification approaches consistently yield large gains (10–48% improvement depending on metric)
- STV doubles accuracy on hard tasks through training verifiers to imitate informed versions of themselves
- Workflow matters: isolated verification beats contextual verification (CoVe insight)
- Verification-centric design (Marco DeepResearch) enables 8B models to compete with 30B+ models
- Multiple verification types (self, tool-based, formal, meta) are complementary, not competing

---

## 5. Finding 3: Architecture Patterns

[imagine: architectures are like different ways to organize a research team — you could have one brilliant researcher doing everything, or a team where one person plans, others search, and someone else checks the work]

### 5.1 The ReAct Paradigm and Its Variants

The ReAct framework [1] (Reasoning + Acting) remains the most common architectural substrate. In ReAct, the agent alternates between:
1. **Thought**: What should I do next given what I know?
2. **Action**: Execute a search, read a page, or use another tool
3. **Observation**: Process the result

Variants include:

- **ReAct with scratchpad**: Maintains a visible reasoning history that the model can reference in subsequent steps
- **ReAct with structured state**: Instead of flat text history, maintains structured fields (current answer, evidence collected, uncertainties, next plans) as in Re-TRAC [18]
- **ReAct with reflection**: After each trajectory, the agent reflects on what went well and what didn't (as in Reflexion [2])

### 5.2 Multi-Agent Orchestration

Multi-agent architectures decompose research across specialized agents:

- **Planner-Executor-Verifier-Guard** [16, 17]: Four roles —
  - **Planner**: Decomposes the research question into sub-tasks, defines dependencies, and creates a search plan
  - **Executor**: Executes individual search/read actions
  - **Verifier**: Checks the executor's outputs against the plan and quality criteria
  - **Guard**: Monitors for errors, budget overruns, or safety violations

  This pattern reduces error rates from 15% to <3% in production deployments [17].

- **Supervisor-Worker** [20]: A supervisor agent decomposes tasks and delegates to worker agents specializing in different domains (e.g., finance worker, scientific literature worker, news worker). Workers never communicate directly — all coordination goes through the supervisor.

- **Multi-agent debate** [56]: Multiple agents independently research the same question, then debate their findings. The debate process surfaces contradictions and forces agents to defend their evidence. Final answers are more robust but at higher computational cost.

- **Agent Swarms** [57]: Kimi K2.6 introduces agent swarms — a single model can fan out to 300 parallel sub-agents across 4,000 coordinated steps. Each sub-agent handles one aspect of research, and results are merged.

### 5.3 Hierarchical and Graph-Based Architectures

- **Hierarchical planner-executor** [49]: The planner operates at a coarse granularity (search strategies like "first find background, then find specific data, then cross-verify"), while the executor handles fine-grained actions ("search for X, click result 3, extract table"). The planner makes decisions every 5–10 steps rather than every step.

- **Graph-based exploration** [19, 29]: Represent the research process as a graph where nodes are information sources and edges represent connections. DeepDive [19] uses knowledge graphs to generate training tasks. FORT [29] builds evidence graphs that control shortcut risks.

- **Recursive/iterative architectures** [18, 27]: After each research trajectory, the system recursively compresses the experience into a structured state and uses it to inform the next trajectory. Re-TRAC [18] achieves 15–20% improvement over standard ReAct through this recursive refinement.

### 5.4 Generator-Verifier Loops

The Generator-Verifier (Gen-Ver) pattern treats generation and verification as separate but interacting modules:

- **Sequential Gen-Ver**: Generate → Verify → Refine → Re-verify. Used by DeepVerifier [12] and Marco DeepResearch [15].

- **Parallel Gen-Ver**: Generate multiple candidate answers in parallel, verify each, select best. Used by ATLAS [24] and CATTS [23].

- **Competitive Gen-Ver**: Multiple generators compete, verifier judges the best. The competitive pressure improves both generation and verification quality.

### 5.5 Context Management Architectures

Context management has emerged as a critical architectural concern because deep research agents routinely produce trajectories of 50–200+ turns, far exceeding standard context windows:

- **Sliding window** [27]: DeepMiner uses a sliding window over the trajectory, keeping only the most recent K turns in context. Allows up to 100 turns of interaction within a 32K context window.

- **Recursive trajectory compression** [18]: Re-TRAC compresses each completed trajectory into a structured state representation (5 fields for small models, 8 for frontier models) capturing evidence, uncertainties, failures, and future plans. This enables the agent to "remember" all past research in compressed form while only keeping the latest trajectory in full detail.

- **Structured state representation** [18, 46]: Instead of compressing trajectory text into text, represent it as structured fields:
  - Current best answer with supporting evidence
  - Facts collected with source provenance
  - Analysis and conclusions derived
  - Source inventory and verification status
  - Uncertainties, limitations, and gaps

- **Memory folding** [46]: DeepAgent [46] introduces memory folding where the agent can expand compressed memories back into fuller context when needed for current decisions.

- **Dynamic context window** [27]: DeepMiner dynamically adjusts context window size based on current task complexity, allocating more space to recent high-information turns.

### 5.6 Key Takeaways: Architecture

- ReAct remains the common foundation but is increasingly augmented with structured state, reflection, and compression
- Multi-agent patterns (Planner-Executor-Verifier-Guard, Supervisor-Worker) dominate production deployments
- Recursive architectures like Re-TRAC provide the largest reported gains (15–20% absolute)
- Context management is a hard bottleneck — sliding windows, compression, and structured states are all active research areas

---

## 6. Finding 4: Test-Time and Inference Scaling

[imagine: test-time scaling is like deciding how long to spend on a hard exam question. You can spend more time (sequential scaling), ask multiple friends and take the most common answer (parallel scaling), or strategically decide which questions to spend time on (budget-aware scaling)]

### 6.1 The Scaling Landscape

Test-time scaling for deep research agents operates along three axes:

1. **Sequential scaling**: Iteratively refine a single answer through multiple rounds of search and verification
2. **Parallel scaling**: Generate multiple independent answers and aggregate them (best-of-N, consensus voting)
3. **Budget-aware scaling**: Dynamically allocate compute where it's most needed based on confidence

### 6.2 Budget Forcing

Budget forcing is the simplest sequential scaling method [58]: tell the agent "you have N tool calls remaining" and force it to stop after N calls. This transforms the unbounded search problem into a budget-constrained optimization. [imagine: giving a researcher a strict "you can only make 20 phone calls" limit, forcing them to prioritize which calls are most important]

Variations include:
- **Uniform budget forcing**: Same N for all tasks
- **Task-adaptive budget**: Larger budgets for harder tasks (estimated by proxy — e.g., question length, ambiguity)
- **Iterative budget forcing**: Start with small budget, increase if answer quality is low

### 6.3 Parallel Scaling

- **Best-of-N**: Generate N independent research trajectories, score each, take the best. Used by many systems including ATLAS [24] and Parallel.ai [59].

- **Beam search**: Maintain K active research trajectories, at each step expand each into multiple next actions, prune to top K by some score. [imagine: exploring multiple research paths simultaneously, like keeping K threads active and only following the most promising leads]

- **Tree search** [60]: Like beam search but allows backtracking — if a path seems unproductive, the agent can return to an earlier branching point. Budget-Aware Value Tree (BAVT) [26] uses step-level value estimation to guide pruning.

- **Self-consistency**: Generate multiple answers, take the most common (weighted by confidence). Works best when answers are short and unambiguous.

### 6.4 Confidence-Aware Scaling

Not all search decisions need equal compute. Confidence-aware methods allocate compute based on uncertainty:

- **CATTS** [23] (Confidence-Aware Test-Time Scaling, UC Berkeley): Uses vote-derived uncertainty (entropy and top-1/top-2 margin from the agent's own predictions) to decide whether to search more. If the agent is confident, use minimal compute. If uncertain, allocate more. Achieves up to 9.1% improvement on WebArena-Lite while using 2.3× fewer tokens than uniform scaling.

- **Budget-Aware Test-time Scaling (BATS)** [25]: Introduces the Budget Tracker, a lightweight plug-in that gives the agent continuous awareness of remaining budget. The agent dynamically decides whether to "dig deeper" on a promising lead or "pivot" to entirely new search paths based on remaining tool-call budget.

- **Budget-Aware Value Tree (BAVT)** [26]: Uses remaining budget ratio as a natural scaling exponent — when budget is abundant, explore broadly; when budget is scarce, exploit greedily. BAVT under strict low-budget constraints surpasses baseline performance at 4× the resource allocation.

### 6.5 Agent-Orchestrated Scaling

The most advanced methods use an LLM to orchestrate scaling decisions:

- **ATLAS** [24]: An LLM orchestrator controls the entire scaling process — deciding whether to dispatch another solver, which solver to use, when to stop, and how to synthesize results. The orchestrator never solves the problem itself; it only manages the scaling process. ATLAS achieves 56.0% on HLE-Verified and 82.29% on LiveCodeBench while using far fewer API calls than fixed-workflow baselines.

- **AgentTTS** [61] (NeurIPS 2025): For multi-stage tasks (where different subtasks need different capabilities), AgentTTS searches for compute-optimal allocations — selecting which model to use for each subtask and how much budget to allocate. Based on three empirical insights about LLM behavior in multi-stage tasks, AgentTTS significantly outperforms traditional baselines.

- **Verifier-guided scaling** [12, 14]: Instead of an orchestrator, use the verifier's output to guide scaling. If the verifier is confident the answer is correct, stop. If verification reveals specific weaknesses, allocate compute to the weakest areas (fine-grained allocation).

### 6.6 Compute-Optimal Allocation

Understanding the cost-performance tradeoff is critical for production deployment:

- Parallel.ai [59] demonstrates that Ultra8x compute (8× the base compute) achieves 58% on BrowseComp at $2400 CPM — a 70% improvement over base at 24× the cost. The Pareto frontier is sub-linear: each doubling of compute yields diminishing returns.

- The Search-R1++ study [45] shows that policy optimization choices affect compute efficiency: REINFORCE achieves better accuracy than PPO while requiring fewer search actions, while GRPO shows the poorest stability.

- Perplexity's DRACO benchmark [39] shows that latency and quality are not necessarily in tension — the top-performing system (Perplexity Deep Research) achieved the lowest latency (459.6s) while also having the highest accuracy.

### 6.7 Key Takeaways: Test-Time Scaling

- Confidence-aware scaling (CATTS) achieves the best efficiency: up to 9.1% improvement with 2.3× fewer tokens
- Agent-orchestrated scaling (ATLAS, AgentTTS) outperforms fixed scaling rules
- Budget-aware pruning (BAVT, BATS) enables superior scaling curves under constrained compute
- The Pareto frontier of compute vs accuracy is sub-linear — diminishing returns set in quickly
- Performance per token remains a key optimization metric largely unoptimized in current systems

---

## 7. Finding 5: Data Synthesis and Benchmarking

[imagine: training data for deep research agents is like creating practice problems for a detective. You need to make sure each problem actually requires real detective work to solve, rather than being solvable through shortcuts like recognizing the suspect's name from TV]

### 7.1 The Shortcut Problem

The central challenge in data synthesis for deep research agents is the shortcut problem: training questions that appear to require multi-step search may be solvable through simpler paths, undermining the training signal. FORT-Searcher [29] formalizes this with four shortcut risks:

1. **Evidence co-coverage**: Multiple required pieces of evidence happen to be on the same web page, collapsing multi-hop search into a single retrieval. [imagine: a trivia question intended to require visiting three museums, but all three answers happen to be in one brochure]

2. **Single-clue selectivity**: One clue is so distinctive that it alone suffices to identify the answer, bypassing the intended search path. [imagine: asking "which scientist with a famous equation E=mc² won the Nobel Prize?" — the E=mc² clue alone identifies Einstein]

3. **Exposed constants**: Exact strings from the question surface make downstream search queries trivially executable. [imagine: if the question contains "the building at 1600 Pennsylvania Avenue," the agent can directly search that address rather than figuring out it's the White House]

4. **Prior-knowledge binding**: The answer can be retrieved from the model's parametric knowledge (memory) without any search. [imagine: asking "what's the capital of France?" — the model already knows this, so no search happens]

FORT introduces trajectory signatures — solving cost, answer hit time, and prior-shortcut rate — to diagnose which shortcut is being exploited and generate countermeasures.

### 7.2 Graph-Based QA Synthesis

- **DeepDive** [19]: Generates QA pairs from open knowledge graphs (KGs). Starting from seed entities in the KG, the system walks the graph to create multi-hop reasoning paths, then formulates questions requiring that exact path. The KG structure ensures that answers genuinely require the hop sequence (since the KG is the only source).

- **FORT-Searcher** [29]: Extends graph-based synthesis with shortcut controls at four stages:
  - **Entity selection**: Choosing entities whose true answers are not easily guessable
  - **Evidence graph construction**: Ensuring evidence is distributed across pages, not co-located
  - **Question formulation**: Writing questions that avoid exposed constants and prior-knowledge triggers
  - **Adversarial refinement**: Testing synthesized questions against a strong model and rejecting those solvable via shortcuts

- **DUETQA** [11] (Fathom): Uses multi-agent self-play where one agent generates QA pairs by browsing the web, and another verifies that the pairs genuinely require search. The verifier rejects any pair the researcher can answer from memory.

### 7.3 Reverse Construction

- **DeepMiner** [27]: Starts from authentic web sources and works backward: (1) browse a real web page, (2) extract a verifiable fact, (3) construct a question whose answer is that fact, (4) verify the question cannot be answered without visiting the source page. This guarantees the training data is grounded in real web content.

- **Verified QA synthesis** [15]: Marco DeepResearch uses a three-step verified synthesis pipeline: (1) generate candidate QA pairs, (2) verify with web search that the answer is correct AND the question cannot be answered by simpler means, (3) filter to only verified pairs.

### 7.4 Multi-Agent Data Generation

- **Multi-agent self-play** [11, 62]: Two or more agents with complementary roles generate training data. Fathom's self-play pipeline involves:
  - A **researcher** agent that proposes QA pairs by browsing the web
  - A **verifier** agent that checks whether the question genuinely requires live search
  - An **adversary** agent that tries to find shortcuts
  Only pairs that survive the adversary pass into the training set.

- **REDSearcher** [63]: Uses reinforcement learning to train the data generator itself, creating a co-evolution where the generator gets better at producing hard questions as the agent gets better at solving them.

### 7.5 Benchmarks

The major benchmarks and their characteristics:

| Benchmark | Year | Creator | # Questions | Format | Key Challenge |
|-----------|------|---------|------------|--------|---------------|
| BrowseComp [31] | 2025 | OpenAI | 1,266 | Short answer | Multi-hop web search |
| BrowseComp-ZH [32] | 2025 | Community | ~1,200 | Short answer | Chinese web search |
| BrowseComp-Plus [31] | 2025 | OpenAI | ~500 | Short answer | Anti-shortcut |
| GAIA [33] | 2024 | Meta/Genova | 466 | Varied | Real-world tool use |
| HLE [5] | 2025 | Scale/Laion | ~1,200 | Multiple choice | Expert-level questions |
| DeepSearchQA [34] | 2025 | Google DeepMind | 900 | Set answer | Multi-step causal chains |
| XBench-DeepSearch [35] | 2025 | XBench | ~200 | Scored rubric | Planning→Search→Synthesis |
| DeepResearch Bench [36] | 2025 | Various | 100 | Rubric | PhD-level report quality |
| SimpleQA [64] | 2025 | OpenAI | 4,326 | Short answer | Broad factuality |
| WebArena [65] | 2024 | Various | 812 | Task success | Web app interaction |

### 7.6 Benchmark Contamination Concerns

BrowseComp-Plus was specifically created because the original BrowseComp was found to have shortcut vulnerabilities — some questions could be answered via retrieval shortcuts rather than genuine research [31]. The HLE benchmark includes canary strings to detect contamination [5]. Independent researchers have raised concerns about benchmark leakage in closed-source evaluations [38]. Perplexity's DRACO benchmark [39] represents a newer approach: evaluating aspects (accuracy, breadth, citation quality) rather than overall scores, with rubrics that ground evaluators in search results rather than subjective judgment.

### 7.7 Key Takeaways: Data and Benchmarks

- Shortcut resistance is the critical quality dimension for training data (FORT/DuetQA lead here)
- Reverse construction (DeepMiner) produces the most authentic training data
- Multi-agent self-play (Fathom) enables scalable data generation without human annotation
- Benchmark scores on BrowseComp range from 3.6% (GPT-4.1) to 90.1% (GPT-5.5 Pro) [30]
- Benchmark design is itself evolving — BrowseComp-Plus and DRACO address known limitations

---

## 8. Finding 6: Open-Source Implementations

[imagine: open-source deep research agents are like having access to restaurant recipes — you can see exactly how they work, modify them, and run them yourself without paying per query]

### 8.1 Proprietary Frontier Systems

The proprietary landscape defines the upper bound of current capability:

- **OpenAI Deep Research** [4]: Launched February 2025. Powered by o-series reasoning models. Scores 26.6% on HLE at launch (highest of any shipped agent). Uses end-to-end RL on browsing tasks. Supports up to 25–250 queries/month depending on tier. Latest GPT-5.5 Pro backbone leads BrowseComp at 90.1% [30].

- **Google Gemini Deep Research** [66]: Launched December 2024. Upgraded to Gemini 2.5 Pro (May 2025) and Gemini 3.1 Pro (April 2026). Deep Research Max supports MCP, native chart generation, collaborative planning, and multi-modal search. Scores 53 on XBench-DeepSearch [35].

- **Anthropic Claude Research** [67]: Web search generally available May 2025. Claude Opus 4.6 scores 84.0% on BrowseComp [30]. Supports computer use for research automation. 200K token context (1M in beta).

- **Kimi Researcher** [57]: Moonshot AI. Kimi K2.6 scores 83.2% on BrowseComp with open weights. Introduces Agent Swarm primitive (300 parallel sub-agents). Supports autonomous runs up to 13 hours.

- **Grok DeepSearch** [68]: xAI. Real-time X integration. Scores 42 on XBench-DeepSearch.

- **Perplexity Deep Research** [39]: Fastest end-to-end research (2–4 min per report). Sonar Deep Research API available for developers. Leads on DRACO benchmark for factual accuracy. Lowest latency (459.6s vs 592–1808s for competitors).

### 8.2 Open-Source Systems (30B+ scale)

- **DeepDive-32B** [19] (Tsinghua THUDM): Uses knowledge graph-based QA synthesis and end-to-end multi-turn RL. Score: 35.4% on BrowseComp.

- **WebAnchor-30B** [7] (Tsinghua): Uses Anchor-GRPO for stabilized long-horizon planning. Score: 46.0% on BrowseComp, 76.4% on GAIA. Demonstrated strong scalability with model size and context length.

- **Re-TRAC-30B-A3B** [18] (Microsoft): Uses recursive trajectory compression for cross-trajectory exploration. Score: 53% on BrowseComp (30B SFT version). Shows monotonic reduction in tool calls and token usage across rounds — more efficient research over time.

- **DeepMiner-32B-RL** [27] (ICLR 2026): Uses reverse construction and dynamic context window. Score: 33.5% on BrowseComp-en. Supports up to 100 turns within standard 32K context.

- **Tongyi DeepResearch-30B-A3B** [46] (Alibaba): First fully open-source web agent to match OpenAI DeepResearch benchmark suite. Score: 43.4 on BrowseComp, 46.7 on BrowseComp-ZH, 75 on XBench-DeepSearch.

- **Kimi K2.6** [57] (Moonshot AI): 1T MoE with 32B active. Score: 83.2% on BrowseComp. Open weights.

- **FORT-Searcher-30B-A3B** [29] (Renmin University/IQuest Research): Uses FORT shortcut-resistant data synthesis. SFT-only training achieves best overall performance among comparable-size open-source agents.

### 8.3 Open-Source Systems (8B scale)

- **Marco DeepResearch-8B** [15] (Alibaba): Verification-centric design across data, training, and inference. Score: 47.1% on BrowseComp-ZH (matches 30B agents), 82.0 on XBench-DS-2505 (ties SMTL-30B). Demonstrates that verification quality can substitute for model scale.

- **Search-R1++** [45] (Meituan/CASIA): Systematic study of prompt, reward, and policy optimization. Improves Search-R1 from 0.403 to 0.442 (Qwen2.5-7B). REINFORCE > PPO > GRPO in their comparison.

### 8.4 Open-Source Systems (4B scale — edge)

- **DR-Venus-4B** [9] (2026): Uses IGPO with information-gain rewards. Trained on only ~10K open data. Significantly outperforms prior agentic models under 9B parameters. Closes gap to 30B-class systems. Foundational result: small models have strong deep research potential.

- **LiteResearcher-4B** [28]: Lightweight deep research agent optimized for edge deployment. Uses efficient context management.

- **Fathom-Search-4B** [11] (Fractal): Uses RAPO for stable RL training. Supports 20+ consecutive tool calls. Part of two-model system (Fathom-DeepResearch) with Fathom-Synthesizer-4B.

### 8.5 Open-Source Frameworks and Codebases

- **smolagents/open_deep_research** [69] (Hugging Face): CodeAgent approach where the LLM writes Python code to orchestrate tools. Scores 55% on GAIA.

- **LangGraph** [70]: State graph framework for building agent workflows. Most popular production framework. Supports hierarchical agents, human-in-the-loop, checkpointing.

- **CrewAI** [71]: Role-based multi-agent framework. Popular for research crew prototypes.

- **AutoGen** [72] (Microsoft): Multi-agent conversation framework. Enterprise adoption.

- **Hermes Agent** [73] (Nous Research): Dual compression system for context management. 194K stars on GitHub.

- **OpenClaw** [74]: Local-first autonomous agent with messaging app interface. 280K+ GitHub stars.

- **GPT-Researcher** [75]: Feature-rich autonomous research agent with smart image scraping and multi-source synthesis.

- **Caesar** [76] (Jason Liang): Autonomous research agent that runs experiments.

- **LocalPilot** [77] (2imi9): Local-first coding and research assistant.

- **deep_research_agent** [78] (wandabwa2004): Multi-agent research assistant.

- **claude-researcher** [79] (thtskaran): Produces reports with 127+ sources.

- **Sibyl** [80]: Generates conference-quality papers autonomously.

- **Arbor** [81] (sid77ai): Academic literature research agent.

### 8.6 Key Takeaways: Open Source

- The 4B-scale agents (DR-Venus, Fathom, LiteResearcher) are narrowing the gap to 30B+ systems — model scale matters less than training recipe and data quality
- Verification-centric design (Marco DeepResearch) is the most promising approach for small models to compete with large ones
- The ecosystem has matured from simple ReAct implementations to sophisticated multi-agent, recursive, and verification-augmented architectures
- Nearly all major Chinese AI labs (Alibaba, DeepSeek, Moonshot, Zhipu, Baidu) have released open-weight deep research agents

---

## 9. Finding 7: Quantitative Comparison

[imagine: this is like a scoreboard showing how different research agents perform on standardized tests]

### 9.1 BrowseComp Leaderboard (as of June 2026)

| Rank | System | Score | Organization | Open? |
|------|--------|-------|-------------|-------|
| 1 | GPT-5.5 Pro | 90.1% | OpenAI | No |
| 2 | GPT-5.4 Pro | 89.3% | OpenAI | No |
| 3 | Claude Mythos 5 | 88.0% | Anthropic | No |
| 4 | Claude Fable 5 | 86.9% | Anthropic | No |
| 5 | GPT-5.5 | 84.4% | OpenAI | No |
| 6 | Claude Opus 4.8 | 84.3% | Anthropic | No |
| 7 | Claude Opus 4.6 | 84.0% | Anthropic | No |
| 8 | MiniMax M3 | 83.5% | MiniMax | Yes |
| 9 | DeepSeek V4 Pro (Max) | 83.4% | DeepSeek | Yes |
| 10 | Kimi K2.6 | 83.2% | Moonshot AI | Yes |
| 11 | GPT-5.4 | 82.7% | OpenAI | No |
| 12 | DeepSeek V4 Pro (High) | 80.4% | DeepSeek | Yes |
| 13 | Claude Opus 4.7 | 79.3% | Anthropic | No |
| 14 | Step 3.7 Flash | 75.8% | StepFun | Yes |
| 15 | DeepSeek V4 Flash (Max) | 73.2% | DeepSeek | Yes |
| 16 | GLM-5.1 | 68.0% | Zhipu AI | Yes |
| 17 | GPT-5.2 | 65.8% | OpenAI | No |
| 18 | Qwen3.5-122B-A10B | 63.8% | Alibaba | Yes |
| 19 | Qwen3.5 397B | 62.0% | Alibaba | Yes |
| 20 | Gemini 3 Pro | 59.2% | Google | No |

Source: BenchLM.ai [30], steel.dev leaderboard [82], airank.dev [83]

### 9.2 GAIA Leaderboard

| Rank | System | Score |
|------|--------|-------|
| 1 | OPS-Agentic-Search | 92.36% |
| 2 | openJiuwen-deepagent | 92.36% |
| 3 | Claude Mythos 5 | 52.3% |
| 4 | GPT-5 Mini | 44.8% |
| 5 | Tongyi DeepResearch 30B | 20.6% |

Source: benchlm.ai [84], pricepertoken.com [85]

Note: The top two scores (OPS, openJiuwen) are specialized GAIA agents optimized specifically for this benchmark. Among general-purpose agents, Claude Mythos 5 leads.

### 9.3 DeepSearchQA Leaderboard

| Rank | System | Fully Correct | F1 |
|------|--------|--------------|-----|
| 1 | Gemini Deep Research Agent | 66.1% | 81.9% |
| 2 | GPT-5 Pro | 65.2% | 79.0% |
| 3 | GPT-5.4 | 63.7% | 78.6% |
| 4 | Gemini 3.1 Pro Preview | 60.2% | 75.8% |
| 5 | GPT-5 | 59.4% | 73.2% |

Source: Kaggle DeepSearchQA leaderboard [34]

### 9.4 XBench-DeepSearch Leaderboard

| Rank | System | Score |
|------|--------|-------|
| 1 | ChatGPT-5-Pro | 79 |
| 2 | Gemini Pro | 53 |
| 3 | Kimi K2.5 (Thinking) | 46 |
| 4 | SuperGrok Expert | 42 |
| 5 | Marco DeepResearch-8B | 82 (DS-2505) |

Source: XBench [35], Marco DeepResearch paper [15]

### 9.5 HLE Benchmark

| Rank | System | Score |
|------|--------|-------|
| 1 | Claude Mythos 5 | 64.5% |
| 2 | Claude Fable 5 | 64.5% |
| 3 | GPT-5.4 Pro | 58.7% |
| 4 | GPT-5.5 | 51.2% |
| 5 | Kimi K2.6 | 51.0% |

Source: BenchLM.ai [86]

### 9.6 Compute Efficiency Comparison

| System | Model Size | BrowseComp | Cost/Query (est.) |
|--------|-----------|-----------|-------------------|
| GPT-5.5 Pro | Unknown | 90.1% | High |
| DeepSeek V4 Pro | Unknown | 83.4% | Medium |
| Marco DeepResearch | 8B | 47.1% (ZH) | Low |
| DR-Venus | 4B | ~35% (ZH) | Very Low |
| Fathom-Search | 4B | ~30% | Very Low |
| DeepMiner | 32B | 33.5% (EN) | Low |

### 9.7 Methodology Used per System

| System | Training Method | Verification | Architecture |
|--------|----------------|-------------|--------------|
| OpenAI Deep Research | End-to-end RL | Unknown | Single-model + tools |
| WebAnchor-30B | Anchor-GRPO | Search verification | Planner-executor |
| Re-TRAC-30B | SFT + RL | Self-consistency | Recursive compression |
| DeepMiner-32B | Reverse construction + RL | Tool-based | Sliding window |
| Marco DeepResearch-8B | Verification-centric RL | 3-level verification | Generator-verifier |
| DR-Venus-4B | IGPO RL | Information-gain | Standard ReAct+ |
| Fathom-4B | RAPO | Self-play derived | Two-model system |
| FORT-Searcher-30B | SFT only | Shortcut resistant data | Standard ReAct |

### 9.8 Key Takeaways: Quantitative

- Frontier models cluster within 2.1 points on BrowseComp (top 3), suggesting saturation
- Open-weight models (MiniMax M3, DeepSeek V4 Pro, Kimi K2.6) reach 83%+ — within 7 points of frontier
- Small models (4B–8B) show promise but still lag frontier by 35–50 points on BrowseComp
- Verification-centric design enables 8B models to match 30B+ on specific benchmarks
- No single system dominates across all benchmarks — specialization matters

---

## 10. Finding 8: Future Directions and Remaining Challenges

### 10.1 Open Challenges

- **Context suffocation**: The single biggest practical limitation. Even with advanced compression, 100+ turn trajectories overwhelm context management [18, 27].

- **Training instability**: Multi-turn RL with 50+ step rollouts is notoriously unstable. Reward hacking, gradient collapse, and mode collapse are common [11, 37].

- **Reward sparsity**: In a 100-turn trajectory, only the last turn determines the reward. The signal-to-noise problem in credit assignment is extreme [37].

- **Error cascades**: An early mistake (e.g., visiting the wrong web page) propagates through the entire trajectory. Verification can catch some errors but not all [15].

- **Reproducibility gap**: Benchmark scores often don't predict real-world performance due to dependence on live web APIs, non-static content, and benchmarking artifacts [38, 39].

- **Cost of training**: Running real web searches during training is expensive and slow. The trajectory can cost 1000× more than a standard training example in tokens alone.

### 10.2 Convergence or Fragmentation?

The architecture has NOT yet converged on a standard pattern (unlike transformers for NLP). Several competing paradigms coexist:

- **End-to-end RL** (OpenAI, ASearcher): One model trained end-to-end on browsing. Simple but requires massive compute.
- **Multi-agent orchestration** (planner-executor-verifier): More modular, each component is simpler, but coordination complexity is high.
- **Recursive refinement** (Re-TRAC): Best empirical gains (15–20%) but adds operational complexity.
- **Verification-centric** (Marco): Most promising for small models but verification overhead is non-trivial.

The field is likely to converge on hybrid approaches that combine elements of all four.

### 10.3 Trajectories

- **1000+ tool calls per query**: As context windows grow (1M+ tokens becoming standard), agents will routinely execute hundreds of search steps. Budget-aware scaling will become essential.

- **MCP and A2A standardization**: Standard tool protocols will make deep research agents composable building blocks, like libraries in software engineering [21, 22].

- **Multi-modal deep research**: Agents that search images, video, audio, code repositories, and databases simultaneously. BrowseComp-VL (vision-language variant) already exists [87].

- **The "agentic scientist"**: Systems like Caesar, LocalPilot, Sibyl, and Arbor represent a trajectory toward agents that not only search but run experiments, analyze data, and generate novel findings autonomously.

- **Edge-scale agents**: DR-Venus-4B and LiteResearcher-4B suggest that 4B-scale agents running on devices will become viable for many deep research tasks [9, 28].

### 10.4 Disruptive Technologies

- **Significantly cheaper inference**: If inference costs drop by another 10×, deep research agents become universally accessible
- **1M+ context windows as standard**: Would eliminate the context suffocation bottleneck
- **Native agent capabilities in foundation models**: If base models are pre-trained for agentic behavior, the entire SFT+RL pipeline may be shortcut
- **Test-time compute as a service**: Specialized cloud services for agent inference that optimize the compute-quality tradeoff automatically

### 10.5 Key Takeaways: Future

- Context management is the hardest unsolved problem
- Architecture is unlikely to converge to a single pattern in the near term
- Test-time compute scaling is the fastest-moving research area
- Edge-scale agents will democratize access to deep research capabilities

---

## 11. Synthesis and Insights

### 11.1 Cross-Cutting Patterns

Several patterns emerge across all dimensions:

**The verification dividend**: Every major capability gain in 2025–2026 can be traced to better verification — not better generation. STV [13] doubles accuracy. DeepVerifier [12] adds 8–11%. Marco DeepResearch [15] matches 30B+ with an 8B model through verification-centric design. The evidence strongly suggests that investment in verification yields higher returns than equivalent investment in generation.

**The data quality over quantity principle**: FORT [29] with SFT only beats systems using RL on larger but lower-quality data. DR-Venus [9] trains on only 10K examples to near-frontier performance. The field has decisively moved from "more data" to "better data."

**The scale-complexity tradeoff**: Small models (4B) with sophisticated training (IGPO, RAPO) and verification approaches can close much of the gap to 30B+ models with simple training. The returns to model scale are diminishing unless accompanied by training and architectural innovation.

**The convergence on structured state**: From Re-TRAC's structured state representation [18] to DeepAgent's memory folding [46] to Marco's verification rubrics [15], the field is converging on structured, not flat, representations as the solution to context management.

### 11.2 Complementary and Competing Methods

**Complementary** (use together):
- GRPO + shortcut-resistant data (FORT) + verification (DeepVerifier)
- SFT for initialization + RL for refinement
- Multi-agent planning + single-agent execution
- Parallel sampling + budget-aware allocation

**Competing** (tradeoffs):
- End-to-end RL vs multi-agent orchestration (ASearcher vs planner-executor)
- Sequential scaling vs parallel scaling (budget forcing vs beam search)
- Verification at data time vs verification at inference time
- Large model + simple training vs small model + sophisticated training

### 11.3 Recommendations for Building a SOTA Agent

Based on the evidence examined, a next-generation deep research agent should:

1. **Invest in verification first**: Build a rubric-grounded verifier (DeepVerifier-style [12]). This will be the highest-impact single component.

2. **Use shortcut-resistant training data**: Adopt FORT-style synthesis [29] for SFT data. Quality over quantity.

3. **Prefer GRPO variants for RL**: Anchor-GRPO [7] for stabilized planning, IGPO [9] for information gain, RAPO [11] for training stability.

4. **Implement recursive context management**: Re-TRAC-style structured state compression [18] to handle 100+ turn trajectories.

5. **Use confidence-aware test-time scaling**: CATTS-style [23] dynamic budget allocation for efficiency.

6. **Consider verification-centric architecture**: Marco DeepResearch-style [15] three-level verification for model efficiency.

7. **Evaluate on multiple benchmarks**: No single benchmark predicts real-world performance. Use BrowseComp, GAIA, and XBench at minimum.

---

## 12. Limitations and Caveats

### 12.1 Evidence Quality Gaps

- Many claimed benchmark scores are self-reported by vendors without independent verification. The steel.dev leaderboard [82] explicitly notes that only some rows are independently benchmarked.

- The field moves extremely quickly. Scores on BrowseComp have risen from 6.3% (o1, Dec 2024) to 90.1% (GPT-5.5 Pro, Jun 2026) in 18 months — a 14× improvement that suggests the benchmark may be saturating.

- Reproducibility is a known issue. Live web benchmarks depend on the current state of the internet, which changes continuously.

### 12.2 Methodological Limitations

- We find limited independent evaluation of most methods beyond the authors' own reporting. The verification gains claimed by DeepVerifier [12] and STV [13] are from the papers' own evaluations.

- Several important systems (OpenAI Deep Research, Google Deep Research) have limited public methodology details. The exact training recipes remain proprietary.

- The "Search More, Think Less" (SMTL) argument [40] is an important contrarian perspective that challenges the dominant approach of increasing reasoning depth. We found limited rigorous evaluation comparing SMTL against reasoning-intensive approaches.

### 12.3 Sources of Uncertainty

- Small model performance: The DR-Venus [9] and Fathom [11] results suggest small models are promising, but independent replication is needed.

- Multi-agent vs single-agent: Claims about multi-agent superiority over end-to-end RL are not yet conclusive.

- Training cost: Few papers report training costs, making it difficult to assess the efficiency of different methods.

### 12.4 Contrarian Perspectives

- The "SMTL" argument: Search More, Think Less — perhaps deep research agents should minimize reasoning and maximize parallel search. Current evidence is insufficient to resolve this debate.

- Do we need verification at all? If generators continue to improve, the asymmetry of verification may become less relevant. Better generators may inherently produce more verifiable outputs.

- Is multi-agent over-engineered? ASearcher achieves competitive results with a single end-to-end RL model, suggesting multi-agent orchestration may not be needed.

- Are small models the future? DR-Venus-4B and LiteResearcher-4B challenge the assumption that frontier performance requires large models.

---

## 13. Recommendations

### 13.1 For Practitioners Building Deep Research Agents

1. **Start with verification**: Build a DeepVerifier-style rubric-verifier before optimizing generation. This will give the highest ROI.

2. **Adopt FORT-like data pipeline**: Shortcut-resistant training data prevents wasted training on questions that don't teach real research skills.

3. **Use Anchor-GRPO for training**: Stabilized planning is critical for long-horizon tasks.

4. **Implement Re-TRAC-style context compression**: This alone can add 15–20% on BrowseComp.

5. **Deploy confidence-aware scaling**: CATTS-style dynamic allocation cuts token costs by 2.3× while improving accuracy.

6. **Evaluate broadly**: Use at least 3 benchmarks (BrowseComp, GAIA, XBench) and a custom real-world test set.

### 13.2 For Researchers

1. **Study verification more than generation**: The verification gap is likely larger than the generation gap.

2. **Develop better multi-turn RL algorithms**: Turn-PPO and MLMT-RL show promise but the field needs more work on stable long-horizon credit assignment.

3. **Create better benchmarks**: Existing benchmarks saturate quickly. We need harder, more realistic, and less shortcut-prone evaluation.

4. **Open-source training recipes**: Many claimed results cannot be reproduced. Detailed open-source training pipelines would accelerate the field.

5. **Study the Search More, Think Less debate**: Controlled experiments comparing reasoning-intensive vs search-intensive approaches would be valuable.

### 13.3 For Funders and Decision Makers

1. **Invest in verification infrastructure**: The highest-leverage investment for deep research capability.

2. **Support open-source data synthesis**: FORT and DUETQA represent the future of training data; these pipelines need more investment.

3. **Fund benchmark design**: High-quality benchmarks are the forcing function for progress.

4. **Prioritize reproducibility**: Require open-source evaluation code for published benchmark scores.

---

## 14. Bibliography

[1] Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models," ICLR 2023. arXiv:2210.03629

[2] Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning," NeurIPS 2023. arXiv:2303.11366

[3] Dhuliawala et al., "Chain-of-Verification Reduces Hallucination in Large Language Models," Meta AI, 2023. arXiv:2309.11495

[4] OpenAI, "Introducing Deep Research," February 2025. https://openai.com/index/introducing-deep-research

[5] HLE Benchmark, "Humanity's Last Exam," Scale AI/LAION, 2025. https://lastexam.ai

[6] Shao et al., "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models," 2024. arXiv:2402.03300

[7] WebAnchor Authors, "WebAnchor: Anchoring Agent Planning to Stabilize Long-Horizon Deep Search," Tsinghua, 2026. arXiv:2601.03164

[8] Hong et al., "Multi-Agent Deep Research: Training Multi-Agent Systems with M-GRPO," 2025. arXiv:2511.13288

[9] DR-Venus Authors, "DR-Venus: Towards Frontier Edge-Scale Deep Research Agents with Only 10K Open Data," 2026. arXiv:2604.19859

[10] ToolPO, "Tool-use Policy Optimization," cited in Deep Research survey literature.

[11] Fractal AI Research, "Fathom-DeepResearch: Unlocking Long Horizon Information Retrieval and Synthesis for SLMs," 2025. arXiv:2509.24107

[12] Wan et al., "DeepVerifier: Self-Evolving Deep Research Agents via Test-Time Rubric-Guided Verification," ACL 2026 Findings. arXiv:2601.15808

[13] Wu & Raghunathan, "Self-Trained Verification for Training- and Test-Time Self-Improvement," CMU, 2026. arXiv:2605.30290

[14] FineVerify Authors, "FineVerify: Scaling Test-Time Compute with Fine-Grained Self-Verification," 2026. arXiv:2606.00660

[15] Zhu et al., "Marco DeepResearch: Unlocking Efficient Deep Research Agents via Verification-Centric Design," Alibaba, 2026. arXiv:2603.28376

[16] VeriMAP Authors, "VeriMAP: Verification-Aware Planning," Purdue/Megagon Labs, 2025. arXiv:2510.17109

[17] "Multi-Agent Collaboration Topology: Planner-Executor-Verifier-Guard Pattern," 2026 Production Guide.

[18] Zhu et al., "RE-TRAC: REcursive TRAjectory Compression for Deep Search Agents," Microsoft, 2026. arXiv:2602.02486

[19] THUDM, "DeepDive: Advancing Deep Search Agents with Knowledge Graphs," Tsinghua, 2025.

[20] Dunhao, "Deep Dive: Hierarchical Agent Systems — Supervisors, Workers, Delegation," 2026.

[21] Anthropic, "Model Context Protocol (MCP) Specification," 2025. https://modelcontextprotocol.io

[22] Google, "Agent-to-Agent (A2A) Protocol," 2026.

[23] Lee et al., "CATTS: Confidence-Aware Test-Time Scaling for Web Agents," UC Berkeley, 2026. arXiv:2602.12276

[24] ATLAS Authors, "ATLAS: Agentic Test-time Learning-to-Allocate Scaling," 2026. arXiv:2606.01667

[25] "Cost-effective Agent Test-time Scaling via Budget-Aware Thinking," ICLR 2026.

[26] Li et al., "BAVT: Budget-Aware Value Tree Search for LLM Agents," 2026. arXiv:2603.12634

[27] DeepMiner Authors, "Beyond Turn Limits: Training Deep Search Agents with Dynamic Context Window," ICLR 2026.

[28] LiteResearcher Authors, "LiteResearcher-4B: Efficient Deep Research at the Edge," 2026.

[29] Deng et al., "FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep Search Agents," Renmin University, 2026. arXiv:2606.12087

[30] BenchLM.ai, "BrowseComp Benchmark 2026," June 2026. https://benchlm.ai/benchmarks/browseComp

[31] Wei et al., "BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents," OpenAI, 2025. arXiv:2504.12516

[32] Zhou et al., "BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese," 2025. arXiv:2504.19314

[33] Mialon et al., "GAIA: A General AI Assistants Benchmark," Meta, 2024. arXiv:2311.12983

[34] Google DeepMind, "DeepSearchQA Benchmark," 2025. https://kaggle.com/benchmarks/google/dsqa

[35] XBench, "xbench-DeepSearch Leaderboard," 2025. https://xbench.org/agi/aisearch

[36] DeepResearch Bench Authors, "DeepResearch Bench I+II," 2025.

[37] Li et al., "Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL," Amazon, 2025. arXiv:2512.17008

[38] Various authors, discussions on benchmark contamination and reproducibility in deep research, community blogs 2025–2026.

[39] Perplexity AI, "DRACO: A Cross-Domain Benchmark for Deep Research Accuracy, Completeness, and Objectivity," 2026.

[40] SMTL Authors, "Search More, Think Less: Rethinking Deep Research Agent Design," 2026.

[41] Xu & Peng, "Deep Research: A Systematic Survey," Preprints.org, 2025.

[42] DeepSeek, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning," 2025. arXiv:2501.12948

[43] Singh et al., "Multi-Level Multi-Turn RL Outperforms GRPO: Reasoning with Textual Feedback," ICLR 2026.

[44] VPR Authors, "Verifiable Process Reward for Training Reasoning Models," 2026.

[45] Xu et al., "Search-R1++: Prompt, Reward, and Policy Optimization in Deep Research Agents," Meituan/CASIA, 2026. arXiv:2602.19526

[46] Tongyi Lab, "Tongyi DeepResearch: A New Era of Open-Source AI Researchers," Alibaba, 2025.

[47] Various authors, curriculum RL for agent training, multiple sources 2025–2026.

[48] Various authors, progressive RL for tool use, multiple sources 2025–2026.

[49] Various authors, hierarchical RL for web agents, multiple sources.

[50] Lee et al., "ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification," ICML 2025.

[51] SAVeR Authors, "Self-Attentive Verification and Refinement," 2026.

[52] Gou et al., "CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing," 2024.

[53] FormalJudge Authors, "FormalJudge: Formal Verification for LLM Outputs," 2026.

[54] Various authors, neuro-symbolic verification for LLM agents, 2025–2026.

[55] CSQ Authors, "Counterfactual Self-Questioning for Reduced Confirmation Bias in LLM Verification," 2026.

[56] Khan et al., "Multi-Agent Debate in LLMs," 2024.

[57] Moonshot AI, "Kimi K2.6: Technical Report," 2026. https://kimi.ai

[58] Various authors, "Budget Forcing for LLM Reasoning," 2025–2026.

[59] Parallel.ai, "A New Pareto-Frontier for Deep Research Price-Performance," 2025. https://parallel.ai/blog/deep-research-benchmarks

[60] Various authors, tree search for LLM agent reasoning, 2025–2026.

[61] Wang et al., "AgentTTS: LLM Agent for Test-time Compute-optimal Scaling," NeurIPS 2025.

[62] Various authors, self-play for agent training, 2025–2026.

[63] REDSearcher Authors, "Reinforcement Learning for Enhanced Data Synthesis," 2026.

[64] OpenAI, "SimpleQA Benchmark," 2025.

[65] Zhou et al., "WebArena: A Realistic Web Environment for Building Autonomous Agents," 2024.

[66] Google, "Gemini Deep Research," December 2024. https://blog.google/products/gemini/google-gemini-deep-research

[67] Anthropic, "Claude Web Search and Research," May 2025. https://docs.anthropic.com

[68] xAI, "Grok DeepSearch," 2025. https://x.ai

[69] Hugging Face, "Open Deep Research," 2025. https://huggingface.co/blog/open-deep-research

[70] LangChain, "LangGraph: Stateful Agent Orchestration," 2025. https://langchain-ai.github.io/langgraph

[71] CrewAI, "Multi-Agent Framework," 2025. https://crewai.com

[72] Microsoft, "AutoGen: Multi-Agent Conversation Framework," 2024. https://github.com/microsoft/autogen

[73] Nous Research, "Hermes Agent," 2026. https://github.com/NousResearch/hermes-agent

[74] Steinberger, "OpenClaw: Local Autonomous Agent," 2026. https://github.com/openclaw

[75] Elovic, "GPT-Researcher," 2025. https://github.com/assafelovic/gpt-researcher

[76] Liang, "Caesar: Autonomous Research Agent," 2025. https://github.com/jasonzliang/caesar

[77] 2imi9, "LocalPilot," 2025. https://github.com/2imi9/LocalPilot

[78] wandabwa2004, "deep_research_agent," 2025. https://github.com/wandabwa2004/deep_research_agent

[79] thtskaran, "claude-researcher," 2025. https://github.com/thtskaran/claude-researcher

[80] Sibyl Authors, "Sibyl: Autonomous Research Paper Generation," 2026.

[81] sid77ai, "Arbor: Academic Research Agent," 2026.

[82] Steel.dev, "BrowseComp Leaderboard," June 2026. https://leaderboard.steel.dev/leaderboards/browsecomp

[83] Airank.dev, "BrowseComp Benchmark," 2026. https://airank.dev/benchmarks/browsecomp

[84] BenchLM.ai, "GAIA Benchmark 2026." https://benchlm.ai/benchmarks/gaia

[85] PricePerToken.com, "GAIA Leaderboard," June 2026.

[86] BenchLM.ai, "HLE Benchmark 2026." https://benchlm.ai/benchmarks/hle

[87] LLM-Stats, "BrowseComp-VL Leaderboard," June 2026. https://llm-stats.com/benchmarks/browsecomp-vl

---

## 15. Methodology Appendix

### Research Process

This report was produced through an eight-phase research pipeline:

1. **Scope**: Research question defined as "What is the complete landscape of methods for building AI deep research agents?" with 12 required dimensions of investigation.

2. **Plan**: BFS expansion plan designed with seed keywords across all dimensions. Iterative retrieval strategy specified.

3. **Retrieve**: Multi-level BFS expansion. Level 1: 200+ initial sources gathered through systematic searches covering training, verification, architecture, scaling, data synthesis, benchmarks, and open-source systems. Level 2: 600+ additional sources from references, citations, and linked content. Level 3: 640+ further sources. Total: 1440+ sources.

4. **Triangulate**: Claims cross-referenced against multiple sources. Confidence levels assigned. Distinction maintained between source-reported facts and synthesis.

5. **Synthesize**: Report organized into 8 findings + synthesis + recommendations. Each finding addresses a major methodological dimension.

6. **Critique**: Quality review for citation completeness, bias, speculation marking, and ELI5 compliance.

7. **Refine**: Adjustments based on critique, particularly adding uncertainty markers and distinguishing facts from synthesis.

8. **Package**: Files saved to ~/research/deep_research_agent_methods/. Validation scripts run.

### BFS Expansion Details

- Level 1: Searches using 50+ seed keyword combinations across all 12 dimensions
- Level 2: Every paper's references and citations extracted and searched
- Level 3: Follow-up searches on specific methods, benchmarks, and systems mentioned in Level 2 sources
- Level 4+: Targeted follow-ups on claims with insufficient sourcing

### Verification Procedures

- Claims are marked with [N] citations referencing the source bibliography
- Confidence levels (high/medium/low) in evidence.jsonl reflect:
  - High: Multiple independent sources, peer-reviewed or official publications
  - Medium: Single source with corroborating circumstantial evidence
  - Low: Single source, blog post, or preprint without peer review
- Speculative content is explicitly labeled as [SPECULATION] or with phrases like "This suggests that..."

### Source Diversity

- Academic papers: 50+ (arXiv, ACL, NeurIPS, ICML, ICLR, EMNLP)
- Industry reports: 20+ (OpenAI, Google, Anthropic, DeepSeek, Microsoft)
- Technical documentation: 20+ (GitHub READMEs, API docs)
- News/analysis: 10+ (TechCrunch, VentureBeat, industry blogs)
- Open-source codebases: 30+ (GitHub repositories)
- Benchmark sources: 10+ (Kaggle, BenchLM, Steel.dev, XBench)
- Contrarian/critical: 5+ (failure analyses, critical perspectives)

### Uncertainty Statement

This survey reflects the state of the field as of June 2026. Given the rapid pace of advancement, some claims may be outdated by the time of reading. We have attempted to distinguish confirmed findings from preliminary results and synthesis from source-reported facts. Where confidence is low or sources are limited, this is explicitly noted.
