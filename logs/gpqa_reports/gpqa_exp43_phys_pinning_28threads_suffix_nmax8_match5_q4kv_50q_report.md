# 50-Question GPQA Diamond Report: Exp 43: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Calibrated Precision Suffix Speculation (n_max=8, match=5, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp43_phys_pinning_28threads_suffix_nmax8_match5_q4kv`
- **Total Score (50Q):** **17 / 50 (34.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`20.04 tokens/second`**
- **Peak Generation Speed:** **`36.62 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 18.09 | 88.57 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 17.54 | 90.05 |
| 3 | `gpqa_2` | B | C | WRONG | 1536 | 18.20 | 86.25 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 17.18 | 91.51 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 20.06 | 78.87 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 19.39 | 81.93 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 17.45 | 89.36 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 16.72 | 93.51 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 31.10 | 66.77 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 18.71 | 167.86 |
| 11 | `gpqa_3` | C | C | CORRECT | 1536 | 20.26 | 77.17 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 19.27 | 81.62 |
| 13 | `gpqa_30` | B | A | WRONG | 1536 | 18.95 | 82.67 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 18.40 | 88.85 |
| 15 | `gpqa_169` | C | C | CORRECT | 1526 | 21.16 | 73.71 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 18.70 | 83.88 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 18.98 | 82.58 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 18.12 | 86.20 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 19.42 | 81.65 |
| 20 | `gpqa_44` | C | None | WRONG | 1536 | 18.88 | 82.98 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 20.54 | 76.52 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 18.59 | 84.30 |
| 23 | `gpqa_84` | B | None | WRONG | 1536 | 19.40 | 81.30 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 21.27 | 74.05 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 19.29 | 81.95 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 18.56 | 84.38 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 19.19 | 82.41 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 20.93 | 74.86 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 19.73 | 79.67 |
| 30 | `gpqa_78` | A | C | WRONG | 1536 | 19.00 | 162.39 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 18.48 | 85.52 |
| 32 | `gpqa_66` | C | A | WRONG | 1536 | 20.14 | 78.36 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 19.67 | 79.26 |
| 34 | `gpqa_184` | C | B | WRONG | 1536 | 20.36 | 77.04 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 18.22 | 86.58 |
| 36 | `gpqa_52` | D | D | CORRECT | 1536 | 18.84 | 83.37 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 18.84 | 82.99 |
| 38 | `gpqa_174` | B | D | WRONG | 954 | 18.28 | 54.04 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 19.90 | 79.81 |
| 40 | `gpqa_60` | D | None | WRONG | 3 | 36.23 | 2.04 |
| 41 | `gpqa_170` | C | C | CORRECT | 1536 | 19.38 | 165.74 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 19.19 | 81.47 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 19.72 | 80.14 |
| 44 | `gpqa_103` | B | B | CORRECT | 1536 | 19.80 | 79.69 |
| 45 | `gpqa_193` | D | A | WRONG | 1536 | 20.25 | 77.88 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 19.10 | 82.02 |
| 47 | `gpqa_144` | C | None | WRONG | 3 | 36.62 | 1.29 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 18.30 | 85.87 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 18.95 | 83.74 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 18.72 | 84.06 |
