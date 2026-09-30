# 50-Question GPQA Diamond Report: Exp 28: Window-Bounded Precision Chained Speculation (N=8, M=8, Hits=3) + Native MTP + Q4_0 KV Cache + SER 2,0.5

- **Experiment ID:** `exp28_window_chained_q4kv`
- **Total Score (50Q):** **16 / 50 (32.0%)**
- **Standard 20Q Subset:** **6 / 20 (30.0%)**
- **Average Generation Speed:** **`17.98 tokens/second`**
- **Peak Generation Speed:** **`21.15 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 17.80 | 89.33 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 19.86 | 79.62 |
| 3 | `gpqa_2` | B | None | WRONG | 1536 | 17.75 | 88.39 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 17.50 | 89.45 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 18.45 | 85.72 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 18.10 | 87.48 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 17.68 | 88.34 |
| 8 | `gpqa_13` | B | C | WRONG | 1536 | 16.70 | 93.51 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 15.06 | 119.88 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 17.70 | 88.64 |
| 11 | `gpqa_3` | C | B | WRONG | 1536 | 19.07 | 82.08 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 17.74 | 88.31 |
| 13 | `gpqa_30` | B | C | WRONG | 1536 | 18.15 | 86.23 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 17.91 | 91.07 |
| 15 | `gpqa_169` | C | A | WRONG | 1536 | 19.27 | 81.48 |
| 16 | `gpqa_15` | D | C | WRONG | 1536 | 19.11 | 82.17 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 18.58 | 84.64 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 18.55 | 84.53 |
| 19 | `gpqa_134` | D | C | WRONG | 1536 | 18.36 | 86.38 |
| 20 | `gpqa_44` | C | None | WRONG | 1536 | 19.24 | 81.69 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 19.11 | 82.12 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 18.28 | 85.76 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 19.77 | 79.98 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 17.47 | 90.15 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 18.10 | 87.25 |
| 26 | `gpqa_73` | D | D | CORRECT | 1241 | 19.09 | 66.85 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 17.59 | 89.91 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 17.99 | 86.99 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 18.82 | 83.55 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 18.67 | 85.13 |
| 31 | `gpqa_160` | A | B | WRONG | 1536 | 17.84 | 88.63 |
| 32 | `gpqa_66` | C | A | WRONG | 1536 | 18.94 | 83.28 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 17.79 | 87.64 |
| 34 | `gpqa_184` | C | C | CORRECT | 1536 | 17.10 | 91.67 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 16.60 | 94.88 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 16.74 | 93.90 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 17.82 | 87.78 |
| 38 | `gpqa_174` | B | B | CORRECT | 677 | 18.14 | 39.13 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 17.41 | 91.03 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 17.30 | 90.83 |
| 41 | `gpqa_170` | C | None | WRONG | 1536 | 16.78 | 93.51 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 16.82 | 93.21 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 17.99 | 88.01 |
| 44 | `gpqa_103` | B | B | CORRECT | 1536 | 18.57 | 84.76 |
| 45 | `gpqa_193` | D | A | WRONG | 1536 | 21.15 | 74.45 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 18.49 | 84.64 |
| 47 | `gpqa_144` | C | None | WRONG | 3 | 13.07 | 1.47 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 17.77 | 88.16 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 17.77 | 89.09 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 17.62 | 89.37 |
