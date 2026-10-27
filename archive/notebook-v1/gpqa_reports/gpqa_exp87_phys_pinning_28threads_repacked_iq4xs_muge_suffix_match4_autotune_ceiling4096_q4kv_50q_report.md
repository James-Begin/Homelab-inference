# 50-Question GPQA Diamond Report: Exp 87: High-Frequency Suffix Speculation (match_len=4, n_max=4, depth=32 + Spec Autotune + Persistent Slot 0.50 + MTP + 4K Ceiling)

- **Experiment ID:** `exp87_phys_pinning_28threads_repacked_iq4xs_muge_suffix_match4_autotune_ceiling4096_q4kv`
- **Total Score (50Q):** **7 / 50 (14.0%)**
- **Standard 20Q Subset:** **3 / 20 (15.0%)**
- **Average Generation Speed:** **`20.74 tokens/second`**
- **Peak Generation Speed:** **`35.12 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 19.57 | 212.02 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 20.72 | 199.75 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 21.69 | 190.46 |
| 4 | `gpqa_156` | A | A | CORRECT | 3204 | 20.26 | 159.82 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 25.16 | 165.02 |
| 6 | `gpqa_12` | D | C | WRONG | 4096 | 22.79 | 182.32 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 19.55 | 210.90 |
| 8 | `gpqa_13` | B | C | WRONG | 1637 | 18.90 | 87.96 |
| 9 | `gpqa_127` | D | D | CORRECT | 4096 | 35.12 | 133.14 |
| 10 | `gpqa_69` | C | None | WRONG | 4096 | 28.83 | 143.94 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 21.02 | 196.22 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 21.26 | 194.52 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 19.24 | 214.47 |
| 14 | `gpqa_165` | C | A | WRONG | 3701 | 19.14 | 198.53 |
| 15 | `gpqa_169` | C | None | WRONG | 4096 | 21.64 | 190.90 |
| 16 | `gpqa_15` | D | C | WRONG | 4096 | 19.24 | 214.74 |
| 17 | `gpqa_159` | A | B | WRONG | 4096 | 19.84 | 432.46 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 18.93 | 217.99 |
| 19 | `gpqa_134` | D | A | WRONG | 1393 | 20.65 | 70.02 |
| 20 | `gpqa_44` | C | None | WRONG | 4096 | 19.63 | 210.26 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 21.07 | 196.27 |
| 22 | `gpqa_53` | B | A | WRONG | 4096 | 18.58 | 222.14 |
| 23 | `gpqa_84` | B | B | CORRECT | 2816 | 20.11 | 142.08 |
| 24 | `gpqa_80` | D | None | WRONG | 4096 | 22.70 | 182.36 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 19.91 | 207.73 |
| 26 | `gpqa_73` | D | None | WRONG | 4096 | 20.43 | 202.31 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 20.50 | 201.77 |
| 28 | `gpqa_126` | B | None | WRONG | 4096 | 19.28 | 214.01 |
| 29 | `gpqa_122` | B | B | CORRECT | 4096 | 19.34 | 213.88 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 19.16 | 216.74 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 19.09 | 216.75 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 20.30 | 367.91 |
| 33 | `gpqa_45` | C | None | WRONG | 4096 | 19.14 | 215.38 |
| 34 | `gpqa_184` | C | None | WRONG | 4096 | 20.22 | 204.13 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 20.15 | 205.55 |
| 36 | `gpqa_52` | D | A | WRONG | 4096 | 17.90 | 230.87 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 19.87 | 207.43 |
| 38 | `gpqa_174` | B | None | WRONG | 4096 | 18.17 | 227.17 |
| 39 | `gpqa_10` | B | B | CORRECT | 3611 | 20.26 | 181.11 |
| 40 | `gpqa_60` | D | A | WRONG | 4096 | 18.58 | 222.39 |
| 41 | `gpqa_170` | C | B | WRONG | 4096 | 18.98 | 217.82 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 18.33 | 224.93 |
| 43 | `gpqa_131` | A | None | WRONG | 4096 | 19.17 | 215.81 |
| 44 | `gpqa_103` | B | B | CORRECT | 2766 | 20.97 | 133.97 |
| 45 | `gpqa_193` | D | None | WRONG | 2 | 30.35 | 1.98 |
| 46 | `gpqa_95` | D | A | WRONG | 4096 | 19.38 | 212.79 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 18.34 | 224.55 |
| 48 | `gpqa_100` | D | A | WRONG | 4096 | 18.49 | 223.13 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 25.73 | 162.11 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 19.23 | 215.07 |
