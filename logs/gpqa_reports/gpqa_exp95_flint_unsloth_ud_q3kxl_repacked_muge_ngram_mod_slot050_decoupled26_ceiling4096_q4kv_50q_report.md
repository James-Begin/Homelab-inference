# 50-Question GPQA Diamond Report: Exp 95: Recursive Flint 40B MoE Unsloth UD Q3_K_XL on ik_llama.cpp (Merged Up/Gate -muge + Repacked AVX2 Q3_K_R4/Q4_0_R8 + N-Gram Mod Speculation n_max=4, match=4 + Slot Cache 0.50 + Decoupled Prefill -tb 26 + 4K Ceiling)

- **Experiment ID:** `exp95_flint_unsloth_ud_q3kxl_repacked_muge_ngram_mod_slot050_decoupled26_ceiling4096_q4kv`
- **Total Score (50Q):** **17 / 50 (34.0%)**
- **Standard 20Q Subset:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`17.31 tokens/second`**
- **Peak Generation Speed:** **`22.07 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | None | WRONG | 4096 | 18.00 | 229.18 |
| 2 | `gpqa_42` | A | A | CORRECT | 4096 | 16.12 | 255.36 |
| 3 | `gpqa_2` | B | B | CORRECT | 630 | 18.00 | 36.10 |
| 4 | `gpqa_156` | A | A | CORRECT | 324 | 19.27 | 18.19 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 16.68 | 246.92 |
| 6 | `gpqa_12` | D | C | WRONG | 4096 | 16.93 | 243.87 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 16.93 | 242.97 |
| 8 | `gpqa_13` | B | C | WRONG | 4096 | 16.17 | 254.48 |
| 9 | `gpqa_127` | D | A | WRONG | 4096 | 22.07 | 197.25 |
| 10 | `gpqa_69` | C | A | WRONG | 4096 | 16.64 | 247.21 |
| 11 | `gpqa_3` | C | A | WRONG | 4096 | 17.42 | 236.12 |
| 12 | `gpqa_185` | A | C | WRONG | 4096 | 18.01 | 228.62 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 16.35 | 251.49 |
| 14 | `gpqa_165` | C | A | WRONG | 4096 | 17.10 | 243.48 |
| 15 | `gpqa_169` | C | C | CORRECT | 1817 | 18.31 | 100.20 |
| 16 | `gpqa_15` | D | D | CORRECT | 4096 | 17.55 | 234.62 |
| 17 | `gpqa_159` | A | A | CORRECT | 3475 | 16.10 | 217.32 |
| 18 | `gpqa_36` | B | D | WRONG | 4096 | 16.58 | 248.07 |
| 19 | `gpqa_134` | D | D | CORRECT | 3159 | 18.43 | 173.19 |
| 20 | `gpqa_44` | C | B | WRONG | 4096 | 16.06 | 256.11 |
| 21 | `gpqa_5` | C | C | CORRECT | 1911 | 18.12 | 106.66 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 16.94 | 242.67 |
| 23 | `gpqa_84` | B | B | CORRECT | 2665 | 17.42 | 154.55 |
| 24 | `gpqa_80` | D | A | WRONG | 4096 | 17.37 | 237.18 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 17.60 | 234.40 |
| 26 | `gpqa_73` | D | D | CORRECT | 2640 | 18.52 | 143.59 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 17.84 | 231.55 |
| 28 | `gpqa_126` | B | A | WRONG | 4096 | 18.10 | 227.31 |
| 29 | `gpqa_122` | B | B | CORRECT | 3369 | 16.49 | 205.55 |
| 30 | `gpqa_78` | A | A | CORRECT | 4096 | 16.62 | 248.25 |
| 31 | `gpqa_160` | A | C | WRONG | 4096 | 16.14 | 255.76 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 16.57 | 248.62 |
| 33 | `gpqa_45` | C | None | WRONG | 4096 | 16.76 | 245.36 |
| 34 | `gpqa_184` | C | C | CORRECT | 605 | 18.64 | 33.51 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 18.19 | 226.80 |
| 36 | `gpqa_52` | D | None | WRONG | 4096 | 16.58 | 248.33 |
| 37 | `gpqa_192` | C | B | WRONG | 4096 | 16.82 | 244.46 |
| 38 | `gpqa_174` | B | D | WRONG | 914 | 18.19 | 51.54 |
| 39 | `gpqa_10` | B | A | WRONG | 4096 | 17.55 | 235.33 |
| 40 | `gpqa_60` | D | None | WRONG | 4096 | 16.45 | 250.20 |
| 41 | `gpqa_170` | C | C | CORRECT | 4096 | 16.84 | 244.60 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 16.10 | 255.46 |
| 43 | `gpqa_131` | A | None | WRONG | 4096 | 16.81 | 245.43 |
| 44 | `gpqa_103` | B | B | CORRECT | 2537 | 18.41 | 139.10 |
| 45 | `gpqa_193` | D | D | CORRECT | 1733 | 17.71 | 99.06 |
| 46 | `gpqa_95` | D | D | CORRECT | 1124 | 17.34 | 65.66 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 16.25 | 252.78 |
| 48 | `gpqa_100` | D | A | WRONG | 4096 | 16.72 | 246.22 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 16.71 | 247.36 |
| 50 | `gpqa_61` | B | A | WRONG | 4096 | 17.16 | 240.05 |
