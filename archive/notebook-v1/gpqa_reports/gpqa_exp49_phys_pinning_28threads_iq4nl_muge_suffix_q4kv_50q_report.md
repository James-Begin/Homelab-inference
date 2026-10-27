# 50-Question GPQA Diamond Report: Exp 49: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Custom Non-Linear Dense Quantization (IQ4_NL Attention + Q4_0 MoE) + Merged Up/Gate Experts (-muge) + Precision Suffix Speculation (n_max=8, match=5) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp49_phys_pinning_28threads_iq4nl_muge_suffix_q4kv`
- **Total Score (50Q):** **17 / 50 (34.0%)**
- **Standard 20Q Subset:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`20.91 tokens/second`**
- **Peak Generation Speed:** **`38.31 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 20.17 | 79.14 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 22.39 | 70.84 |
| 3 | `gpqa_2` | B | None | WRONG | 1536 | 22.13 | 71.08 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 20.22 | 77.88 |
| 5 | `gpqa_128` | A | B | WRONG | 1536 | 21.12 | 75.10 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 20.22 | 78.58 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.48 | 76.29 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 20.91 | 75.04 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 38.31 | 59.46 |
| 10 | `gpqa_69` | C | C | CORRECT | 1536 | 19.51 | 80.61 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 20.60 | 76.05 |
| 12 | `gpqa_185` | A | C | WRONG | 1536 | 20.45 | 76.92 |
| 13 | `gpqa_30` | B | A | WRONG | 1536 | 20.06 | 77.97 |
| 14 | `gpqa_165` | C | C | CORRECT | 1536 | 19.65 | 84.09 |
| 15 | `gpqa_169` | C | A | WRONG | 1536 | 21.72 | 72.25 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 20.29 | 77.60 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 20.50 | 76.93 |
| 18 | `gpqa_36` | B | A | WRONG | 1536 | 20.41 | 76.96 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 21.47 | 74.28 |
| 20 | `gpqa_44` | C | None | WRONG | 1536 | 22.21 | 71.02 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 22.63 | 69.67 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 19.24 | 81.74 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 19.61 | 80.63 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 20.20 | 78.09 |
| 25 | `gpqa_64` | D | C | WRONG | 1536 | 20.30 | 78.32 |
| 26 | `gpqa_73` | D | None | WRONG | 1536 | 21.75 | 72.29 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 20.28 | 78.15 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 19.92 | 78.55 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 20.40 | 77.22 |
| 30 | `gpqa_78` | A | C | WRONG | 1536 | 21.49 | 74.57 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 18.97 | 83.63 |
| 32 | `gpqa_66` | C | A | WRONG | 1536 | 20.25 | 78.08 |
| 33 | `gpqa_45` | C | None | WRONG | 1536 | 21.04 | 74.19 |
| 34 | `gpqa_184` | C | C | CORRECT | 1536 | 20.75 | 75.72 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 21.44 | 74.16 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.11 | 82.44 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 19.85 | 78.75 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 19.41 | 81.12 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 21.53 | 74.48 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 19.31 | 81.75 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 20.69 | 76.25 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 19.35 | 81.17 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 20.46 | 77.53 |
| 44 | `gpqa_103` | B | B | CORRECT | 1536 | 20.52 | 76.72 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 22.25 | 70.82 |
| 46 | `gpqa_95` | D | D | CORRECT | 1536 | 22.09 | 71.15 |
| 47 | `gpqa_144` | C | C | CORRECT | 1536 | 20.56 | 76.09 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 18.66 | 84.33 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 19.51 | 81.85 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 21.34 | 74.01 |
