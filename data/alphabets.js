const alphabetQuestions = [
  // ── EASY ──────────────────────────────────────────────────────────────────
  {
    id: "alp-easy-01",
    difficulty: "easy",
    question: "A, B, C, D, ?",
    options: ["E", "F", "G", "H"],
    answer: "E",
    explanation: "Simple alphabetical order: A → B → C → D → <strong>E</strong>."
  },
  {
    id: "alp-easy-02",
    difficulty: "easy",
    question: "Z, Y, X, W, ?",
    options: ["U", "V", "T", "S"],
    answer: "V",
    explanation: "Reverse alphabetical order: Z → Y → X → W → <strong>V</strong>."
  },
  {
    id: "alp-easy-03",
    difficulty: "easy",
    question: "A, C, E, G, ?",
    options: ["H", "I", "J", "K"],
    answer: "I",
    explanation: "Every alternate letter (skipping one): A → C → E → G → <strong>I</strong>."
  },
  {
    id: "alp-easy-04",
    difficulty: "easy",
    question: "B, D, F, H, ?",
    options: ["I", "J", "K", "L"],
    answer: "J",
    explanation: "Every alternate letter starting from B: B → D → F → H → <strong>J</strong>."
  },
  {
    id: "alp-easy-05",
    difficulty: "easy",
    question: "M, N, O, P, ?",
    options: ["Q", "R", "S", "T"],
    answer: "Q",
    explanation: "Consecutive letters in alphabetical order: M → N → O → P → <strong>Q</strong>."
  },

  // ── MEDIUM ────────────────────────────────────────────────────────────────
  {
    id: "alp-med-01",
    difficulty: "medium",
    question: "A, D, G, J, ?",
    options: ["L", "M", "N", "O"],
    answer: "M",
    explanation: "Each letter skips 2 letters (+3 positions): A → D → G → J → <strong>M</strong>."
  },
  {
    id: "alp-med-02",
    difficulty: "medium",
    question: "Z, X, V, T, ?",
    options: ["P", "Q", "R", "S"],
    answer: "R",
    explanation: "Going backwards, skipping one letter each time (−2): Z → X → V → T → <strong>R</strong>."
  },
  {
    id: "alp-med-03",
    difficulty: "medium",
    question: "A, Z, B, Y, C, ?",
    options: ["D", "W", "X", "V"],
    answer: "X",
    explanation: "Two interlaced sequences: A, B, C (forward) and Z, Y, X (backward). Next is <strong>X</strong>."
  },
  {
    id: "alp-med-04",
    difficulty: "medium",
    question: "B, E, H, K, ?",
    options: ["L", "M", "N", "O"],
    answer: "N",
    explanation: "Each letter moves +3 positions: B(2) → E(5) → H(8) → K(11) → <strong>N(14)</strong>."
  },
  {
    id: "alp-med-05",
    difficulty: "medium",
    question: "A, B, D, G, K, ?",
    options: ["N", "O", "P", "Q"],
    answer: "P",
    explanation: "The gap increases by 1 each time: +1, +2, +3, +4, +5. K(11) + 5 = P(16) = <strong>P</strong>."
  },

  // ── HARD ──────────────────────────────────────────────────────────────────
  {
    id: "alp-hard-01",
    difficulty: "hard",
    question: "A, C, F, J, O, ?",
    options: ["T", "U", "V", "W"],
    answer: "U",
    explanation: "Gaps increase by 1: +2, +3, +4, +5, +6. O(15) + 6 = U(21) = <strong>U</strong>."
  },
  {
    id: "alp-hard-02",
    difficulty: "hard",
    question: "Z, A, Y, B, X, C, ?",
    options: ["W", "D", "V", "E"],
    answer: "W",
    explanation: "Two alternating sequences: Z, Y, X (descending) and A, B, C (ascending). Next in descending sequence is <strong>W</strong>."
  },
  {
    id: "alp-hard-03",
    difficulty: "hard",
    question: "AZ, BY, CX, DW, ?",
    options: ["EV", "EU", "FV", "FU"],
    answer: "EV",
    explanation: "First letter goes A→B→C→D→<strong>E</strong>; second letter goes Z→Y→X→W→<strong>V</strong>. Answer: <strong>EV</strong>."
  },
  {
    id: "alp-hard-04",
    difficulty: "hard",
    question: "A, B, D, H, P, ?",
    options: ["X", "Z", "AB", "AF"],
    answer: "AF",
    explanation: "Each position doubles: 1, 2, 4, 8, 16, 32. Position 32 = <strong>AF</strong> (A=1, F=6 → 1×26+6=32)."
  },
  {
    id: "alp-hard-05",
    difficulty: "hard",
    question: "M, A, R, S, ?",
    options: ["H", "J", "U", "V"],
    answer: "H",
    explanation: "These spell out planets: MARS → next planet is <strong>EARTH</strong>, whose first letter is <strong>E</strong>... actually these are the letters M-A-R-S and next planet sequence spells EARTH. The pattern here: M(13), A(1), R(18), S(19) — positions sum to spell MARS. Next letter from EARTH = <strong>E</strong>. Hint: The sequence spells planet names: MARS → next is EARTH → first new letter is <strong>E</strong>."
  }
];
