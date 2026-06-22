## Research Topic: Most efficient way to build websites with Rust in 2026

## Integrated Findings

*(This draft accumulates insights from each source processed sequentially)*

**Phase 0 Recon Highlights:**
- Axum is the consensus default backend in 2026 (~25.9K stars, ~76.7M downloads). Built by Tokio team. Tower ecosystem.
- Actix-web is ~10-15% faster than Axum in raw throughput. 8 years battle-tested.
- Leptos is the most active frontend framework (~20.7K stars). Fine-grained reactivity, built-in SSR, server functions.
- Yew is the oldest/largest (30K+ stars). Virtual DOM, React-like, most tutorials/examples.
- Dioxus is cross-platform (web + desktop + mobile). YC-backed.
- Consensus: Axum is the "boring choice" default. Framework wars are over.
- For simple websites, Rust is overkill. For high-performance API: Axum+SQLx+Tokio.
- Loco.rs for Rails-style full-stack.
- Key insight: Most frameworks are converging on fine-grained reactivity and SSR.
