# 50-Question GPQA Diamond Report: Exp 61: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Grand Composite Champion (Suffix n_max=8, match=5 + Confidence MTP p_min=0.15 + Spec Autotune + Slot Similarity 0.20 + Q4_0 KV + SER 2,0.5)

- **Experiment ID:** `exp61_phys_pinning_28threads_repacked_iq4xs_muge_grand_composite_champion_q4kv`
- **Total Score (50Q):** **18 / 50 (36.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`21.14 tokens/second`**
- **Peak Generation Speed:** **`37.85 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 19.81 | 80.40 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.54 | 73.84 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 22.72 | 69.08 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 19.55 | 80.38 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 22.06 | 71.73 |
| 6 | `gpqa_12` | D | None | WRONG | 1536 | 37.85 | 43.15 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.92 | 74.70 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 18.99 | 82.31 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 21.08 | 90.24 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 20.60 | 76.36 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 24.28 | 64.64 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 21.54 | 73.18 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 20.87 | 74.95 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 22.01 | 74.94 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 22.02 | 71.34 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 20.61 | 76.34 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 19.94 | 78.67 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 20.32 | 77.06 |
| 19 | `gpqa_134` | D | B | WRONG | 1536 | 20.59 | 77.27 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 20.56 | 76.25 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 21.70 | 72.69 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 19.98 | 78.49 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 21.02 | 75.25 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 21.24 | 74.46 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.56 | 76.87 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 21.51 | 72.94 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 20.86 | 75.72 |
| 28 | `gpqa_126` | B | D | WRONG | 1536 | 19.16 | 81.79 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 21.31 | 73.91 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.38 | 78.22 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 20.29 | 78.06 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 21.10 | 74.89 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 19.71 | 78.99 |
| 34 | `gpqa_184` | C | C | CORRECT | 1185 | 20.51 | 59.39 |
| 35 | `gpqa_32` | B | None | WRONG | 1536 | 21.14 | 75.18 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.70 | 79.94 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 20.02 | 77.97 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 19.19 | 81.72 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 21.65 | 73.87 |
| 40 | `gpqa_60` | D | B | WRONG | 1536 | 19.87 | 79.26 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 19.51 | 80.60 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 19.61 | 79.78 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 19.96 | 79.31 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 20.98 | 74.96 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 21.01 | 74.87 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 20.98 | 74.79 |
| 47 | `gpqa_144` | C | C | CORRECT | 1536 | 18.91 | 82.39 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.25 | 81.57 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 26.70 | 60.37 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 21.34 | 73.89 |
