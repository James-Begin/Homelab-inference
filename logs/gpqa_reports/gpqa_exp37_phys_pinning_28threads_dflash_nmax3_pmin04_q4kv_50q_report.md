# 50-Question GPQA Diamond Report: Exp 37: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Calibrated Speculative Diffusion (DFlash n_max=3, p_min=0.40 + Q4_0 KV + SER 2,0.5)

- **Experiment ID:** `exp37_phys_pinning_28threads_dflash_nmax3_pmin04_q4kv`
- **Total Score (50Q):** **16 / 50 (32.0%)**
- **Standard 20Q Subset:** **10 / 20 (50.0%)**
- **Average Generation Speed:** **`20.11 tokens/second`**
- **Peak Generation Speed:** **`25.27 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 18.87 | 83.84 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.56 | 73.08 |
| 3 | `gpqa_2` | B | A | WRONG | 1536 | 24.94 | 62.95 |
| 4 | `gpqa_156` | A | A | CORRECT | 779 | 18.23 | 44.32 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 19.52 | 80.53 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 17.91 | 87.92 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 21.84 | 71.54 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 17.40 | 89.56 |
| 9 | `gpqa_127` | D | None | WRONG | 1536 | 16.72 | 105.22 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 19.88 | 78.96 |
| 11 | `gpqa_3` | C | C | CORRECT | 1425 | 19.16 | 75.83 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 17.37 | 89.91 |
| 13 | `gpqa_30` | B | A | WRONG | 1536 | 19.17 | 81.40 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 18.36 | 88.53 |
| 15 | `gpqa_169` | C | C | CORRECT | 1136 | 25.27 | 46.43 |
| 16 | `gpqa_15` | D | C | WRONG | 1536 | 18.96 | 82.69 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 20.76 | 75.47 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 19.03 | 82.04 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 20.25 | 78.07 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 22.30 | 70.22 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 24.37 | 64.81 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 19.56 | 80.07 |
| 23 | `gpqa_84` | B | None | WRONG | 1536 | 19.90 | 79.15 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 17.53 | 89.23 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 17.82 | 88.14 |
| 26 | `gpqa_73` | D | D | CORRECT | 1220 | 23.25 | 54.08 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 18.02 | 87.30 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 19.02 | 82.12 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 22.80 | 69.15 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 19.24 | 82.25 |
| 31 | `gpqa_160` | A | B | WRONG | 1536 | 19.50 | 80.84 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 23.06 | 68.28 |
| 33 | `gpqa_45` | C | A | WRONG | 1536 | 19.31 | 80.74 |
| 34 | `gpqa_184` | C | A | WRONG | 1536 | 24.03 | 65.31 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 18.28 | 86.34 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.61 | 79.94 |
| 37 | `gpqa_192` | C | C | CORRECT | 779 | 23.86 | 33.87 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 20.23 | 77.53 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 17.51 | 90.06 |
| 40 | `gpqa_60` | D | None | WRONG | 3 | 19.54 | 1.73 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 19.01 | 82.56 |
| 42 | `gpqa_47` | A | None | WRONG | 1536 | 17.40 | 89.72 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 20.39 | 77.29 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 19.40 | 80.95 |
| 45 | `gpqa_193` | D | A | WRONG | 1536 | 24.87 | 63.65 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 22.13 | 70.78 |
| 47 | `gpqa_144` | C | None | WRONG | 3 | 21.56 | 1.28 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.63 | 79.87 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 18.91 | 83.93 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 18.12 | 86.71 |
