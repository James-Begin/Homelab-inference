# 50-Question GPQA Diamond Report: Exp 25: Multi-Token Batch Verification Scaling (DFlash n_max=4 + Q4_0 KV Cache + SER 2,0.5)

- **Experiment ID:** `exp25_dflash_nmax4_q4kv`
- **Total Score (50Q):** **14 / 50 (28.0%)**
- **Standard 20Q Subset:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`19.13 tokens/second`**
- **Peak Generation Speed:** **`28.74 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 17.86 | 88.27 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.23 | 74.19 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 24.75 | 63.60 |
| 4 | `gpqa_156` | A | A | CORRECT | 906 | 16.86 | 55.26 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 18.22 | 86.35 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 16.71 | 94.24 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 21.82 | 71.79 |
| 8 | `gpqa_13` | B | C | WRONG | 1536 | 14.59 | 106.62 |
| 9 | `gpqa_127` | D | D | CORRECT | 1536 | 28.74 | 67.24 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 19.46 | 80.37 |
| 11 | `gpqa_3` | C | B | WRONG | 1536 | 20.16 | 77.57 |
| 12 | `gpqa_185` | A | C | WRONG | 1536 | 17.16 | 91.08 |
| 13 | `gpqa_30` | B | C | WRONG | 1536 | 17.90 | 87.16 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 16.73 | 96.68 |
| 15 | `gpqa_169` | C | None | WRONG | 3 | 9.54 | 1.85 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 18.13 | 86.36 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 21.03 | 74.49 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 17.82 | 87.60 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 19.87 | 79.55 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 21.41 | 73.32 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 25.02 | 62.88 |
| 22 | `gpqa_53` | B | None | WRONG | 1536 | 18.94 | 82.66 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 21.09 | 74.80 |
| 24 | `gpqa_80` | D | C | WRONG | 1536 | 15.58 | 100.38 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 16.57 | 94.81 |
| 26 | `gpqa_73` | D | D | CORRECT | 918 | 22.08 | 42.99 |
| 27 | `gpqa_37` | A | B | WRONG | 1536 | 17.52 | 89.60 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 16.66 | 93.62 |
| 29 | `gpqa_122` | B | B | CORRECT | 1536 | 22.17 | 71.02 |
| 30 | `gpqa_78` | A | C | WRONG | 1536 | 18.99 | 83.51 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 17.05 | 92.28 |
| 32 | `gpqa_66` | C | A | WRONG | 1536 | 23.20 | 68.15 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 17.63 | 88.22 |
| 34 | `gpqa_184` | C | C | CORRECT | 1536 | 23.78 | 66.00 |
| 35 | `gpqa_32` | B | C | WRONG | 1536 | 17.41 | 90.23 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 18.46 | 85.06 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 21.06 | 74.31 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 17.77 | 87.99 |
| 39 | `gpqa_10` | B | A | WRONG | 1217 | 16.08 | 78.07 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 16.20 | 96.56 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 17.95 | 87.49 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 15.77 | 98.98 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 18.99 | 82.98 |
| 44 | `gpqa_103` | B | B | CORRECT | 1536 | 20.39 | 77.17 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 26.65 | 59.53 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 21.95 | 71.45 |
| 47 | `gpqa_144` | C | None | WRONG | 1536 | 19.53 | 79.78 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 17.32 | 90.23 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 17.43 | 90.80 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 17.40 | 90.35 |
