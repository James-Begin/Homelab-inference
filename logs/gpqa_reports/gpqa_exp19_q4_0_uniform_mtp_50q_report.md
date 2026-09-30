# 50-Question GPQA Diamond Report: Exp 19: Pure Uniform Q4_0 + Native MTP (Dual NUMA + MegaKernel + Barrier Isolation)

- **Experiment ID:** `exp19_q4_0_uniform_mtp`
- **Total Score (50Q):** **14 / 50 (28.0%)**
- **Standard 20Q Subset:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`20.87 tokens/second`**
- **Peak Generation Speed:** **`22.86 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 20.50 | 77.42 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.37 | 74.27 |
| 3 | `gpqa_2` | B | None | WRONG | 1536 | 22.86 | 69.04 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 19.57 | 80.40 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 20.99 | 75.65 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 20.04 | 79.32 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.86 | 75.12 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 19.34 | 80.86 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 18.76 | 99.68 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 19.87 | 79.00 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 20.62 | 76.10 |
| 12 | `gpqa_185` | A | C | WRONG | 1536 | 20.31 | 77.47 |
| 13 | `gpqa_30` | B | A | WRONG | 1536 | 20.14 | 77.71 |
| 14 | `gpqa_165` | C | B | WRONG | 1536 | 19.40 | 84.94 |
| 15 | `gpqa_169` | C | C | CORRECT | 1536 | 22.70 | 69.39 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 20.47 | 76.84 |
| 17 | `gpqa_159` | A | A | CORRECT | 1524 | 21.51 | 72.67 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 21.47 | 72.99 |
| 19 | `gpqa_134` | D | A | WRONG | 1517 | 21.90 | 71.78 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 22.03 | 71.40 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 22.78 | 69.42 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 21.07 | 74.76 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 21.67 | 73.26 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 20.64 | 76.73 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.49 | 77.12 |
| 26 | `gpqa_73` | D | D | CORRECT | 1036 | 22.09 | 48.54 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 19.94 | 79.29 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 20.68 | 75.72 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 21.81 | 72.39 |
| 30 | `gpqa_78` | A | C | WRONG | 1536 | 20.68 | 77.32 |
| 31 | `gpqa_160` | A | C | WRONG | 1536 | 20.55 | 77.34 |
| 32 | `gpqa_66` | C | C | CORRECT | 1536 | 21.84 | 72.53 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 20.74 | 75.34 |
| 34 | `gpqa_184` | C | A | WRONG | 1536 | 21.79 | 72.26 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 20.74 | 76.81 |
| 36 | `gpqa_52` | D | C | WRONG | 1536 | 20.28 | 77.89 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 21.18 | 73.95 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 19.62 | 80.08 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 19.92 | 80.06 |
| 40 | `gpqa_60` | D | A | WRONG | 1536 | 20.04 | 78.76 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 21.01 | 75.29 |
| 42 | `gpqa_47` | A | C | WRONG | 1536 | 20.36 | 77.28 |
| 43 | `gpqa_131` | A | None | WRONG | 1536 | 20.51 | 77.41 |
| 44 | `gpqa_103` | B | B | CORRECT | 1536 | 21.47 | 73.52 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 21.16 | 74.61 |
| 46 | `gpqa_95` | D | D | CORRECT | 1536 | 21.87 | 71.75 |
| 47 | `gpqa_144` | C | None | WRONG | 1536 | 21.76 | 72.03 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 20.66 | 76.47 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 20.76 | 77.05 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 20.93 | 75.62 |
