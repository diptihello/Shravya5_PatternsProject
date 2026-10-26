# Pattern Master — Logical Reasoning Tutor

An interactive web app for practising logical reasoning patterns, built for students.

## Features

- 🔢 **Number Series** — arithmetic, geometric, Fibonacci, primes, factorials, and more
- 🔷 **Shape Sequences** — visual pattern recognition with animated SVG shapes
- 🔤 **Alphabet Sequences** — skip patterns, reverse, interlaced, and positional series
- 🎚️ **3 Difficulty Levels** — Easy, Medium, Hard (filterable globally)
- 💡 **Display Answer button** — animated reveal with full explanation of the pattern
- 💾 **Progress persistence** — answered questions saved in localStorage
- 📱 **Fully responsive** — works on mobile, tablet, and desktop

## Running Locally

Just open `index.html` in your browser — no build step required.

Or serve it with:

```bash
npx serve .
```

## Deploying to Railway

1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub repo
3. Select this repository
4. Railway auto-detects `railway.json` and deploys
5. Your site will be live at the provided Railway URL

## Project Structure

```
├── index.html          # Main application shell
├── style.css           # Global design system
├── app.js              # Core logic (navigation, rendering, state)
├── data/
│   ├── numbers.js      # 15 number series questions
│   ├── shapes.js       # 15 shape sequence questions
│   └── alphabets.js    # 15 alphabet sequence questions
├── assets/
│   └── shapes.js       # SVG shape renderer
├── railway.json        # Railway deployment config
└── docs/
    ├── problem.md
    └── implementation_plan.md
```
