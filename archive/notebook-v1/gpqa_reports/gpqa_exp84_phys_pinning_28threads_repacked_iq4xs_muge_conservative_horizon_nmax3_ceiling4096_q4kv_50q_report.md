# 50-Question GPQA Diamond Report: Exp 84: Conservative Draft Horizon (n_max=3, match=5, depth=24 + Spec Autotune + Persistent Slot 0.50 + MTP + 4K Ceiling)

- **Experiment ID:** `exp84_phys_pinning_28threads_repacked_iq4xs_muge_conservative_horizon_nmax3_ceiling4096_q4kv`
- **Total Score (50Q):** **7 / 50 (14.0%)**
- **Standard 20Q Subset:** **3 / 20 (15.0%)**
- **Average Generation Speed:** **`20.92 tokens/second`**
- **Peak Generation Speed:** **`30.97 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 20.42 | 203.22 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 21.31 | 194.29 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 21.60 | 191.27 |
| 4 | `gpqa_156` | A | A | CORRECT | 3423 | 19.64 | 176.18 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 22.01 | 188.10 |
| 6 | `gpqa_12` | D | C | WRONG | 4096 | 20.09 | 206.49 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 19.84 | 207.78 |
| 8 | `gpqa_13` | B | B | CORRECT | 1470 | 20.14 | 74.38 |
| 9 | `gpqa_127` | D | A | WRONG | 4096 | 20.41 | 217.37 |
| 10 | `gpqa_69` | C | None | WRONG | 4096 | 30.24 | 137.26 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 21.77 | 189.64 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 19.82 | 208.23 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 19.44 | 212.28 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 21.07 | 199.55 |
| 15 | `gpqa_169` | C | None | WRONG | 4096 | 24.43 | 169.37 |
| 16 | `gpqa_15` | D | C | WRONG | 4096 | 19.35 | 213.38 |
| 17 | `gpqa_159` | A | C | WRONG | 3684 | 20.05 | 185.52 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 19.97 | 206.56 |
| 19 | `gpqa_134` | D | A | WRONG | 1639 | 21.62 | 78.23 |
| 20 | `gpqa_44` | C | None | WRONG | 4096 | 20.74 | 199.10 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 21.87 | 189.24 |
| 22 | `gpqa_53` | B | A | WRONG | 4096 | 19.59 | 409.68 |
| 23 | `gpqa_84` | B | B | CORRECT | 3646 | 20.78 | 177.86 |
| 24 | `gpqa_80` | D | A | WRONG | 4096 | 20.56 | 201.08 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 19.23 | 215.46 |
| 26 | `gpqa_73` | D | None | WRONG | 4096 | 20.77 | 198.80 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 21.49 | 381.66 |
| 28 | `gpqa_126` | B | A | WRONG | 4096 | 20.78 | 198.68 |
| 29 | `gpqa_122` | B | B | CORRECT | 2805 | 21.17 | 134.58 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 19.79 | 209.57 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 19.99 | 207.08 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 21.97 | 188.35 |
| 33 | `gpqa_45` | C | A | WRONG | 4096 | 20.70 | 199.13 |
| 34 | `gpqa_184` | C | None | WRONG | 4096 | 20.99 | 196.73 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 21.10 | 196.68 |
| 36 | `gpqa_52` | D | A | WRONG | 4096 | 19.34 | 213.61 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 20.02 | 206.01 |
| 38 | `gpqa_174` | B | None | WRONG | 4096 | 19.68 | 210.08 |
| 39 | `gpqa_10` | B | None | WRONG | 4096 | 19.98 | 207.78 |
| 40 | `gpqa_60` | D | A | WRONG | 3059 | 20.10 | 153.98 |
| 41 | `gpqa_170` | C | A | WRONG | 4096 | 19.53 | 211.57 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 19.63 | 210.16 |
| 43 | `gpqa_131` | A | None | WRONG | 4096 | 20.06 | 206.42 |
| 44 | `gpqa_103` | B | B | CORRECT | 2451 | 21.12 | 117.96 |
| 45 | `gpqa_193` | D | None | WRONG | 2 | 30.97 | 1.82 |
| 46 | `gpqa_95` | D | D | CORRECT | 2880 | 20.76 | 140.28 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 20.43 | 201.93 |
| 48 | `gpqa_100` | D | A | WRONG | 4096 | 19.88 | 207.85 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 20.10 | 206.38 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 19.89 | 207.98 |
