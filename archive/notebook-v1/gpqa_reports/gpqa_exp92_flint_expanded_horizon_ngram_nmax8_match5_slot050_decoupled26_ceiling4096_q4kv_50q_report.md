# 50-Question GPQA Diamond Report: Exp 92: Recursive Flint 40B MoE Expanded Horizon (N-Gram Mod Speculation n_max=8, match=5 + Persistent Slot Cache 0.50 + Decoupled Prefill -tb 26 + 4K Ceiling)

- **Experiment ID:** `exp92_flint_expanded_horizon_ngram_nmax8_match5_slot050_decoupled26_ceiling4096_q4kv`
- **Total Score (50Q):** **16 / 50 (32.0%)**
- **Standard 20Q Subset:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`9.86 tokens/second`**
- **Peak Generation Speed:** **`14.57 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 9.66 | 426.95 |
| 2 | `gpqa_42` | A | D | WRONG | 4096 | 10.18 | 404.96 |
| 3 | `gpqa_2` | B | B | CORRECT | 1059 | 9.85 | 109.33 |
| 4 | `gpqa_156` | A | A | CORRECT | 398 | 9.76 | 42.80 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 9.10 | 452.47 |
| 6 | `gpqa_12` | D | C | WRONG | 4096 | 9.37 | 440.06 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 8.96 | 458.61 |
| 8 | `gpqa_13` | B | C | WRONG | 4096 | 8.88 | 462.79 |
| 9 | `gpqa_127` | D | A | WRONG | 4096 | 14.57 | 305.39 |
| 10 | `gpqa_69` | C | B | WRONG | 4096 | 11.01 | 373.86 |
| 11 | `gpqa_3` | C | D | WRONG | 2701 | 10.56 | 257.35 |
| 12 | `gpqa_185` | A | C | WRONG | 4096 | 9.82 | 418.87 |
| 13 | `gpqa_30` | B | B | CORRECT | 4096 | 9.26 | 443.61 |
| 14 | `gpqa_165` | C | A | WRONG | 4096 | 9.88 | 422.09 |
| 15 | `gpqa_169` | C | C | CORRECT | 1482 | 9.85 | 152.05 |
| 16 | `gpqa_15` | D | C | WRONG | 4096 | 9.44 | 435.85 |
| 17 | `gpqa_159` | A | C | WRONG | 4096 | 9.02 | 456.14 |
| 18 | `gpqa_36` | B | D | WRONG | 4096 | 9.47 | 434.36 |
| 19 | `gpqa_134` | D | D | CORRECT | 1596 | 11.20 | 145.34 |
| 20 | `gpqa_44` | C | C | CORRECT | 2828 | 9.17 | 310.32 |
| 21 | `gpqa_5` | C | C | CORRECT | 1413 | 9.60 | 149.42 |
| 22 | `gpqa_53` | B | A | WRONG | 4096 | 9.09 | 452.16 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 9.68 | 425.91 |
| 24 | `gpqa_80` | D | A | WRONG | 4096 | 9.79 | 420.47 |
| 25 | `gpqa_64` | D | C | WRONG | 4096 | 10.65 | 387.35 |
| 26 | `gpqa_73` | D | D | CORRECT | 1201 | 9.58 | 126.98 |
| 27 | `gpqa_37` | A | A | CORRECT | 4096 | 10.03 | 411.15 |
| 28 | `gpqa_126` | B | None | WRONG | 4096 | 10.18 | 403.67 |
| 29 | `gpqa_122` | B | B | CORRECT | 2988 | 9.71 | 309.75 |
| 30 | `gpqa_78` | A | C | WRONG | 4096 | 9.52 | 433.92 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 9.52 | 432.76 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 10.07 | 408.79 |
| 33 | `gpqa_45` | C | None | WRONG | 4096 | 9.71 | 423.03 |
| 34 | `gpqa_184` | C | C | CORRECT | 208 | 10.18 | 22.23 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 10.66 | 386.97 |
| 36 | `gpqa_52` | D | C | WRONG | 4096 | 9.09 | 452.35 |
| 37 | `gpqa_192` | C | B | WRONG | 426 | 11.13 | 39.70 |
| 38 | `gpqa_174` | B | D | WRONG | 2933 | 10.37 | 285.10 |
| 39 | `gpqa_10` | B | A | WRONG | 4096 | 10.65 | 388.18 |
| 40 | `gpqa_60` | D | None | WRONG | 4096 | 9.68 | 425.25 |
| 41 | `gpqa_170` | C | B | WRONG | 4096 | 9.21 | 447.27 |
| 42 | `gpqa_47` | A | C | WRONG | 4096 | 9.29 | 442.57 |
| 43 | `gpqa_131` | A | None | WRONG | 4096 | 9.59 | 430.13 |
| 44 | `gpqa_103` | B | B | CORRECT | 3273 | 9.92 | 331.86 |
| 45 | `gpqa_193` | D | D | CORRECT | 874 | 9.90 | 90.23 |
| 46 | `gpqa_95` | D | D | CORRECT | 1953 | 9.70 | 202.87 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 9.10 | 451.22 |
| 48 | `gpqa_100` | D | A | WRONG | 4096 | 9.05 | 454.76 |
| 49 | `gpqa_142` | C | B | WRONG | 4096 | 9.96 | 415.02 |
| 50 | `gpqa_61` | B | A | WRONG | 4096 | 9.60 | 428.86 |
