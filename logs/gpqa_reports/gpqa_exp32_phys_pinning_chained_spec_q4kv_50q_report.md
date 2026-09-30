# 50-Question GPQA Diamond Report: Exp 32: Physical Core Pinning (Anti-SMT) + Precision Chained Spec (N=8, M=12, hits=2) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp32_phys_pinning_chained_spec_q4kv`
- **Total Score (50Q):** **17 / 50 (34.0%)**
- **Standard 20Q Subset:** **11 / 20 (55.0%)**
- **Average Generation Speed:** **`19.43 tokens/second`**
- **Peak Generation Speed:** **`23.03 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 19.46 | 81.62 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 20.13 | 78.48 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 21.52 | 73.11 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 19.20 | 81.98 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 18.87 | 83.87 |
| 6 | `gpqa_12` | D | A | WRONG | 1536 | 18.78 | 84.54 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 19.66 | 79.66 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 19.27 | 81.24 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 15.64 | 115.80 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 18.50 | 84.98 |
| 11 | `gpqa_3` | C | None | WRONG | 12 | 12.26 | 2.55 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 19.19 | 81.97 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 18.88 | 82.91 |
| 14 | `gpqa_165` | C | C | CORRECT | 1536 | 21.93 | 75.54 |
| 15 | `gpqa_169` | C | C | CORRECT | 1536 | 20.39 | 76.90 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 19.15 | 82.15 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 19.60 | 80.39 |
| 18 | `gpqa_36` | B | A | WRONG | 14 | 13.27 | 2.62 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 20.24 | 78.41 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 21.02 | 74.99 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 21.20 | 74.22 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 19.94 | 78.93 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 19.97 | 79.30 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 18.67 | 84.20 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 19.24 | 82.35 |
| 26 | `gpqa_73` | D | A | WRONG | 1536 | 20.74 | 75.82 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 19.88 | 79.67 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 23.03 | 68.24 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 19.89 | 79.17 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 19.48 | 81.64 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 19.36 | 81.63 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 20.48 | 77.24 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 19.57 | 79.83 |
| 34 | `gpqa_184` | C | C | CORRECT | 1536 | 19.69 | 79.81 |
| 35 | `gpqa_32` | B | B | CORRECT | 1536 | 17.60 | 89.58 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 18.35 | 85.86 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 19.69 | 79.35 |
| 38 | `gpqa_174` | B | D | WRONG | 1536 | 18.71 | 83.93 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 20.63 | 77.33 |
| 40 | `gpqa_60` | D | None | WRONG | 3 | 21.05 | 2.09 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 18.97 | 82.80 |
| 42 | `gpqa_47` | A | None | WRONG | 1536 | 18.61 | 84.09 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 19.98 | 79.30 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 19.06 | 82.63 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 19.62 | 80.41 |
| 46 | `gpqa_95` | D | None | WRONG | 1536 | 22.31 | 70.31 |
| 47 | `gpqa_144` | C | None | WRONG | 1536 | 20.90 | 74.88 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.39 | 81.03 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 19.58 | 81.40 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 19.10 | 82.63 |
