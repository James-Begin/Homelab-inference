# 50-Question GPQA Diamond Report: Exp 94: Recursive Flint 40B MoE on ik_llama.cpp (Merged Up/Gate -muge 1 + Repacked AVX2 Q4_0_R8 + N-Gram Mod Speculation n_max=4, match=4 + Slot Cache 0.50 + Decoupled Prefill -tb 26 + 4K Ceiling)

- **Experiment ID:** `exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv`
- **Total Score (50Q):** **19 / 50 (38.0%)**
- **Standard 20Q Subset:** **10 / 20 (50.0%)**
- **Average Generation Speed:** **`18.42 tokens/second`**
- **Peak Generation Speed:** **`27.11 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 17.91 | 230.36 |
| 2 | `gpqa_42` | A | A | CORRECT | 2981 | 17.91 | 167.66 |
| 3 | `gpqa_2` | B | B | CORRECT | 645 | 18.91 | 35.15 |
| 4 | `gpqa_156` | A | A | CORRECT | 364 | 20.16 | 19.39 |
| 5 | `gpqa_128` | A | A | CORRECT | 4096 | 16.97 | 242.91 |
| 6 | `gpqa_12` | D | C | WRONG | 4096 | 17.39 | 237.27 |
| 7 | `gpqa_79` | D | A | WRONG | 4096 | 17.56 | 234.09 |
| 8 | `gpqa_13` | B | C | WRONG | 4096 | 17.91 | 229.64 |
| 9 | `gpqa_127` | D | A | WRONG | 4096 | 20.72 | 208.39 |
| 10 | `gpqa_69` | C | C | CORRECT | 4096 | 18.70 | 220.16 |
| 11 | `gpqa_3` | C | D | WRONG | 2789 | 19.10 | 147.04 |
| 12 | `gpqa_185` | A | C | WRONG | 4096 | 18.58 | 221.54 |
| 13 | `gpqa_30` | B | C | WRONG | 4096 | 17.56 | 234.16 |
| 14 | `gpqa_165` | C | C | CORRECT | 3148 | 19.22 | 167.48 |
| 15 | `gpqa_169` | C | C | CORRECT | 1951 | 18.72 | 105.25 |
| 16 | `gpqa_15` | D | D | CORRECT | 4096 | 18.10 | 227.38 |
| 17 | `gpqa_159` | A | C | WRONG | 4096 | 17.29 | 238.01 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 17.61 | 233.58 |
| 19 | `gpqa_134` | D | A | WRONG | 4096 | 19.66 | 210.20 |
| 20 | `gpqa_44` | C | C | CORRECT | 2701 | 17.33 | 156.92 |
| 21 | `gpqa_5` | C | C | CORRECT | 3577 | 18.88 | 190.57 |
| 22 | `gpqa_53` | B | A | WRONG | 4096 | 17.19 | 239.50 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 18.02 | 229.13 |
| 24 | `gpqa_80` | D | A | WRONG | 4096 | 17.44 | 236.55 |
| 25 | `gpqa_64` | D | B | WRONG | 4096 | 19.06 | 216.52 |
| 26 | `gpqa_73` | D | A | WRONG | 4096 | 17.40 | 236.47 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 18.30 | 225.41 |
| 28 | `gpqa_126` | B | A | WRONG | 4096 | 18.03 | 228.17 |
| 29 | `gpqa_122` | B | B | CORRECT | 2659 | 18.62 | 144.08 |
| 30 | `gpqa_78` | A | D | WRONG | 4096 | 17.92 | 230.33 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 17.60 | 234.30 |
| 32 | `gpqa_66` | C | C | CORRECT | 1669 | 18.95 | 89.38 |
| 33 | `gpqa_45` | C | None | WRONG | 4096 | 17.33 | 237.02 |
| 34 | `gpqa_184` | C | C | CORRECT | 280 | 20.21 | 14.84 |
| 35 | `gpqa_32` | B | C | WRONG | 4096 | 17.56 | 234.79 |
| 36 | `gpqa_52` | D | D | CORRECT | 4096 | 18.05 | 228.40 |
| 37 | `gpqa_192` | C | B | WRONG | 1051 | 19.93 | 53.66 |
| 38 | `gpqa_174` | B | D | WRONG | 4096 | 18.11 | 227.32 |
| 39 | `gpqa_10` | B | A | WRONG | 4096 | 18.55 | 223.12 |
| 40 | `gpqa_60` | D | None | WRONG | 4096 | 17.29 | 238.17 |
| 41 | `gpqa_170` | C | B | WRONG | 4096 | 17.66 | 233.45 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 17.60 | 233.88 |
| 43 | `gpqa_131` | A | None | WRONG | 4096 | 17.86 | 230.91 |
| 44 | `gpqa_103` | B | B | CORRECT | 3452 | 18.69 | 186.17 |
| 45 | `gpqa_193` | D | D | CORRECT | 665 | 19.82 | 34.73 |
| 46 | `gpqa_95` | D | C | WRONG | 4096 | 17.44 | 235.63 |
| 47 | `gpqa_144` | C | C | CORRECT | 4096 | 27.11 | 152.00 |
| 48 | `gpqa_100` | D | C | WRONG | 4096 | 17.07 | 241.16 |
| 49 | `gpqa_142` | C | A | WRONG | 4096 | 17.85 | 231.32 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 18.01 | 228.71 |
