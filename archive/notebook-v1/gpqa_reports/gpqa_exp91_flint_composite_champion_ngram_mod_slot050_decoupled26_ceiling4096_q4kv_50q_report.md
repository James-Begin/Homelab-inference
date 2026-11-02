# 50-Question GPQA Diamond Report: Exp 91: Recursive Flint 40B MoE Composite Champion (N-Gram Mod Speculation n_max=4, match=4 + Persistent Slot Cache 0.50 + Decoupled Prefill -tb 26 + 4K Ceiling)

- **Experiment ID:** `exp91_flint_composite_champion_ngram_mod_slot050_decoupled26_ceiling4096_q4kv`
- **Total Score (50Q):** **20 / 50 (40.0%)**
- **Standard 20Q Subset:** **9 / 20 (45.0%)**
- **Average Generation Speed:** **`10.25 tokens/second`**
- **Peak Generation Speed:** **`19.52 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 9.89 | 417.07 |
| 2 | `gpqa_42` | A | A | CORRECT | 4096 | 9.61 | 428.22 |
| 3 | `gpqa_2` | B | B | CORRECT | 724 | 10.32 | 72.08 |
| 4 | `gpqa_156` | A | A | CORRECT | 392 | 10.61 | 38.89 |
| 5 | `gpqa_128` | A | B | WRONG | 4096 | 9.79 | 420.94 |
| 6 | `gpqa_12` | D | A | WRONG | 4096 | 9.45 | 436.10 |
| 7 | `gpqa_79` | D | A | WRONG | 4096 | 9.88 | 415.77 |
| 8 | `gpqa_13` | B | C | WRONG | 4096 | 9.56 | 429.91 |
| 9 | `gpqa_127` | D | A | WRONG | 4096 | 10.26 | 422.69 |
| 10 | `gpqa_69` | C | C | CORRECT | 4096 | 10.23 | 402.14 |
| 11 | `gpqa_3` | C | D | WRONG | 4096 | 10.26 | 400.81 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 9.97 | 412.57 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 9.96 | 412.87 |
| 14 | `gpqa_165` | C | C | CORRECT | 4096 | 10.60 | 393.60 |
| 15 | `gpqa_169` | C | C | CORRECT | 1281 | 10.60 | 122.37 |
| 16 | `gpqa_15` | D | None | WRONG | 4096 | 9.97 | 412.73 |
| 17 | `gpqa_159` | A | C | WRONG | 4096 | 9.46 | 435.28 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 9.65 | 426.10 |
| 19 | `gpqa_134` | D | D | CORRECT | 3255 | 11.42 | 287.91 |
| 20 | `gpqa_44` | C | C | CORRECT | 3370 | 9.49 | 356.98 |
| 21 | `gpqa_5` | C | C | CORRECT | 3487 | 10.96 | 320.22 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 9.61 | 428.14 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 9.98 | 412.99 |
| 24 | `gpqa_80` | D | A | WRONG | 4096 | 10.23 | 402.50 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 10.58 | 389.83 |
| 26 | `gpqa_73` | D | D | CORRECT | 2250 | 9.80 | 231.20 |
| 27 | `gpqa_37` | A | C | WRONG | 4096 | 10.66 | 386.96 |
| 28 | `gpqa_126` | B | None | WRONG | 4096 | 10.23 | 401.86 |
| 29 | `gpqa_122` | B | B | CORRECT | 4096 | 9.96 | 413.52 |
| 30 | `gpqa_78` | A | C | WRONG | 4096 | 9.74 | 423.82 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 9.59 | 430.26 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 19.52 | 212.03 |
| 33 | `gpqa_45` | C | None | WRONG | 4096 | 9.80 | 419.07 |
| 34 | `gpqa_184` | C | C | CORRECT | 178 | 10.92 | 17.97 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 10.32 | 400.18 |
| 36 | `gpqa_52` | D | C | WRONG | 4096 | 9.34 | 440.50 |
| 37 | `gpqa_192` | C | B | WRONG | 546 | 10.88 | 51.70 |
| 38 | `gpqa_174` | B | D | WRONG | 944 | 10.19 | 94.63 |
| 39 | `gpqa_10` | B | A | WRONG | 4096 | 10.58 | 390.65 |
| 40 | `gpqa_60` | D | None | WRONG | 4096 | 9.55 | 431.04 |
| 41 | `gpqa_170` | C | C | CORRECT | 4096 | 9.53 | 432.06 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 9.67 | 424.97 |
| 43 | `gpqa_131` | A | A | CORRECT | 4096 | 9.79 | 421.21 |
| 44 | `gpqa_103` | B | B | CORRECT | 873 | 10.41 | 85.97 |
| 45 | `gpqa_193` | D | D | CORRECT | 683 | 10.69 | 65.97 |
| 46 | `gpqa_95` | D | D | CORRECT | 2051 | 9.99 | 206.70 |
| 47 | `gpqa_144` | C | C | CORRECT | 4096 | 9.27 | 443.02 |
| 48 | `gpqa_100` | D | None | WRONG | 4096 | 9.82 | 419.23 |
| 49 | `gpqa_142` | C | A | WRONG | 4096 | 10.01 | 412.70 |
| 50 | `gpqa_61` | B | A | WRONG | 4096 | 9.79 | 420.96 |
