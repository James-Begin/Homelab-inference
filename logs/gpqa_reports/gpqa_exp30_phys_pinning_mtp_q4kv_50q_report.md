# 50-Question GPQA Diamond Report: Exp 30: Physical Core Pinning (Anti-SMT) + Native MTP + Q4_0 KV Cache + SER 2,0.5

- **Experiment ID:** `exp30_phys_pinning_mtp_q4kv`
- **Total Score (50Q):** **16 / 50 (32.0%)**
- **Standard 20Q Subset:** **5 / 20 (25.0%)**
- **Average Generation Speed:** **`20.02 tokens/second`**
- **Peak Generation Speed:** **`23.02 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 19.49 | 81.48 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 20.30 | 77.81 |
| 3 | `gpqa_2` | B | A | WRONG | 1536 | 21.94 | 71.73 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 19.17 | 82.15 |
| 5 | `gpqa_128` | A | C | WRONG | 1536 | 19.85 | 79.69 |
| 6 | `gpqa_12` | D | A | WRONG | 1536 | 19.46 | 81.36 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.27 | 77.27 |
| 8 | `gpqa_13` | B | C | WRONG | 1536 | 17.89 | 87.40 |
| 9 | `gpqa_127` | D | D | CORRECT | 1536 | 18.38 | 101.37 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 19.50 | 80.78 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 20.00 | 78.52 |
| 12 | `gpqa_185` | A | None | WRONG | 1536 | 23.02 | 68.64 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 19.88 | 78.78 |
| 14 | `gpqa_165` | C | B | WRONG | 1536 | 18.43 | 88.70 |
| 15 | `gpqa_169` | C | C | CORRECT | 1185 | 21.71 | 56.04 |
| 16 | `gpqa_15` | D | C | WRONG | 1536 | 19.15 | 81.96 |
| 17 | `gpqa_159` | A | C | WRONG | 1536 | 20.18 | 78.08 |
| 18 | `gpqa_36` | B | D | WRONG | 14 | 18.90 | 2.29 |
| 19 | `gpqa_134` | D | None | WRONG | 1536 | 19.59 | 81.17 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 20.64 | 76.29 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 21.46 | 73.58 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 20.40 | 77.23 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 20.51 | 77.05 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 19.65 | 80.33 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 19.13 | 82.50 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 21.40 | 73.42 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 19.29 | 81.98 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 20.02 | 78.29 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 20.70 | 76.31 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 19.91 | 79.89 |
| 31 | `gpqa_160` | A | C | WRONG | 1536 | 18.68 | 84.60 |
| 32 | `gpqa_66` | C | C | CORRECT | 1536 | 20.72 | 76.24 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 20.11 | 77.71 |
| 34 | `gpqa_184` | C | C | CORRECT | 1536 | 21.50 | 73.06 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 19.16 | 82.77 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.90 | 79.31 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 20.87 | 74.96 |
| 38 | `gpqa_174` | B | D | WRONG | 1043 | 20.77 | 51.98 |
| 39 | `gpqa_10` | B | B | CORRECT | 1536 | 18.49 | 85.86 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 19.31 | 81.35 |
| 41 | `gpqa_170` | C | None | WRONG | 1536 | 19.44 | 81.09 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 19.55 | 80.38 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 20.44 | 77.66 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 19.19 | 82.03 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 21.26 | 74.26 |
| 46 | `gpqa_95` | D | D | CORRECT | 1536 | 22.08 | 70.92 |
| 47 | `gpqa_144` | C | C | CORRECT | 1536 | 21.20 | 73.69 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.61 | 80.33 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 19.48 | 81.87 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 19.19 | 82.20 |
