# 50-Question GPQA Diamond Report: Exp 53: Pre-Repacked Offline GGUF (IQ4_XS_R8 / Q4_0_R8) + Merged Experts (-muge) + High-Throughput Precision Suffix (n_max=14, match=8, depth=64) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp53_phys_pinning_28threads_repacked_iq4xs_muge_suffix_nmax14_match8_q4kv`
- **Total Score (50Q):** **15 / 50 (30.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`21.42 tokens/second`**
- **Peak Generation Speed:** **`27.45 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 22.16 | 71.67 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.87 | 72.26 |
| 3 | `gpqa_2` | B | A | WRONG | 1536 | 21.44 | 73.19 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 20.70 | 76.01 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 20.80 | 76.03 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 22.34 | 71.28 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 21.14 | 73.86 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 19.83 | 78.98 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 19.07 | 97.29 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 27.45 | 57.83 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 22.17 | 70.60 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 21.15 | 74.46 |
| 13 | `gpqa_30` | B | A | WRONG | 1536 | 21.15 | 74.00 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 20.98 | 78.44 |
| 15 | `gpqa_169` | C | C | CORRECT | 1536 | 23.63 | 66.53 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 21.53 | 72.99 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 21.38 | 73.39 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 21.67 | 72.33 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 20.99 | 75.73 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 22.05 | 71.15 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 23.14 | 68.22 |
| 22 | `gpqa_53` | B | None | WRONG | 1536 | 21.42 | 73.36 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 21.74 | 72.85 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 19.98 | 78.75 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.23 | 78.07 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 22.10 | 71.09 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 20.60 | 77.00 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 20.91 | 74.79 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 21.77 | 72.44 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.70 | 76.93 |
| 31 | `gpqa_160` | A | None | WRONG | 1536 | 20.63 | 76.85 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 22.74 | 69.33 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 20.52 | 76.17 |
| 34 | `gpqa_184` | C | D | WRONG | 781 | 22.13 | 36.80 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 21.78 | 72.86 |
| 36 | `gpqa_52` | D | C | WRONG | 1536 | 20.25 | 77.86 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 21.08 | 74.13 |
| 38 | `gpqa_174` | B | C | WRONG | 1536 | 21.29 | 73.94 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 21.74 | 73.47 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 20.88 | 75.34 |
| 41 | `gpqa_170` | C | B | WRONG | 1536 | 21.16 | 74.35 |
| 42 | `gpqa_47` | A | None | WRONG | 1536 | 21.15 | 74.31 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 20.84 | 75.87 |
| 44 | `gpqa_103` | B | A | WRONG | 1536 | 21.27 | 73.99 |
| 45 | `gpqa_193` | D | A | WRONG | 1536 | 21.49 | 73.17 |
| 46 | `gpqa_95` | D | D | CORRECT | 1536 | 21.06 | 74.43 |
| 47 | `gpqa_144` | C | A | WRONG | 1536 | 22.02 | 70.82 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.81 | 79.30 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 21.65 | 73.78 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 21.26 | 74.18 |
