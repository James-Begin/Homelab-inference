# 50-Question GPQA Diamond Report: Exp 76: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Concise Reasoning Steering (600 Words) + Spec Autotune + Constrained Suffix (n_max=4) + MTP (p=0.15) + 4K Ceiling

- **Experiment ID:** `exp76_phys_pinning_28threads_repacked_iq4xs_muge_concise_steering_autotune_expanded_ceiling_4096_q4kv`
- **Total Score (50Q):** **11 / 50 (22.0%)**
- **Standard 20Q Subset:** **2 / 20 (10.0%)**
- **Average Generation Speed:** **`21.81 tokens/second`**
- **Peak Generation Speed:** **`36.92 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | B | WRONG | 4096 | 20.00 | 415.19 |
| 2 | `gpqa_42` | A | A | CORRECT | 4096 | 21.00 | 197.09 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 21.71 | 190.25 |
| 4 | `gpqa_156` | A | D | WRONG | 660 | 21.13 | 33.08 |
| 5 | `gpqa_128` | A | A | CORRECT | 4096 | 20.03 | 206.66 |
| 6 | `gpqa_12` | D | None | WRONG | 4096 | 36.92 | 113.22 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 28.11 | 147.28 |
| 8 | `gpqa_13` | B | None | WRONG | 4096 | 19.29 | 213.63 |
| 9 | `gpqa_127` | D | None | WRONG | 4096 | 36.61 | 254.96 |
| 10 | `gpqa_69` | C | None | WRONG | 4096 | 31.44 | 132.21 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 21.67 | 190.53 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 25.50 | 162.37 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 19.80 | 397.72 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 20.37 | 206.34 |
| 15 | `gpqa_169` | C | None | WRONG | 4096 | 22.05 | 187.44 |
| 16 | `gpqa_15` | D | None | WRONG | 4096 | 20.29 | 204.03 |
| 17 | `gpqa_159` | A | B | WRONG | 3168 | 20.78 | 154.45 |
| 18 | `gpqa_36` | B | C | WRONG | 4096 | 25.71 | 161.06 |
| 19 | `gpqa_134` | D | A | WRONG | 1333 | 20.77 | 66.94 |
| 20 | `gpqa_44` | C | None | WRONG | 4096 | 21.91 | 188.66 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 23.22 | 178.15 |
| 22 | `gpqa_53` | B | A | WRONG | 4096 | 20.81 | 198.67 |
| 23 | `gpqa_84` | B | B | CORRECT | 2703 | 21.06 | 130.75 |
| 24 | `gpqa_80` | D | None | WRONG | 4096 | 21.28 | 194.34 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 25.12 | 165.32 |
| 26 | `gpqa_73` | D | D | CORRECT | 3407 | 22.27 | 154.81 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 22.17 | 186.89 |
| 28 | `gpqa_126` | B | None | WRONG | 4096 | 20.07 | 205.61 |
| 29 | `gpqa_122` | B | None | WRONG | 4096 | 20.59 | 200.92 |
| 30 | `gpqa_78` | A | A | CORRECT | 4096 | 19.62 | 211.46 |
| 31 | `gpqa_160` | A | A | CORRECT | 3777 | 19.44 | 196.70 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 20.30 | 203.79 |
| 33 | `gpqa_45` | C | C | CORRECT | 3634 | 19.54 | 187.27 |
| 34 | `gpqa_184` | C | None | WRONG | 4096 | 20.96 | 197.21 |
| 35 | `gpqa_32` | B | B | CORRECT | 4096 | 19.82 | 209.23 |
| 36 | `gpqa_52` | D | A | WRONG | 4096 | 18.83 | 219.45 |
| 37 | `gpqa_192` | C | C | CORRECT | 3630 | 21.95 | 166.76 |
| 38 | `gpqa_174` | B | A | WRONG | 2216 | 19.85 | 113.55 |
| 39 | `gpqa_10` | B | A | WRONG | 3301 | 19.81 | 169.31 |
| 40 | `gpqa_60` | D | None | WRONG | 4096 | 19.36 | 213.70 |
| 41 | `gpqa_170` | C | None | WRONG | 4096 | 19.11 | 216.36 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 19.34 | 213.49 |
| 43 | `gpqa_131` | A | None | WRONG | 4096 | 20.68 | 200.60 |
| 44 | `gpqa_103` | B | B | CORRECT | 2065 | 21.54 | 97.78 |
| 45 | `gpqa_193` | D | D | CORRECT | 1871 | 22.90 | 83.69 |
| 46 | `gpqa_95` | D | None | WRONG | 10 | 16.68 | 2.15 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 19.33 | 213.18 |
| 48 | `gpqa_100` | D | None | WRONG | 4096 | 19.96 | 207.27 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 19.89 | 208.64 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 19.94 | 207.47 |
