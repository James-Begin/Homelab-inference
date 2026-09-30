# 50-Question GPQA Diamond Report: Exp 55: Pre-Repacked Offline GGUF (IQ4_XS_R8 / Q4_0_R8) + Merged Experts (-muge) + Calibrated Speculative Diffusion (DFlash n_max=3, p_min=0.45, cross_ctx=512) + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp55_phys_pinning_28threads_repacked_iq4xs_muge_dflash_nmax3_pmin045_q4kv`
- **Total Score (50Q):** **13 / 50 (26.0%)**
- **Standard 20Q Subset:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`20.28 tokens/second`**
- **Peak Generation Speed:** **`26.32 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 19.29 | 81.71 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.76 | 72.43 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 26.26 | 60.00 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 18.48 | 84.83 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 19.79 | 79.70 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 25.43 | 62.56 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 22.61 | 69.13 |
| 8 | `gpqa_13` | B | A | WRONG | 1536 | 16.40 | 94.79 |
| 9 | `gpqa_127` | D | C | WRONG | 1536 | 19.41 | 92.28 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 20.14 | 78.05 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 22.35 | 70.04 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 18.63 | 84.12 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 19.59 | 79.70 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 17.32 | 93.06 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 25.78 | 61.04 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 18.62 | 84.28 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 21.16 | 74.02 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 18.14 | 86.08 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 21.83 | 72.46 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 23.36 | 67.20 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 26.32 | 60.11 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 19.67 | 79.59 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 20.56 | 76.56 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 16.67 | 93.81 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 19.65 | 80.21 |
| 26 | `gpqa_73` | D | None | WRONG | 1536 | 22.90 | 68.49 |
| 27 | `gpqa_37` | A | C | WRONG | 1536 | 19.59 | 80.40 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 21.01 | 156.48 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 22.92 | 68.71 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 19.50 | 81.03 |
| 31 | `gpqa_160` | A | None | WRONG | 1536 | 20.12 | 78.56 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 22.64 | 69.67 |
| 33 | `gpqa_45` | C | A | WRONG | 1536 | 21.02 | 74.14 |
| 34 | `gpqa_184` | C | A | WRONG | 1345 | 23.68 | 58.17 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 20.32 | 77.73 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 21.68 | 72.50 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 21.92 | 71.30 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 18.81 | 83.28 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 16.42 | 95.88 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 17.58 | 89.07 |
| 41 | `gpqa_170` | C | None | WRONG | 1536 | 18.08 | 86.52 |
| 42 | `gpqa_47` | A | C | WRONG | 1536 | 18.00 | 86.64 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 20.35 | 77.56 |
| 44 | `gpqa_103` | B | A | WRONG | 1536 | 21.45 | 73.46 |
| 45 | `gpqa_193` | D | None | WRONG | 2 | 13.02 | 1.92 |
| 46 | `gpqa_95` | D | D | CORRECT | 1536 | 23.82 | 65.79 |
| 47 | `gpqa_144` | C | None | WRONG | 2 | 14.35 | 1.36 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.44 | 80.72 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 18.09 | 87.24 |
| 50 | `gpqa_61` | B | B | CORRECT | 1536 | 18.21 | 86.33 |
