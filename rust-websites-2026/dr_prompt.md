# DEEP RESEARCH COMMISSION

## Research Question
What is the most efficient way to build websites with Rust in 2026 — considering developer productivity (time-to-ship), runtime performance, ecosystem maturity, and team scalability?

## Purpose & Context
A full-stack developer with Rust experience wants to choose the optimal approach for building production websites with Rust. The term "efficient" is deliberately multi-dimensional: the developer needs to evaluate the tradeoffs between development speed, performance, deployment complexity, and long-term maintainability. The Rust web ecosystem has matured significantly but still has fragmentation — this research should cut through the hype and provide a practical, evidence-based framework for choosing the right stack.

### Audience
- Primary: Experienced Rust developers (2+ years) building production web applications
- Secondary: Full-stack developers considering Rust for their next project
- Tone: Technical, practical, evidence-based. No fanboyism.
- Complexity: Advanced — assumes familiarity with Rust, async, WASM concepts

### Decision Context
- Should I use Rust for the backend only, or full-stack?
- If full-stack Rust: Leptos vs Yew vs Dioxus vs Sycamore?
- If backend-only: Axum vs Actix-web vs Rocket vs Loco vs Poem vs Pavex?
- How do SSR, WASM, and server functions work in practice?
- What about deployment: single binary vs Docker vs WASM+CDN?
- What are the real-world tradeoffs in DX, build times, hot reload?
- How does each option compare for: simple blog, SaaS dashboard, high-traffic API, real-time app?

## Research Scope

### In Scope
- Rust backend web frameworks (Axum, Actix-web, Rocket, Loco, Poem, Pavex, Warp, Tide)
- Rust frontend/WASM frameworks (Leptos, Yew, Dioxus, Sycamore, Perseus, next.rs, Vega)
- Full-stack Rust approaches (Leptos+Axum, server functions, WASM+Spa, SSR+hydration)
- Deployment strategies for Rust websites (Docker, single binary, WASM+CDN, serverless)
- Developer experience metrics: compile times, hot reload quality, debugging ease, testing ergonomics
- Production case studies and benchmarks (2024-2026)
- Ecosystem maturity: middleware, auth, ORM, database drivers, templating, form handling, file upload, sessions
- Learning curve and team onboarding considerations
- Total Cost of Ownership (TCO) for Rust web projects

### Out of Scope
- Non-Rust frameworks (comparisons only for benchmarking context)
- Mobile app development with Rust
- CLI tools or desktop apps (unless they share web-serving infrastructure)
- Game development with Rust/WASM
- Rust-for-JS-transpilers (like Napi-rs for Node.js) — focus is pure Rust
- Low-level networking libraries (hyper, mio, tokio internals) — focus is web frameworks

### Timeframe
2024-2026 with emphasis on 2025-2026

### Geographic Focus
Global — English-speaking Rust ecosystem. No regional constraints.

## Required Dimensions of Investigation

1. **Framework Comparison Matrix** — For each major framework: GitHub stars, download count, latest release, team size, maturity tier (stable/beta/alpha), primary use case, unique advantages, dealbreakers
2. **Rendering Architecture** — SSR vs CSR vs SSG vs ISR. Hydration models (fine-grained vs virtual DOM). How each framework handles data fetching, routing, SEO.
3. **Developer Experience** — Build times (cold/hot), hot reload quality, error messages, IDE support, testing tooling, scaffolding tools, cookbook/cookbook quality
4. **Production Readiness** — Authentication middleware, database access patterns, form handling, CSRF/XSS protection, rate limiting, sessions, file uploads, email sending, background jobs, cron
5. **Performance Benchmarks** — Throughput (req/s), latency (p50/p95/p99), memory usage, binary size, cold start time, WASM bundle size. Include real-world numbers, not just microbenchmarks.
6. **Deployment Options** — Single binary deployment, Docker, Cloudflare Workers, AWS Lambda, Fly.io, Railway, Shuttle, Vercel (WASM), Deno. Compare complexity and cost.
7. **Community & Ecosystem** — Package availability for common web tasks, middleware ecosystem, ORM/query builder maturity (Diesel, SQLx, SeaORM, Prisma), template engines, CSS handling, asset pipeline
8. **Learning Curve** — Time to first working prototype, time to production-ready, resources available (books, courses, tutorials), documentation quality

## Source Requirements

### Source Types Required
- Official framework documentation and comparisons
- GitHub repositories (stars, activity, issues, PRs)
- Production case studies and postmortems
- Benchmarks and performance comparisons (TechEmpower, AreWeWebYet)
- Conference talks and articles (RustConf, RustLab, EuroRust 2024-2026)
- Reddit (r/rust, r/webdev) and Hacker News discussions
- Personal experience reports from production users
- Survey data (Rust Survey, State of Rust in Web)
- Package download data (crates.io)

### Source Diversity
- Both framework creators' claims AND independent benchmark/review data
- Both successful AND failed production deployments
- Small projects AND large-scale applications
- Both full-stack Rust AND backend-only approaches
- Multiple framework ecosystems (not just one camp's viewpoint)

### Required Citations
- EVERY factual claim (downloads, stars, benchmark numbers) followed by [N] citation
- Label each source: official doc, benchmark, community report, case study
- Note: When data comes from framework creators vs independent evaluators
- Admit uncertainty: "No recent benchmarks found for X in 2026"

## Output Requirements

### Report Structure
1. **Executive Summary** — The most efficient way to build websites with Rust in 2026 (multi-dimensional recommendation)
2. **Decision Framework** — Decision tree mapping project type → recommended stack
3. **Backend Framework Deep Dives** (5-10 frameworks) — Each with: overview, architecture, DX assessment, performance data, production readiness, ecosystem, pros/cons
4. **Frontend/WASM Deep Dives** (5-8 frameworks) — Each with: overview, rendering model, DX assessment, bundle size, performance, ecosystem, pros/cons
5. **Full-Stack Approaches** — Leptos+Axum, Dioxus custom, Yew+Actix, Sycamore+Perseus, Loco monolithic — comparison of integration quality, SSR capabilities, server functions, deployment
6. **Deployment & Operations** — Docker, single binary, WASM+CDN, serverless (Workers, Lambda, Shuttle), CI/CD patterns, scaling strategies
7. **Performance Benchmarks Table** — Backend (Axum, Actix, Rocket, etc.) and frontend (Leptos, Yew, Dioxus, etc.) — throughput, latency, memory, bundle size, build times
8. **Production Case Studies** — Real websites built with Rust in 2024-2026, what stack they used, what challenges they faced
9. **Getting Started Guide** — For each major project type (API, full-stack app, static site, real-time app), recommended scaffolding, toolchain, and first steps
10. **Future Outlook** — Where the ecosystem is heading in 2026-2027, emerging frameworks worth watching, when NOT to use Rust for web
11. **Bibliography** — All sources cited

### Quality Mandates
- EVERY claim followed by [N] citation
- Flag each framework's maturity tier clearly
- Note when recommendations are opinion vs evidence-based
- Include negative findings (crashes, bugs, performance regressions) honestly
- Compare against non-Rust alternatives only for context (not as primary analysis)
- Build times must be measured, not estimated
- Bundle sizes must be real-world (default app, not minimal Hello World)

## Seed Keywords

Core: Rust web framework, Rust WASM frontend, Rust full-stack, Axum vs Actix-web 2026, Leptos vs Yew vs Dioxus, Rust SSR

Framework specific: Axum tutorial, Actix-web production, Rocket Rust, Loco Rust framework, Pavex Rust, Leptos server functions, Yew WASM, Dioxus desktop, Sycamore Rust

Assessment: Rust web framework benchmark 2026, Rust compile times web, Rust production website case study, Rust WASM bundle size, AreWeWebYet 2026

Deployment: Rust Docker deploy, Rust Cloudflare Workers, Rust serverless, Shuttle Rust, single binary Rust website

Anti-patterns: Rust web framework burnout, Rust WASM overkill, Rust compile time frustration, Rust ecosystem fragmentation web

## Mode
Deep Research (8-phase pipeline)
