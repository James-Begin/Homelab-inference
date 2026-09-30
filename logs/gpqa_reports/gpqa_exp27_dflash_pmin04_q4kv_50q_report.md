# 50-Question GPQA Diamond Report: Exp 27: Confidence-Filtered Speculative Diffusion (DFlash n_max=3, p_min=0.4 + Q4_0 KV Cache + SER 2,0.5)

- **Experiment ID:** `exp27_dflash_pmin04_q4kv`
- **Total Score (50Q):** **16 / 50 (32.0%)**
- **Standard 20Q Subset:** **10 / 20 (50.0%)**
- **Average Generation Speed:** **`19.57 tokens/second`**
- **Peak Generation Speed:** **`24.57 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 18.52 | 85.17 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.15 | 74.58 |
| 3 | `gpqa_2` | B | A | WRONG | 1536 | 24.23 | 64.83 |
| 4 | `gpqa_156` | A | A | CORRECT | 779 | 17.71 | 45.65 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 18.87 | 83.34 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 17.43 | 90.60 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 21.54 | 72.54 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 17.21 | 90.52 |
| 9 | `gpqa_127` | D | None | WRONG | 1536 | 16.45 | 106.74 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 19.51 | 80.43 |
| 11 | `gpqa_3` | C | C | CORRECT | 1425 | 18.80 | 77.14 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 17.02 | 91.90 |
| 13 | `gpqa_30` | B | A | WRONG | 1536 | 18.83 | 83.00 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 18.11 | 89.54 |
| 15 | `gpqa_169` | C | C | CORRECT | 1136 | 24.57 | 47.80 |
| 16 | `gpqa_15` | D | C | WRONG | 1536 | 18.42 | 84.88 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 20.18 | 77.59 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 18.49 | 84.41 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 19.69 | 80.30 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 21.59 | 72.80 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 23.57 | 66.68 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 18.89 | 82.99 |
| 23 | `gpqa_84` | B | None | WRONG | 1536 | 19.18 | 82.02 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 16.86 | 93.09 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 17.20 | 91.30 |
| 26 | `gpqa_73` | D | D | CORRECT | 1220 | 22.44 | 55.94 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 17.39 | 90.23 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 18.35 | 85.22 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 22.38 | 70.40 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 18.92 | 83.49 |
| 31 | `gpqa_160` | A | B | WRONG | 1536 | 19.14 | 82.29 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 22.60 | 69.87 |
| 33 | `gpqa_45` | C | A | WRONG | 1536 | 18.97 | 82.08 |
| 34 | `gpqa_184` | C | A | WRONG | 1536 | 23.60 | 66.74 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 17.88 | 88.03 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 18.90 | 82.96 |
| 37 | `gpqa_192` | C | C | CORRECT | 779 | 23.05 | 35.04 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 19.53 | 80.23 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 16.92 | 93.42 |
| 40 | `gpqa_60` | D | None | WRONG | 3 | 18.53 | 2.00 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 18.40 | 85.19 |
| 42 | `gpqa_47` | A | None | WRONG | 1536 | 17.01 | 91.84 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 19.93 | 79.15 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 18.99 | 82.79 |
| 45 | `gpqa_193` | D | A | WRONG | 1536 | 24.19 | 65.39 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 21.50 | 72.79 |
| 47 | `gpqa_144` | C | None | WRONG | 3 | 20.54 | 1.31 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.09 | 82.05 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 18.36 | 86.16 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 17.75 | 88.59 |
