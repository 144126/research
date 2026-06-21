# Phase 4: Accessibility & UX Polish

**Goal:** Make the homepage accessible (a11y) while adding the mystery-section confetti reward and final UX polish before launch.

---

## A. Accessibility (a11y) — WCAG 2.1 AA

### A1. Skip Link (`WCAG 2.4.1 — Bypass Blocks`)

- Add `<a href="#main-content" class="skip-link">Skip to main content</a>` as the **first focusable element** inside `<body>`, before the nav.
- Target: `<main id="main-content" tabindex="-1">`
- CSS: `position: absolute; top: -100%; left: 0; z-index: 10000;` On focus: `top: 0`.
- JS: `e.preventDefault()` + `target.scrollIntoView()` + `target.focus()`.
- Lenis: set `anchors: true` in config so `scrollIntoView` is smooth.

### A2. `prefers-reduced-motion` (WCAG 2.3.3 / 2.2.2)

- **CSS**: Wrap all scroll-driven animations and decorative transitions in `@media (prefers-reduced-motion: no-preference)`.
- **Lenis**: conditionally instantiate Lenis only when `!matchMedia('(prefers-reduced-motion: reduce)').matches`.
- **Anime.js timelines**: skip all entrance animations when reduced motion.
- **canvas-confetti**: has built-in `disableForReducedMotion` — enable it.
- **Principle**: reduce, don't remove — opacity fades can remain; parallax, scroll-drive, and large-scale transforms should be skipped.

### A3. Keyboard Navigation & Focus

- Ensure all interactive elements are reachable via Tab.
- Add `:focus-visible` outlines (maintain design system; use `outline: 2px solid var(--color-accent)`).
- Lenis: ensure native scrollbar + keyboard (PgUp/PgDn, arrow keys, Space) work properly.
- Test tab order: skip link → nav → main content → footer.

### A4. ARIA Landmarks

- `role="banner"` on header/nav
- `role="main"` on `<main>`
- `role="contentinfo"` on footer
- Section headings use proper `<h1>`–`<h2>` hierarchy.

---

## B. Mystery Section Confetti (canvas-confetti)

### B1. Install Dependency

```
pnpm add canvas-confetti
pnpm add -D @types/canvas-confetti
```

### B2. Confetti Trigger

- **When**: user scrolls past the mystery section (IntersectionObserver at 50% visibility).
- **How**: `confetti({ particleCount: 150, spread: 80, origin: { y: 0.6 }, disableForReducedMotion: true })`
- **Once**: fire only on first reveal; use a one-shot flag.
- **Follow-up**: small burst on CTA button hover in mystery section (optional, Phase 4+).

### B3. Edge Cases

- Disabled on `prefers-reduced-motion: reduce` (handled by lib option).
- Disabled on slow devices? canvas-confetti is lightweight (< 5KB), no perf concern.
- Test on mobile — reduce particle count to 80 if viewport < 640px.

---

## C. Lenis Tuning

### C1. Config Updates

```js
new Lenis({
  anchors: true,              // enable smooth anchor scrolling
  orientation: 'vertical',
  smoothWheel: true,
  wheelMultiplier: 0.8,
  gestureOrientation: 'vertical',
  touchMultiplier: 1.2,
  normalizeWheel: false,
})
```

### C2. `prefers-reduced-motion` Guard

```js
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
if (!prefersReducedMotion) {
  lenis = new Lenis({ ... })
}
```

---

## D. Awwwards-Level Polish (Remaining Items)

| Item | Status | Action |
|------|--------|--------|
| **Passport SVG badge animation** | ✅ Done | `createDrawable` + drawSVG |
| **TEAMUP entrance** | ✅ Done | Anime timeline, scale + stagger |
| **Timeline line + glow** | ✅ Done | DrawSVG + moving gradient |
| **Pillar card hover micro** | ✅ Done | Tilt + border glow |
| **Milestone counter scroll** | ✅ Done | Anime counter with easeInOut |
| **Section transition consistency** | ❌ Todo | Unify entrance easing (use `easeInOutCubic` across all sections) |
| **Accent color palette audit** | ❌ Todo | Ensure `var(--color-accent)` is used consistently for CTAs, links, focus outlines |
| **CTA micro-animations** | ❌ Todo | Add subtle scale on hover (`transform: scale(1.02)`) + gentle pulse on load for primary CTAs |
| **Parallax depth layers** | ⏳ Optional | Add subtle parallax to hero background / passport globe — only if enhances storytelling |

---

## E. Implementation Order

1. **Skip link** (A1) — quick, high-impact for a11y
2. **ARIA landmarks + heading hierarchy** (A4) — structural
3. **`prefers-reduced-motion` guard + CSS** (A2) — prevents motion sickness
4. **Focus-visible styles** (A3) — keyboard UX
5. **Lenis config update + anchors** (C) — ties scroll + skip link together
6. **canvas-confetti install + mystery trigger** (B) — the fun payoff
7. **Section transition consistency** (D) — polish
8. **Accent color audit** (D) — visual consistency
9. **CTA micro-animations** (D) — final sparkle
10. **Test a11y** — tab through, VoiceOver, reduced-motion emulation

---

## F. Files to Modify

| File | Changes |
|------|---------|
| `src/routes/+layout.svelte` | Skip link, ARIA landmarks, Lenis config |
| `src/routes/+page.svelte` | Mystery section confetti trigger, reduced-motion guards |
| `src/app.css` | Skip link styles, focus-visible, reduced-motion media queries |
| `package.json` | Add `canvas-confetti`, `@types/canvas-confetti` |

---

## G. Testing

1. **Keyboard**: Tab from page load — skip link should be first. Hit Enter — focus moves to `<main>`.
2. **Reduced motion**: Enable in OS settings → Lenis should not init, confetti should not fire, anime entrances should be static.
3. **Confetti**: Scroll to mystery section — confetti should fire once, not repeat on scroll-back.
4. **Lighthouse a11y audit**: Should pass all automated checks after skip link + landmarks added.
5. **VoiceOver / NVDA quick test**: Ensure heading hierarchy reads correctly, skip link is announced.

---

## H. Reference / Prior Art

- **Skip link technique** — [WCAG G1](https://www.w3.org/WAI/WCAG21/Techniques/general/G1)
- **canvas-confetti** — [catdad/canvas-confetti](https://github.com/catdad/canvas-confetti) (12.6k stars, 4.6M weekly npm downloads)
- **Lenis anchors + a11y** — [Lenis docs](https://github.com/studio-freight/lenis) (native scrollbar, keyboard, `data-lenis-prevent`, `anchors` option)
- **Motion sensitivity** — [MDN prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)
