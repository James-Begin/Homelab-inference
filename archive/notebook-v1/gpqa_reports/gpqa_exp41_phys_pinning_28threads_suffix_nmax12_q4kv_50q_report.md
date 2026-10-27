# 50-Question GPQA Diamond Report: Exp 41: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Balanced Suffix Speculation (n_max=12, match=4, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp41_phys_pinning_28threads_suffix_nmax12_q4kv`
- **Total Score (50Q):** **14 / 50 (28.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`20.38 tokens/second`**
- **Peak Generation Speed:** **`63.69 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 18.31 | 86.61 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 17.75 | 88.59 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 20.30 | 77.43 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 19.19 | 81.61 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 18.37 | 85.88 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 17.44 | 90.62 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 17.82 | 87.68 |
| 8 | `gpqa_13` | B | B | CORRECT | 1091 | 18.18 | 61.40 |
| 9 | `gpqa_127` | D | C | WRONG | 1536 | 53.42 | 46.16 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 17.50 | 89.40 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 18.40 | 85.17 |
| 12 | `gpqa_185` | A | None | WRONG | 1536 | 21.23 | 73.96 |
| 13 | `gpqa_30` | B | A | WRONG | 1536 | 17.31 | 90.11 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 18.06 | 90.25 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 20.78 | 75.44 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 17.61 | 89.15 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 17.69 | 88.49 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 17.40 | 89.80 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 18.69 | 84.74 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 17.66 | 88.50 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 19.87 | 78.99 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 16.76 | 93.27 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 19.41 | 81.42 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 19.35 | 81.44 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 17.79 | 88.41 |
| 26 | `gpqa_73` | D | A | WRONG | 1536 | 17.35 | 90.12 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 17.21 | 91.35 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 16.88 | 92.37 |
| 29 | `gpqa_122` | B | B | CORRECT | 1536 | 17.88 | 87.87 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 17.75 | 89.39 |
| 31 | `gpqa_160` | A | C | WRONG | 1536 | 16.99 | 92.67 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 17.07 | 92.06 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 17.00 | 91.54 |
| 34 | `gpqa_184` | C | C | CORRECT | 1536 | 18.92 | 82.79 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 18.44 | 85.78 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 17.48 | 89.73 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 17.63 | 88.51 |
| 38 | `gpqa_174` | B | C | WRONG | 1536 | 16.59 | 94.41 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 19.30 | 82.33 |
| 40 | `gpqa_60` | D | None | WRONG | 3 | 36.35 | 1.87 |
| 41 | `gpqa_170` | C | C | CORRECT | 1536 | 16.97 | 92.44 |
| 42 | `gpqa_47` | A | None | WRONG | 1536 | 16.58 | 94.28 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 19.70 | 80.10 |
| 44 | `gpqa_103` | B | A | WRONG | 1536 | 17.49 | 89.80 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 17.94 | 87.45 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 17.44 | 89.56 |
| 47 | `gpqa_144` | C | None | WRONG | 3 | 36.30 | 1.18 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 16.22 | 96.52 |
| 49 | `gpqa_142` | C | None | WRONG | 1536 | 63.69 | 26.95 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 17.55 | 89.57 |
