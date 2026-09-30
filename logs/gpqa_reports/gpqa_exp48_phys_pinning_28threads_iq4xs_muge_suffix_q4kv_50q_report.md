# 50-Question GPQA Diamond Report: Exp 48: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Custom IQ4_XS Attention + Merged Up/Gate Experts (-muge) + Precision Suffix Speculation (n_max=8, match=5, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp48_phys_pinning_28threads_iq4xs_muge_suffix_q4kv`
- **Total Score (50Q):** **18 / 50 (36.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`21.30 tokens/second`**
- **Peak Generation Speed:** **`38.22 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 21.09 | 75.58 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.86 | 72.19 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 22.93 | 68.52 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 19.69 | 79.83 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 22.27 | 71.14 |
| 6 | `gpqa_12` | D | None | WRONG | 1536 | 38.22 | 42.75 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 21.07 | 74.24 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 19.13 | 81.69 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 21.26 | 89.72 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 20.78 | 75.72 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 24.47 | 64.17 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 21.74 | 72.39 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 21.04 | 74.28 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 22.20 | 74.52 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 22.27 | 70.59 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 20.77 | 75.72 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 20.11 | 78.16 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 20.50 | 76.58 |
| 19 | `gpqa_134` | D | B | WRONG | 1536 | 20.77 | 76.61 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 20.73 | 75.75 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 21.89 | 72.05 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 20.16 | 77.83 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 21.18 | 74.52 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 21.44 | 73.65 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.75 | 76.31 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 20.29 | 77.17 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 20.53 | 77.03 |
| 28 | `gpqa_126` | B | D | WRONG | 1536 | 19.31 | 81.06 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 21.47 | 73.41 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.56 | 77.49 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 20.46 | 77.39 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 21.28 | 74.18 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 19.91 | 78.32 |
| 34 | `gpqa_184` | C | C | CORRECT | 1185 | 20.68 | 58.88 |
| 35 | `gpqa_32` | B | None | WRONG | 1536 | 21.31 | 74.23 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.84 | 79.44 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 20.14 | 77.56 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 19.35 | 81.17 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 21.81 | 72.93 |
| 40 | `gpqa_60` | D | B | WRONG | 1536 | 20.01 | 78.72 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 19.67 | 80.12 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 19.78 | 79.31 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 20.15 | 78.53 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 21.14 | 74.39 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 21.16 | 74.43 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 21.15 | 74.31 |
| 47 | `gpqa_144` | C | C | CORRECT | 1536 | 19.07 | 81.66 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.42 | 81.11 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 26.94 | 59.64 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 21.50 | 73.46 |
