# 50-Question GPQA Diamond Report: Exp 17: Combined Champion (Dual NUMA + MegaKernel + Precision Chained Spec + SER + Fused Barrier Isolation)

- **Experiment ID:** `exp17_combined_champion`
- **Total Score (50Q):** **18 / 50 (36.0%)**
- **Standard 20Q Subset:** **9 / 20 (45.0%)**
- **Average Generation Speed:** **`18.41 tokens/second`**
- **Peak Generation Speed:** **`20.89 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 18.51 | 86.40 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 18.76 | 84.14 |
| 3 | `gpqa_2` | B | None | WRONG | 1536 | 19.03 | 82.60 |
| 4 | `gpqa_156` | A | A | CORRECT | 817 | 17.49 | 48.81 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 18.53 | 85.21 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 17.85 | 88.97 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 18.63 | 84.02 |
| 8 | `gpqa_13` | B | B | CORRECT | 1026 | 17.23 | 61.18 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 16.13 | 113.87 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 18.86 | 83.49 |
| 11 | `gpqa_3` | C | B | WRONG | 1536 | 17.57 | 89.21 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 17.94 | 87.55 |
| 13 | `gpqa_30` | B | C | WRONG | 1536 | 17.74 | 88.29 |
| 14 | `gpqa_165` | C | B | WRONG | 1536 | 17.52 | 93.50 |
| 15 | `gpqa_169` | C | C | CORRECT | 1536 | 20.89 | 75.19 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 18.50 | 85.01 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 18.84 | 83.76 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 19.29 | 81.22 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 19.19 | 82.99 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 19.54 | 80.41 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 18.41 | 85.24 |
| 22 | `gpqa_53` | B | None | WRONG | 1536 | 18.19 | 86.32 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 18.34 | 86.03 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 18.33 | 86.17 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 18.72 | 84.65 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 19.23 | 81.63 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 17.63 | 89.57 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 19.11 | 82.19 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 18.11 | 87.02 |
| 30 | `gpqa_78` | A | C | WRONG | 1536 | 17.73 | 89.71 |
| 31 | `gpqa_160` | A | C | WRONG | 1536 | 17.72 | 89.08 |
| 32 | `gpqa_66` | C | C | CORRECT | 1536 | 18.50 | 85.35 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 19.29 | 80.92 |
| 34 | `gpqa_184` | C | C | CORRECT | 1153 | 18.99 | 62.45 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 17.89 | 88.58 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 17.50 | 89.70 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 18.36 | 85.31 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 17.75 | 88.57 |
| 39 | `gpqa_10` | B | C | WRONG | 1536 | 18.41 | 86.52 |
| 40 | `gpqa_60` | D | A | WRONG | 1536 | 17.77 | 88.55 |
| 41 | `gpqa_170` | C | C | CORRECT | 1536 | 18.57 | 84.89 |
| 42 | `gpqa_47` | A | B | WRONG | 207 | 18.82 | 12.59 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 18.53 | 85.70 |
| 44 | `gpqa_103` | B | B | CORRECT | 1536 | 19.03 | 82.90 |
| 45 | `gpqa_193` | D | D | CORRECT | 1536 | 20.12 | 78.47 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 18.56 | 84.60 |
| 47 | `gpqa_144` | C | A | WRONG | 1536 | 18.93 | 82.63 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 17.66 | 89.14 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 18.17 | 87.29 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 18.22 | 86.44 |
