# 50-Question GPQA Diamond Report: Exp 54: Pre-Repacked Offline GGUF (IQ4_XS_R8 / Q4_0_R8) + Merged Experts (-muge) + Confidence-Gated Burst Suffix (n_max=16, match=8, p_min=0.10, depth=64) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp54_phys_pinning_28threads_repacked_iq4xs_muge_suffix_nmax16_match8_pmin010_q4kv`
- **Total Score (50Q):** **14 / 50 (28.0%)**
- **Standard 20Q Subset:** **6 / 20 (30.0%)**
- **Average Generation Speed:** **`21.51 tokens/second`**
- **Peak Generation Speed:** **`28.26 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 21.47 | 74.26 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 22.54 | 70.23 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 22.99 | 68.29 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 20.64 | 76.11 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 21.31 | 74.38 |
| 6 | `gpqa_12` | D | A | WRONG | 1536 | 21.52 | 73.87 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.71 | 75.54 |
| 8 | `gpqa_13` | B | C | WRONG | 1536 | 20.09 | 77.84 |
| 9 | `gpqa_127` | D | C | WRONG | 1536 | 20.17 | 92.65 |
| 10 | `gpqa_69` | C | D | WRONG | 1536 | 20.84 | 75.50 |
| 11 | `gpqa_3` | C | C | CORRECT | 1536 | 21.96 | 71.43 |
| 12 | `gpqa_185` | A | C | WRONG | 1536 | 21.75 | 72.23 |
| 13 | `gpqa_30` | B | A | WRONG | 1536 | 20.93 | 74.80 |
| 14 | `gpqa_165` | C | D | WRONG | 1536 | 20.37 | 80.69 |
| 15 | `gpqa_169` | C | A | WRONG | 1536 | 22.92 | 68.61 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 21.30 | 73.82 |
| 17 | `gpqa_159` | A | C | WRONG | 1536 | 21.55 | 72.79 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 20.73 | 75.60 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 21.58 | 73.62 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 22.28 | 70.68 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 22.51 | 70.09 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 21.08 | 74.54 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 22.41 | 70.58 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 19.82 | 79.47 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 21.11 | 75.03 |
| 26 | `gpqa_73` | D | D | CORRECT | 1487 | 22.50 | 67.80 |
| 27 | `gpqa_37` | A | C | WRONG | 1536 | 25.89 | 61.42 |
| 28 | `gpqa_126` | B | C | WRONG | 1536 | 21.59 | 72.50 |
| 29 | `gpqa_122` | B | C | WRONG | 1536 | 21.44 | 73.36 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.36 | 78.39 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 21.62 | 73.31 |
| 32 | `gpqa_66` | C | C | CORRECT | 1536 | 21.65 | 72.82 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 21.01 | 151.96 |
| 34 | `gpqa_184` | C | A | WRONG | 1155 | 21.97 | 54.17 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 21.06 | 75.08 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 21.29 | 74.02 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 20.34 | 76.81 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 21.25 | 74.22 |
| 39 | `gpqa_10` | B | B | CORRECT | 1536 | 20.09 | 79.18 |
| 40 | `gpqa_60` | D | B | WRONG | 1536 | 20.76 | 76.00 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 20.72 | 76.03 |
| 42 | `gpqa_47` | A | None | WRONG | 1536 | 28.26 | 56.00 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 20.92 | 75.72 |
| 44 | `gpqa_103` | B | B | CORRECT | 1536 | 21.08 | 74.58 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 21.75 | 72.53 |
| 46 | `gpqa_95` | D | D | CORRECT | 1536 | 22.63 | 69.51 |
| 47 | `gpqa_144` | C | A | WRONG | 1536 | 20.96 | 74.45 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 20.33 | 77.23 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 20.82 | 76.62 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 20.52 | 76.72 |
