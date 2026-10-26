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

## Deploying to Vercel

1. Push this repo to GitHub
2. Go to [vercel.com](https://vercel.com) → **Add New...** → **Project**
3. Select `diptihello/Shravya5_PatternsProject` from your GitHub repos
4. Set Project Name to `shravya5-patterns-project` (all lowercase, dashes allowed)
5. Framework Preset: **Other**
6. Root Directory: `./`
7. Click **Deploy** — your site will be live on Vercel with automatic SSL and continuous deployment!

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
├── vercel.json         # Vercel deployment config
├── streamlit/          # Optional Python/Streamlit UI
│   ├── streamlit_app.py
│   ├── shapes.py
│   ├── data.py
│   └── requirements.txt
└── docs/
    ├── problem.md
    └── implementation_plan.md
```
