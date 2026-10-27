# 50-Question GPQA Diamond Report: Exp 16: Dual NUMA + Native MTP + Fused Operator Graph Compilation & Barrier NUMA Isolation

- **Experiment ID:** `exp16_fused_graph_compilation`
- **Total Score (50Q):** **16 / 50 (32.0%)**
- **Standard 20Q Subset:** **9 / 20 (45.0%)**
- **Average Generation Speed:** **`19.17 tokens/second`**
- **Peak Generation Speed:** **`21.01 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 18.60 | 86.18 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 19.18 | 82.51 |
| 3 | `gpqa_2` | B | A | WRONG | 1536 | 21.01 | 74.85 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 17.97 | 87.53 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 19.31 | 81.86 |
| 6 | `gpqa_12` | D | C | WRONG | 1536 | 19.06 | 83.41 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 18.99 | 82.47 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 17.79 | 88.09 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 17.14 | 108.71 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 17.64 | 88.89 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 19.63 | 79.95 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 19.13 | 82.08 |
| 13 | `gpqa_30` | B | A | WRONG | 1536 | 18.90 | 82.77 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 18.43 | 89.49 |
| 15 | `gpqa_169` | C | C | CORRECT | 1536 | 20.27 | 77.64 |
| 16 | `gpqa_15` | D | C | WRONG | 1536 | 19.11 | 82.42 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 20.05 | 78.34 |
| 18 | `gpqa_36` | B | A | WRONG | 1536 | 19.36 | 81.01 |
| 19 | `gpqa_134` | D | A | WRONG | 1126 | 20.26 | 58.52 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 20.16 | 78.01 |
| 21 | `gpqa_5` | C | A | WRONG | 1536 | 20.62 | 76.31 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 19.53 | 80.44 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 19.61 | 80.95 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 18.80 | 84.10 |
| 25 | `gpqa_64` | D | C | WRONG | 1536 | 18.65 | 84.77 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 19.87 | 79.28 |
| 27 | `gpqa_37` | A | B | WRONG | 1536 | 18.82 | 84.01 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 19.46 | 80.56 |
| 29 | `gpqa_122` | B | B | CORRECT | 1536 | 19.65 | 80.22 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 18.94 | 84.16 |
| 31 | `gpqa_160` | A | C | WRONG | 1411 | 18.62 | 78.13 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 20.12 | 78.67 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 18.69 | 83.68 |
| 34 | `gpqa_184` | C | A | WRONG | 1536 | 20.01 | 78.73 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 18.95 | 83.80 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 18.61 | 84.52 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 19.30 | 81.05 |
| 38 | `gpqa_174` | B | D | WRONG | 1536 | 18.46 | 85.15 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 18.48 | 86.23 |
| 40 | `gpqa_60` | D | C | WRONG | 1536 | 19.47 | 80.98 |
| 41 | `gpqa_170` | C | C | CORRECT | 1536 | 18.33 | 85.94 |
| 42 | `gpqa_47` | A | C | WRONG | 1536 | 18.70 | 83.95 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 18.21 | 87.16 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 19.09 | 82.40 |
| 45 | `gpqa_193` | D | D | CORRECT | 1536 | 20.21 | 78.21 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 20.53 | 76.51 |
| 47 | `gpqa_144` | C | None | WRONG | 1536 | 20.06 | 77.93 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.06 | 82.56 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 18.62 | 85.47 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 18.86 | 83.51 |
