# 50-Question GPQA Diamond Report: Exp 51: Pre-Repacked Offline GGUF (IQ4_XS_R8 / Q4_0_R8) + Merged Experts (-muge) + Calibrated Horizon Expansion (n_max=10, match=6, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp51_phys_pinning_28threads_repacked_iq4xs_muge_suffix_nmax10_match6_q4kv`
- **Total Score (50Q):** **15 / 50 (30.0%)**
- **Standard 20Q Subset:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`21.19 tokens/second`**
- **Peak Generation Speed:** **`39.09 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 20.09 | 79.35 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.10 | 74.94 |
| 3 | `gpqa_2` | B | A | WRONG | 1536 | 21.82 | 72.01 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 20.44 | 76.95 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 21.35 | 74.11 |
| 6 | `gpqa_12` | D | A | WRONG | 1536 | 39.09 | 41.82 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 21.03 | 74.36 |
| 8 | `gpqa_13` | B | C | WRONG | 1536 | 19.13 | 81.71 |
| 9 | `gpqa_127` | D | C | WRONG | 1536 | 20.84 | 91.32 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 20.28 | 77.38 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 20.84 | 75.17 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 20.83 | 75.36 |
| 13 | `gpqa_30` | B | C | WRONG | 1536 | 20.28 | 77.18 |
| 14 | `gpqa_165` | C | B | WRONG | 1536 | 19.33 | 84.60 |
| 15 | `gpqa_169` | C | C | CORRECT | 1235 | 23.13 | 54.92 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 20.09 | 78.20 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 20.75 | 75.87 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 21.15 | 74.13 |
| 19 | `gpqa_134` | D | A | WRONG | 1405 | 20.51 | 71.08 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 20.58 | 76.37 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 21.09 | 74.63 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 21.10 | 74.44 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 21.58 | 73.44 |
| 24 | `gpqa_80` | D | C | WRONG | 1536 | 23.38 | 67.75 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.87 | 75.58 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 21.47 | 73.13 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 20.49 | 77.18 |
| 28 | `gpqa_126` | B | C | WRONG | 1536 | 20.51 | 76.32 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 22.30 | 70.68 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.75 | 76.64 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 19.89 | 79.48 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 20.23 | 77.75 |
| 33 | `gpqa_45` | C | None | WRONG | 1536 | 20.15 | 77.39 |
| 34 | `gpqa_184` | C | C | CORRECT | 984 | 21.51 | 47.38 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 21.42 | 73.94 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 20.22 | 77.71 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 20.83 | 75.16 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 20.17 | 77.97 |
| 39 | `gpqa_10` | B | A | WRONG | 1163 | 21.90 | 55.80 |
| 40 | `gpqa_60` | D | A | WRONG | 1536 | 19.39 | 81.11 |
| 41 | `gpqa_170` | C | B | WRONG | 1536 | 19.92 | 79.07 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 19.69 | 79.57 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 19.86 | 79.71 |
| 44 | `gpqa_103` | B | B | CORRECT | 1536 | 20.81 | 75.60 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 24.46 | 64.46 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 21.77 | 72.13 |
| 47 | `gpqa_144` | C | A | WRONG | 1536 | 20.05 | 77.90 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.96 | 78.75 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 20.15 | 78.81 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 20.71 | 76.33 |
