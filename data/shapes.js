const shapeQuestions = [
  // ── EASY ──────────────────────────────────────────────────────────────────
  {
    id: "shp-easy-01",
    difficulty: "easy",
    question: "What comes next in the sequence?",
    sequence: ["circle", "circle", "circle", "circle", "?"],
    options: ["circle", "square", "triangle", "star"],
    answer: "circle",
    explanation: "The pattern repeats a single shape — <strong>circle</strong> — throughout the sequence."
  },
  {
    id: "shp-easy-02",
    difficulty: "easy",
    question: "What comes next in the sequence?",
    sequence: ["circle", "square", "circle", "square", "?"],
    options: ["triangle", "circle", "star", "pentagon"],
    answer: "circle",
    explanation: "The pattern alternates: circle → square → circle → square… Next is <strong>circle</strong>."
  },
  {
    id: "shp-easy-03",
    difficulty: "easy",
    question: "What comes next in the sequence?",
    sequence: ["triangle", "triangle", "circle", "triangle", "triangle", "circle", "?"],
    options: ["circle", "square", "triangle", "star"],
    answer: "triangle",
    explanation: "The pattern repeats every 3: triangle, triangle, circle. After 'circle' comes <strong>triangle</strong>."
  },
  {
    id: "shp-easy-04",
    difficulty: "easy",
    question: "What comes next in the sequence?",
    sequence: ["square", "square", "square", "?"],
    options: ["circle", "triangle", "square", "pentagon"],
    answer: "square",
    explanation: "All shapes in the sequence are squares. The next is <strong>square</strong>."
  },
  {
    id: "shp-easy-05",
    difficulty: "easy",
    question: "What comes next in the sequence?",
    sequence: ["circle", "triangle", "circle", "triangle", "circle", "?"],
    options: ["circle", "square", "triangle", "star"],
    answer: "triangle",
    explanation: "The pattern alternates: circle → triangle → circle → triangle… Next is <strong>triangle</strong>."
  },

  // ── MEDIUM ────────────────────────────────────────────────────────────────
  {
    id: "shp-med-01",
    difficulty: "medium",
    question: "What comes next in the sequence?",
    sequence: ["triangle", "square", "pentagon", "hexagon", "?"],
    options: ["circle", "heptagon", "octagon", "star"],
    answer: "heptagon",
    explanation: "Each shape gains one side: 3 → 4 → 5 → 6 → <strong>7 (heptagon)</strong>."
  },
  {
    id: "shp-med-02",
    difficulty: "medium",
    question: "What comes next in the sequence?",
    sequence: ["circle", "square", "triangle", "circle", "square", "?"],
    options: ["circle", "square", "triangle", "star"],
    answer: "triangle",
    explanation: "The pattern repeats every 3: circle → square → triangle. Next is <strong>triangle</strong>."
  },
  {
    id: "shp-med-03",
    difficulty: "medium",
    question: "What comes next in the sequence?",
    sequence: ["small-circle", "medium-circle", "large-circle", "?"],
    options: ["small-circle", "medium-circle", "large-circle", "xlarge-circle"],
    answer: "xlarge-circle",
    explanation: "Each circle grows larger in size: small → medium → large → <strong>extra-large</strong>."
  },
  {
    id: "shp-med-04",
    difficulty: "medium",
    question: "What comes next in the sequence?",
    sequence: ["star", "circle", "star", "star", "circle", "star", "star", "star", "?"],
    options: ["star", "circle", "triangle", "square"],
    answer: "circle",
    explanation: "The pattern is 1 star, then 1 circle; 2 stars, then 1 circle; 3 stars, then 1 circle… Next is <strong>circle</strong>."
  },
  {
    id: "shp-med-05",
    difficulty: "medium",
    question: "What comes next in the sequence?",
    sequence: ["square", "triangle", "square", "square", "triangle", "square", "?"],
    options: ["circle", "square", "triangle", "star"],
    answer: "square",
    explanation: "The repeating group is: square, triangle, square. Next in group is <strong>square</strong>."
  },

  // ── HARD ──────────────────────────────────────────────────────────────────
  {
    id: "shp-hard-01",
    difficulty: "hard",
    question: "What comes next in the sequence?",
    sequence: ["circle", "square", "circle", "triangle", "circle", "pentagon", "?"],
    options: ["circle", "square", "hexagon", "triangle"],
    answer: "circle",
    explanation: "Every odd position is a circle: 1st, 3rd, 5th… The 7th position is <strong>circle</strong>."
  },
  {
    id: "shp-hard-02",
    difficulty: "hard",
    question: "What comes next in the sequence?",
    sequence: ["triangle", "square", "pentagon", "triangle", "square", "pentagon", "triangle", "?"],
    options: ["triangle", "square", "pentagon", "hexagon"],
    answer: "square",
    explanation: "The sequence repeats the group: triangle, square, pentagon. After triangle comes <strong>square</strong>."
  },
  {
    id: "shp-hard-03",
    difficulty: "hard",
    question: "What comes next in the sequence?",
    sequence: ["hexagon", "pentagon", "square", "triangle", "?"],
    options: ["circle", "square", "pentagon", "line"],
    answer: "circle",
    explanation: "Each shape loses one side: 6 → 5 → 4 → 3 → <strong>0 sides (circle)</strong>."
  },
  {
    id: "shp-hard-04",
    difficulty: "hard",
    question: "What comes next in the sequence?",
    sequence: ["circle", "circle", "square", "circle", "circle", "circle", "square", "?"],
    options: ["circle", "square", "triangle", "star"],
    answer: "circle",
    explanation: "Pattern: 2 circles + 1 square, then 3 circles + 1 square. After the square comes <strong>circle</strong> (starting the next group of 4)."
  },
  {
    id: "shp-hard-05",
    difficulty: "hard",
    question: "What comes next in the sequence?",
    sequence: ["star", "pentagon", "square", "triangle", "?"],
    options: ["circle", "line", "square", "hexagon"],
    answer: "circle",
    explanation: "Sides decrease: star (5 points) → pentagon (5 sides) → square (4) → triangle (3) → <strong>circle (0 corners)</strong>."
  }
];
