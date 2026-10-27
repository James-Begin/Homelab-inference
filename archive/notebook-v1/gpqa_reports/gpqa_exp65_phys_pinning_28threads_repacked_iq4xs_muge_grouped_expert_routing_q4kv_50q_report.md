# 50-Question GPQA Diamond Report: Exp 65: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Grouped Expert Routing (-ger) + Precision Suffix (n_max=8, match=5) + Confidence MTP (p_min=0.15) + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp65_phys_pinning_28threads_repacked_iq4xs_muge_grouped_expert_routing_q4kv`
- **Total Score (50Q):** **18 / 50 (36.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`21.11 tokens/second`**
- **Peak Generation Speed:** **`37.84 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 20.84 | 76.45 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.60 | 73.19 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 22.69 | 69.29 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 19.49 | 80.63 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 22.01 | 71.93 |
| 6 | `gpqa_12` | D | None | WRONG | 1536 | 37.84 | 43.12 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.83 | 75.12 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 18.93 | 82.50 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 21.06 | 90.24 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 20.54 | 76.60 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 24.22 | 64.85 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 21.49 | 73.33 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 20.81 | 75.09 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 21.96 | 75.34 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 22.03 | 71.12 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 20.54 | 76.47 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 19.88 | 79.09 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 20.29 | 77.20 |
| 19 | `gpqa_134` | D | B | WRONG | 1536 | 20.52 | 77.55 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 20.46 | 76.77 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 21.67 | 72.76 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 19.92 | 78.75 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 20.94 | 75.45 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 21.18 | 74.61 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.51 | 77.18 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 21.45 | 73.25 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 20.82 | 75.95 |
| 28 | `gpqa_126` | B | D | WRONG | 1536 | 19.09 | 81.98 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 21.23 | 74.08 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.33 | 78.30 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 20.21 | 78.24 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 21.03 | 75.16 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 19.66 | 79.28 |
| 34 | `gpqa_184` | C | C | CORRECT | 1185 | 20.47 | 59.60 |
| 35 | `gpqa_32` | B | None | WRONG | 1536 | 21.09 | 74.97 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.65 | 80.17 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 19.95 | 78.33 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 19.13 | 82.14 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 21.58 | 73.78 |
| 40 | `gpqa_60` | D | B | WRONG | 1536 | 19.81 | 79.34 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 19.46 | 80.70 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 19.57 | 80.16 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 19.93 | 79.46 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 20.94 | 75.31 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 20.96 | 75.33 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 20.92 | 74.90 |
| 47 | `gpqa_144` | C | C | CORRECT | 1536 | 18.87 | 82.62 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.22 | 81.76 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 26.69 | 60.41 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 21.27 | 74.30 |
