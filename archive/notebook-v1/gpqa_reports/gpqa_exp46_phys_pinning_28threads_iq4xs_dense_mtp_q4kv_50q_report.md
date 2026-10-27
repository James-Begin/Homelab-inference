# 50-Question GPQA Diamond Report: Exp 46: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Custom Non-Linear Dense Quantization (IQ4_XS Attention + Q4_0 MoE) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp46_phys_pinning_28threads_iq4xs_dense_mtp_q4kv`
- **Total Score (50Q):** **16 / 50 (32.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`22.50 tokens/second`**
- **Peak Generation Speed:** **`23.88 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 20.44 | 77.97 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.62 | 73.16 |
| 3 | `gpqa_2` | B | A | WRONG | 1536 | 23.34 | 67.39 |
| 4 | `gpqa_156` | A | A | CORRECT | 704 | 22.06 | 33.52 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 22.01 | 71.78 |
| 6 | `gpqa_12` | D | A | WRONG | 1536 | 22.55 | 70.43 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 22.44 | 69.83 |
| 8 | `gpqa_13` | B | B | CORRECT | 1494 | 20.31 | 74.87 |
| 9 | `gpqa_127` | D | D | CORRECT | 1536 | 19.71 | 94.92 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 22.49 | 69.78 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 23.32 | 67.24 |
| 12 | `gpqa_185` | A | None | WRONG | 1536 | 23.05 | 68.23 |
| 13 | `gpqa_30` | B | C | WRONG | 1536 | 21.93 | 71.43 |
| 14 | `gpqa_165` | C | B | WRONG | 1536 | 21.27 | 77.75 |
| 15 | `gpqa_169` | C | C | CORRECT | 1536 | 23.88 | 65.85 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 22.40 | 70.22 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 23.76 | 66.48 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 22.48 | 69.87 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 22.83 | 69.81 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 23.62 | 66.86 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 23.86 | 66.31 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 22.72 | 69.15 |
| 23 | `gpqa_84` | B | None | WRONG | 1536 | 22.96 | 69.05 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 21.57 | 72.95 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 22.19 | 71.23 |
| 26 | `gpqa_73` | D | None | WRONG | 1536 | 23.59 | 66.75 |
| 27 | `gpqa_37` | A | B | WRONG | 1536 | 22.79 | 69.43 |
| 28 | `gpqa_126` | B | C | WRONG | 1536 | 23.04 | 68.01 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 23.13 | 68.30 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 23.36 | 68.45 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 22.61 | 70.07 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 23.41 | 67.44 |
| 33 | `gpqa_45` | C | A | WRONG | 1536 | 22.03 | 70.81 |
| 34 | `gpqa_184` | C | C | CORRECT | 1536 | 23.77 | 66.36 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 22.45 | 70.64 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 22.51 | 70.31 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 22.40 | 70.06 |
| 38 | `gpqa_174` | B | D | WRONG | 1536 | 22.67 | 69.54 |
| 39 | `gpqa_10` | B | B | CORRECT | 1536 | 20.55 | 77.62 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 22.19 | 70.95 |
| 41 | `gpqa_170` | C | None | WRONG | 1536 | 21.76 | 72.55 |
| 42 | `gpqa_47` | A | C | WRONG | 1536 | 22.47 | 69.85 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 22.21 | 71.42 |
| 44 | `gpqa_103` | B | A | WRONG | 1536 | 22.79 | 69.20 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 23.55 | 66.83 |
| 47 | `gpqa_144` | C | C | CORRECT | 1536 | 23.24 | 67.14 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 22.15 | 71.13 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 22.53 | 70.78 |
| 50 | `gpqa_61` | B | B | CORRECT | 1536 | 22.36 | 70.79 |
| 50 | `gpqa_61` | B | B | CORRECT | 1536 | 22.42 | 70.54 |
