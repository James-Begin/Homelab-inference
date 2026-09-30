# 50-Question GPQA Diamond Report: Exp 40: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Burst-16 Suffix Speculation (n_max=16, match=5, depth=64) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp40_phys_pinning_28threads_suffix_burst16_q4kv`
- **Total Score (50Q):** **12 / 50 (24.0%)**
- **Standard 20Q Subset:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`20.97 tokens/second`**
- **Peak Generation Speed:** **`66.25 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 19.29 | 82.46 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 18.74 | 83.99 |
| 3 | `gpqa_2` | B | None | WRONG | 1536 | 20.18 | 77.63 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 19.33 | 81.21 |
| 5 | `gpqa_128` | A | None | WRONG | 1536 | 66.25 | 25.48 |
| 6 | `gpqa_12` | D | A | WRONG | 1536 | 26.37 | 60.86 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.53 | 76.25 |
| 8 | `gpqa_13` | B | C | WRONG | 1536 | 17.72 | 88.13 |
| 9 | `gpqa_127` | D | D | CORRECT | 1536 | 48.50 | 49.18 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 18.31 | 85.74 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 17.55 | 88.94 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 19.42 | 80.78 |
| 13 | `gpqa_30` | B | A | WRONG | 1536 | 18.47 | 84.65 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 18.04 | 90.50 |
| 15 | `gpqa_169` | C | C | CORRECT | 1086 | 19.46 | 57.42 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 19.94 | 78.87 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 17.99 | 87.06 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 18.66 | 84.05 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 19.35 | 81.94 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 19.09 | 82.18 |
| 21 | `gpqa_5` | C | None | WRONG | 1536 | 20.98 | 74.94 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 17.15 | 91.36 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 19.10 | 82.54 |
| 24 | `gpqa_80` | D | None | WRONG | 1536 | 19.69 | 80.13 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 18.09 | 87.30 |
| 26 | `gpqa_73` | D | None | WRONG | 1536 | 19.85 | 79.02 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 18.18 | 86.65 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 16.66 | 93.74 |
| 29 | `gpqa_122` | B | C | WRONG | 1536 | 18.05 | 86.94 |
| 30 | `gpqa_78` | A | C | WRONG | 1536 | 18.81 | 84.38 |
| 31 | `gpqa_160` | A | C | WRONG | 1536 | 17.56 | 89.83 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 17.96 | 87.59 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 18.21 | 85.58 |
| 34 | `gpqa_184` | C | A | WRONG | 1536 | 18.50 | 84.69 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 18.16 | 86.93 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 16.77 | 93.43 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 17.34 | 89.96 |
| 38 | `gpqa_174` | B | D | WRONG | 1090 | 17.83 | 62.91 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 20.89 | 76.31 |
| 40 | `gpqa_60` | D | None | WRONG | 3 | 35.49 | 2.07 |
| 41 | `gpqa_170` | C | B | WRONG | 1536 | 17.52 | 89.55 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 16.91 | 92.39 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 16.93 | 93.22 |
| 44 | `gpqa_103` | B | B | CORRECT | 1536 | 20.87 | 75.65 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 19.36 | 81.14 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 17.82 | 87.72 |
| 47 | `gpqa_144` | C | None | WRONG | 3 | 35.92 | 1.31 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 17.08 | 91.74 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 19.79 | 80.31 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 18.02 | 87.42 |
