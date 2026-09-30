# 50-Question GPQA Diamond Report: Exp 31: Physical Core Pinning (Anti-SMT) + Confidence-Gated Speculative Diffusion (DFlash n_max=4, p_min=0.45 + Q4_0 KV + SER 2,0.5)

- **Experiment ID:** `exp31_phys_pinning_dflash_nmax4_q4kv`
- **Total Score (50Q):** **14 / 50 (28.0%)**
- **Standard 20Q Subset:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`19.92 tokens/second`**
- **Peak Generation Speed:** **`29.91 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 18.56 | 85.03 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 22.06 | 71.57 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 25.77 | 60.98 |
| 4 | `gpqa_156` | A | A | CORRECT | 906 | 17.52 | 53.27 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 18.93 | 83.19 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 17.42 | 90.66 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 22.71 | 68.90 |
| 8 | `gpqa_13` | B | C | WRONG | 1536 | 15.30 | 101.97 |
| 9 | `gpqa_127` | D | D | CORRECT | 1536 | 29.91 | 65.01 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 20.23 | 77.36 |
| 11 | `gpqa_3` | C | B | WRONG | 1536 | 20.99 | 74.58 |
| 12 | `gpqa_185` | A | C | WRONG | 1536 | 17.86 | 87.54 |
| 13 | `gpqa_30` | B | C | WRONG | 1536 | 18.59 | 84.04 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 17.35 | 93.19 |
| 15 | `gpqa_169` | C | None | WRONG | 3 | 9.95 | 1.78 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 18.78 | 83.35 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 21.86 | 71.91 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 18.49 | 84.55 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 20.59 | 76.86 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 22.22 | 70.57 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 25.99 | 60.79 |
| 22 | `gpqa_53` | B | None | WRONG | 1536 | 19.62 | 79.77 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 22.22 | 71.22 |
| 24 | `gpqa_80` | D | C | WRONG | 1536 | 16.41 | 95.37 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 17.26 | 91.14 |
| 26 | `gpqa_73` | D | D | CORRECT | 918 | 23.08 | 41.23 |
| 27 | `gpqa_37` | A | B | WRONG | 1536 | 18.28 | 86.07 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 17.33 | 90.10 |
| 29 | `gpqa_122` | B | B | CORRECT | 1536 | 23.04 | 68.39 |
| 30 | `gpqa_78` | A | C | WRONG | 1536 | 19.73 | 80.44 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 17.72 | 88.78 |
| 32 | `gpqa_66` | C | A | WRONG | 1536 | 24.12 | 65.34 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 18.32 | 84.95 |
| 34 | `gpqa_184` | C | C | CORRECT | 1536 | 24.71 | 63.71 |
| 35 | `gpqa_32` | B | C | WRONG | 1536 | 18.11 | 86.76 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.19 | 81.92 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 21.66 | 72.31 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 18.23 | 85.78 |
| 39 | `gpqa_10` | B | A | WRONG | 1217 | 16.55 | 76.07 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 16.69 | 93.87 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 18.68 | 84.19 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 16.67 | 93.52 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 20.06 | 78.63 |
| 44 | `gpqa_103` | B | B | CORRECT | 1536 | 21.54 | 73.00 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 27.85 | 57.09 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 22.97 | 68.37 |
| 47 | `gpqa_144` | C | None | WRONG | 1536 | 20.43 | 76.23 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 18.10 | 86.51 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 18.20 | 87.10 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 17.93 | 87.66 |
