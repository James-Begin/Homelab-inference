# 50-Question GPQA Diamond Report: Exp 39: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Tuned Window Chained Spec (n_max=10, N=8, M=16, hits=2) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp39_phys_pinning_28threads_tuned_chained_spec_q4kv`
- **Total Score (50Q):** **16 / 50 (32.0%)**
- **Standard 20Q Subset:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`20.45 tokens/second`**
- **Peak Generation Speed:** **`26.09 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 20.43 | 77.95 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 20.61 | 76.62 |
| 3 | `gpqa_2` | B | None | WRONG | 1536 | 21.04 | 74.54 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 21.73 | 72.35 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 20.56 | 76.93 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 20.03 | 79.11 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.70 | 75.69 |
| 8 | `gpqa_13` | B | B | CORRECT | 1223 | 19.16 | 65.28 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 26.09 | 76.20 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 19.77 | 79.34 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 19.98 | 78.39 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 20.14 | 78.05 |
| 13 | `gpqa_30` | B | C | WRONG | 1536 | 19.69 | 79.56 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 19.44 | 84.53 |
| 15 | `gpqa_169` | C | C | CORRECT | 1075 | 22.29 | 49.69 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 20.10 | 78.26 |
| 17 | `gpqa_159` | A | C | WRONG | 1536 | 20.11 | 78.16 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 20.50 | 76.32 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 20.82 | 76.58 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 21.04 | 74.58 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 22.02 | 71.47 |
| 22 | `gpqa_53` | B | None | WRONG | 1536 | 20.82 | 75.42 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 20.86 | 75.73 |
| 24 | `gpqa_80` | D | D | CORRECT | 39 | 17.60 | 4.31 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.40 | 77.42 |
| 26 | `gpqa_73` | D | D | CORRECT | 1444 | 20.71 | 71.33 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 19.85 | 79.70 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 20.39 | 76.66 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 20.39 | 77.13 |
| 30 | `gpqa_78` | A | C | WRONG | 1536 | 20.30 | 78.57 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 19.91 | 79.56 |
| 32 | `gpqa_66` | C | A | WRONG | 1536 | 20.59 | 76.77 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 20.66 | 75.49 |
| 34 | `gpqa_184` | C | A | WRONG | 1536 | 20.97 | 74.78 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 19.34 | 81.70 |
| 36 | `gpqa_52` | D | D | CORRECT | 1536 | 19.01 | 82.70 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 19.95 | 78.30 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 20.14 | 77.99 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 21.38 | 74.40 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 19.45 | 80.87 |
| 41 | `gpqa_170` | C | C | CORRECT | 1536 | 20.22 | 77.67 |
| 42 | `gpqa_47` | A | C | WRONG | 1536 | 19.15 | 81.69 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 20.80 | 76.15 |
| 44 | `gpqa_103` | B | A | WRONG | 1536 | 20.75 | 75.83 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 23.80 | 66.63 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 20.07 | 78.25 |
| 47 | `gpqa_144` | C | None | WRONG | 3 | 18.79 | 1.27 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.68 | 80.05 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 20.44 | 78.18 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 20.05 | 78.68 |
