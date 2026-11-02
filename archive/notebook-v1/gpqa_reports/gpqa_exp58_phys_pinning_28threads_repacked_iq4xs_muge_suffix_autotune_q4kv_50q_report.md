# 50-Question GPQA Diamond Report: Exp 58: Pre-Repacked Offline GGUF (IQ4_XS_R8 / Q4_0_R8) + Merged Experts (-muge) + Suffix Spec (n_max=8, match=5) + Speculative Autotuning (--spec-autotune) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp58_phys_pinning_28threads_repacked_iq4xs_muge_suffix_autotune_q4kv`
- **Total Score (50Q):** **18 / 50 (36.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`21.09 tokens/second`**
- **Peak Generation Speed:** **`37.67 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 20.83 | 76.17 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.58 | 73.22 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 22.62 | 69.34 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 19.48 | 80.70 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 21.97 | 71.95 |
| 6 | `gpqa_12` | D | None | WRONG | 1536 | 37.67 | 43.00 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.83 | 75.04 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 18.92 | 82.53 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 21.00 | 90.74 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 20.54 | 76.54 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 24.21 | 64.87 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 21.48 | 73.40 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 20.81 | 75.14 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 21.96 | 75.26 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 21.97 | 71.28 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 20.53 | 76.60 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 19.88 | 79.03 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 20.24 | 77.29 |
| 19 | `gpqa_134` | D | B | WRONG | 1536 | 20.51 | 77.47 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 20.47 | 76.81 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 21.62 | 72.80 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 19.89 | 78.94 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 20.93 | 75.47 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 21.17 | 74.64 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.48 | 77.17 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 21.43 | 73.19 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 20.78 | 76.05 |
| 28 | `gpqa_126` | B | D | WRONG | 1536 | 19.09 | 81.99 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 21.22 | 74.25 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.32 | 78.33 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 20.21 | 78.20 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 21.04 | 75.09 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 19.67 | 79.22 |
| 34 | `gpqa_184` | C | C | CORRECT | 1185 | 20.46 | 59.41 |
| 35 | `gpqa_32` | B | None | WRONG | 1536 | 21.06 | 75.12 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.64 | 80.05 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 19.93 | 78.31 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 19.13 | 82.33 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 21.59 | 73.67 |
| 40 | `gpqa_60` | D | B | WRONG | 1536 | 19.81 | 79.63 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 19.45 | 80.73 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 19.55 | 80.24 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 19.91 | 79.40 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 20.92 | 75.40 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 20.94 | 75.27 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 20.90 | 74.90 |
| 47 | `gpqa_144` | C | C | CORRECT | 1536 | 18.85 | 82.71 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.19 | 81.79 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 26.58 | 60.48 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 21.26 | 74.24 |
