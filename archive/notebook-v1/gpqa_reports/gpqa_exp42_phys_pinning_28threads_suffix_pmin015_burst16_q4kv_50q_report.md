# 50-Question GPQA Diamond Report: Exp 42: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Confidence-Gated Suffix Speculation (n_max=16, p_min=0.15, match=4, depth=64) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp42_phys_pinning_28threads_suffix_pmin015_burst16_q4kv`
- **Total Score (50Q):** **14 / 50 (28.0%)**
- **Standard 20Q Subset:** **6 / 20 (30.0%)**
- **Average Generation Speed:** **`18.84 tokens/second`**
- **Peak Generation Speed:** **`66.30 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 18.08 | 87.71 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 16.61 | 94.48 |
| 3 | `gpqa_2` | B | A | WRONG | 1536 | 20.03 | 78.28 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 18.04 | 86.83 |
| 5 | `gpqa_128` | A | None | WRONG | 1536 | 66.30 | 25.38 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 27.02 | 59.37 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 17.01 | 91.65 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 16.63 | 93.76 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 16.16 | 111.97 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 16.72 | 93.45 |
| 11 | `gpqa_3` | C | B | WRONG | 1536 | 17.84 | 87.52 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 18.15 | 86.32 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 17.39 | 89.81 |
| 14 | `gpqa_165` | C | B | WRONG | 1536 | 16.74 | 97.12 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 18.93 | 82.74 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 16.93 | 92.53 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 16.84 | 92.93 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 17.72 | 88.26 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 18.26 | 86.72 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 16.26 | 96.14 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 19.89 | 78.89 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 16.00 | 97.69 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 17.93 | 87.62 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 17.63 | 89.21 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 17.16 | 91.78 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 17.60 | 89.02 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 16.32 | 96.33 |
| 28 | `gpqa_126` | B | None | WRONG | 1536 | 17.81 | 87.68 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 16.38 | 95.65 |
| 30 | `gpqa_78` | A | C | WRONG | 1536 | 18.68 | 85.00 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 15.93 | 98.63 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 16.61 | 94.31 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 15.72 | 98.92 |
| 34 | `gpqa_184` | C | A | WRONG | 1536 | 17.08 | 91.56 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 16.26 | 96.99 |
| 36 | `gpqa_52` | D | B | WRONG | 1536 | 16.44 | 95.38 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 16.58 | 94.18 |
| 38 | `gpqa_174` | B | B | CORRECT | 1536 | 16.24 | 96.46 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 18.87 | 84.09 |
| 40 | `gpqa_60` | D | None | WRONG | 3 | 25.16 | 1.95 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 17.29 | 90.67 |
| 42 | `gpqa_47` | A | C | WRONG | 1536 | 15.74 | 99.00 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 15.84 | 99.19 |
| 44 | `gpqa_103` | B | A | WRONG | 1536 | 19.62 | 80.28 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 17.84 | 87.80 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 16.12 | 96.92 |
| 47 | `gpqa_144` | C | None | WRONG | 3 | 31.37 | 1.27 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 15.80 | 98.99 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 16.86 | 93.70 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 17.52 | 89.80 |
