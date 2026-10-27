# 50-Question GPQA Diamond Report: Exp 15: Dual NUMA + Native MTP + MegaKernel + Dynamic Expert Pruning (-ser 2,0.05)

- **Experiment ID:** `exp15_dynamic_expert_pruning`
- **Total Score (50Q):** **17 / 50 (34.0%)**
- **Standard 20Q Subset:** **10 / 20 (50.0%)**
- **Average Generation Speed:** **`19.01 tokens/second`**
- **Peak Generation Speed:** **`20.82 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 19.68 | 81.03 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 19.61 | 80.70 |
| 3 | `gpqa_2` | B | A | WRONG | 1536 | 20.82 | 75.64 |
| 4 | `gpqa_156` | A | A | CORRECT | 817 | 17.37 | 49.07 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 19.16 | 82.77 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 18.77 | 84.45 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 19.50 | 80.40 |
| 8 | `gpqa_13` | B | B | CORRECT | 1026 | 17.24 | 61.13 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 17.61 | 106.28 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 19.24 | 81.81 |
| 11 | `gpqa_3` | C | C | CORRECT | 1536 | 18.85 | 83.22 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 18.94 | 83.36 |
| 13 | `gpqa_30` | B | C | WRONG | 1536 | 18.01 | 86.78 |
| 14 | `gpqa_165` | C | B | WRONG | 1536 | 17.50 | 94.28 |
| 15 | `gpqa_169` | C | C | CORRECT | 1536 | 20.60 | 76.22 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 18.05 | 86.97 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 19.70 | 80.00 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 19.66 | 79.92 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 19.29 | 82.60 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 19.70 | 80.00 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 20.28 | 77.75 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 19.37 | 81.17 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 19.82 | 80.03 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 18.63 | 84.85 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 18.50 | 85.66 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 19.83 | 79.32 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 18.88 | 83.96 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 19.62 | 80.00 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 18.28 | 86.62 |
| 30 | `gpqa_78` | A | C | WRONG | 1536 | 17.45 | 91.76 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 18.60 | 85.16 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 19.38 | 81.28 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 18.94 | 82.37 |
| 34 | `gpqa_184` | C | C | CORRECT | 1224 | 20.04 | 62.81 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 17.88 | 88.36 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 18.91 | 83.32 |
| 37 | `gpqa_192` | C | B | WRONG | 1536 | 19.32 | 80.96 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 18.74 | 84.16 |
| 39 | `gpqa_10` | B | C | WRONG | 1536 | 18.39 | 86.48 |
| 40 | `gpqa_60` | D | A | WRONG | 1536 | 18.49 | 85.32 |
| 41 | `gpqa_170` | C | B | WRONG | 1536 | 19.03 | 82.77 |
| 42 | `gpqa_47` | A | B | WRONG | 207 | 18.56 | 12.79 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 19.37 | 81.67 |
| 44 | `gpqa_103` | B | B | CORRECT | 1378 | 19.28 | 73.55 |
| 45 | `gpqa_193` | D | A | WRONG | 1536 | 20.14 | 78.50 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 20.24 | 77.56 |
| 47 | `gpqa_144` | C | A | WRONG | 1536 | 18.85 | 82.96 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 18.79 | 83.97 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 18.78 | 84.93 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 18.73 | 84.39 |
