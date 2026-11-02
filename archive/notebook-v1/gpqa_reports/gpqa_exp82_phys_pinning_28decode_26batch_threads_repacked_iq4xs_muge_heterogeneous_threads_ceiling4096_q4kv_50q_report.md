# 50-Question GPQA Diamond Report: Exp 82: Dynamic Thread Heterogeneity (28 Decode Threads -t 28, 26 Batch Prefill Threads -tb 26 + Persistent Slot 0.50 + Autotune + MTP + 4K Ceiling)

- **Experiment ID:** `exp82_phys_pinning_28decode_26batch_threads_repacked_iq4xs_muge_heterogeneous_threads_ceiling4096_q4kv`
- **Total Score (50Q):** **8 / 50 (16.0%)**
- **Standard 20Q Subset:** **5 / 20 (25.0%)**
- **Average Generation Speed:** **`18.49 tokens/second`**
- **Peak Generation Speed:** **`34.08 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | None | WRONG | 4096 | 17.15 | 241.36 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 18.31 | 225.78 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 19.06 | 216.58 |
| 4 | `gpqa_156` | A | A | CORRECT | 2465 | 17.98 | 139.10 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 17.17 | 240.74 |
| 6 | `gpqa_12` | D | None | WRONG | 4096 | 34.08 | 122.93 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 17.67 | 233.14 |
| 8 | `gpqa_13` | B | C | WRONG | 2190 | 17.36 | 127.71 |
| 9 | `gpqa_127` | D | D | CORRECT | 4096 | 30.70 | 151.23 |
| 10 | `gpqa_69` | C | None | WRONG | 4096 | 18.60 | 221.86 |
| 11 | `gpqa_3` | C | C | CORRECT | 1865 | 20.00 | 94.86 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 17.31 | 238.60 |
| 13 | `gpqa_30` | B | B | CORRECT | 4096 | 16.77 | 245.62 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 18.28 | 229.72 |
| 15 | `gpqa_169` | C | None | WRONG | 4096 | 21.23 | 194.60 |
| 16 | `gpqa_15` | D | D | CORRECT | 2331 | 18.90 | 125.17 |
| 17 | `gpqa_159` | A | C | WRONG | 3915 | 17.88 | 220.79 |
| 18 | `gpqa_36` | B | C | WRONG | 4096 | 17.61 | 234.42 |
| 19 | `gpqa_134` | D | None | WRONG | 4096 | 17.82 | 232.64 |
| 20 | `gpqa_44` | C | None | WRONG | 4096 | 17.84 | 231.43 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 18.81 | 219.67 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 18.31 | 225.61 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 17.21 | 240.08 |
| 24 | `gpqa_80` | D | None | WRONG | 4096 | 17.29 | 239.16 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 16.84 | 245.68 |
| 26 | `gpqa_73` | D | None | WRONG | 4096 | 18.43 | 224.07 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 17.81 | 467.36 |
| 28 | `gpqa_126` | B | A | WRONG | 4096 | 17.53 | 235.27 |
| 29 | `gpqa_122` | B | None | WRONG | 4096 | 17.50 | 236.30 |
| 30 | `gpqa_78` | A | A | CORRECT | 4096 | 16.45 | 251.80 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 17.06 | 242.50 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 17.51 | 236.06 |
| 33 | `gpqa_45` | C | None | WRONG | 4096 | 17.33 | 237.81 |
| 34 | `gpqa_184` | C | None | WRONG | 4096 | 18.07 | 228.46 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 27.35 | 152.22 |
| 36 | `gpqa_52` | D | None | WRONG | 4096 | 16.65 | 248.11 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 17.34 | 237.56 |
| 38 | `gpqa_174` | B | A | WRONG | 4096 | 16.61 | 248.28 |
| 39 | `gpqa_10` | B | None | WRONG | 4096 | 18.09 | 229.13 |
| 40 | `gpqa_60` | D | A | WRONG | 4096 | 16.42 | 251.27 |
| 41 | `gpqa_170` | C | None | WRONG | 4096 | 16.55 | 249.58 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 17.69 | 233.24 |
| 43 | `gpqa_131` | A | B | WRONG | 4096 | 17.29 | 239.50 |
| 44 | `gpqa_103` | B | B | CORRECT | 2847 | 18.06 | 159.74 |
| 45 | `gpqa_193` | D | A | WRONG | 4096 | 18.22 | 226.72 |
| 46 | `gpqa_95` | D | None | WRONG | 4096 | 18.17 | 226.97 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 16.63 | 247.66 |
| 48 | `gpqa_100` | D | None | WRONG | 4096 | 16.75 | 246.47 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 17.85 | 232.50 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 16.99 | 243.15 |
