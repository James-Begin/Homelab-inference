# 50-Question GPQA Diamond Report: Exp 62: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Direct NUMA Map Pinning (--numa numactl) + Precision Suffix (n_max=8, match=5) + Confidence MTP (p_min=0.15) + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp62_phys_pinning_28threads_repacked_iq4xs_muge_numactl_pinning_q4kv`
- **Total Score (50Q):** **18 / 50 (36.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`21.57 tokens/second`**
- **Peak Generation Speed:** **`38.58 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 21.25 | 74.63 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 22.04 | 71.73 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 23.15 | 67.79 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 19.88 | 79.00 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 22.47 | 70.50 |
| 6 | `gpqa_12` | D | None | WRONG | 1536 | 38.58 | 42.16 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 21.27 | 73.52 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 19.31 | 80.85 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 21.46 | 87.92 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 21.01 | 74.74 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 24.74 | 63.54 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 21.98 | 71.72 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 21.32 | 73.43 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 22.43 | 73.64 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 22.48 | 69.73 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 20.97 | 74.96 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 20.31 | 77.39 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 20.66 | 75.71 |
| 19 | `gpqa_134` | D | B | WRONG | 1536 | 20.95 | 75.89 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 20.91 | 75.02 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 22.15 | 71.19 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 20.37 | 77.08 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 21.41 | 73.81 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 21.65 | 73.00 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.97 | 75.53 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 21.95 | 71.43 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 21.32 | 74.15 |
| 28 | `gpqa_126` | B | D | WRONG | 1536 | 19.58 | 79.88 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 21.77 | 72.40 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.82 | 76.41 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 20.72 | 76.33 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 21.54 | 73.24 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 20.11 | 77.43 |
| 34 | `gpqa_184` | C | C | CORRECT | 1185 | 20.91 | 58.19 |
| 35 | `gpqa_32` | B | None | WRONG | 1536 | 21.53 | 73.66 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 20.04 | 78.49 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 20.38 | 76.70 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 19.57 | 80.27 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 22.05 | 72.22 |
| 40 | `gpqa_60` | D | B | WRONG | 1536 | 20.26 | 77.67 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 19.91 | 79.02 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 20.03 | 78.34 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 20.38 | 77.58 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 21.40 | 73.58 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 21.42 | 73.61 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 21.36 | 73.43 |
| 47 | `gpqa_144` | C | C | CORRECT | 1536 | 19.27 | 80.92 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.61 | 79.98 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 27.24 | 59.25 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 21.75 | 72.49 |
