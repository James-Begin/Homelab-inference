# 50-Question GPQA Diamond Report: Exp 45: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Merged Up/Gate Experts (-muge) + Precision Suffix Spec (n_max=9, match=5) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp45_phys_pinning_28threads_muge_suffix_nmax9_match5_q4kv`
- **Total Score (50Q):** **14 / 50 (28.0%)**
- **Standard 20Q Subset:** **6 / 20 (30.0%)**
- **Average Generation Speed:** **`21.98 tokens/second`**
- **Peak Generation Speed:** **`57.55 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 20.53 | 77.61 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 20.20 | 78.03 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 21.63 | 72.58 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 18.91 | 83.02 |
| 5 | `gpqa_128` | A | None | WRONG | 1536 | 57.55 | 29.06 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 33.14 | 48.84 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 19.39 | 80.59 |
| 8 | `gpqa_13` | B | D | WRONG | 1536 | 17.75 | 88.00 |
| 9 | `gpqa_127` | D | D | CORRECT | 1536 | 38.36 | 57.22 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 19.64 | 79.88 |
| 11 | `gpqa_3` | C | B | WRONG | 1536 | 21.79 | 72.02 |
| 12 | `gpqa_185` | A | None | WRONG | 1536 | 19.35 | 81.08 |
| 13 | `gpqa_30` | B | C | WRONG | 1536 | 19.03 | 82.06 |
| 14 | `gpqa_165` | C | B | WRONG | 1536 | 17.89 | 91.15 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 20.26 | 77.43 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 19.96 | 78.58 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 18.92 | 165.15 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 18.74 | 83.61 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 19.36 | 81.85 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 19.39 | 80.96 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 20.07 | 78.38 |
| 22 | `gpqa_53` | B | None | WRONG | 1536 | 18.55 | 84.48 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 19.06 | 82.69 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 19.23 | 82.02 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 18.72 | 84.41 |
| 26 | `gpqa_73` | D | A | WRONG | 1536 | 19.12 | 82.00 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 18.74 | 84.23 |
| 28 | `gpqa_126` | B | C | WRONG | 1536 | 20.17 | 77.53 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 19.90 | 78.98 |
| 30 | `gpqa_78` | A | C | WRONG | 1536 | 19.58 | 81.02 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 18.19 | 86.58 |
| 32 | `gpqa_66` | C | C | CORRECT | 1536 | 19.93 | 79.14 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 18.25 | 85.33 |
| 34 | `gpqa_184` | C | C | CORRECT | 789 | 22.15 | 37.21 |
| 35 | `gpqa_32` | B | C | WRONG | 1536 | 18.44 | 85.71 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 18.18 | 86.33 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 18.52 | 84.43 |
| 38 | `gpqa_174` | B | C | WRONG | 1336 | 18.39 | 74.42 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 19.77 | 80.52 |
| 40 | `gpqa_60` | D | None | WRONG | 3 | 35.69 | 2.09 |
| 41 | `gpqa_170` | C | C | CORRECT | 1536 | 19.05 | 82.62 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 17.83 | 87.60 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 19.57 | 80.81 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 18.69 | 84.13 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 22.86 | 68.94 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 19.35 | 80.93 |
| 47 | `gpqa_144` | C | None | WRONG | 3 | 36.13 | 1.32 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 18.24 | 86.03 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 46.33 | 35.99 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 18.72 | 84.32 |
