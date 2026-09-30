# 50-Question GPQA Diamond Report: Exp 29: Confidence-Gated Speculative Diffusion Scaling (DFlash n_max=4, p_min=0.45 + Q4_0 KV Cache + SER 2,0.5)

- **Experiment ID:** `exp29_dflash_nmax4_pmin045_q4kv`
- **Total Score (50Q):** **14 / 50 (28.0%)**
- **Standard 20Q Subset:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`19.64 tokens/second`**
- **Peak Generation Speed:** **`29.72 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 16.51 | 95.40 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 19.86 | 79.45 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 23.13 | 68.06 |
| 4 | `gpqa_156` | A | A | CORRECT | 906 | 16.03 | 58.33 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 18.66 | 84.21 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 17.32 | 91.17 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 22.48 | 69.72 |
| 8 | `gpqa_13` | B | C | WRONG | 1536 | 15.19 | 102.46 |
| 9 | `gpqa_127` | D | D | CORRECT | 1536 | 29.72 | 65.09 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 20.02 | 78.42 |
| 11 | `gpqa_3` | C | B | WRONG | 1536 | 20.74 | 75.32 |
| 12 | `gpqa_185` | A | C | WRONG | 1536 | 17.65 | 88.57 |
| 13 | `gpqa_30` | B | C | WRONG | 1536 | 18.38 | 84.85 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 17.17 | 94.35 |
| 15 | `gpqa_169` | C | None | WRONG | 3 | 9.91 | 1.80 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 18.58 | 84.21 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 21.61 | 72.66 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 18.29 | 85.44 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 20.36 | 77.78 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 21.98 | 71.33 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 25.73 | 61.26 |
| 22 | `gpqa_53` | B | None | WRONG | 1536 | 19.43 | 80.72 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 21.70 | 72.83 |
| 24 | `gpqa_80` | D | C | WRONG | 1536 | 16.01 | 97.87 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 16.85 | 93.23 |
| 26 | `gpqa_73` | D | D | CORRECT | 918 | 22.52 | 42.39 |
| 27 | `gpqa_37` | A | B | WRONG | 1536 | 17.81 | 88.31 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 17.39 | 89.56 |
| 29 | `gpqa_122` | B | B | CORRECT | 1536 | 23.11 | 68.03 |
| 30 | `gpqa_78` | A | C | WRONG | 1536 | 19.77 | 80.05 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 17.75 | 88.69 |
| 32 | `gpqa_66` | C | A | WRONG | 1536 | 24.14 | 65.50 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 18.36 | 84.79 |
| 34 | `gpqa_184` | C | C | CORRECT | 1536 | 24.74 | 63.55 |
| 35 | `gpqa_32` | B | C | WRONG | 1536 | 18.12 | 86.94 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.24 | 81.68 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 21.73 | 72.05 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 18.27 | 85.77 |
| 39 | `gpqa_10` | B | A | WRONG | 1217 | 16.59 | 75.96 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 16.74 | 93.40 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 18.46 | 84.92 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 16.50 | 94.46 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 19.86 | 79.45 |
| 44 | `gpqa_103` | B | B | CORRECT | 1536 | 21.35 | 73.82 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 27.97 | 56.77 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 23.07 | 67.84 |
| 47 | `gpqa_144` | C | None | WRONG | 1536 | 20.55 | 75.89 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 18.19 | 86.13 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 18.27 | 86.72 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 17.99 | 87.23 |
