# 50-Question GPQA Diamond Report: Exp 52: Pre-Repacked Offline GGUF (IQ4_XS_R8 / Q4_0_R8) + Merged Experts (-muge) + Deep Precision Suffix (n_max=12, match=7, depth=64) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp52_phys_pinning_28threads_repacked_iq4xs_muge_suffix_nmax12_match7_q4kv`
- **Total Score (50Q):** **13 / 50 (26.0%)**
- **Standard 20Q Subset:** **6 / 20 (30.0%)**
- **Average Generation Speed:** **`22.06 tokens/second`**
- **Peak Generation Speed:** **`48.74 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 21.09 | 75.57 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 22.22 | 71.08 |
| 3 | `gpqa_2` | B | A | WRONG | 1536 | 22.75 | 69.09 |
| 4 | `gpqa_156` | A | A | CORRECT | 1266 | 21.09 | 61.60 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 22.99 | 68.93 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 21.22 | 74.87 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 21.43 | 72.97 |
| 8 | `gpqa_13` | B | A | WRONG | 1536 | 19.28 | 80.90 |
| 9 | `gpqa_127` | D | C | WRONG | 1536 | 48.74 | 48.87 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 37.33 | 42.97 |
| 11 | `gpqa_3` | C | C | CORRECT | 1536 | 22.44 | 69.88 |
| 12 | `gpqa_185` | A | None | WRONG | 1536 | 21.55 | 73.07 |
| 13 | `gpqa_30` | B | A | WRONG | 1536 | 20.79 | 75.34 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 20.26 | 81.35 |
| 15 | `gpqa_169` | C | A | WRONG | 1536 | 22.77 | 68.98 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 21.44 | 73.40 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 20.49 | 76.61 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 20.50 | 76.43 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 21.26 | 74.87 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 21.62 | 72.79 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 22.19 | 70.90 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 21.16 | 74.36 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 21.25 | 74.30 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 21.42 | 73.53 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.59 | 76.62 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 21.77 | 72.27 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 20.52 | 76.92 |
| 28 | `gpqa_126` | B | C | WRONG | 1536 | 20.84 | 75.18 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 21.24 | 73.97 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.70 | 76.74 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 19.97 | 79.34 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 22.42 | 70.34 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 21.25 | 73.45 |
| 34 | `gpqa_184` | C | A | WRONG | 1109 | 22.92 | 50.10 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 20.24 | 78.08 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.74 | 79.57 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 20.78 | 75.29 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 20.87 | 75.36 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 21.55 | 74.06 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 20.65 | 76.33 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 21.10 | 154.37 |
| 42 | `gpqa_47` | A | C | WRONG | 1536 | 19.80 | 79.03 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 20.64 | 76.67 |
| 44 | `gpqa_103` | B | A | WRONG | 1536 | 21.05 | 74.72 |
| 45 | `gpqa_193` | D | A | WRONG | 1536 | 21.96 | 71.65 |
| 46 | `gpqa_95` | D | D | CORRECT | 1536 | 22.17 | 70.82 |
| 47 | `gpqa_144` | C | A | WRONG | 1536 | 20.98 | 74.32 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 20.06 | 78.38 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 20.27 | 78.56 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 21.49 | 73.61 |
