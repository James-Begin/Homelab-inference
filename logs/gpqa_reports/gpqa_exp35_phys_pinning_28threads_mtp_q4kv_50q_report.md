# 50-Question GPQA Diamond Report: Exp 35: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp35_phys_pinning_28threads_mtp_q4kv`
- **Total Score (50Q):** **16 / 50 (32.0%)**
- **Standard 20Q Subset:** **5 / 20 (25.0%)**
- **Average Generation Speed:** **`20.81 tokens/second`**
- **Peak Generation Speed:** **`23.02 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 20.35 | 78.27 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.02 | 74.95 |
| 3 | `gpqa_2` | B | A | WRONG | 1536 | 22.21 | 70.64 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 20.01 | 78.46 |
| 5 | `gpqa_128` | A | C | WRONG | 1536 | 20.49 | 77.16 |
| 6 | `gpqa_12` | D | A | WRONG | 1536 | 20.39 | 78.07 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.99 | 74.56 |
| 8 | `gpqa_13` | B | C | WRONG | 1536 | 19.10 | 81.69 |
| 9 | `gpqa_127` | D | D | CORRECT | 1536 | 18.83 | 98.58 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 20.25 | 77.72 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 20.82 | 75.24 |
| 12 | `gpqa_185` | A | None | WRONG | 1536 | 23.02 | 68.31 |
| 13 | `gpqa_30` | B | None | WRONG | 0 | 0.00 | 231.97 |
| 14 | `gpqa_165` | C | B | WRONG | 1536 | 19.31 | 84.91 |
| 15 | `gpqa_169` | C | C | CORRECT | 1185 | 22.20 | 54.89 |
| 16 | `gpqa_15` | D | C | WRONG | 1536 | 20.10 | 78.42 |
| 17 | `gpqa_159` | A | C | WRONG | 1536 | 20.86 | 75.48 |
| 18 | `gpqa_36` | B | D | WRONG | 14 | 20.60 | 2.24 |
| 19 | `gpqa_134` | D | None | WRONG | 1536 | 20.58 | 77.17 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 21.48 | 73.11 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 21.91 | 71.78 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 20.99 | 74.98 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 21.35 | 74.29 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 20.65 | 76.21 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.28 | 77.83 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 21.99 | 71.60 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 20.24 | 78.07 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 20.75 | 75.47 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 21.43 | 73.40 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.77 | 76.84 |
| 31 | `gpqa_160` | A | C | WRONG | 1536 | 19.79 | 79.91 |
| 32 | `gpqa_66` | C | C | CORRECT | 1536 | 21.62 | 72.88 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 21.08 | 74.04 |
| 34 | `gpqa_184` | C | C | CORRECT | 1536 | 21.80 | 71.97 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 20.02 | 79.21 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 20.82 | 75.77 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 21.39 | 73.13 |
| 38 | `gpqa_174` | B | D | WRONG | 1043 | 21.31 | 50.60 |
| 39 | `gpqa_10` | B | B | CORRECT | 1536 | 19.63 | 80.97 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 20.29 | 77.64 |
| 41 | `gpqa_170` | C | None | WRONG | 1536 | 20.22 | 78.00 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 20.55 | 76.53 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 21.01 | 75.21 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 20.17 | 77.87 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 21.83 | 72.19 |
| 46 | `gpqa_95` | D | D | CORRECT | 1536 | 22.40 | 70.02 |
| 47 | `gpqa_144` | C | C | CORRECT | 1536 | 21.61 | 72.26 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 20.74 | 76.00 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 20.33 | 78.27 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 20.28 | 77.86 |
