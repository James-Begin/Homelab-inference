# 50-Question GPQA Diamond Report: Exp 50: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Pre-Repacked Offline GGUF (IQ4_XS_R8 / Q4_0_R8) + Merged Up/Gate Experts (-muge) + Precision Suffix Speculation (n_max=8, match=5) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv`
- **Total Score (50Q):** **18 / 50 (36.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`21.33 tokens/second`**
- **Peak Generation Speed:** **`38.23 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 20.94 | 76.06 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.84 | 72.24 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 22.91 | 68.57 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 19.68 | 79.83 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 22.24 | 71.32 |
| 6 | `gpqa_12` | D | None | WRONG | 1536 | 38.23 | 42.46 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 21.04 | 74.36 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 19.10 | 81.70 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 21.21 | 90.24 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 20.75 | 75.79 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 24.47 | 64.22 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 21.72 | 72.50 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 21.03 | 74.45 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 22.14 | 74.62 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 22.26 | 70.53 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 20.75 | 75.73 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 20.09 | 78.27 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 20.47 | 76.46 |
| 19 | `gpqa_134` | D | B | WRONG | 1536 | 20.74 | 76.59 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 20.69 | 75.93 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 21.91 | 71.83 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 20.12 | 78.01 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 21.14 | 74.77 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 21.40 | 73.71 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.73 | 76.40 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 21.67 | 72.50 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 21.02 | 75.15 |
| 28 | `gpqa_126` | B | D | WRONG | 1536 | 19.31 | 81.09 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 21.48 | 73.38 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.53 | 77.66 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 20.44 | 77.32 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 21.26 | 74.33 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 19.90 | 78.31 |
| 34 | `gpqa_184` | C | C | CORRECT | 1185 | 20.69 | 58.85 |
| 35 | `gpqa_32` | B | None | WRONG | 1536 | 21.29 | 74.64 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.84 | 79.29 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 20.17 | 77.48 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 19.34 | 81.08 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 21.80 | 73.36 |
| 40 | `gpqa_60` | D | B | WRONG | 1536 | 20.01 | 78.71 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 19.67 | 79.99 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 19.77 | 79.29 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 20.13 | 78.44 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 21.16 | 74.28 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 21.19 | 74.40 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 21.13 | 74.36 |
| 47 | `gpqa_144` | C | C | CORRECT | 1536 | 19.06 | 81.69 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.40 | 81.20 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 26.93 | 59.62 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 21.51 | 73.52 |
