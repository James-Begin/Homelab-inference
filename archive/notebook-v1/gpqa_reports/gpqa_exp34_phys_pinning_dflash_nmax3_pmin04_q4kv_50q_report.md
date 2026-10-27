# 50-Question GPQA Diamond Report: Exp 34: Physical Core Pinning (Anti-SMT) + Calibrated Speculative Diffusion (DFlash n_max=3, p_min=0.40 + Q4_0 KV + SER 2,0.5)

- **Experiment ID:** `exp34_phys_pinning_dflash_nmax3_pmin04_q4kv`
- **Total Score (50Q):** **16 / 50 (32.0%)**
- **Standard 20Q Subset:** **10 / 20 (50.0%)**
- **Average Generation Speed:** **`19.90 tokens/second`**
- **Peak Generation Speed:** **`25.18 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 18.89 | 83.47 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.22 | 74.20 |
| 3 | `gpqa_2` | B | A | WRONG | 1536 | 24.91 | 63.27 |
| 4 | `gpqa_156` | A | A | CORRECT | 779 | 18.20 | 44.31 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 19.39 | 81.22 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 18.00 | 87.54 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 21.99 | 71.23 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 17.51 | 89.13 |
| 9 | `gpqa_127` | D | None | WRONG | 1536 | 16.57 | 106.03 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 19.75 | 79.22 |
| 11 | `gpqa_3` | C | C | CORRECT | 1425 | 18.99 | 76.37 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 17.17 | 90.96 |
| 13 | `gpqa_30` | B | A | WRONG | 1536 | 19.00 | 82.14 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 18.32 | 88.64 |
| 15 | `gpqa_169` | C | C | CORRECT | 1136 | 25.18 | 46.70 |
| 16 | `gpqa_15` | D | C | WRONG | 1536 | 18.88 | 82.89 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 20.68 | 75.82 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 18.94 | 82.55 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 20.20 | 78.41 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 21.96 | 71.60 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 24.00 | 65.71 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 19.22 | 81.33 |
| 23 | `gpqa_84` | B | None | WRONG | 1536 | 19.53 | 80.68 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 17.21 | 90.93 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 17.50 | 89.66 |
| 26 | `gpqa_73` | D | D | CORRECT | 1220 | 22.88 | 54.82 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 17.73 | 88.68 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 18.73 | 83.39 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 22.40 | 70.50 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 18.98 | 83.24 |
| 31 | `gpqa_160` | A | B | WRONG | 1536 | 19.20 | 82.16 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 22.71 | 69.37 |
| 33 | `gpqa_45` | C | A | WRONG | 1536 | 18.99 | 82.06 |
| 34 | `gpqa_184` | C | A | WRONG | 1536 | 23.86 | 66.01 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 18.08 | 87.14 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.49 | 80.57 |
| 37 | `gpqa_192` | C | C | CORRECT | 779 | 23.67 | 34.14 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 20.09 | 78.24 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 17.40 | 90.68 |
| 40 | `gpqa_60` | D | None | WRONG | 3 | 18.81 | 2.06 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 18.69 | 83.94 |
| 42 | `gpqa_47` | A | None | WRONG | 1536 | 17.14 | 91.09 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 20.06 | 78.69 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 19.11 | 82.10 |
| 45 | `gpqa_193` | D | A | WRONG | 1536 | 24.81 | 63.67 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 21.80 | 71.98 |
| 47 | `gpqa_144` | C | None | WRONG | 3 | 21.22 | 1.29 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.33 | 81.22 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 18.64 | 85.09 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 17.93 | 87.65 |
