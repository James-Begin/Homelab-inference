# 50-Question GPQA Diamond Report: Exp 44: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Merged Up/Gate Experts (-muge) + Dynamic Suffix Speculation (n_max=8, match=4) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp44_phys_pinning_28threads_muge_suffix_q4kv`
- **Total Score (50Q):** **16 / 50 (32.0%)**
- **Standard 20Q Subset:** **10 / 20 (50.0%)**
- **Average Generation Speed:** **`20.78 tokens/second`**
- **Peak Generation Speed:** **`48.86 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 19.39 | 82.00 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 18.12 | 86.79 |
| 3 | `gpqa_2` | B | None | WRONG | 1536 | 20.23 | 77.58 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 18.51 | 84.77 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 20.48 | 77.06 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 35.66 | 45.62 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.44 | 76.53 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 17.93 | 87.16 |
| 9 | `gpqa_127` | D | None | WRONG | 1536 | 38.39 | 56.84 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 17.98 | 87.03 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 19.81 | 78.97 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 19.46 | 80.64 |
| 13 | `gpqa_30` | B | C | WRONG | 1536 | 17.81 | 87.64 |
| 14 | `gpqa_165` | C | C | CORRECT | 1536 | 19.46 | 84.27 |
| 15 | `gpqa_169` | C | C | CORRECT | 1299 | 20.06 | 66.22 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 18.37 | 85.42 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 17.87 | 87.77 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 18.42 | 85.11 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 17.99 | 87.87 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 17.57 | 89.22 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 21.42 | 73.33 |
| 22 | `gpqa_53` | B | None | WRONG | 1536 | 20.61 | 76.05 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 18.60 | 84.72 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 18.45 | 85.30 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 18.56 | 84.92 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 17.84 | 87.86 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 17.92 | 87.92 |
| 28 | `gpqa_126` | B | None | WRONG | 1536 | 21.05 | 74.47 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 18.42 | 85.24 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 19.86 | 80.07 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 17.02 | 92.53 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 19.17 | 82.08 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 17.45 | 89.11 |
| 34 | `gpqa_184` | C | A | WRONG | 1536 | 19.14 | 81.80 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 18.07 | 87.21 |
| 36 | `gpqa_52` | D | B | WRONG | 1536 | 17.28 | 91.03 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 48.86 | 32.85 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 17.52 | 89.41 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 19.81 | 80.21 |
| 40 | `gpqa_60` | D | None | WRONG | 3 | 36.66 | 1.81 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 17.46 | 89.93 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 16.79 | 92.95 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 19.69 | 80.32 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 18.48 | 85.15 |
| 45 | `gpqa_193` | D | A | WRONG | 1536 | 21.11 | 145.31 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 17.57 | 88.98 |
| 47 | `gpqa_144` | C | None | WRONG | 3 | 36.77 | 1.23 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 17.82 | 88.05 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 17.15 | 92.27 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 18.27 | 86.19 |
