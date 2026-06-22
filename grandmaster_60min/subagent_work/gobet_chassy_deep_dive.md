# Subagent Deep-Dive: Gobet & Chassy on Perceptual Intuition in Chess

## Source
- **Research Topic**: Gobet & Chassy's 2023 study on perceptual intuition in chess, Gobet's template theory (1998), and the 2009 unified theory of intuition (SIT framework)
- **Date of Research**: 2026-06-22

---

## Executive Summary

This report synthesizes findings from the Gobet-Chassy research program on expert intuition in chess, spanning 1998-2023. The research covers: (1) the 2023 Psychological Research study with world-class players (N=63, Elo 2000-2800+) showing skill accounts for 44% of variance in rapid position evaluation after just 5 seconds; (2) template theory (1998) as an evolution from chunking theory; (3) the 2009 unified theory of intuition reconciling Dreyfus (holistic) and Simon (analytic) views; (4) the neural basis of expert pattern recognition; and (5) the CHREST cognitive architecture that computationally implements these theories.

---

## Key Sources

| Source | Year | Publication | DOI |
|--------|------|-------------|-----|
| Chassy, Lahaye, Didierjean & Gobet | 2023 | Psychological Research, 87(8), 2380-2389 | 10.1007/s00426-023-01823-x |
| Gobet & Simon | 1998 | Memory, 6(3), 225-255 | 10.1080/741942359 |
| Gobet & Simon | 1998 | Cognition, 66, 115-152 | 10.1016/s0010-0277(98)00020-1 |
| Gobet & Chassy | 2009 | Minds and Machines, 19(2), 151-180 | 10.1007/s11023-008-9131-5 |
| Chassy & Gobet | 2011 | Review of General Psychology, 15(3), 198-212 | 10.1037/a0023958 |
| Gobet & Simon | 1996 | Cognitive Psychology, 31, 1-40 | 10.1006/cogp.1996.0011 |
| Gobet | 2013 | Frontiers in Psychology | - |
| Lane & Gobet | 2010 | CHREST Tutorial, Cognitive Science Society | - |

---

## Finding 1: The 2023 Study — How Grandmasters "See" Solutions in 1-3 Seconds

### Study Design
Chassy, Lahaye, Didierjean & Gobet (2023) conducted the most rigorous test of expert intuition ever attempted in chess:

- **Participants**: 63 chess players ranging from candidate masters (Elo 2000-2200) to world-class players (Elo 2600-2800+). Eight players had >2700 Elo; one had >2800. At data collection time, only 39 players worldwide had 2700+. This is the highest-caliber sample ever assembled for an intuition study.
- **Task**: Players evaluated 56 chess positions shown for only **5 seconds**. Evaluation required assessing who had the advantage on a 7-point scale (from -3 "Black decisive" to +3 "White decisive") — an explicitly **holistic** judgment.
- **Positions**: 7 levels of balance × 2 levels of complexity (simple: ~16 pieces; complex: ~25 pieces). Positions were from recent master games unlikely to be familiar.

### Key Results

**1. Skill effect was massive.** Skill accounted for **44% of the variance** in evaluation error (r=0.664, p<0.001). World-class players (M=1.17 error) dramatically outperformed candidate masters (M=1.58 error). The regression equation: `Evaluation Error = -0.000721 × Elo + 3.148`.

**2. No speed-accuracy trade-off.** Response times did NOT differ by skill level (p=0.71). This is crucial — experts were NOT just faster at the same processing; they were genuinely *seeing more* in the same time window. A time-bin analysis showed that Elo predicted evaluation accuracy even in the 0-1 second bin (r²=0.151, p=0.041), strongest in the 1-2 second bin (r²=0.189, p=0.001), and remained significant through 4 seconds — but NOT for the 4-5 second bin (r²=0.005, p=0.625), suggesting that intuition's work is done within the first 3-4 seconds.

**3. Complexity effect confirmed.** Simple positions were evaluated better than complex ones (F=34.27, p<0.01, η²=0.367). This supports Gobet & Chassy's prediction (vs. Dreyfus): experts DO identify subcomponents incrementally, taking more time with complex positions.

**4. Balance effect.** Accuracy diminished when positions were more extreme (one side had a decisive advantage). Players were most accurate on equal positions.

### What This Means for "Seeing" in 1-3 Seconds

The 2023 study shows that grandmasters' intuition is:
- **Holistic but built from parts**: Experts don't need a "vibe" — they rapidly recognize chunks and templates that accumulate into a full positional understanding within 3-4 seconds
- **Purely perceptual**: The intuition comes from perception-memory interaction, not conscious reasoning
- **Quantifiable**: Each ~100 Elo points corresponds to measurably better evaluation accuracy
- **Automatic**: No extra time is needed — experts see the evaluation within the same 5-second window as weaker players, they just see it *better*

**Extrapolation from the regression line**: Perfect intuition (zero error) would theoretically be reached at Elo 4366 — far beyond Magnus Carlsen's 2859 — suggesting that even the world's best still have room for intuitive improvement. [SPECULATION: This implies intuition improves with knowledge across the entire range of human expertise.]

---

## Finding 2: Template Theory vs. Chunking Theory

### The Original Chunking Theory (Chase & Simon, 1973)
Chase and Simon proposed that chess expertise is built on **chunks** — familiar clusters of pieces containing 5-6 pieces each, stored in long-term memory (LTM). Key claims:
- Experts store ~50,000 chunks (Simon & Gilmartin estimate)
- Short-term memory (STM) holds ~7 chunks at once
- During 5-second recall, chunks are accessed from LTM but NOT stored back to LTM
- Skill comes from recognizing more and larger chunks

### Three Weaknesses of Chunking Theory
Gobet & Simon (1998) identified critical flaws:

1. **Interference resistance**: Charness (1976) showed that chess memory is NOT disrupted by interfering material between trials — implying information was rapidly stored in LTM, contradicting the chunking theory's assumption of STM-only encoding.

2. **Multiple board recall**: Gobet & Simon (1996) showed that a Chessmaster could recall up to 9 boards with >70% accuracy — far exceeding the ~7 chunks × 5 pieces = 35 pieces that chunking theory would predict.

3. **Chunk size**: Masters in Gobet & Simon's (1998) replication used substantially larger chunks than the master in Chase & Simon's 1973 study, suggesting chunk size itself grows with skill beyond the 5-6 piece limit.

### Template Theory (Gobet & Simon, 1996, 1998)
Template theory retains chunks but adds a critical new structure:

| Feature | Chunking Theory | Template Theory |
|---------|----------------|-----------------|
| Memory structure | Chunks only (5-6 pieces) | Chunks + Templates (schema-like, 10+ pieces) |
| STM limit | 7 chunks | 3 chunks (visual STM); ~4 items |
| LTM storage in 5s | None (only chunk recognition) | ~250ms per slot in template |
| Discrimination net | Yes | Yes (same mechanism) |
| Rapid encoding mechanism | None | Template slots (250ms instantiation) |
| Chunk evolution | Static | Chunks → templates through repeated exposure |
| Reaction to interference | Predicts vulnerability | Predicts resistance (fast LTM storage) |
| Random position recall | Novice-level | Experts slightly better (more chunks) |

**What is a template?** A template is a schema-like structure with two parts:
- **Core**: Stable, invariant information (the fixed pattern of pieces)
- **Slots**: Variable positions that can be rapidly instantiated (~250ms each) with new information

Templates are created when a chunk is encountered frequently enough. The mechanism is called **template formation** — an automatic process where CHREST identifies stable and variable information across multiple encounters with similar chunks, creating the core (stable) and slots (variable).

**Three roles of templates in problem-solving (Gobet, 1997):**
1. Rapid LTM storage during position encoding
2. Search at the template-space level (not just move-space)
3. Compensation for decay in the "mind's eye" (visual working memory)

### Educational Implications (Gobet & Jansen, in press)
Template theory predicts:
- Slow learning rates (~8 seconds per new chunk; ~2 seconds to add info to existing chunk)
- Need for massive pattern exposure (~10 years / 10,000 hours)
- Schemas (templates) develop automatically through repeated exposure
- Teaching should focus on pattern recognition, not just search/calculation

---

## Finding 3: The SIT (Synchrony of Intuition and Thought) Framework (2009)

**Note**: The acronym "SIT" does **not** appear in the Gobet & Chassy (2009) paper itself. The framework is simply called "the template theory of intuition" or "the unified theory of intuition." However, the concept of *synchrony between intuitive and analytical processes* is central to their theory. The term "SIT" or "Synchrony of Intuition and Thought" may be a secondary literature label.

### The Core Problem They Solved
Before 2009, two incompatible theories dominated:

| Dimension | Simon's Theory (1995) | Dreyfus & Dreyfus (1986) |
|-----------|----------------------|--------------------------|
| Intuition = | Pattern recognition | Holistic understanding |
| Role of analysis | Search + evaluation | Rarely used by experts |
| Encoding | Small perceptual chunks | No subcomponent identification |
| AI possibility | Yes (physical symbol system) | No (embodied cognition) |
| Complexity effect | Yes (more chunks to recognize) | No (holistic is instantaneous) |

### The 2009 Unified Theory
Gobet & Chassy (2009) proposed that **both** are partially correct:

**Five key characteristics of expert intuition** (Gobet & Chassy, 2008, 2009):
1. **Rapid perception** of key features (matches Simon)
2. **Lack of awareness** of how decisions are reached (matches Dreyfus)
3. **Presence of emotions** (unique addition — neither Simon nor Dreyfus emphasized this)
4. **Holistic grasp** of the situation (matches Dreyfus)
5. **Decisions correct more often than chance** (matches both)

**The reconciliation mechanism**: Templates provide the bridge between analytic chunking and holistic intuition:
- **Local level**: Small chunks are recognized rapidly (Simon's pattern recognition)
- **Integration**: Multiple chunks incrementally build a representation
- **Holistic result**: By the end of presentation time (3-5 seconds), the network of recognized chunks + filled template slots creates a full-board Gestalt (Dreyfus's holistic understanding)
- **Emotions**: Emotional responses become associated with chunks/templates during practice; they act as rapid heuristic signals that can guide decision-making before conscious analysis

Gobet and Chassy (2009) wrote: "The template theory of intuition maintains many aspects of Simon's earlier theory, including the emphasis on pattern recognition and selective search; the presence of large templates also makes it possible to account for the Gestalt-like quality of intuition."

### Divergent Predictions Tested in 2023
The 2023 study directly tested where Dreyfus and Gobet-Chassy diverge:

- **Dreyfus predicts**: No complexity effect — experts understand holistically regardless of complexity
- **Gobet-Chassy predicts**: Complexity effect — more complex positions require more chunk/template recognition time

**Result**: Strong complexity effect (F=34.27, p<0.01, η²=0.367). **Gobet-Chassy confirmed; Dreyfus disconfirmed** on this point.

### The Synchrony Concept
Although no single paper uses "Synchrony of Intuition and Thought" as a formal acronym, the framework consistently describes:
1. Intuition and analytical thought operate **in parallel**, not in sequence (contra Kahneman's System 1→System 2)
2. Pattern recognition feeds both the intuitive *evaluation* and the *selective search* that follows
3. The same knowledge structures (chunks/templates) serve both rapid intuition and deeper analysis
4. Emotions act as a **synchronization signal**, linking perception to appropriate action responses

---

## Finding 4: How Experts' Brains Process Positions Differently From Novices

### Behavioral-Level Differences

| Measure | Experts | Novices |
|---------|---------|---------|
| Fixation patterns | More fixations *between* pieces | More fixations *on* individual pieces |
| Visual span | Dramatically larger (gaze-contingent window studies) | Smaller, piece-by-piece |
| Reaction time on recognition tasks | 4x faster (knight task study) | Slower |
| First fixation duration | Differentiates target from lure positions (rapid recognition) | No first-fixation differentiation |
| Error rate on rapid evaluation | 44% of variance explained by Elo | Higher error rates |
| Chunk size | 10+ pieces per template | 3-5 pieces per chunk |
| Prime duration effects | Priming effects even with short primes | Only with longer primes |

### Neural-Level Differences

**Key brain regions identified (Bilalić et al., 2010-2019 series):**

1. **Posterior Middle Temporal Gyrus (pMTG)** — Object recognition
   - Links object identity to object affordances (what can I DO with this piece configuration?)
   - Connected with dorsal visual stream + parieto-prefrontal action network
   - Involved in semantic processing + inhibition/attention

2. **Collateral Sulcus (CoS)** — Pattern recognition
   - Links piece positions with typical spatio-functional layouts stored in memory
   - Connected with posterior medial cortex + hippocampus (scene perception, navigation)
   - Involved in face/shape perception

3. **Posterior Cingulate Cortex** — Holistic processing
   - Active in experts for chess configurations vs. scrambled displays
   - NOT overlapping with face-processing regions (FFA)
   - Specifically tuned to chess, not general visual expertise

4. **Right Hemisphere Homologues** — Bilateral engagement
   - Experts uniquely activate right-hemisphere areas homologous to left-lateralized regions in novices
   - Right hemisphere: global/ Gestalt processing
   - Left hemisphere: local/ analytic processing
   - Experts use BOTH hemispheres in parallel → automatic, holistic + analytic simultaneously

**Key neural findings:**
- **FFA (Fusiform Face Area)** is NOT re-purposed for chess expertise (contra the "expertise hypothesis"). FFA responds to chess stimuli in experts only when full-board naturalistic positions are used, and this is driven by stimulus properties, not skill per se.
- **ERPs (Event-Related Potentials)** differentiate experts from novices as early as **240 ms post-stimulus** (Wright, Gobet, Chassy & Ramchandani, 2013)
- **Theta power** in posterior regions is linked to chunk retrieval (EEG study, 2019)
- **Dorsal stream** (action-oriented "where/how" pathway) is more engaged in experts than ventral stream (object identification "what" pathway)

### The Biological Basis: Cell Assemblies (Chassy & Gobet, 2011)

Chassy & Gobet (2011) proposed that Hebb's (1949) concept of **cell assemblies** is the biological realization of chunks:
- Neurons that fire together, wire together → repeated exposure to similar patterns creates stable neural networks
- Cell assemblies can recruit neurons across multiple brain modules
- Recognition occurs when a perceived object activates the corresponding cell assembly in ~200-300ms
- The brain processes information in a sequence of stages, each operating in **parallel**
- Neural networks continuously reorganize to increase the number of recognizable patterns
- Experts may store up to **300,000 chunks** (Gobet et al., 2001)

This bridges:
- **Molecular level**: Synaptic plasticity (LTP/LTD) → 
- **Cellular level**: Cell assembly formation → 
- **Systems level**: Distributed networks across brain regions → 
- **Behavioral level**: Chunk/template recognition and intuitive decision-making

---

## Finding 5: Specific Mechanisms of Rapid Pattern Recognition

### The CHREST Architecture (Chunk Hierarchy and REtrieval Structures)

CHREST is the computational implementation of template theory, developed by Fernand Gobet and Peter Lane. Key parameters:

| Parameter | Value | What it means |
|-----------|-------|---------------|
| New chunk creation time | ~8 seconds | How long to form a new chunk |
| Information addition to existing chunk | ~2 seconds | Familiarization time |
| Template slot instantiation | ~250 ms | Rapid encoding of variable position |
| Visual STM capacity | 3 chunks | What can be held at once |
| LTM → STM transfer | 50 ms | Time to bring a chunk into awareness |
| Saccade/ attention shift | ~200 ms | Time to move visual focus |

### The Recognition Pipeline

```
1. Visual Input (0-100ms)
   ↓
2. Discrimination Net Traversal (100-300ms)
   ↓ — testing perceptual features at each node
3. Chunk Recognition (200-500ms)
   ↓ — matching patterns against stored chunks
4. Template Activation (300-600ms)
   ↓ — activating schema with slots
5. Slot Instantiation (600ms-2s)
   ↓ — encoding variable information (250ms per slot)
6. Production Activation (300ms-1s)
   ↓ — "if pattern X, consider move Y"
7. Emotional Tag Retrieval (200-500ms)
   ↓ — accessing associated emotional valence
8. Holistic Board Representation (2-5s)
   ↓ — cumulative integration across all recognized patterns
9. Intuitive Evaluation (1-5s)
```

### Three Mechanisms of Template-Supported Search

Gobet (1997) identified three specific mechanisms:

**Mechanism 1: Rapid LTM Storage**
Templates have slots that can be filled in ~250ms. During the 5-second presentation, experts can store 10-20 pieces of variable information into pre-existing template structures. This explains why experts can recall ~80% of a position after 5 seconds while novices recall ~30%.

**Mechanism 2: Search in Template Space**
Instead of searching only through possible moves (the physical space), experts can search through *template space* — recognizing that a position belongs to a known strategic category and accessing pre-compiled plans. Example: recognizing a "Sicilian Dragon" template accesses stored knowledge about typical kingside attacks, pawn breaks, and piece maneuvers — without having to calculate each branch.

**Mechanism 3: Mind's Eye Compensation**
Visual working memory ("mind's eye") decays rapidly. Templates provide a stable LTM structure that can refresh the mind's eye when attention returns to a position during analysis. This enables deeper search: the expert can "look away" from the board and still maintain an accurate internal representation.

### The Production System Connection

Chunks and templates are linked to **productions** (condition-action rules from Newell & Simon's SOAR):
- Condition: pattern recognized on the board
- Action: recommended move, plan, or evaluation

Example production from template theory (Gobet & Chassy, 2009): "If there is an open file, consider moving a rook onto it." These productions are:
- Acquired through years of practice
- Automatically activated upon pattern recognition
- Highly selective (only ~100 terminal nodes explored in expert search, vs. thousands by computers)
- Both intuitive (rapid, unconscious activation) and rational (justifiable after the fact)

### Why This Is NOT Just "Intuition vs. Analysis"

The template theory framework shows that the debate between "intuition vs. analysis" is a false dichotomy. Two important findings:

1. **Gobet (1998)** found that when given complex positions and NO time limit, strong masters searched 10x deeper than previous studies suggested — but they still relied on pattern recognition to guide that search selectively.

2. **Chabris & Hearst (2003)** found that grandmasters DO make more errors in rapid chess vs. slow chess, but the effect is modest — supporting the view that pattern recognition carries most of the load even in slow play.

3. **Campitelli & Gobet (2004)** showed 5-second move-finding tasks produce large skill differences, and the quality of the first move chosen (intuitive) correlates strongly with ultimate choice after deliberation.

The template theory resolves this: pattern recognition enables selective search; selective search refines pattern recognition. They are not competing mechanisms but cooperating ones operating on the same knowledge base.

---

## Synthesis: How the Pieces Fit Together

### Timeline of Theory Development

```
1973: Chase & Simon — Chunking Theory
  - Expert memory = 50,000 chunks in LTM
  - STM limited to ~7 chunks
  ↓ (empirical challenges emerge: interference resistance, multi-board recall)
1996: Gobet & Simon — Template Theory
  - Adds templates (schema with slots)
  - ~250ms slot instantiation
  - CHREST computational implementation begins
  ↓ (applied to problem-solving, search, nursing, education)
2008-2009: Gobet & Chassy — Unified Theory of Intuition
  - Reconciles Dreyfus (holistic) and Simon (analytic)
  - Five characteristics of expert intuition
  - Emotion as integral component
  ↓ (biological level needed)
2011: Chassy & Gobet — Biological Basis
  - Cell assemblies as neural substrate for chunks
  - Emotions modulate perception-memory interaction
  ↓ (empirical test of key predictions)
2023: Chassy, Lahaye, Didierjean & Gobet — World-Class Study
  - 44% of variance explained by Elo
  - Complexity effect confirmed (supporting template theory over Dreyfus)
  - Holistic intuition validated with highest-ever skill sample
```

### The Core Insight

The research program from 1973-2023 has progressively refined one key insight: **Expert intuition is not magic and not pure analysis — it is the rapid, unconscious, holistic output of a massive, well-organized, emotionally-tagged database of patterns, built through years of deliberate practice, operating within severe cognitive constraints (limited STM, slow learning, bounded rationality).**

---

## Limitations and Caveats

1. **The "SIT" acronym**: Extensive search found no paper by Gobet & Chassy that uses "SIT" or "Synchrony of Intuition and Thought" as a formal label. The 2009 paper is simply "Expertise and intuition: A tale of three theories." The term may be from secondary literature or informal usage. The *concept* of synchrony is definitely present; the *acronym* may not be.

2. **Evaluation vs. move choice**: The 2023 study uses position EVALUATION as the measure of intuition. This is arguably more holistic than move CHOICE, but it may not capture all aspects of chess intuition (e.g., tactical alertness, strategic planning).

3. **Computational reference**: The 2023 study used Fritz 12 (a chess engine) to establish ground-truth evaluations. Engines evaluate differently from humans — they may miss positional subtleties that humans value.

4. **Sample limitations**: Although the 2023 sample is the best ever assembled, it's still 63 players (15 female). Gender analysis wasn't possible. Cross-cultural factors were not examined.

5. **Emotion measurement**: The 2023 study didn't directly measure emotional responses during evaluation. The emotional component of intuition (proposed in 2009) remains experimentally underexplored.

6. **CHREST aging**: The CHREST architecture, while still maintained, has not kept pace with modern AI/neural network approaches. Its Lisp implementation and symbolic discrimination net approach may miss distributed processing aspects that modern connectionist models capture.

---

## Weakest Evidence

1. **The 250ms slot instantiation timing**: This core parameter of template theory comes from computational fitting, not direct neural measurement. No independent replication has confirmed this specific timing.

2. **300,000 chunk estimate**: The claim that top experts store ~300,000 chunks (from CHREST simulations) is an extrapolation from chess databases. Direct empirical confirmation at this scale is impossible with current methods.

3. **Emotion → intuition link**: While theoretically plausible and supported by nursing studies, the specific mechanism by which emotional tags on chunks/templates influence chess decision-making has not been directly measured or manipulated.

---

## Key Implications for Grandmaster-in-60-Minutes Project

1. **Pattern recognition is the bottleneck**, not search speed or intelligence. The 2023 study shows 44% of variance in evaluation accuracy is just Elo (knowledge).

2. **Template formation requires repeated exposure** (~8 seconds per chunk, thousands of repetitions). This severely constrains any accelerated learning approach.

3. **The 3-4 second window** is critical: The 2023 data shows intuition's work is done within the first 3-4 seconds. Training evaluation within this window may be effective.

4. **Emotional tagging** of positions (positive/negative "feel") is part of expert intuition. Training might leverage emotional resonance to accelerate chunk formation.

5. **Bilateral brain engagement** (right + left hemisphere) characterizes expert processing. Training methods that engage both analytic (L) and Gestalt (R) processing may be more effective.

6. **The 4366 Elo ceiling**: Extrapolating from the regression, even Magnus Carlsen has room for intuitive improvement — suggesting that there is NO ceiling on pattern recognition improvement within human limits.

---

## Bibliography

1. Chassy, P., Lahaye, R., Didierjean, A., & Gobet, F. (2023). Intuition in chess: A study with world-class players. *Psychological Research, 87*(8), 2380-2389. https://doi.org/10.1007/s00426-023-01823-x

2. Gobet, F., & Simon, H. A. (1998). Expert chess memory: Revisiting the chunking hypothesis. *Memory, 6*(3), 225-255. https://doi.org/10.1080/741942359

3. Gobet, F., & Simon, H. A. (1998). Expert memory: A comparison of four theories. *Cognition, 66*, 115-152. https://doi.org/10.1016/s0010-0277(98)00020-1

4. Gobet, F., & Chassy, P. (2009). Expertise and intuition: A tale of three theories. *Minds and Machines, 19*(2), 151-180. https://doi.org/10.1007/s11023-008-9131-5

5. Chassy, P., & Gobet, F. (2011). A hypothesis about the biological basis of expert intuition. *Review of General Psychology, 15*(3), 198-212. https://doi.org/10.1037/a0023958

6. Gobet, F., & Simon, H. A. (1996). Templates in chess memory: A mechanism for recalling several boards. *Cognitive Psychology, 31*, 1-40. https://doi.org/10.1006/cogp.1996.0011

7. Chase, W. G., & Simon, H. A. (1973). Perception in chess. *Cognitive Psychology, 4*, 55-81.

8. Dreyfus, H. L., & Dreyfus, S. E. (1986). *Mind over machine: The power of human intuition and expertise in the era of the computer*. Free Press.

9. Gobet, F. (1997). A pattern-recognition theory of search in expert problem solving. *Thinking and Reasoning, 3*(4), 291-313.

10. Bilalić, M., Kiesel, A., Pohl, C., Erb, M., & Grodd, W. (2011). It takes two—Skilled recognition of objects engages left and right hemispheres. *PLoS ONE, 6*(1), e16202.

11. Bilalić, M., Langner, R., Erb, M., & Grodd, W. (2010). Mechanisms and neural basis of object and pattern recognition: A study with chess experts. *Journal of Experimental Psychology: General, 139*(4), 728-742.

12. Bilalić, M., Turella, L., Campitelli, G., Erb, M., & Grodd, W. (2012). Expertise modulates the neural basis of context dependent recognition of objects and their relations. *Human Brain Mapping, 33*, 2728-2740.

13. Gobet, F. (2013). Chunks, schemata, and retrieval structures. *Frontiers in Psychology, 6*, 1785.

14. Lane, P. C. R., & Gobet, F. (2010). Building models of learning and expertise with CHREST. *Proceedings of the Cognitive Science Society*.

15. Gobet, F., Lane, P. C. R., Croker, S., Cheng, P. C.-H., Jones, G., Oliver, I., & Pine, J. M. (2001). Chunking mechanisms in human learning. *Trends in Cognitive Sciences, 5*(6), 236-243.

16. Gobet, F., & Jansen, P. (in press). Training in chess: A scientific approach. In *Education and chess*.

17. Wright, M. J., Gobet, F., Chassy, P., & Ramchandani, P. N. (2013). ERP responses to chess stimuli in expert players. *Cognitive Neuroscience, 4*(2), 104-111.

18. De Groot, A. D., & Gobet, F. (1996). *Perception and memory in chess: Studies in the heuristics of the professional eye*. Van Gorcum.

19. Campitelli, G., & Gobet, F. (2004). Adaptive expert decision making: The interaction between search and recognition. *International Computer Games Association Journal, 27*(4), 201-214.

20. Charness, N., Reingold, E. M., Pomplun, M., & Stampe, D. M. (2001). The perceptual aspect of skilled performance in chess: Evidence from eye movements. *Memory & Cognition, 29*(8), 1146-1152.

21. Chabris, C. F., & Hearst, E. S. (2003). Visualization, pattern recognition, and forward search: Effects of playing speed and sight of the position on grandmaster chess errors. *Cognitive Science, 27*, 637-648.

22. Simon, H. A. (1995). Explaining the ineffable: AI on the topics of intuition, insight and inspiration. *Proceedings of the 14th International Joint Conference on AI*, 939-948.

23. Klein, G. (2003). *Intuition at work*. Doubleday.

24. Hebb, D. O. (1949). *The organization of behavior*. Wiley.

25. Reingold, E. M., Charness, N., Pomplun, M., & Stampe, D. M. (2001). Visual span in expert chess players: Evidence from eye movements. *Psychological Science, 12*(1), 48-55.
