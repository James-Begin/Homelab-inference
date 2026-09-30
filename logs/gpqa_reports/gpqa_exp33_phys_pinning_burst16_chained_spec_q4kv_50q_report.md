# 50-Question GPQA Diamond Report: Exp 33: Physical Core Pinning (Anti-SMT) + Burst-16 Chained Spec (n_max=16, N=8, M=24, hits=2) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp33_phys_pinning_burst16_chained_spec_q4kv`
- **Total Score (50Q):** **16 / 50 (32.0%)**
- **Standard 20Q Subset:** **7 / 20 (35.0%)**
- **Average Generation Speed:** **`18.60 tokens/second`**
- **Peak Generation Speed:** **`22.09 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 18.04 | 88.04 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 20.42 | 77.51 |
| 3 | `gpqa_2` | B | None | WRONG | 1536 | 18.14 | 86.46 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 17.60 | 88.96 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 18.71 | 84.30 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 18.36 | 86.35 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 18.15 | 86.12 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 17.13 | 91.31 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 14.98 | 121.30 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 18.16 | 86.49 |
| 11 | `gpqa_3` | C | B | WRONG | 1536 | 19.45 | 80.42 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 17.78 | 88.33 |
| 13 | `gpqa_30` | B | C | WRONG | 1536 | 18.46 | 84.82 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 18.13 | 90.37 |
| 15 | `gpqa_169` | C | A | WRONG | 1536 | 19.70 | 79.60 |
| 16 | `gpqa_15` | D | C | WRONG | 1536 | 19.61 | 80.07 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 19.26 | 81.46 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 19.33 | 81.09 |
| 19 | `gpqa_134` | D | None | WRONG | 1536 | 18.88 | 84.10 |
| 20 | `gpqa_44` | C | None | WRONG | 1536 | 19.90 | 79.01 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 19.91 | 79.05 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 19.16 | 82.02 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 20.50 | 77.28 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 17.92 | 87.84 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 19.30 | 81.87 |
| 26 | `gpqa_73` | D | D | CORRECT | 1215 | 20.01 | 62.52 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 18.32 | 86.08 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 18.35 | 85.35 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 19.50 | 80.80 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 19.39 | 81.97 |
| 31 | `gpqa_160` | A | B | WRONG | 1536 | 18.56 | 85.24 |
| 32 | `gpqa_66` | C | A | WRONG | 1536 | 19.25 | 81.96 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 18.36 | 85.02 |
| 34 | `gpqa_184` | C | C | CORRECT | 1536 | 18.07 | 86.91 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 18.26 | 86.68 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 17.26 | 91.18 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 18.74 | 83.44 |
| 38 | `gpqa_174` | B | B | CORRECT | 689 | 20.14 | 36.29 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 18.12 | 87.65 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 18.09 | 86.79 |
| 41 | `gpqa_170` | C | None | WRONG | 1536 | 17.35 | 90.55 |
| 42 | `gpqa_47` | A | None | WRONG | 1536 | 17.79 | 88.03 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 18.48 | 85.72 |
| 44 | `gpqa_103` | B | B | CORRECT | 1536 | 19.47 | 80.62 |
| 45 | `gpqa_193` | D | A | WRONG | 1536 | 22.09 | 71.59 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 19.31 | 81.08 |
| 47 | `gpqa_144` | C | None | WRONG | 3 | 13.04 | 1.46 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 18.39 | 85.50 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 18.50 | 85.87 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 18.05 | 87.15 |
