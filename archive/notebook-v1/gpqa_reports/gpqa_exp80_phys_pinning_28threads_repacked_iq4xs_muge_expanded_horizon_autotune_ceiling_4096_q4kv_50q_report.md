# 50-Question GPQA Diamond Report: Exp 80: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Horizon-Expanded Autotuned Speculation (n_max=5, match=4, depth=36) + Calibrated MTP (p=0.10) + 4K Ceiling

- **Experiment ID:** `exp80_phys_pinning_28threads_repacked_iq4xs_muge_expanded_horizon_autotune_ceiling_4096_q4kv`
- **Total Score (50Q):** **8 / 50 (16.0%)**
- **Standard 20Q Subset:** **4 / 20 (20.0%)**
- **Average Generation Speed:** **`21.56 tokens/second`**
- **Peak Generation Speed:** **`36.70 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 19.43 | 213.52 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 21.28 | 194.39 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 21.28 | 194.10 |
| 4 | `gpqa_156` | A | A | CORRECT | 2192 | 19.96 | 111.45 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 21.14 | 195.78 |
| 6 | `gpqa_12` | D | A | WRONG | 4096 | 18.21 | 227.67 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 34.46 | 120.15 |
| 8 | `gpqa_13` | B | B | CORRECT | 1206 | 19.68 | 62.56 |
| 9 | `gpqa_127` | D | A | WRONG | 1616 | 24.72 | 81.88 |
| 10 | `gpqa_69` | C | None | WRONG | 4096 | 33.99 | 122.21 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 20.38 | 202.71 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 24.38 | 169.64 |
| 13 | `gpqa_30` | B | D | WRONG | 4096 | 19.26 | 214.18 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 22.23 | 189.61 |
| 15 | `gpqa_169` | C | C | CORRECT | 2664 | 23.44 | 115.12 |
| 16 | `gpqa_15` | D | None | WRONG | 4096 | 19.18 | 215.31 |
| 17 | `gpqa_159` | A | None | WRONG | 4096 | 19.37 | 430.74 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 19.00 | 217.03 |
| 19 | `gpqa_134` | D | None | WRONG | 4096 | 20.97 | 197.80 |
| 20 | `gpqa_44` | C | None | WRONG | 4096 | 19.95 | 206.93 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 24.49 | 169.10 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 21.95 | 188.15 |
| 23 | `gpqa_84` | B | None | WRONG | 4096 | 20.12 | 205.96 |
| 24 | `gpqa_80` | D | None | WRONG | 4096 | 21.67 | 190.85 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 18.62 | 222.11 |
| 26 | `gpqa_73` | D | D | CORRECT | 1405 | 20.13 | 71.25 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 19.70 | 210.09 |
| 28 | `gpqa_126` | B | A | WRONG | 4096 | 19.04 | 216.55 |
| 29 | `gpqa_122` | B | None | WRONG | 4096 | 20.37 | 202.88 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 19.03 | 218.01 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 19.64 | 210.82 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 20.17 | 205.08 |
| 33 | `gpqa_45` | C | None | WRONG | 4096 | 20.13 | 204.71 |
| 34 | `gpqa_184` | C | C | CORRECT | 868 | 22.02 | 40.99 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 32.11 | 129.70 |
| 36 | `gpqa_52` | D | None | WRONG | 4096 | 18.28 | 226.03 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 19.98 | 206.63 |
| 38 | `gpqa_174` | B | None | WRONG | 4096 | 18.46 | 223.75 |
| 39 | `gpqa_10` | B | B | CORRECT | 2996 | 19.76 | 154.36 |
| 40 | `gpqa_60` | D | D | CORRECT | 4096 | 18.06 | 228.58 |
| 41 | `gpqa_170` | C | None | WRONG | 3 | 36.70 | 461.37 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 17.51 | 235.19 |
| 43 | `gpqa_131` | A | B | WRONG | 4096 | 18.86 | 219.38 |
| 44 | `gpqa_103` | B | A | WRONG | 1845 | 19.42 | 96.76 |
| 45 | `gpqa_193` | D | None | WRONG | 4096 | 19.64 | 210.42 |
| 46 | `gpqa_95` | D | None | WRONG | 4096 | 19.07 | 216.23 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 21.54 | 191.29 |
| 48 | `gpqa_100` | D | B | WRONG | 4096 | 18.51 | 223.15 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 24.23 | 171.98 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 26.73 | 155.30 |
