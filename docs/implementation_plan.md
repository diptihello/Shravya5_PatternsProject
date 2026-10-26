# Implementation Plan — Logical Reasoning Tutor

> Based on [`problem.md`](file:///d:/Sharvaya%20Site/docs/problem.md)

---

## Tech Stack

| Layer | Choice | Reason |
|---|---|---|
| Structure | HTML5 | Semantic, lightweight |
| Styling | Vanilla CSS | Full control, vibrant design |
| Logic | Vanilla JavaScript | No dependencies needed |
| Deployment | Railway (static site) | As specified |

---

## Project Structure

```
d:\Sharvaya Site\
├── index.html            # Landing page / home
├── style.css             # Global design system & theme
├── app.js                # Core logic (routing, state, answer reveal)
├── data/
│   ├── numbers.js        # Number series questions (Easy/Medium/Hard)
│   ├── shapes.js         # Shape sequence questions
│   └── alphabets.js      # Alphabet sequence questions
├── assets/
│   └── shapes/           # SVG shape assets for shape sequences
├── docs/
│   ├── problem.md
│   └── implementation_plan.md
├── railway.json          # Railway deployment config
└── README.md
```

---

## Data Design

Each question follows a standard schema:

```js
{
  id: "num-easy-01",
  difficulty: "easy",          // easy | medium | hard
  question: "2, 4, 6, 8, ?",
  options: [9, 10, 11, 12],    // optional multiple choice
  answer: 10,
  explanation: "Each number increases by 2 (even numbers). The next in the series is 10."
}
```

### Question Bank Plan

| Category | Easy | Medium | Hard | Total |
|---|---|---|---|---|
| Number Series | 5 | 5 | 5 | 15 |
| Shape Sequences | 5 | 5 | 5 | 15 |
| Alphabet Sequences | 5 | 5 | 5 | 15 |
| **Total** | **15** | **15** | **15** | **45** |

---

## UI/UX Design

### Colour Palette
- Background: Deep navy `#0f0c29` → `#302b63` gradient
- Accent: Vibrant purple `#a855f7`, coral `#f97316`, teal `#06b6d4`
- Cards: Glassmorphism (semi-transparent white with blur)
- Text: White / light grey

### Typography
- Font: **Outfit** (Google Fonts) — modern, rounded, student-friendly

### Layout
- Sticky top navbar with logo + difficulty filter tabs
- Hero section with animated title
- Three section cards (Numbers / Shapes / Alphabets) on the homepage
- Individual section pages display question cards in a responsive grid
- Each card has:
  - Question display
  - (Optional) multiple-choice options
  - **"Display Answer"** button → animated reveal with explanation
  - Difficulty badge (🟢 Easy / 🟡 Medium / 🔴 Hard)

### Animations
- Cards fade-in on scroll
- Answer reveal with slide-down + highlight animation
- Difficulty filter with smooth tab transition
- Hover glow on cards

---

## Implementation Phases

### Phase 1 — Foundation & Design System
- [ ] Set up project folder structure
- [ ] Create `index.html` with semantic layout
- [ ] Build `style.css`: colour tokens, typography, card styles, button styles, animations
- [ ] Create sticky navbar with logo and navigation links
- [ ] Create hero section with animated heading
- [ ] Build three clickable category cards on homepage

### Phase 2 — Number Series Section
- [ ] Create `data/numbers.js` with 15 questions (5 per difficulty)
- [ ] Build number question card component in JS
- [ ] Implement **"Display Answer"** button with animated explanation reveal
- [ ] Wire up difficulty filter to show/hide appropriate cards

### Phase 3 — Shape Sequences Section
- [ ] Generate SVG assets for shape sequences (circles, triangles, squares, etc.)
- [ ] Create `data/shapes.js` with 15 questions (5 per difficulty)
- [ ] Build shape card component displaying SVG shapes inline
- [ ] Implement answer reveal showing the correct next shape

### Phase 4 — Alphabet Sequences Section
- [ ] Create `data/alphabets.js` with 15 questions (5 per difficulty)
  - Examples: A, C, E, G, ? | Z, X, V, T, ? | A, B, D, G, ?
- [ ] Build alphabet card component
- [ ] Implement answer reveal with pattern explanation

### Phase 5 — Difficulty Level System
- [ ] Add global difficulty filter (Easy / Medium / Hard / All) in navbar
- [ ] Persist selected difficulty in `localStorage`
- [ ] Filter question cards dynamically when difficulty changes
- [ ] Add difficulty badge to every question card

### Phase 6 — Polish & Responsiveness
- [ ] Ensure fully responsive layout (mobile, tablet, desktop)
- [ ] Add micro-animations (card hover glow, answer reveal slide)
- [ ] Add a progress tracker (X of Y questions answered per section)
- [ ] Add a "Reset All" button to clear revealed answers
- [ ] Final cross-browser testing

### Phase 7 — Deployment to Railway
- [ ] Create `railway.json` with static site config
- [ ] Push project to a GitHub repository
- [ ] Connect GitHub repo to Railway
- [ ] Set root directory and deploy
- [ ] Verify live URL

---

## Railway Deployment Config

```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "npx serve .",
    "restartPolicyType": "ON_FAILURE"
  }
}
```

> **Note:** Since this is a pure static site (HTML/CSS/JS), Railway will serve it via `npx serve .` with no build step needed.

---

## Milestones

| Phase | Deliverable | Est. Effort |
|---|---|---|
| 1 | Homepage with design system | ~1 hr |
| 2 | Number Series fully working | ~1 hr |
| 3 | Shape Sequences fully working | ~1.5 hr |
| 4 | Alphabet Sequences fully working | ~1 hr |
| 5 | Difficulty filter system | ~30 min |
| 6 | Polish + responsiveness | ~1 hr |
| 7 | Railway deployment live | ~30 min |
| **Total** | | **~6.5 hrs** |
