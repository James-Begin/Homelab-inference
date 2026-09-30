# 50-Question GPQA Diamond Report: Exp 38: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Dynamic Suffix-Tree Speculation (n_max=8, match=4, depth=32) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp38_phys_pinning_28threads_suffix_spec_q4kv`
- **Total Score (50Q):** **16 / 50 (32.0%)**
- **Standard 20Q Subset:** **10 / 20 (50.0%)**
- **Average Generation Speed:** **`20.75 tokens/second`**
- **Peak Generation Speed:** **`48.88 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 19.33 | 82.16 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 18.08 | 86.93 |
| 3 | `gpqa_2` | B | None | WRONG | 1536 | 20.16 | 77.69 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 18.50 | 84.86 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 20.39 | 77.77 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 35.55 | 45.73 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.38 | 76.63 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 17.86 | 87.64 |
| 9 | `gpqa_127` | D | None | WRONG | 1536 | 38.48 | 57.37 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 17.97 | 87.32 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 19.80 | 78.98 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 19.43 | 80.70 |
| 13 | `gpqa_30` | B | C | WRONG | 1536 | 17.80 | 87.80 |
| 14 | `gpqa_165` | C | C | CORRECT | 1536 | 19.46 | 84.22 |
| 15 | `gpqa_169` | C | C | CORRECT | 1299 | 20.02 | 66.45 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 18.36 | 85.44 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 17.84 | 87.81 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 18.39 | 85.07 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 17.97 | 87.96 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 17.54 | 89.26 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 21.41 | 73.55 |
| 22 | `gpqa_53` | B | None | WRONG | 1536 | 20.58 | 76.34 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 18.56 | 84.87 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 18.42 | 85.31 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 18.54 | 85.16 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 17.84 | 87.71 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 17.91 | 87.96 |
| 28 | `gpqa_126` | B | None | WRONG | 1536 | 21.02 | 74.54 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 18.40 | 85.34 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 19.82 | 80.13 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 17.03 | 92.38 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 19.16 | 82.08 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 17.44 | 89.17 |
| 34 | `gpqa_184` | C | A | WRONG | 1536 | 19.14 | 81.84 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 18.06 | 87.39 |
| 36 | `gpqa_52` | D | B | WRONG | 1536 | 17.28 | 90.82 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 48.88 | 32.94 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 17.52 | 89.50 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 19.81 | 80.40 |
| 40 | `gpqa_60` | D | None | WRONG | 3 | 36.08 | 1.82 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 17.45 | 89.80 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 16.77 | 93.17 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 19.68 | 80.35 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 18.47 | 85.26 |
| 45 | `gpqa_193` | D | A | WRONG | 1536 | 21.09 | 145.09 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 17.57 | 88.92 |
| 47 | `gpqa_144` | C | None | WRONG | 3 | 37.01 | 1.18 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 17.82 | 87.98 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 17.14 | 92.47 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 18.25 | 86.30 |
