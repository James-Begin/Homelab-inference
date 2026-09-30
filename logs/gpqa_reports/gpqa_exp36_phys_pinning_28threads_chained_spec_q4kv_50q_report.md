# 50-Question GPQA Diamond Report: Exp 36: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Window Chained Spec (N=8, M=12, hits=2) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp36_phys_pinning_28threads_chained_spec_q4kv`
- **Total Score (50Q):** **17 / 50 (34.0%)**
- **Standard 20Q Subset:** **11 / 20 (55.0%)**
- **Average Generation Speed:** **`20.41 tokens/second`**
- **Peak Generation Speed:** **`23.81 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 20.43 | 77.90 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 20.82 | 75.73 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 22.22 | 70.69 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 20.25 | 77.52 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 19.94 | 79.20 |
| 6 | `gpqa_12` | D | A | WRONG | 1536 | 19.89 | 79.87 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.67 | 75.65 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 20.39 | 76.59 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 17.21 | 106.62 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 19.42 | 80.66 |
| 11 | `gpqa_3` | C | None | WRONG | 12 | 13.35 | 2.40 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 20.36 | 77.15 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 19.86 | 78.85 |
| 14 | `gpqa_165` | C | C | CORRECT | 1536 | 23.09 | 71.90 |
| 15 | `gpqa_169` | C | C | CORRECT | 1536 | 21.17 | 73.96 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 20.39 | 77.08 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 20.48 | 76.65 |
| 18 | `gpqa_36` | B | A | WRONG | 14 | 14.29 | 2.58 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 21.07 | 75.54 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 21.86 | 71.87 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 22.17 | 71.25 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 20.78 | 75.53 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 20.70 | 76.58 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 19.77 | 79.60 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.24 | 78.10 |
| 26 | `gpqa_73` | D | A | WRONG | 1536 | 21.33 | 73.81 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 21.06 | 74.96 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 23.81 | 65.87 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 20.58 | 76.53 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.21 | 78.47 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 20.21 | 78.26 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 21.31 | 74.08 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 20.48 | 76.20 |
| 34 | `gpqa_184` | C | C | CORRECT | 1536 | 20.46 | 76.66 |
| 35 | `gpqa_32` | B | B | CORRECT | 1536 | 18.95 | 83.49 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.26 | 81.57 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 20.85 | 75.17 |
| 38 | `gpqa_174` | B | D | WRONG | 1536 | 19.79 | 79.28 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 21.98 | 72.75 |
| 40 | `gpqa_60` | D | None | WRONG | 3 | 21.32 | 1.89 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 19.98 | 78.63 |
| 42 | `gpqa_47` | A | None | WRONG | 1536 | 19.68 | 79.74 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 21.22 | 74.70 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 20.13 | 78.03 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 20.67 | 76.18 |
| 46 | `gpqa_95` | D | None | WRONG | 1536 | 23.43 | 67.00 |
| 47 | `gpqa_144` | C | None | WRONG | 1536 | 21.61 | 72.17 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 20.41 | 77.05 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 20.75 | 76.88 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 20.44 | 77.25 |
