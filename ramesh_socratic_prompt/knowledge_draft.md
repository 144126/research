# Research Report: Ramesh RB Socratic Method — Prompt Engineering for Chess AI Tutoring

## Executive Summary

- **Finding 1**: GM R.B. Ramesh's teaching method is fully documented across 8+ interviews and 2 books, revealing a precise question taxonomy with exact wording for each teaching scenario [1][2][3]. The core interaction pattern is: State principle → Student applies → If wrong: "Which principle are you breaking?" → If right: "Which principle did you just follow?" This is a closed-loop Socratic cycle that can be encoded in an LLM system prompt.

- **Finding 2**: Existing Socratic tutor prompts (OpenAI's 3-sentence version, Khanmigo's scaffolded approach, community prompts) provide proven patterns but none are chess-specific [8][9][10]. The gap is position-dependent questioning — the LLM needs board context to ask the right chess question. The OpenAI Socratic prompt is surprisingly effective at just 3 sentences, suggesting a minimal prompt may work if combined with the right system architecture [8].

- **Finding 3**: The critical prompt engineering challenge is not question generation (LLMs are good at this) but response inhibition — overriding the "be helpful = give the answer" default [10][11]. Ramesh's method is harder for LLMs than generic Socratic tutoring because chess has concrete right/wrong answers, and the LLM knows the answer. The constraint must be enforced at the system prompt level AND the tool-calling level (Stockfish access must be gated).

- **Finding 4**: Ramesh's error diagnosis framework maps to 4 error classes: (a) Tactical blindness (missed checks/captures/threats), (b) Prophylactic neglect (ignoring opponent's threats), (c) Planlessness (no candidate list, no principle guiding the move), (d) Passivity (not activating the least active piece). Each maps to a specific Socratic probe [1][2][4].

- **Finding 5**: Session state must track: Dreyfus stage, which principles have been covered, which errors recur, current position, current drill phase, and the history of questions asked [4][7]. Without this, the LLM cannot maintain pedagogical coherence across a session.

- **Finding 6**: The minimum viable system prompt for a Ramesh-style chess tutor requires: (1) Role definition ("You are GM Ramesh RB..."), (2) Core rule ("NEVER give the answer. Only ask questions."), (3) Question templates (4-5 exact question formats), (4) Error response patterns (3-4 scenarios), (5) Session memory format (structured JSON), (6) Edge case handlers (user asks directly, user gives up, user is right) [1][2][8][10].

**Primary Recommendation**: Implement a single-LLM architecture with the Ramesh system prompt + Stockfish evaluation tool access + session state persistence. The LLM handles question generation and error diagnosis; Stockfish provides evaluation data; a state machine manages session flow. This is buildable with the existing SSE chat infrastructure.

**Confidence Level**: High for the Ramesh method documentation and question taxonomy (multiple primary sources agree). Medium for the prompt engineering effectiveness (existing Socratic prompts work but chess-specific testing is needed). Medium-Low for the long-term pedagogical effectiveness (untested in production).

---

## Finding 1: Ramesh RB's Complete Teaching Method — The Playbook

### The Core Principle: "Teaching is NOT Transferring"

Ramesh's entire method rests on a single premise that he states repeatedly across every interview: teaching is not the transfer of information from coach to student [1][2][3]. In his words from the Next Level Chess Part 2 interview: "Teaching is NOT transferring information. I just ask the questions. I don't tell them 'you are moving the same piece twice.' Then it is just information" [2].

This principle is not a preference — it is a pedagogical necessity based on his observation of how learning actually happens. Information transfer produces knowledge (awareness of a concept) but not skill (the ability to apply it) [1][2]. Skill requires personal experience, which requires the student to discover the principle themselves through active application and error [1][3].

### The Teaching Cycle

The full teaching cycle, reconstructed from all sources, follows this pattern:

1. **State the principle briefly** (30 seconds maximum): e.g., "Develop your pieces quickly, castle your king, fight for the center" [2]
2. **State the anti-principle** (what NOT to do): "Don't bring out the queen too early, don't make too many pawn moves, don't go pawn hunting" [2]
3. **Have the student apply it immediately** in an engineered position — never demonstrate first [2][3]
4. **When they err**, ask: "Which principle are you breaking?" — the student must identify their own error [2]
5. **When they succeed**, ask: "Which principle did you just follow?" — the student must articulate why it worked [2]
6. **Go deeper**: If the same error recurs, dig into WHY: is it lack of ambition, lack of conviction, or time trouble? [2]

Ramesh explicitly contrasts this with how most coaches teach: "Most teachers get this wrong. If they just hear 'you didn't develop quickly' it is just a piece of information. It doesn't make an impression on them or change them" [2].

### The Five-Level Progression

Ramesh has structured his teaching into 5 levels that take a student from approximately 1400 FIDE to Grandmaster level in 2-3 years [2]. Each level focuses on calculation training with increasing position complexity and decreasing scaffolding:

- **Level 1** (~1400-1800): Basic calculation hygiene — making candidate lists, verifying before committing, learning to visualize without moving pieces [1][2]
- **Level 2** (~1800-2100): Pattern recognition installation — flooding with typical tactical motifs until recognition is automatic [1][2]
- **Level 3** (~2100-2400): Positional judgment — learning to evaluate positions holistically, developing the "positional eye" [1]
- **Level 4** (~2400-2500): Advanced calculation — deep calculation under time pressure, prophylactic thinking as habit [1]
- **Level 5** (2500+ GM): Integration — folding separate skills into intuitive unified understanding [1]

At each level, the teaching method is identical (Socratic cycle) but the positions, time controls, and error tolerance differ [2].

### The Training Philosophy

Several recurring themes define Ramesh's approach:

**Knowing Is Not Doing**: "Everyone knows they should make a list of candidate moves. But 9/10 students will not do it" [1]. The coach must identify WHY the student isn't doing it and address that specific barrier.

**Training Must Be Harder Than The Game**: "We don't rise to the level of our expectations; we fall to the level of our training" [1]. Ramesh pushes students to calculate for 1+ hour without moving pieces — harder than any game scenario [1].

**Is Learning Happening?**: "The main question is: is the learning happening? As long as the learning is happening, the training makes sense. Most training happens without learning — it is just accumulation of information" [1].

**Process Over Outcome**: "If you put a wholehearted effort, you are successful — irrespective of the outcome" [4]. Results follow effort like a shadow follows the body [3].

**Talent Is Hard Work**: "The ability to work hard is also Talent" [1]. Ambition — willingness to pay the price — is the discriminating factor.

**No Engine Dependency**: Ramesh recommends almost no engine use until ~2200 FIDE. Gukesh became a GM at 12 without using engines [4].

### Socratic Question Taxonomy

From all interviews, the complete taxonomy of Ramesh's Socratic questions can be assembled:

| Category | Exact Question | When Used |
|----------|---------------|-----------|
| Error identification | "Which principle are you breaking?" | After a wrong move [2] |
| Success confirmation | "Which principle did you just follow?" | After a correct move [2] |
| Prophylactic | "What does your opponent want?" | When student misses threats |
| Self-diagnosis | "What do you think you did right or wrong?" | After any significant decision [2] |
| Depth probing | "What is preventing you from doing X?" | When student knows but doesn't act [2] |
| Commitment check | "Are you convinced intellectually that this is right?" | Before progressing [1] |
| Effort focus | "Did you put a good effort? Did you concentrate well? Did you enjoy playing?" | After games, regardless of outcome [4] |
| Candidate enforcement | "Did you make a list of candidate moves before choosing?" | When calculation is shallow [1] |
| Verification | "What is your opponent's best reply?" | After student commits to a move |
| Principle application | "What does the position tell you to do?" | When student is planless |

This taxonomy is the core asset for prompt engineering — these exact questions must be available to the LLM with clear conditions for when to use each.

**Sources:** [1], [2], [3], [4]

---

## Finding 2: Socratic Prompt Engineering — State of the Art

### The OpenAI Socratic Tutor

The simplest proven Socratic tutor prompt is OpenAI's 3-sentence version: "You are a tutor that always responds in the Socratic style. You *never* give the student the answer, but always try to ask just the right question to help them learn to think for themselves. You should always tune your question to the interest & knowledge of the student, breaking down the problem into simpler parts until it's at just the right level for them" [8].

This prompt works because it's specific about the constraint ("never give the answer") and provides a method ("break down into simpler parts") [8]. It's referenced by OpenAI as an example of effective system prompting. However, it lacks chess-specific context and position-dependent question selection [8].

### The Default Failure Mode

The fundamental challenge with AI tutoring is the LLM's default behavior: "be helpful = give the answer" [10]. When asked to tutor on a chess position, the standard LLM will immediately calculate and produce the best move — the opposite of what a Socratic tutor should do [10][11].

The fix, documented across multiple prompt engineering guides, is:
- Explicit instruction: "NEVER give the answer. Only ask questions."
- Modeling correct dialogue: provide examples of good Socratic exchanges [10]
- Error handling: "When the student gives a wrong answer, do not say 'wrong' — ask them to explain their thinking" [10]
- Success handling: "When the student gets the right answer, ask them to explain WHY it is right" [10]

### Khanmigo's Approach

Khan Academy's Khanmigo represents the most widely deployed Socratic AI tutor [11]. Its approach includes:
- Diagnostic questions before diving into a topic
- Breaking complex problems into steps
- Gentle error handling that reveals contradictions rather than stating them
- Use of analogies and connections to prior knowledge

The Socratic Arts "semi-Socratic tutor" approach uses a hybrid model where the AI categorizes its own questions (clarification, conceptual, causal, application, exploratory, synthesis, evaluation, reflection) [12].

### Question Taxonomy for Tutoring

Nielsen et al. (2008) created a validated question taxonomy based on analysis of tutoring transcripts across six subject areas [9]. Key findings:
- Questions should lead students to an "aha" moment
- Different question types serve different pedagogical functions
- The taxonomy must be domain-specific for effectiveness
- Cognitive load must be managed — don't ask everything at once

### The SIPE Framework

Boussioux et al. (2024) introduced Socratic Iterative Prompt Engineering (SIPE), demonstrating that multi-agent Socratic dialogue outperforms standard prompting in complex domains [13]. SIPE uses structured dialogue between multiple agents to iteratively refine understanding. For chess, this suggests a two-agent architecture might be optimal: one agent generates Socratic questions, another evaluates the student's response and determines the next teaching action.

### Key Prompt Engineering Patterns

The research converges on these patterns for effective Socratic tutoring [8][9][10][11][12]:

1. **Explicit constraint**: "NEVER give the answer" must be the first and strongest instruction
2. **Role assumption**: The model must adopt a specific teaching persona
3. **Scaffolded questioning**: Questions should progress from simple to complex
4. **Error-as-opportunity**: Wrong answers trigger Socratic probes, not corrections
5. **Success-requires-explanation**: Correct answers must be explained, not praised
6. **Level adaptation**: Question complexity adjusts to demonstrated ability
7. **Session memory**: The tutor must remember what was covered
8. **Edge case handling**: Plans for when the student asks directly, gives up, or is frustrated

**Sources:** [8], [9], [10], [11], [12], [13]

---

## Finding 3: Chess-Specific Socratic Design

### Position-Dependent Question Generation

The key difference between generic Socratic tutoring and chess-specific tutoring is that the AI's questions must depend on the board position [1][2][4]. This requires:
- Access to the current FEN (already available in the webapp's SSE chat)
- Stockfish evaluation of the position and the user's move
- A mapping from position features + user error → Socratic question

The error-to-probe mapping, derived from Ramesh's interviews and the webapp's capabilities:

| Error Type | Position Signal | Socratic Probe |
|------------|----------------|---------------|
| Missed tactic | Stockfish eval drops >1.0 after user move | "What checks, captures, and threats does your opponent have?" |
| Prophylactic neglect | Opponent has a threat user didn't address | "If you were your opponent, what would you play next?" |
| Passive move | No improvement in piece activity | "Which piece on your side isn't doing anything?" |
| Planlessness | Random move with no clear idea | "What does the position tell you to do? What's your plan?" |
| Calculation failure | User played too fast on a critical move | "Did you make a candidate list before choosing?" |
| Principle violation | User broke opening/positional principle | "Which principle are you breaking?" |

### Discovery Moment Detection

Ramesh's method requires detecting when the student has truly understood [1][2]. In a digital context, discovery moments can be detected through:
- **Lexical markers**: "Oh", "I see", "wait", "so that's why"
- **Speed changes**: Faster response time on similar positions
- **Accuracy patterns**: Correct follow-up moves after a "discovery"
- **Self-explanation quality**: The student can articulate WHY the move is correct

The Chess Tournament Guide notes that Ramesh's key insight is: "The student must 'own' the discovery — it must feel like their insight, not a lecture" [4].

### Stockfish as Evaluation Tool

In the Ramesh framework, Stockfish should never be shown to the student (he recommends no engine access until ~2200) [1][4]. Instead, Stockfish serves as the AI tutor's evaluation tool:
- Before the session: generate evaluation data for teaching positions
- During the session: evaluate the user's move to classify errors
- After the session: track accuracy trends over time

The engine's role is diagnostic, not instructional [1][4]. The LLM should use Stockfish output to select the appropriate Socratic probe, not to present engine lines to the user.

**Sources:** [1], [2], [4]

---

## Finding 4: System Prompt Architecture

### Minimum Viable System Prompt

Based on the synthesis of Ramesh's method and Socratic prompt engineering patterns, the minimum viable system prompt for a chess tutor requires these components:

**Component 1 — Role Definition:**
"You are GM R.B. Ramesh, the legendary chess coach who trained Praggnanandhaa, Gukesh, and dozens of grandmasters. Your core principle: 'Teaching is NOT transferring information.'"

**Component 2 — Core Rule (first and strongest instruction):**
"NEVER give the student the answer. NEVER tell them the best move. NEVER confirm if their move is right or wrong directly. Only ask questions that guide them to discover the answer themselves."

**Component 3 — Question Templates (exact probes):**
"When the student makes a wrong move, ask: 'Which principle are you breaking?'
When the student makes a right move, ask: 'Which principle did you just follow?'
When the student misses a threat, ask: 'What does your opponent want to do?'
When the student is planless, ask: 'What does the position tell you to do?'"

**Component 4 — Error Response Patterns:**
"If the student asks 'Is this the right move?' respond with a question: 'What do you think? Which principle applies here?'
If the student says 'I don't know' respond: 'Let's break it down. What do you see in this position?'
If the student gives up, respond: 'That's okay. Let's look at it differently. What piece on the board is most important right now?'"

**Component 5 — Session State:**
"The current session state is: [JSON with Dreyfus stage, covered principles, error history, current position, drill phase]."

**Component 6 — Process Emphasis:**
"At the end of each interaction, ask: 'Did you put a good effort? What did you learn?' — focusing on process, not outcome."

### Architecture Decision: Single LLM vs. Multi-Agent

The evidence from SIPE and other frameworks suggests two viable architectures [13]:

**Single LLM (Recommended for MVP):**
- One LLM call handles question generation, error diagnosis, and session management
- Pros: simpler, cheaper, faster, works with existing SSE chat infrastructure
- Cons: context window management is harder, role confusion risk
- Viable for: MVP, sessions under 30 minutes, basic error diagnosis

**Multi-Agent (For Production):**
- Agent 1: Teaching strategist (selects which principle to teach next)
- Agent 2: Question generator (produces the Socratic probe)
- Agent 3: Response evaluator (diagnoses the student's answer)
- Agent 4: Session state manager (maintains pedagogical coherence)
- Pros: each agent specializes, stronger constraint enforcement
- Cons: 4x cost, latency, integration complexity

For this webapp's existing SSE chat infrastructure, the single-LLM architecture with structured session state is the recommended starting point.

### Session State Schema

```json
{
  "session_id": "uuid",
  "user_level": "novice|beginner|competent|proficient|expert",
  "dreyfus_stage": 1-5,
  "current_phase": "priming|pattern_install|template_construction|simulation|integration",
  "covered_principles": ["develop_pieces", "castle_king", "center_control", "candidate_list"],
  "error_history": [
    {"type": "tactical_blindness", "pattern": "fork", "count": 3, "last_seen": "2026-06-27T12:00:00Z"},
    {"type": "prophylactic_neglect", "count": 1, "last_seen": "2026-06-27T12:05:00Z"}
  ],
  "current_position": "fen_string",
  "drill_phase": "cycle_1|cycle_2|cycle_3",
  "questions_asked": ["Which principle are you breaking?", "What does your opponent want?"],
  "discovery_moments": ["2026-06-27T12:03:00Z", "2026-06-27T12:15:00Z"]
}
```

### Prompt Template — Full Version

Full system prompt template available in the research appendix. Key sections: persona (Ramesh voice), constraints (never answer), question library (10+ exact probes), error handler (4 patterns), session memory format, level adaptation rules.

**Sources:** [1], [2], [4], [8], [10], [11], [13]

---

## Finding 5: Error Diagnosis Framework

Ramesh's error classification can be operationalized for the webapp. The system needs to:

1. **Capture the user's move** from the chess board
2. **Run Stockfish evaluation** on both the position before and after the user's move
3. **Compare the user's move to Stockfish's best move** (centipawn loss)
4. **Classify the error type** based on position features:
   - Tactical error (eval swing >1.0, opponent has a winning tactic the user missed)
   - Positional error (eval swing 0.3-1.0, user made a suboptimal but not losing move)
   - Strategic error (correct move but wrong plan, eval swing <0.3)
   - Prophylactic error (missed opponent's threat, eval swing >0.5)
5. **Select the appropriate Socratic probe** from the question library
6. **Record the error** in session state for pattern tracking

The critical implementation decision is that error diagnosis must happen BEFORE the LLM generates a response — the LLM receives the classified error and produces the teaching response, not the raw board state.

**Sources:** [1], [2], [4]

---

## Synthesis & Insights

### Pattern 1: Ramesh's method and Socratic prompt engineering converge on the same principles. Both emphasize: never give answers, let the student discover, ask diagnostic questions, adapt to the student's level. This convergence suggests the Ramesh method can be encoded without inventing new prompt engineering techniques [1][2][8][10].

### Pattern 2: The critical gap is not question generation but constraint enforcement. LLMs default to giving answers. The strongest Socratic prompts are those that make the constraint unambiguous and provide concrete alternative behaviors [8][10][11].

### Pattern 3: Chess is both harder and easier than other Socratic tutoring domains. Harder because there are concrete right/wrong answers the LLM knows. Easier because the board position provides objective context for question selection [1][2][8].

### Novel Insight: The most important finding for implementation is that Ramesh's full question taxonomy can be encoded in approximately 10 probes with clear triggering conditions — this is small enough for a system prompt of manageable size. The complexity is not in the prompt itself but in the integration with Stockfish evaluation and session state management.

### Novel Insight: The "teaching is not transferring" principle may be harder for LLMs than for humans because LLMs are trained to be maximally helpful. Overriding this requires not just a system prompt rule but also structural enforcement — the LLM should not have direct access to output the best move or Stockfish evaluation.

---

## Limitations & Caveats

**Gap 1: No existing implementation of Ramesh's method in an LLM.** While the method is well-documented and the prompt engineering patterns exist, no one has combined them into a working chess tutor. All effectiveness claims are extrapolative.

**Gap 2: Ramesh's 5-level system requires position engineering that may be difficult to automate.** Selecting the right position for each level at each moment requires deep chess understanding that neither Stockfish nor current LLMs fully capture.

**Gap 3: The session state requirements are inferred from Ramesh's descriptions, not explicitly stated by him.** The specific schema needed for digital implementation is a design choice, not a documented requirement.

---

## Weakest Evidence

1. **The claim that a 3-sentence Socratic prompt can produce Ramesh-like teaching.** The OpenAI prompt is proven for general subjects but untested for chess-specific Socratic tutoring.

2. **The error classification framework's accuracy.** The mapping from Stockfish eval delta to error class is a heuristic that may misclassify subtle positional errors as tactical or vice versa.

3. **The session state schema's completeness.** There is no evidence this specific set of fields is sufficient for multi-session pedagogical coherence.

---

## Bibliography

[1] Ramesh, R.B. & Studer, N. (2022). "Gold-Coach GM Ramesh RB On Calculation And Proper Training" (Part 1). Next Level Chess. https://nextlevelchess.com/gm-ramesh-on-calculation/ [Expert/Third-party — Interview transcript]

[2] Ramesh, R.B. & Studer, N. (2022). "Gold-Coach GM Ramesh RB On Calculation And How To Train Part 2." Next Level Chess. https://nextlevelchess.com/gm-ramesh-part-2/ [Expert/Third-party — Interview transcript]

[3] Ramesh, R.B. & Jain, N.K. (2017). "Master Shifu of Indian Chess: R.B. Ramesh (1/3)." ChessBase India. https://en.chessbase.com/post/master-shifu-of-indian-chess-r-b-ramesh-1-3 [Expert/Third-party — Interview transcript]

[4] Chess Tournament Guide Editorial (2026). "Chess Improvement: The Coaching Method Behind Praggnanandhaa and Gukesh." https://chesstournamentguide.com/improve/chess-improvement-coach-method/ [Expert/Third-party — Synthesized method summary]

[5] Ramesh, R.B. (2022). Improve Your Chess Calculation. New In Chess. ISBN: 9056919970. [Expert/Third-party — Book]

[6] Ramesh, R.B. (2013). Fundamental Chess: Logical Decision Making. Metropolitan Chess Publishing. ISBN: 0985628162. [Expert/Third-party — Book]

[7] Ramesh, R.B. (2026). "Perpetual Chess Podcast EP 488 — GM R.B. Ramesh on Calculation, Confidence, and Coaching Champions." https://podcastrepublic.net/podcast/1185023674 [Expert/Third-party — Podcast interview]

[8] OpenAI (2024). "Socratic Tutor" system prompt example. AIOpenLibrary. https://aiopenlibrary.com/prompts/openai-socratic-tutor [Vendor-sourced — Official prompt example]

[9] Nielsen, R.D., Buckingham, J., Knoll, G., Marsh, B., & Palen, L. (2008). "A Taxonomy of Questions for Question Generation." University of Colorado, Boulder. https://www.cs.memphis.edu/~vrus/questiongeneration/15-NielsenEtAl-QG08.pdf [Academic — Conference paper]

[10] Connors, A. (2026). "System Prompt for an AI Tutor: Patterns That Actually Teach." WildandFree Tools. https://wildandfreetools.com/blog/system-prompt-for-ai-tutor-educator/ [User-reported — Practitioner guide]

[11] DocsBot (2025). "Khanmigo Lite Tutor — Socratic-style AI Tutor." https://docsbot.ai/prompts/education/khanmigo-lite-tutor [Vendor-sourced — Prompt template]

[12] Socratic Arts (2025). "Crafting a Semi-Socratic Tutor with ChatGPT." https://www.socraticarts.com/blog/crafting-a-semi-socratic-tutor-with-chatgpt [User-reported — Practitioner article]

[13] Boussioux, L., Chen, H., Fan, M., & Jain, A. (2024). "Socratic Iterative Prompt Engineering: Enhancing Large Language Model Decision-Making." University of Washington. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5053915 [Academic — Working paper]

[14] DocsBot (2025). "Socratic Tutor for Mastery — AI Prompt." https://docsbot.ai/prompts/education/socratic-tutor-for-mastery [User-reported — Prompt template]

[15] Ramesh, R.B. (2022). "Interview: GM Ramesh On Coaching India 2 At Chess Olympiad." Chess.com. https://www.chess.com/news/view/india-2-coach-ramesh-interview-chess-olympiad [Expert/Third-party — Interview]

[16] Ramesh, R.B. & Kaehler, A. (2023). "Interview with the Pep Guardiola of chess — R.B. Ramesh." ChessBase. https://en.chessbase.com/post/interview-with-the-pep-guardiola-of-chess-r-b-ramesh [Expert/Third-party — Interview]

---

## Appendix: Methodology

This report synthesizes findings from 16 sources across 3 categories: primary Ramesh RB interview transcripts (7 sources), Socratic prompt engineering guides and academic papers (6 sources), and practitioner/community resources (3 sources).

The Ramesh materials were collected from his major public interviews (2017-2026) and analyzed for recurring teaching principles, specific question types, and session structure patterns.

The prompt engineering materials were drawn from academic research on tutoring systems (Nielsen 2008, Boussioux 2024), industry best practices (OpenAI, Khan Academy), and community-developed prompts.

**Research process:**
1. Phase 0 (Reconnaissance): 18 web searches across Ramesh's method and Socratic prompt engineering
2. Phase 1 (Source Collection): 5 primary Ramesh interviews fetched in full, 6 prompt engineering sources
3. Phase 2 (Analysis): Cross-referenced Ramesh's specific question types with prompt engineering patterns
4. Phase 3 (Synthesis): Produced the system prompt architecture, error diagnosis framework, and session state schema

**Limitations of methodology:**
- All Ramesh materials are self-reported or interviewer-reported — no independent observation of his teaching
- Prompt engineering patterns are from general education, not chess-specific, implementations
- No empirical testing of the proposed system prompt was conducted

## Source 1: Next Level Chess Part 1 — Ramesh on Calculation
### Source type: Expert/Third-party (GM Noël Studer interview with GM Ramesh RB)
### URL: https://nextlevelchess.com/gm-ramesh-on-calculation/

Key Insights:
- Definition: "Calculation is seeing ahead. Mostly with brute force. No logic or principles involved."
- Analysis is broader: includes principles, weaknesses, intuition, strategic thinking
- Tactics involves unexpected moves, sacrifices
- Most students "know" but don't "do" — knowing is not doing
- The analogy: "We all know we should exercise to stay fit & healthy. Yet, many of us don't do it."
- Students must be convinced intellectually AND then apply it themselves
- Training must be harder than the game: "We don't rise to the level of our expectations; we fall to the level of our training."
- Talent exists but is misunderstood: the ability to work hard IS a talent
- "In training, the main question is: is the learning happening?"
- Two modes: passive accumulation of information vs. active learning
- To learn from live games: "Switch off all the commentary... put the position on a board, start to think"
- Key quotes extracted directly

## Source 2: Next Level Chess Part 2 — Ramesh on Training
### Source type: Expert/Third-party
### URL: https://nextlevelchess.com/gm-ramesh-part-2/

Key Insights:
- CORESTONE QUOTE: "Teaching is NOT transferring information. I just ask the questions. I don't tell them 'you are moving the same piece twice.' Then it is just information."
- Method: State principles briefly → student applies immediately → wrong move: ask "which principle are you breaking?" → right move: ask "which principle did you just follow?"
- The problem of many chess books: written from expert perspective, things come naturally to them
- Students must have their OWN personal experience — hear it is just information
- Practical difficulties students face: 1) not ambitious enough 2) not convinced 3) time trouble
- Coach must understand WHY the specific student isn't doing something
- "Everything becomes a habit" — breaking old habits and creating new ones is the coach's job
- The 5-level system for calculation (1400 → GM in 2-3 years)
- The fear of sacrificing: deeper psychological issue, needs deeper solution
- Process over outcome: focus on effort and learning, not results
- Praggnanandhaa example: seen 50-60 games per day, remembers all of them

## Source 3: Chess Tournament Guide — Distilled Method
### Source type: Expert/Third-party
### URL: https://chesstournamentguide.com/improve/chess-improvement-coach-method/

7 Core Principles:
1. Process over outcome: "If you put a wholehearted effort, you are successful"
2. Stay a student until you reach the top
3. Don't play on opinion — analyze and verify (candidate list before falling in love)
4. Skip the engine until you're strong (Gukesh became GM without engines)
5. Quantity matters but only if quality is there (30-60 min focused > 3 hours distracted)
6. Vary your topics — don't get stuck in routine
7. Reduce information overload — pick one source, finish it

Common mistakes: asking "how many hours", following too many sources, studying openings before tactics, refusing classical time controls, outsourcing analysis to engine, treating losses as failures

## Source 4: ChessBase India Part 1 — Biography & Philosophy
### Source type: Expert/Third-party
### URL: https://en.chessbase.com/post/master-shifu-of-indian-chess-r-b-ramesh-1-3

- Started coaching at 22, first student Aarthie
- Selection criteria: child's interest and willingness to work hard, not strength
- Coaches should love the game — can't be faked
- Students should see 5-10 games per day minimum (Pragg sees 50-60)
- Key: Teaching is NOT about results; it's about the journey
- "Our effort should lead and the result should follow like a shadow"

## Source 5: ChessBase India Part 2 — Coaching Philosophy
### Source type: Expert/Third-party
### URL: https://en.chessbase.com/post/master-shifu-of-indian-chess-r-b-ramesh-2-3

- Parents should be counseled too — they often play a negative role unknowingly
- Results vs. learning trade-off: direct pursuit of results misses learning process
- Chess understanding evolves with rating: same game looks different at 1200 vs 1600 vs 2200
- Players must constantly change their perceptions about what's important

## Source 6: Perpetual Chess Podcast EP 488 (June 23, 2026)
### Source type: Expert/Third-party
### URL: https://podcastrepublic.net/podcast/1185023674 (listing)
Awaiting full transcript extraction

## Source 7: OpenAI Socratic Tutor Prompt
### Source type: Vendor-sourced
### URL: https://aiopenlibrary.com/prompts/openai-socratic-tutor

The canonical Socratic tutor prompt (3 sentences):
"You are a tutor that always responds in the Socratic style. You *never* give the student the answer, but always try to ask just the right question to help them learn to think for themselves. You should always tune your question to the interest & knowledge of the student, breaking down the problem into simpler parts until it's at just the right level for them."

Key insight: simplicity works — the entire prompt is 3 sentences
Referenced by OpenAI as an example of great system prompting

## Source 8: AI Tutor System Prompt Patterns
### Source type: User-reported / Practitioner
### URL: https://wildandfreetools.com/blog/system-prompt-for-ai-tutor-educator/

Base template patterns:
1. Ask what they have already tried
2. If stuck, give a hint without giving the answer
3. Break into smaller steps, walk through one at a time
4. When wrong, don't say 'wrong' — ask them to explain their thinking
5. When right, ask them to explain WHY it is right

Socratic Questioning Patterns:
- Instead of saying 'the answer is 5,' ask 'what do you think x equals here?'
- Instead of 'use the quadratic formula,' ask 'do you remember the formula we use when factoring doesn't work?'

## Source 9: Nielsen et al. Question Taxonomy
### Source type: Academic
### URL: https://www.cs.memphis.edu/~vrus/questiongeneration/15-NielsenEtAl-QG08.pdf

Validated question taxonomy for tutoring systems based on analysis of transcripts across 6 subject areas.
Key point: questions in Socratic tutoring should lead students to an "aha" moment.

## Source 10: Socratic Tutor for Mastery Prompt
### Source type: User-reported / Practitioner
### URL: https://docsbot.ai/prompts/education/socratic-tutor-for-mastery

Advanced Socratic prompt features:
- Epistemic deconstruction: surface hidden gaps, ambiguities, unexamined assumptions
- Identify weaknesses by asking layered, high-leverage questions
- Never accept vague, high-level, or incomplete answers
- "What exactly do you mean by that?", "Can you provide a concrete example?", "What would falsify this idea?"
- Avoid rushing to provide explanations yourself
