# 50-Question GPQA Diamond Report: Exp 64: Pre-Repacked Offline GGUF + Merged Experts (-muge) + N-Gram Mod Hash Spec (n_max=10, N=8, M=16, hits=2) + Confidence MTP (p_min=0.15) + Spec Autotune + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp64_phys_pinning_28threads_repacked_iq4xs_muge_ngram_mod_hybrid_q4kv`
- **Total Score (50Q):** **17 / 50 (34.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`21.47 tokens/second`**
- **Peak Generation Speed:** **`23.68 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 21.35 | 74.33 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 22.19 | 71.16 |
| 3 | `gpqa_2` | B | None | WRONG | 1536 | 22.72 | 69.17 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 21.27 | 73.82 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 21.95 | 71.98 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 22.76 | 69.80 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 22.14 | 70.64 |
| 8 | `gpqa_13` | B | C | WRONG | 1536 | 20.34 | 76.88 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 19.08 | 97.47 |
| 10 | `gpqa_69` | C | C | CORRECT | 1536 | 21.57 | 72.75 |
| 11 | `gpqa_3` | C | C | CORRECT | 1536 | 22.31 | 70.35 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 22.19 | 70.81 |
| 13 | `gpqa_30` | B | D | WRONG | 1536 | 21.05 | 74.38 |
| 14 | `gpqa_165` | C | B | WRONG | 1536 | 19.86 | 82.69 |
| 15 | `gpqa_169` | C | C | CORRECT | 1246 | 23.68 | 54.05 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 22.04 | 71.37 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 21.68 | 72.62 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 20.84 | 75.13 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 21.77 | 73.13 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 21.95 | 71.72 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 22.16 | 70.96 |
| 22 | `gpqa_53` | B | None | WRONG | 1536 | 21.64 | 72.54 |
| 23 | `gpqa_84` | B | None | WRONG | 1536 | 22.91 | 69.13 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 21.56 | 73.07 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 21.70 | 73.00 |
| 26 | `gpqa_73` | D | A | WRONG | 1536 | 21.80 | 72.14 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 22.13 | 71.59 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 23.47 | 66.76 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 22.08 | 71.35 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.68 | 76.95 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 22.26 | 71.10 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 22.39 | 70.45 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 21.31 | 144.48 |
| 34 | `gpqa_184` | C | C | CORRECT | 963 | 21.89 | 45.48 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 22.59 | 70.17 |
| 36 | `gpqa_52` | D | D | CORRECT | 1536 | 21.66 | 72.78 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 21.31 | 73.41 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 20.88 | 75.51 |
| 39 | `gpqa_10` | B | B | CORRECT | 1536 | 20.27 | 78.49 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 20.94 | 75.36 |
| 41 | `gpqa_170` | C | None | WRONG | 3 | 19.32 | 2.18 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 20.72 | 75.60 |
| 43 | `gpqa_131` | A | D | WRONG | 1536 | 20.98 | 75.42 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 22.08 | 71.34 |
| 45 | `gpqa_193` | D | None | WRONG | 2 | 12.83 | 2.11 |
| 46 | `gpqa_95` | D | D | CORRECT | 1536 | 21.70 | 72.25 |
| 47 | `gpqa_144` | C | A | WRONG | 1536 | 22.93 | 68.09 |
| 48 | `gpqa_100` | D | C | WRONG | 1536 | 21.36 | 73.78 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 21.41 | 74.25 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 21.80 | 72.63 |
