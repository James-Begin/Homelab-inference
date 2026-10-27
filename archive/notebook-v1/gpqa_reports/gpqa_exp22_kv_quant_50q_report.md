# 50-Question GPQA Diamond Report: Exp 22: KV Cache Quantization Ladder (-ctk q4_0 -ctv q4_0 + DFlash Spec + SER 2,0.5)

- **Experiment ID:** `exp22_kv_quant`
- **Total Score (50Q):** **16 / 50 (32.0%)**
- **Standard 20Q Subset:** **10 / 20 (50.0%)**
- **Average Generation Speed:** **`18.92 tokens/second`**
- **Peak Generation Speed:** **`23.76 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 17.94 | 87.81 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 20.09 | 78.38 |
| 3 | `gpqa_2` | B | A | WRONG | 1536 | 23.26 | 67.58 |
| 4 | `gpqa_156` | A | A | CORRECT | 779 | 17.03 | 47.33 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 18.18 | 86.27 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 16.78 | 93.97 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.59 | 75.91 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 16.43 | 94.87 |
| 9 | `gpqa_127` | D | None | WRONG | 1536 | 15.86 | 110.38 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 18.73 | 83.46 |
| 11 | `gpqa_3` | C | C | CORRECT | 1425 | 18.08 | 80.14 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 16.37 | 95.32 |
| 13 | `gpqa_30` | B | A | WRONG | 1536 | 18.00 | 86.69 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 17.39 | 92.92 |
| 15 | `gpqa_169` | C | C | CORRECT | 1136 | 23.76 | 49.29 |
| 16 | `gpqa_15` | D | C | WRONG | 1536 | 17.89 | 87.50 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 19.61 | 80.00 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 17.94 | 87.13 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 19.14 | 82.59 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 21.11 | 74.19 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 23.04 | 68.33 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 18.49 | 84.47 |
| 23 | `gpqa_84` | B | None | WRONG | 1536 | 18.78 | 83.64 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 16.54 | 94.60 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 16.80 | 93.46 |
| 26 | `gpqa_73` | D | D | CORRECT | 1220 | 21.93 | 57.25 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 16.98 | 92.39 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 17.90 | 87.33 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 21.45 | 73.48 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 18.13 | 87.17 |
| 31 | `gpqa_160` | A | B | WRONG | 1536 | 18.40 | 85.68 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 21.71 | 72.43 |
| 33 | `gpqa_45` | C | A | WRONG | 1536 | 18.15 | 85.74 |
| 34 | `gpqa_184` | C | A | WRONG | 1536 | 22.63 | 69.47 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 17.19 | 91.53 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 18.41 | 85.30 |
| 37 | `gpqa_192` | C | C | CORRECT | 779 | 22.31 | 36.15 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 18.95 | 82.62 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 16.47 | 95.94 |
| 40 | `gpqa_60` | D | None | WRONG | 3 | 18.09 | 2.03 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 17.88 | 87.68 |
| 42 | `gpqa_47` | A | None | WRONG | 1536 | 16.39 | 95.15 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 19.15 | 82.18 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 18.23 | 86.07 |
| 45 | `gpqa_193` | D | A | WRONG | 1536 | 23.47 | 67.31 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 20.93 | 74.82 |
| 47 | `gpqa_144` | C | None | WRONG | 3 | 20.24 | 1.27 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 18.57 | 84.38 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 17.88 | 88.37 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 16.93 | 92.83 |
