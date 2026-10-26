const numberQuestions = [
  // ── EASY ──────────────────────────────────────────────────────────────────
  {
    id: "num-easy-01",
    difficulty: "easy",
    question: "2, 4, 6, 8, ?",
    options: [9, 10, 11, 12],
    answer: 10,
    explanation: "Each number increases by 2 (consecutive even numbers). 8 + 2 = <strong>10</strong>."
  },
  {
    id: "num-easy-02",
    difficulty: "easy",
    question: "5, 10, 15, 20, ?",
    options: [22, 24, 25, 30],
    answer: 25,
    explanation: "Each number increases by 5 (multiples of 5). 20 + 5 = <strong>25</strong>."
  },
  {
    id: "num-easy-03",
    difficulty: "easy",
    question: "1, 3, 5, 7, ?",
    options: [8, 9, 10, 11],
    answer: 9,
    explanation: "Each number increases by 2 (consecutive odd numbers). 7 + 2 = <strong>9</strong>."
  },
  {
    id: "num-easy-04",
    difficulty: "easy",
    question: "10, 20, 30, 40, ?",
    options: [45, 48, 50, 55],
    answer: 50,
    explanation: "Each number increases by 10 (multiples of 10). 40 + 10 = <strong>50</strong>."
  },
  {
    id: "num-easy-05",
    difficulty: "easy",
    question: "100, 90, 80, 70, ?",
    options: [55, 60, 65, 68],
    answer: 60,
    explanation: "Each number decreases by 10. 70 − 10 = <strong>60</strong>."
  },

  // ── MEDIUM ────────────────────────────────────────────────────────────────
  {
    id: "num-med-01",
    difficulty: "medium",
    question: "1, 1, 2, 3, 5, 8, ?",
    options: [11, 12, 13, 14],
    answer: 13,
    explanation: "This is the <strong>Fibonacci sequence</strong> — each number is the sum of the two before it. 5 + 8 = <strong>13</strong>."
  },
  {
    id: "num-med-02",
    difficulty: "medium",
    question: "2, 6, 18, 54, ?",
    options: [108, 144, 162, 216],
    answer: 162,
    explanation: "Each number is multiplied by 3. 54 × 3 = <strong>162</strong>."
  },
  {
    id: "num-med-03",
    difficulty: "medium",
    question: "1, 4, 9, 16, ?",
    options: [20, 24, 25, 36],
    answer: 25,
    explanation: "These are perfect squares: 1², 2², 3², 4²… The next is 5² = <strong>25</strong>."
  },
  {
    id: "num-med-04",
    difficulty: "medium",
    question: "3, 6, 12, 24, ?",
    options: [36, 42, 48, 54],
    answer: 48,
    explanation: "Each number is doubled (multiplied by 2). 24 × 2 = <strong>48</strong>."
  },
  {
    id: "num-med-05",
    difficulty: "medium",
    question: "1, 3, 7, 15, ?",
    options: [28, 30, 31, 33],
    answer: 31,
    explanation: "Each term = previous × 2 + 1. 15 × 2 + 1 = <strong>31</strong>."
  },

  // ── HARD ──────────────────────────────────────────────────────────────────
  {
    id: "num-hard-01",
    difficulty: "hard",
    question: "2, 3, 5, 7, 11, 13, ?",
    options: [14, 15, 16, 17],
    answer: 17,
    explanation: "These are <strong>prime numbers</strong>. The next prime after 13 is <strong>17</strong>."
  },
  {
    id: "num-hard-02",
    difficulty: "hard",
    question: "1, 8, 27, 64, ?",
    options: [100, 115, 125, 128],
    answer: 125,
    explanation: "These are perfect cubes: 1³, 2³, 3³, 4³… The next is 5³ = <strong>125</strong>."
  },
  {
    id: "num-hard-03",
    difficulty: "hard",
    question: "2, 5, 10, 17, 26, ?",
    options: [35, 36, 37, 38],
    answer: 37,
    explanation: "The pattern is n² + 1: 1²+1, 2²+1, 3²+1, 4²+1, 5²+1… The next is 6² + 1 = <strong>37</strong>."
  },
  {
    id: "num-hard-04",
    difficulty: "hard",
    question: "1, 2, 6, 24, 120, ?",
    options: [240, 480, 600, 720],
    answer: 720,
    explanation: "These are <strong>factorials</strong>: 1!, 2!, 3!, 4!, 5!… The next is 6! = <strong>720</strong>."
  },
  {
    id: "num-hard-05",
    difficulty: "hard",
    question: "0, 1, 1, 2, 4, 7, 13, ?",
    options: [20, 22, 24, 26],
    answer: 24,
    explanation: "Each number is the sum of the three numbers before it: 4 + 7 + 13 = <strong>24</strong>."
  }
];
