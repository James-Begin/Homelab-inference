# 50-Question GPQA Diamond Report: Exp 93: Recursive Flint 40B MoE + Dense Auxiliary Drafter (Qwen 3.5 0.8B Drafter + Persistent Slot Cache 0.50 + Decoupled Prefill -tb 26 + 4K Ceiling)

- **Experiment ID:** `exp93_flint_dense_drafter_qwen08b_slot050_decoupled26_ceiling4096_q4kv`
- **Total Score (50Q):** **17 / 50 (34.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`10.04 tokens/second`**
- **Peak Generation Speed:** **`12.45 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | None | WRONG | 4096 | 10.72 | 396.80 |
| 2 | `gpqa_42` | A | A | CORRECT | 4096 | 11.50 | 358.28 |
| 3 | `gpqa_2` | B | B | CORRECT | 613 | 12.37 | 51.15 |
| 4 | `gpqa_156` | A | A | CORRECT | 373 | 12.45 | 31.82 |
| 5 | `gpqa_128` | A | C | WRONG | 4096 | 11.20 | 367.90 |
| 6 | `gpqa_12` | D | C | WRONG | 4096 | 11.10 | 371.73 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 11.65 | 352.90 |
| 8 | `gpqa_13` | B | C | WRONG | 4096 | 11.24 | 365.94 |
| 9 | `gpqa_127` | D | A | WRONG | 4096 | 9.50 | 456.64 |
| 10 | `gpqa_69` | C | A | WRONG | 4096 | 9.79 | 420.24 |
| 11 | `gpqa_3` | C | C | CORRECT | 4096 | 9.59 | 428.62 |
| 12 | `gpqa_185` | A | C | WRONG | 4096 | 10.14 | 405.64 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 10.16 | 404.62 |
| 14 | `gpqa_165` | C | A | WRONG | 4096 | 9.45 | 440.63 |
| 15 | `gpqa_169` | C | C | CORRECT | 1907 | 10.16 | 189.15 |
| 16 | `gpqa_15` | D | None | WRONG | 4096 | 9.68 | 425.23 |
| 17 | `gpqa_159` | A | A | CORRECT | 1629 | 10.17 | 162.07 |
| 18 | `gpqa_36` | B | C | WRONG | 4096 | 9.73 | 422.64 |
| 19 | `gpqa_134` | D | D | CORRECT | 1723 | 10.16 | 172.36 |
| 20 | `gpqa_44` | C | C | CORRECT | 2955 | 9.87 | 301.08 |
| 21 | `gpqa_5` | C | C | CORRECT | 1452 | 10.15 | 144.83 |
| 22 | `gpqa_53` | B | A | WRONG | 4096 | 9.65 | 425.93 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 9.57 | 430.57 |
| 24 | `gpqa_80` | D | A | WRONG | 4096 | 9.61 | 428.64 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 9.62 | 428.41 |
| 26 | `gpqa_73` | D | D | CORRECT | 2134 | 9.99 | 215.17 |
| 27 | `gpqa_37` | A | B | WRONG | 4096 | 9.57 | 430.65 |
| 28 | `gpqa_126` | B | None | WRONG | 4096 | 9.60 | 428.04 |
| 29 | `gpqa_122` | B | B | CORRECT | 3019 | 9.76 | 311.20 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 9.62 | 429.46 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 9.62 | 428.50 |
| 32 | `gpqa_66` | C | C | CORRECT | 1191 | 10.16 | 119.39 |
| 33 | `gpqa_45` | C | None | WRONG | 4096 | 9.64 | 425.92 |
| 34 | `gpqa_184` | C | C | CORRECT | 225 | 10.49 | 23.07 |
| 35 | `gpqa_32` | B | C | WRONG | 4096 | 9.56 | 431.41 |
| 36 | `gpqa_52` | D | None | WRONG | 4096 | 9.61 | 428.27 |
| 37 | `gpqa_192` | C | B | WRONG | 455 | 10.44 | 45.10 |
| 38 | `gpqa_174` | B | D | WRONG | 1264 | 10.14 | 126.64 |
| 39 | `gpqa_10` | B | C | WRONG | 4096 | 9.41 | 439.07 |
| 40 | `gpqa_60` | D | None | WRONG | 4096 | 9.53 | 431.76 |
| 41 | `gpqa_170` | C | A | WRONG | 4096 | 9.37 | 439.44 |
| 42 | `gpqa_47` | A | C | WRONG | 4096 | 9.23 | 445.26 |
| 43 | `gpqa_131` | A | None | WRONG | 4096 | 9.36 | 440.71 |
| 44 | `gpqa_103` | B | B | CORRECT | 949 | 9.41 | 102.89 |
| 45 | `gpqa_193` | D | D | CORRECT | 769 | 10.18 | 77.60 |
| 46 | `gpqa_95` | D | D | CORRECT | 1990 | 9.94 | 201.69 |
| 47 | `gpqa_144` | C | A | WRONG | 4096 | 9.63 | 426.70 |
| 48 | `gpqa_100` | D | None | WRONG | 4096 | 9.50 | 433.20 |
| 49 | `gpqa_142` | C | B | WRONG | 4096 | 9.46 | 436.22 |
| 50 | `gpqa_61` | B | A | WRONG | 4096 | 9.69 | 424.96 |
