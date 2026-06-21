# Phase 0: Narrative Architecture & Content Plan

Brand: BEEE Spectacular Chess Championship + TEAMUP
Design System: Warm cream (#faf9f5), coral (#F27830), dark navy (#181715)
Type: Copernicus serif (headlines), Inter/StyreneB (body)
Framework: Svelte 5 (runes) + Anime.js v4

---

## 1. Narrative Arc

**Core positioning:** "Enroll your child in an elite youth development journey that culminates in a Spectacular Chess Championship — not 'Register for a chess tournament.'"

**Emotional arc across the scroll:**
1. **Awe/Curiosity** → 2. **Belief/Possibility** → 3. **Trust/Evidence** → 4. **Intrigue** → 5. **Decision/Commitment**

**The 5 chapters (scroll weight):**

| Chapter | Scroll % | Sections | Emotional Goal |
|---------|----------|----------|----------------|
| I. INVITATION | 10% | Sticky Header, Hero | Awe — "This is different, this matters" |
| II. TRANSFORMATION | 35% | Trust Bar, Why BEEE, TEAMUP | Belief — "This program builds futures" |
| III. JOURNEY | 30% | Passport, Timeline, Benefits | Trust — "Here's exactly how it works" |
| IV. MYSTERY | 15% | Mystery, Parent Section, Awards | Intrigue — "There's more to discover" |
| V. COMMITMENT | 10% | FAQ, Final CTA, Footer | Decision — "Register now" |

---

## 2. Section-by-Section Content

### S1: Sticky Header
- **Logo:** BEEE wordmark (coral spike-mark + "BEEE" in ink)
- **Nav links:** About · TEAMUP · Journey · FAQ
- **CTA:** "Register Now" — `button-primary` (coral)
- **Behavior:** Transparent on hero (logo + CTA only), gains cream backdrop + full nav on scroll past hero

### S2: Hero — "The Chess Theatre"
- **Headline (h1, display-xl):** "Every Move Builds a Future"
- **Subhead (title-lg):** "The BEEE Spectacular Chess Championship — where the T.E.A.M.U.P. journey meets the board."
- **CTA primary:** "Start the Journey" → scrolls to next section
- **CTA secondary:** "Watch the Story" → opens explainer video
- **Visual:** Animated chess pieces (SVG) floating on cream canvas, arranging into formation as scroll progresses; piece movement trails in coral + amber
- **Baseline (no JS):** Static hero image with assembled chess formation, headline visible

### S3: Trust Bar — "Numbers That Speak"
- **Container:** Full-width cream band, auto-scrolling horizontally
- **Stats:** "500+ Young Champions" · "50 Schools" · "6 Pillar Programme" · "2026 Edition"
- **Visual:** Each stat animates on entry with counter tween from 0 to target
- **Mobile:** Stacked 2x2 grid

### S4: Why BEEE Exists — "The Gap We Close"
- **Headline (display-lg):** "Chess Alone Isn't Enough"
- **Body (body-md):** "A child who plays chess learns strategy. A child in the T.E.A.M.U.P. programme learns strategy, technology, enterprise, art, mentorship, upskilling, and personal development — then proves it at the BEEE Spectacular Chess Championship."
- **Visual:** Split screen — left: text, right: illustration of a child's progression path (simple line art in coral + ink on cream)
- **Sticky:** Right illustration stays pinned while left text scrolls

### S5: TEAMUP — "The Six Pillars"
- **Headline (display-lg):** "T.E.A.M.U.P."
- **Subhead (title-md):** "Six pillars. One journey. Unlimited potential."
- **Cards (6):**
  1. Technology (King) — "The Digital Foundation"
  2. Enterprise (Queen) — "Building Futures"
  3. Art (Bishop) — "Creative Thinking"
  4. Mentorship (Knight) — "Guided Growth"
  5. Upskill (Rook) — "Practical Mastery"
  6. Personal Development (Pawn) — "Character First"
- **Layout:** Bento grid at desktop; stacked cards at mobile
- **Visual:** Each card uses chess piece SVG icon in its accent color; hover expands card slightly (Anime.js FLIP)

### S6: Development Passport — "Your Child's Growth, Visible"
- **Headline (display-lg):** "The Development Passport"
- **Body:** "Every skill earned. Every milestone reached. Every stamp collected."
- **Visual:** Interactive SVG passport widget showing 6 pillar badge slots, progress bars for each, animated stamp effect on enter
- **Sticky:** Passport widget pinned right; scrollable steps on left
- **Mobile:** Full-width passport, steps above/below

### S7: Championship Journey Timeline — "The Road to the Board"
- **Headline (display-lg):** "From First Move to Championship"
- **Subhead:** "6 stages. 12 weeks. One transformation."
- **Stages (horizontal scroll illusion):**
  1. Discovery — "Find Your Passion"
  2. Foundation — "Learn the Basics"
  3. Practice — "Sharpen Your Skills"
  4. Compete — "School Qualifiers"
  5. Semi-Finals — "Regional Face-Off"
  6. Finals — "The BEEE Spectacular"
- **Visual:** Horizontal timeline with milestone markers; current stage glows in coral; completed stages in teal

### S8: Benefits Grid — "What Your Child Gains"
- **Headline (display-lg):** "Skills That Last a Lifetime"
- **Layout:** 3x2 grid of `feature-card` components
- **Cards:** Strategic Thinking · Digital Literacy · Confidence · Teamwork · Creativity · Discipline
- **Each card:** Icon (top), title-md headline, body-sm description
- **Animation:** Grid staggered entrance from bottom; cards slightly elevate on hover

### S9: Mystery Section — "What's Your Next Move?"
- **Headline (display-lg, partially obscured):** "What's Your Next Move?"
- **Body:** "Something extraordinary is coming. Something that blends chess, technology, and surprise."
- **Visual:** Blurred/partially-obscured chess position with glowing coral pieces; on scroll, blur gradually resolves
- **CTA (teal #5db8a6):** "Unlock the Secret" → reveals full content + triggers confetti-like animation
- **Mobile:** Simplified — blurred image + CTA only

### S10: Parent Section — "Why Parents Trust BEEE"
- **Headline (display-lg):** "Built for Parents. Designed for Children."
- **Subhead:** "Every decision we make starts with two questions: Is this good for the child? Is this clear for the parent?"
- **Trust signals:** Testimonial quote from parent · Safety protocol badge · Certified instructors · Transparent pricing callout
- **Visual:** `product-mockup-card-dark` with parent testimonial + child photo

### S11: Awards & Recognition — "Recognised Excellence"
- **Headline (display-lg):** "Recognised. Accredited. Trusted."
- **Logos/Citations:** Partner school logos · Educational board accreditation · Media mentions
- **Visual:** Scrolling logo marquee (Anime.js infinite loop, paused on hover)
- **Mobile:** Static grid of logos

### S12: FAQ — "Questions You Might Have"
- **Headline (display-lg, centered):** "Still Have Questions?"
- **Layout:** Centered accordion (max-width 720px)
- **Items (6):**
  1. "What age group is this for?" → Ages 7-17
  2. "Does my child need chess experience?" → No, all levels welcome
  3. "How much does it cost?" → Tiered pricing with scholarship options
  4. "What's the time commitment?" → 2hrs/week + championship day
  5. "How do I register my school?" → School coordinator contact + online form
  6. "What if my child can't attend all sessions?" → Flexible attendance policy
- **Visual:** Details/summary elements with smooth open/close via Anime.js `createLayout()`

### S13: Final CTA — "Make the First Move"
- **Background:** `cta-band-coral` (full-width coral) or `cta-band-dark` (dark navy)
- **Headline (display-sm):** "The Best Move Is the First One."
- **Body:** "Register your child for the BEEE Spectacular Chess Championship 2026."
- **CTA button:** Cream (`button-secondary` inverted on coral) or coral (`button-primary` on dark)
- **Visual optional:** Animated chess piece sliding into final position

### S14: Footer
- **Background:** `surface-dark` (#181715)
- **Columns:** Program (TEAMUP, Passport, Curriculum) · Event (Schedule, Venues, Rules) · Company (About, Blog, Contact) · Legal (Privacy, Terms)
- **Brand:** BEEE wordmark (white), spike-mark
- **Social:** Instagram · Twitter · YouTube
- **Copyright:** Small `on-dark-soft` text

---

## 3. Mobile-First Wireframes (per section)

### Breakpoints
- **Mobile (< 768px):** Single column, stacked layout, native scroll, no sticky elements
- **Tablet (768-1024px):** 2-column where possible, sticky in portrait only
- **Desktop (> 1024px):** Full scrollytelling with sticky + scroll-synced animations

### Key mobile adaptations:
- **Hero:** Single column — headline, subhead, CTAs stacked; chess pieces as static decorative SVG (no Three.js)
- **TEAMUP:** Stacked cards (not bento); pillar name + short description only
- **Passport:** Full-width passport widget (no side-by-side); steps above
- **Timeline:** Vertical timeline (not horizontal illusion); each stage a row
- **FAQ:** Same accordion, full-width
- **CTA:** Full-width button, easier to tap

---

## 4. Animation Intent (per section)

| Section | What Animates | Anime.js API | Trigger |
|---------|---------------|-------------|---------|
| S1 Header | Logo opacity, nav items stagger | `animate()` + `stagger()` | scroll position past hero |
| S2 Hero | Chess piece float → formation, headline split-text, trail lines | `createTimeline({ autoplay: onScroll })`, `splitText()`, `createDrawable()` | scroll 0-10% |
| S3 Trust Bar | Counter tweens (0→N), horizontal marquee | `animate()` with modifier, `createTimeline()` | section enters viewport |
| S4 Why BEEE | Text fade/slide, illustration sticky scale | `animate()` on scroll, CSS `position: sticky` | scroll within section |
| S5 TEAMUP | Card stagger entrance, hover FLIP expand | `createLayout()`, `stagger()`, `animate()` | section enters viewport |
| S6 Passport | Badge stamp animation, progress bar fill, stagger rows | `createDrawable()`, `stagger()`, `animate()` | scroll within sticky section |
| S7 Timeline | Horizontal strip scroll, milestone glow, counter | `onScroll({ axis: 'x' })`, `animate()` | scroll within pinned container |
| S8 Benefits | Grid stagger entrance, card hover lift | `stagger()`, `animate()` | section enters viewport |
| S9 Mystery | Blur dissolve, reveal animation, particle burst | `animate()` blur → 0, `stagger()` | scroll OR click |
| S10 Parent | Fade-in elements staggered | `stagger()`, `animate()` | section enters |
| S11 Awards | Logo marquee infinite scroll | `animate({ loop: true })` | on mount |
| S12 FAQ | Details/summary smooth open/close | `createLayout()`, `animate()` | on toggle |
| S13 CTA | Piece slide-in, button pulse | `animate()`, `createTimer()` | section enters |
| S14 Footer | Static (no animation) | — | — |
