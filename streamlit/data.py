# ── Question Data ──────────────────────────────────────────────────────────
# All 45 questions across 3 categories × 3 difficulties

NUMBER_QUESTIONS = [
    # EASY
    {"id": "num-easy-01", "difficulty": "Easy",   "question": "2, 4, 6, 8, ?",           "options": [9, 10, 11, 12],       "answer": 10,  "explanation": "Each number increases by **2** (even numbers). 8 + 2 = **10**."},
    {"id": "num-easy-02", "difficulty": "Easy",   "question": "5, 10, 15, 20, ?",         "options": [22, 24, 25, 30],      "answer": 25,  "explanation": "Multiples of 5. 20 + 5 = **25**."},
    {"id": "num-easy-03", "difficulty": "Easy",   "question": "1, 3, 5, 7, ?",            "options": [8, 9, 10, 11],        "answer": 9,   "explanation": "Consecutive odd numbers. 7 + 2 = **9**."},
    {"id": "num-easy-04", "difficulty": "Easy",   "question": "10, 20, 30, 40, ?",        "options": [45, 48, 50, 55],      "answer": 50,  "explanation": "Multiples of 10. 40 + 10 = **50**."},
    {"id": "num-easy-05", "difficulty": "Easy",   "question": "100, 90, 80, 70, ?",       "options": [55, 60, 65, 68],      "answer": 60,  "explanation": "Decreasing by 10. 70 − 10 = **60**."},
    # MEDIUM
    {"id": "num-med-01",  "difficulty": "Medium", "question": "1, 1, 2, 3, 5, 8, ?",     "options": [11, 12, 13, 14],      "answer": 13,  "explanation": "**Fibonacci sequence** — each term = sum of two before it. 5 + 8 = **13**."},
    {"id": "num-med-02",  "difficulty": "Medium", "question": "2, 6, 18, 54, ?",          "options": [108, 144, 162, 216],  "answer": 162, "explanation": "Each number × 3. 54 × 3 = **162**."},
    {"id": "num-med-03",  "difficulty": "Medium", "question": "1, 4, 9, 16, ?",           "options": [20, 24, 25, 36],      "answer": 25,  "explanation": "Perfect squares: 1², 2², 3², 4²… Next is 5² = **25**."},
    {"id": "num-med-04",  "difficulty": "Medium", "question": "3, 6, 12, 24, ?",          "options": [36, 42, 48, 54],      "answer": 48,  "explanation": "Each number doubled. 24 × 2 = **48**."},
    {"id": "num-med-05",  "difficulty": "Medium", "question": "1, 3, 7, 15, ?",           "options": [28, 30, 31, 33],      "answer": 31,  "explanation": "Each term = previous × 2 + 1. 15 × 2 + 1 = **31**."},
    # HARD
    {"id": "num-hard-01", "difficulty": "Hard",   "question": "2, 3, 5, 7, 11, 13, ?",   "options": [14, 15, 16, 17],      "answer": 17,  "explanation": "**Prime numbers**. Next prime after 13 = **17**."},
    {"id": "num-hard-02", "difficulty": "Hard",   "question": "1, 8, 27, 64, ?",          "options": [100, 115, 125, 128],  "answer": 125, "explanation": "Perfect cubes: 1³, 2³, 3³, 4³… Next is 5³ = **125**."},
    {"id": "num-hard-03", "difficulty": "Hard",   "question": "2, 5, 10, 17, 26, ?",      "options": [35, 36, 37, 38],      "answer": 37,  "explanation": "Pattern: n² + 1. Next is 6² + 1 = **37**."},
    {"id": "num-hard-04", "difficulty": "Hard",   "question": "1, 2, 6, 24, 120, ?",      "options": [240, 480, 600, 720],  "answer": 720, "explanation": "**Factorials**: 1!, 2!, 3!, 4!, 5!… Next is 6! = **720**."},
    {"id": "num-hard-05", "difficulty": "Hard",   "question": "0, 1, 1, 2, 4, 7, 13, ?", "options": [20, 22, 24, 26],      "answer": 24,  "explanation": "Each term = sum of the 3 before it. 4 + 7 + 13 = **24**."},
]

SHAPE_QUESTIONS = [
    # EASY
    {"id": "shp-easy-01", "difficulty": "Easy",   "sequence": ["circle","circle","circle","circle","?"],                        "options": ["circle","square","triangle","star"],    "answer": "circle",   "explanation": "All shapes are **circles**. Next is 🔵 **circle**."},
    {"id": "shp-easy-02", "difficulty": "Easy",   "sequence": ["circle","square","circle","square","?"],                        "options": ["triangle","circle","star","pentagon"],  "answer": "circle",   "explanation": "Alternating: circle → square → circle → square → **circle**."},
    {"id": "shp-easy-03", "difficulty": "Easy",   "sequence": ["triangle","triangle","circle","triangle","triangle","circle","?"],"options": ["circle","square","triangle","star"],  "answer": "triangle", "explanation": "Pattern repeats every 3: △△○. After ○ comes **triangle**."},
    {"id": "shp-easy-04", "difficulty": "Easy",   "sequence": ["square","square","square","?"],                                  "options": ["circle","triangle","square","pentagon"],"answer": "square",   "explanation": "Only squares. Next is **square**."},
    {"id": "shp-easy-05", "difficulty": "Easy",   "sequence": ["circle","triangle","circle","triangle","circle","?"],            "options": ["circle","square","triangle","star"],    "answer": "triangle", "explanation": "Alternating: circle → triangle → **triangle** next."},
    # MEDIUM
    {"id": "shp-med-01",  "difficulty": "Medium", "sequence": ["triangle","square","pentagon","hexagon","?"],                    "options": ["circle","heptagon","octagon","star"],   "answer": "heptagon", "explanation": "Each shape gains one side: 3→4→5→6→**7 sides (heptagon)**."},
    {"id": "shp-med-02",  "difficulty": "Medium", "sequence": ["circle","square","triangle","circle","square","?"],              "options": ["circle","square","triangle","star"],    "answer": "triangle", "explanation": "Repeating group of 3: circle→square→triangle. Next is **triangle**."},
    {"id": "shp-med-03",  "difficulty": "Medium", "sequence": ["circle","circle","circle","?"],                                  "options": ["circle","square","triangle","star"],    "answer": "circle",   "explanation": "Growing circle sizes: small→medium→large→**extra-large**."},
    {"id": "shp-med-04",  "difficulty": "Medium", "sequence": ["star","circle","star","star","circle","star","star","star","?"], "options": ["star","circle","triangle","square"],    "answer": "circle",   "explanation": "1 star+circle, 2 stars+circle, 3 stars+**circle**."},
    {"id": "shp-med-05",  "difficulty": "Medium", "sequence": ["square","triangle","square","square","triangle","square","?"],   "options": ["circle","square","triangle","star"],    "answer": "square",   "explanation": "Repeating group: square, triangle, square. Next is **square**."},
    # HARD
    {"id": "shp-hard-01", "difficulty": "Hard",   "sequence": ["circle","square","circle","triangle","circle","pentagon","?"],   "options": ["circle","square","hexagon","triangle"], "answer": "circle",   "explanation": "Every odd position (1,3,5,7…) is a **circle**."},
    {"id": "shp-hard-02", "difficulty": "Hard",   "sequence": ["triangle","square","pentagon","triangle","square","pentagon","triangle","?"],"options": ["triangle","square","pentagon","hexagon"],"answer": "square","explanation": "Repeating: △, □, ⬠. After △ comes **square**."},
    {"id": "shp-hard-03", "difficulty": "Hard",   "sequence": ["hexagon","pentagon","square","triangle","?"],                    "options": ["circle","square","pentagon","line"],    "answer": "circle",   "explanation": "Sides decrease: 6→5→4→3→**0 (circle)**."},
    {"id": "shp-hard-04", "difficulty": "Hard",   "sequence": ["circle","circle","square","circle","circle","circle","square","?"],"options": ["circle","square","triangle","star"],  "answer": "circle",   "explanation": "Groups of 2+sq, 3+sq… After square starts next group: **circle**."},
    {"id": "shp-hard-05", "difficulty": "Hard",   "sequence": ["star","pentagon","square","triangle","?"],                       "options": ["circle","line","square","hexagon"],     "answer": "circle",   "explanation": "Sides decrease: 5pt→5→4→3→**0 (circle)**."},
]

ALPHABET_QUESTIONS = [
    # EASY
    {"id": "alp-easy-01", "difficulty": "Easy",   "question": "A, B, C, D, ?",     "options": ["E","F","G","H"],      "answer": "E",  "explanation": "Alphabetical order. After D comes **E**."},
    {"id": "alp-easy-02", "difficulty": "Easy",   "question": "Z, Y, X, W, ?",     "options": ["U","V","T","S"],      "answer": "V",  "explanation": "Reverse order. After W comes **V**."},
    {"id": "alp-easy-03", "difficulty": "Easy",   "question": "A, C, E, G, ?",     "options": ["H","I","J","K"],      "answer": "I",  "explanation": "Every alternate letter (+2). After G comes **I**."},
    {"id": "alp-easy-04", "difficulty": "Easy",   "question": "B, D, F, H, ?",     "options": ["I","J","K","L"],      "answer": "J",  "explanation": "Alternate letters starting B. After H comes **J**."},
    {"id": "alp-easy-05", "difficulty": "Easy",   "question": "M, N, O, P, ?",     "options": ["Q","R","S","T"],      "answer": "Q",  "explanation": "Consecutive letters. After P comes **Q**."},
    # MEDIUM
    {"id": "alp-med-01",  "difficulty": "Medium", "question": "A, D, G, J, ?",     "options": ["L","M","N","O"],      "answer": "M",  "explanation": "Skip 2 letters each time (+3). J + 3 = **M**."},
    {"id": "alp-med-02",  "difficulty": "Medium", "question": "Z, X, V, T, ?",     "options": ["P","Q","R","S"],      "answer": "R",  "explanation": "Backwards, skipping one (−2). T − 2 = **R**."},
    {"id": "alp-med-03",  "difficulty": "Medium", "question": "A, Z, B, Y, C, ?",  "options": ["D","W","X","V"],      "answer": "X",  "explanation": "Two interlaced: A,B,C (forward) & Z,Y,X (backward). Next is **X**."},
    {"id": "alp-med-04",  "difficulty": "Medium", "question": "B, E, H, K, ?",     "options": ["L","M","N","O"],      "answer": "N",  "explanation": "+3 each step. K(11) + 3 = N(14) = **N**."},
    {"id": "alp-med-05",  "difficulty": "Medium", "question": "A, B, D, G, K, ?",  "options": ["N","O","P","Q"],      "answer": "P",  "explanation": "Gap increases by 1: +1,+2,+3,+4,+5. K + 5 = **P**."},
    # HARD
    {"id": "alp-hard-01", "difficulty": "Hard",   "question": "A, C, F, J, O, ?",  "options": ["T","U","V","W"],      "answer": "U",  "explanation": "Gaps increase by 1: +2,+3,+4,+5,+6. O + 6 = **U**."},
    {"id": "alp-hard-02", "difficulty": "Hard",   "question": "Z, A, Y, B, X, C, ?","options": ["W","D","V","E"],     "answer": "W",  "explanation": "Alternating Z,Y,X… and A,B,C…. Next in descending: **W**."},
    {"id": "alp-hard-03", "difficulty": "Hard",   "question": "AZ, BY, CX, DW, ?", "options": ["EV","EU","FV","FU"],  "answer": "EV", "explanation": "First letter A→B→C→D→**E**; second Z→Y→X→W→**V**. Answer: **EV**."},
    {"id": "alp-hard-04", "difficulty": "Hard",   "question": "A, B, D, H, P, ?",  "options": ["X","Z","AB","AF"],    "answer": "AF", "explanation": "Positions double: 1,2,4,8,16,32. Position 32 = **AF**."},
    {"id": "alp-hard-05", "difficulty": "Hard",   "question": "M, A, R, S, ?",     "options": ["H","J","E","V"],      "answer": "E",  "explanation": "Spells planet names: **MARS** → next planet **EARTH** → first letter **E**."},
]
