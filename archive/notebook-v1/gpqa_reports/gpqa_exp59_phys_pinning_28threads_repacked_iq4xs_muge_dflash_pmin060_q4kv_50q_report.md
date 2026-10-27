# 50-Question GPQA Diamond Report: Exp 59: Pre-Repacked Offline GGUF (IQ4_XS_R8 / Q4_0_R8) + Merged Experts (-muge) + High-Confidence Speculative Diffusion (DFlash n_max=3, p_min=0.60, cross_ctx=512) + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp59_phys_pinning_28threads_repacked_iq4xs_muge_dflash_pmin060_q4kv`
- **Total Score (50Q):** **13 / 50 (26.0%)**
- **Standard 20Q Subset:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`20.43 tokens/second`**
- **Peak Generation Speed:** **`26.43 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 20.74 | 76.21 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.91 | 72.13 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 26.39 | 59.60 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 18.56 | 84.26 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 19.87 | 79.43 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 25.57 | 62.38 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 22.74 | 68.91 |
| 8 | `gpqa_13` | B | A | WRONG | 1536 | 16.49 | 94.31 |
| 9 | `gpqa_127` | D | C | WRONG | 1536 | 19.52 | 91.96 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 20.25 | 77.55 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 22.47 | 69.80 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 18.73 | 83.66 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 19.65 | 79.55 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 17.38 | 93.02 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 25.90 | 60.64 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 18.73 | 83.56 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 21.30 | 73.50 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 18.25 | 85.63 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 21.95 | 72.22 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 23.50 | 66.74 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 26.43 | 59.79 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 19.77 | 79.08 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 20.64 | 76.28 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 16.75 | 93.44 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 19.75 | 79.88 |
| 26 | `gpqa_73` | D | None | WRONG | 1536 | 22.99 | 68.35 |
| 27 | `gpqa_37` | A | C | WRONG | 1536 | 19.70 | 79.88 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 21.12 | 155.68 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 23.07 | 68.24 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 19.60 | 80.89 |
| 31 | `gpqa_160` | A | None | WRONG | 1536 | 20.26 | 78.00 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 22.76 | 69.31 |
| 33 | `gpqa_45` | C | A | WRONG | 1536 | 21.14 | 73.68 |
| 34 | `gpqa_184` | C | A | WRONG | 1345 | 23.84 | 57.88 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 20.46 | 77.15 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 21.81 | 72.18 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 22.06 | 70.87 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 18.94 | 82.70 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 16.55 | 95.04 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 17.72 | 88.26 |
| 41 | `gpqa_170` | C | None | WRONG | 1536 | 18.22 | 86.06 |
| 42 | `gpqa_47` | A | C | WRONG | 1536 | 18.10 | 86.22 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 20.49 | 77.25 |
| 44 | `gpqa_103` | B | A | WRONG | 1536 | 21.59 | 72.79 |
| 45 | `gpqa_193` | D | None | WRONG | 2 | 13.16 | 1.96 |
| 46 | `gpqa_95` | D | D | CORRECT | 1536 | 23.98 | 65.35 |
| 47 | `gpqa_144` | C | None | WRONG | 2 | 14.60 | 1.22 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.55 | 80.21 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 18.20 | 86.85 |
| 50 | `gpqa_61` | B | B | CORRECT | 1536 | 18.33 | 85.82 |
