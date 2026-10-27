# 50-Question GPQA Diamond Report: Exp 63: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Dynamic 3-Expert Pruning (expert_used_count=int:3) + Precision Suffix (n_max=8, match=5) + Confidence MTP (p_min=0.15) + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp63_phys_pinning_28threads_repacked_iq4xs_muge_3experts_pruning_q4kv`
- **Total Score (50Q):** **11 / 50 (22.0%)**
- **Standard 20Q Subset:** **5 / 20 (25.0%)**
- **Average Generation Speed:** **`21.16 tokens/second`**
- **Peak Generation Speed:** **`43.97 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 21.79 | 73.14 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.09 | 74.82 |
| 3 | `gpqa_2` | B | A | WRONG | 1536 | 23.27 | 67.72 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 19.36 | 80.94 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 21.41 | 73.88 |
| 6 | `gpqa_12` | D | A | WRONG | 1536 | 19.59 | 80.79 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 19.87 | 78.77 |
| 8 | `gpqa_13` | B | A | WRONG | 824 | 19.20 | 44.25 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 40.56 | 54.39 |
| 10 | `gpqa_69` | C | None | WRONG | 3 | 17.72 | 2.02 |
| 11 | `gpqa_3` | C | C | CORRECT | 774 | 21.38 | 37.76 |
| 12 | `gpqa_185` | A | None | WRONG | 1536 | 21.06 | 74.50 |
| 13 | `gpqa_30` | B | C | WRONG | 1536 | 19.70 | 79.52 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 20.18 | 81.25 |
| 15 | `gpqa_169` | C | A | WRONG | 1536 | 22.53 | 69.82 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 20.10 | 78.01 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 20.24 | 77.50 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 21.11 | 74.30 |
| 19 | `gpqa_134` | D | A | WRONG | 1430 | 21.05 | 70.34 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 20.48 | 76.68 |
| 21 | `gpqa_5` | C | None | WRONG | 1536 | 22.69 | 69.31 |
| 22 | `gpqa_53` | B | None | WRONG | 3 | 43.97 | 1.82 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 22.15 | 71.50 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 20.89 | 75.41 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.09 | 78.52 |
| 26 | `gpqa_73` | D | A | WRONG | 1536 | 20.78 | 75.42 |
| 27 | `gpqa_37` | A | B | WRONG | 1536 | 20.97 | 75.27 |
| 28 | `gpqa_126` | B | A | WRONG | 1536 | 22.01 | 71.22 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 20.82 | 75.61 |
| 30 | `gpqa_78` | A | C | WRONG | 1536 | 19.81 | 79.93 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 19.55 | 80.69 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 19.94 | 129.70 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 20.11 | 77.51 |
| 34 | `gpqa_184` | C | C | CORRECT | 934 | 20.86 | 46.34 |
| 35 | `gpqa_32` | B | A | WRONG | 1536 | 22.86 | 69.42 |
| 36 | `gpqa_52` | D | C | WRONG | 1536 | 20.11 | 78.28 |
| 37 | `gpqa_192` | C | C | CORRECT | 1536 | 19.73 | 79.35 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 18.50 | 84.76 |
| 39 | `gpqa_10` | B | B | CORRECT | 1536 | 20.87 | 76.12 |
| 40 | `gpqa_60` | D | A | WRONG | 1536 | 18.74 | 83.74 |
| 41 | `gpqa_170` | C | B | WRONG | 1536 | 21.05 | 74.89 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 18.84 | 83.03 |
| 43 | `gpqa_131` | A | C | WRONG | 1536 | 20.56 | 76.95 |
| 44 | `gpqa_103` | B | None | WRONG | 9 | 15.71 | 2.51 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 22.44 | 70.22 |
| 46 | `gpqa_95` | D | None | WRONG | 9 | 10.88 | 2.40 |
| 47 | `gpqa_144` | C | A | WRONG | 1536 | 19.59 | 79.59 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 20.31 | 77.38 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 21.17 | 75.31 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 20.42 | 77.17 |
