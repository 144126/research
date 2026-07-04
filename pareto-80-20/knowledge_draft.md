## Research Topic: The 80/20 (Pareto) Principle — Causal Mechanisms, Empirical Scope, and Limits

## Integrated Findings

### Mathematics (Finding 1)
- Pareto distribution PDF: f(x) = αx_min^α / x^(α+1) for x ≥ x_min [1]
- 80/20 corresponds exactly to Pareto index α = log(5)/log(4) ≈ 1.16 [2]
- Power law: p(x) ∝ x^(-α) — no characteristic scale [3]
- Clauset, Shalizi, Newman (2009): rigorous framework for fitting/testing power laws, applied to 24 datasets [4]
- Newman (2005): power laws appear in city sizes, earthquakes, moon craters, solar flares, wars, word frequencies, citations, web hits, book sales, species, incomes [5]

### Causal Mechanism 1: Preferential Attachment (Finding 2)
- Yule (1925): first mathematical model — species/genus distribution via birth process [6]
- Simon (1955): generalized Yule process to word frequencies, wealth [7]
- Price (1976): "cumulative advantage" — citation networks, first network model [8]
- Barabási-Albert (1999): preferential attachment for web links, degree distribution ~k^(-3) [9]
- Mitzenmacher (2004): review of generative models — preferential attachment yields power law when attachment kernel is linear (γ=1) [10]
- Matthew effect (Merton): "rich get richer" — well-documented across science collaboration, citations, language evolution [11]

### Causal Mechanism 2: Multiplicative Processes (Finding 3)
- Gibrat's law of proportionate effect: log-normal from multiplicative random growth [12]
- Multiplicative noise + lower bound → power law (Sornette, 1998) [13]
- Levy & Solomon (1996): "Power Laws are Logarithmic Boltzmann Laws" — multiplicative dynamics = Boltzmann in log space [14]
- Log-normal vs. power law: empirically difficult to distinguish, many claims of power law may be log-normal [4][15]

### Causal Mechanism 3: Self-Organized Criticality (Finding 4)
- Bak, Tang, Wiesenfeld (1987/1988): sandpile model — systems naturally evolve to critical state with power-law avalanches [16]
- Dhar (1990): Abelian sandpile model — exact characterization of critical state [17]
- Earthquakes (Gutenberg-Richter): magnitude-frequency power law [18]
- SOC explains power laws without fine-tuning parameters [16][17]

### Causal Mechanism 4: Bottlenecks & Diminishing Returns (Finding 5)
- Juran's original insight: "vital few and trivial many" from quality control — 80% defects from 20% causes [19]
- Juran later admitted Pareto hadn't claimed universality; Lorenz curves properly attributed [20]
- "The Non-Pareto Principle: Mea Culpa" (Juran, 1975): acknowledged misattribution [21]

### Empirical Scope (Finding 6)
- Wealth distribution: α ≈ 1.5-2.5 depending on country/time [1][5]
- City sizes (Zipf's law): α ≈ 1 in upper tail; Gibrat's law explains [22][23]
- Earthquakes (Gutenberg-Richter): magnitude-frequency power law [18]
- Word frequencies (Zipf's law): rank ~1/frequency [5]
- Software bugs: 80/20 holds approximately but Weibull/Double Pareto may fit better [24][25]
- Sales concentration: actual ratio closer to 70/20 or 60/20 (Sharp et al., 2019) [26]
- COVID-19 superspreading: ~10-19% of cases cause 80% of transmission (k≈0.3-0.55) [27][28]

### Criticisms & Limitations (Finding 7)
- Pareto's original data: 27.7% had 72.3%, not 20/80 [29]
- Marketing: Ehrenberg-Bass study found 60/20, not 80/20 [26]
- Taleb's critique: power law domains are "Extremistan" — 80/20 thinking underestimates tail risks; needs 10^11 more data than Gaussian to stabilize mean [30]
- Clauset et al. (2009): many claimed power laws fail rigorous testing [4]
- Post-hoc classification: labeling top 20% as "vital few" is always true by definition — question is concentration steepness [31]
- "Trivial many" often essential: Mona Lisa needs all brushstrokes [32]
- Confirmation bias: we remember cases fitting 80/20, forget others [31]

### Practical Guidance (Finding 8)
- Trust: quality control, resource allocation with diminishing returns, high-dimensional optimization [19][31]
- Doubt: tail risk management, systems where remaining 80% is critical, domains with true randomness [30][32]
- Use retrospectively, not prescriptively — identify what worked after the fact [32]
- Formalization (2024): "generalized Pareto principle" — specific 0.2/0.8 is just one point on continuum, not special [31]
