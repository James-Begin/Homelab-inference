# 50-Question GPQA Diamond Report: Exp 47: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Custom Non-Linear Dense Quantization (IQ4_XS Attention + Q4_0 MoE) + Precision Suffix Speculation (n_max=8, match=5, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp47_phys_pinning_28threads_iq4xs_suffix_match5_q4kv`
- **Total Score (50Q):** **18 / 50 (36.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`21.30 tokens/second`**
- **Peak Generation Speed:** **`38.35 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 21.03 | 75.89 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.83 | 72.42 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 22.90 | 68.55 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 19.65 | 79.97 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 22.20 | 71.35 |
| 6 | `gpqa_12` | D | None | WRONG | 1536 | 38.35 | 42.30 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.98 | 74.61 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 19.06 | 82.02 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 21.19 | 89.39 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 20.71 | 75.93 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 24.44 | 64.28 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 21.68 | 72.57 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 20.99 | 74.45 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 22.14 | 74.67 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 22.23 | 70.61 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 20.70 | 75.95 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 20.06 | 78.41 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 20.44 | 76.72 |
| 19 | `gpqa_134` | D | B | WRONG | 1536 | 20.68 | 76.77 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 20.67 | 75.94 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 21.88 | 72.11 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 20.08 | 78.21 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 21.10 | 74.84 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 21.37 | 74.01 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.69 | 76.52 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 21.63 | 72.48 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 21.01 | 75.30 |
| 28 | `gpqa_126` | B | D | WRONG | 1536 | 19.28 | 81.25 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 21.41 | 73.64 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.50 | 77.49 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 20.39 | 77.45 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 21.22 | 74.28 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 19.85 | 78.50 |
| 34 | `gpqa_184` | C | C | CORRECT | 1185 | 20.67 | 58.94 |
| 35 | `gpqa_32` | B | None | WRONG | 1536 | 21.29 | 74.30 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.81 | 79.36 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 20.12 | 77.77 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 19.30 | 81.36 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 21.75 | 73.21 |
| 40 | `gpqa_60` | D | B | WRONG | 1536 | 19.97 | 78.90 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 19.62 | 80.22 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 19.74 | 79.46 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 20.10 | 78.69 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 21.13 | 74.48 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 21.16 | 74.40 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 21.10 | 74.42 |
| 47 | `gpqa_144` | C | C | CORRECT | 1536 | 19.02 | 81.92 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.37 | 81.14 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 26.92 | 59.87 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 21.49 | 73.56 |
