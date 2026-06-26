## Research Topic: AI Text & Speech Humanization

## Integrated Findings

### Core Mechanism
- AI text sounds robotic due to neural text degeneration (Holtzman et al. 2020 [1]), exposure bias (Chiang & Chen 2021 [2]), and the likelihood trap
- Two core signals: perplexity (word predictability) and burstiness (sentence length variance) [12][13]
- AI detectors measure statistical properties, not content quality — this is why synonym swapping fails

### Prompt-Level Techniques
- Voice profiling and style priming is the highest-leverage technique [11][19]
- Providing writing samples outperforms abstract tone descriptions
- Vague prompts produce robotic output because AI defaults to generic patterns [19]

### Post-Generation Editing
- Structural rewriting > surface-level changes [8][9]
- Sentence length variation, contraction usage, specificity injection most effective
- 33 identifiable patterns of AI writing [10]

### Automated Tools
- Significant gap between vendor claims and independent test results [8][9][12]
- Top tools: 70-91% bypass rates; bottom tools: <40%
- Meaning drift is a common failure mode

### TTS Humanization
- SSML breaks, prosody tags, phoneme tags provide fine-grained control [6][16][21]
- Post-processing (compression, EQ) closes realism gap [7]
- Script structure and punctuation cues matter as much as voice selection [7]

### Detection Bias
- 61% false positive rate on non-native English writing [3][4]
- 25+ universities restricted detectors after auditing [14]

### Key Insight
- The "last 10%" residual detectability remains unsolved — the gap between technically proficient and genuinely human text
