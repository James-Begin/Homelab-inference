# 50-Question GPQA Diamond Report: Exp 18: Calibrated SER (Dual NUMA + Native MTP + -ser 2,0.5 + Fused Barrier Isolation)

- **Experiment ID:** `exp18_calibrated_ser`
- **Total Score (50Q):** **19 / 50 (38.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`19.11 tokens/second`**
- **Peak Generation Speed:** **`21.07 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 18.58 | 85.50 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 20.40 | 77.52 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 20.76 | 75.83 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 18.46 | 85.22 |
| 5 | `gpqa_128` | A | C | WRONG | 1536 | 19.42 | 81.39 |
| 6 | `gpqa_12` | D | A | WRONG | 1536 | 20.63 | 76.97 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 19.41 | 80.64 |
| 8 | `gpqa_13` | B | B | CORRECT | 1289 | 16.90 | 77.92 |
| 9 | `gpqa_127` | D | D | CORRECT | 1536 | 17.10 | 108.40 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 18.43 | 85.27 |
| 11 | `gpqa_3` | C | C | CORRECT | 1536 | 18.45 | 84.86 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 18.60 | 84.38 |
| 13 | `gpqa_30` | B | C | WRONG | 1536 | 18.43 | 85.08 |
| 14 | `gpqa_165` | C | D | WRONG | 1536 | 18.02 | 91.11 |
| 15 | `gpqa_169` | C | A | WRONG | 1536 | 20.22 | 77.46 |
| 16 | `gpqa_15` | D | C | WRONG | 1536 | 18.64 | 84.29 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 19.35 | 81.53 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 19.01 | 82.33 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 19.44 | 81.83 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 20.63 | 76.25 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 20.72 | 76.31 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 18.85 | 83.27 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 19.72 | 80.37 |
| 24 | `gpqa_80` | D | D | CORRECT | 1536 | 18.94 | 83.08 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 18.57 | 85.29 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 20.49 | 76.66 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 18.62 | 84.94 |
| 28 | `gpqa_126` | B | C | WRONG | 1536 | 20.22 | 77.72 |
| 29 | `gpqa_122` | B | None | WRONG | 1536 | 19.84 | 79.54 |
| 30 | `gpqa_78` | A | B | WRONG | 1536 | 18.89 | 84.02 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 17.72 | 89.14 |
| 32 | `gpqa_66` | C | C | CORRECT | 1210 | 19.97 | 62.86 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 18.53 | 84.22 |
| 34 | `gpqa_184` | C | A | WRONG | 1536 | 20.32 | 77.57 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 18.06 | 87.69 |
| 36 | `gpqa_52` | D | C | WRONG | 1536 | 18.47 | 85.10 |
| 37 | `gpqa_192` | C | C | CORRECT | 1341 | 20.24 | 67.82 |
| 38 | `gpqa_174` | B | B | CORRECT | 1536 | 18.15 | 86.53 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 17.59 | 90.39 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 18.86 | 83.69 |
| 41 | `gpqa_170` | C | C | CORRECT | 1536 | 18.52 | 85.07 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 18.72 | 83.62 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 19.07 | 83.24 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 19.23 | 81.90 |
| 45 | `gpqa_193` | D | D | CORRECT | 1351 | 21.07 | 66.08 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 19.67 | 79.79 |
| 47 | `gpqa_144` | C | A | WRONG | 1536 | 19.52 | 80.10 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 18.95 | 83.25 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 18.44 | 86.42 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 18.66 | 84.33 |
