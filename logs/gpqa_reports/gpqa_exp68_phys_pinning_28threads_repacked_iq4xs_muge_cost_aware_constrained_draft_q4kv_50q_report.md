# 50-Question GPQA Diamond Report: Exp 68: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Constrained Draft Depth (n_max=4, depth=32) + Direct NUMA Map Pinning (--numa numactl) + Confidence MTP (p_min=0.15) + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp68_phys_pinning_28threads_repacked_iq4xs_muge_cost_aware_constrained_draft_q4kv`
- **Total Score (50Q):** **4 / 50 (8.0%)**
- **Standard 20Q Subset:** **2 / 20 (10.0%)**
- **Average Generation Speed:** **`22.41 tokens/second`**
- **Peak Generation Speed:** **`41.69 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | None | WRONG | 1536 | 21.81 | 73.14 |
| 2 | `gpqa_42` | A | None | WRONG | 1536 | 21.89 | 72.23 |
| 3 | `gpqa_2` | B | None | WRONG | 1536 | 23.22 | 67.66 |
| 4 | `gpqa_156` | A | None | WRONG | 1536 | 21.70 | 72.48 |
| 5 | `gpqa_128` | A | None | WRONG | 1536 | 21.70 | 72.96 |
| 6 | `gpqa_12` | D | A | WRONG | 1536 | 24.13 | 65.86 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.67 | 75.63 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 20.56 | 76.04 |
| 9 | `gpqa_127` | D | None | WRONG | 1536 | 30.45 | 66.59 |
| 10 | `gpqa_69` | C | None | WRONG | 1536 | 21.36 | 73.73 |
| 11 | `gpqa_3` | C | None | WRONG | 1536 | 22.80 | 68.78 |
| 12 | `gpqa_185` | A | None | WRONG | 1536 | 22.64 | 69.65 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 20.91 | 74.98 |
| 14 | `gpqa_165` | C | None | WRONG | 1536 | 20.87 | 78.83 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 23.22 | 67.76 |
| 16 | `gpqa_15` | D | None | WRONG | 1536 | 21.24 | 74.06 |
| 17 | `gpqa_159` | A | A | CORRECT | 1536 | 21.22 | 74.02 |
| 18 | `gpqa_36` | B | None | WRONG | 1536 | 21.46 | 72.97 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 21.68 | 73.26 |
| 20 | `gpqa_44` | C | None | WRONG | 1536 | 22.44 | 70.19 |
| 21 | `gpqa_5` | C | None | WRONG | 1536 | 22.92 | 68.72 |
| 22 | `gpqa_53` | B | C | WRONG | 1536 | 21.11 | 74.44 |
| 23 | `gpqa_84` | B | None | WRONG | 1536 | 22.15 | 71.36 |
| 24 | `gpqa_80` | D | None | WRONG | 1536 | 24.67 | 138.29 |
| 25 | `gpqa_64` | D | None | WRONG | 1536 | 21.10 | 75.01 |
| 26 | `gpqa_73` | D | None | WRONG | 1536 | 23.64 | 66.71 |
| 27 | `gpqa_37` | A | None | WRONG | 1536 | 21.28 | 74.26 |
| 28 | `gpqa_126` | B | None | WRONG | 1536 | 21.53 | 72.80 |
| 29 | `gpqa_122` | B | B | CORRECT | 1536 | 21.33 | 73.74 |
| 30 | `gpqa_78` | A | None | WRONG | 1536 | 21.56 | 73.94 |
| 31 | `gpqa_160` | A | None | WRONG | 1536 | 20.66 | 76.70 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 21.13 | 74.72 |
| 33 | `gpqa_45` | C | None | WRONG | 1536 | 20.99 | 74.25 |
| 34 | `gpqa_184` | C | None | WRONG | 1536 | 22.52 | 69.80 |
| 35 | `gpqa_32` | B | None | WRONG | 1536 | 41.69 | 39.20 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 21.49 | 73.43 |
| 37 | `gpqa_192` | C | None | WRONG | 1536 | 22.14 | 70.81 |
| 38 | `gpqa_174` | B | None | WRONG | 1536 | 20.38 | 77.03 |
| 39 | `gpqa_10` | B | None | WRONG | 1536 | 21.37 | 74.50 |
| 40 | `gpqa_60` | D | None | WRONG | 1536 | 20.79 | 75.83 |
| 41 | `gpqa_170` | C | None | WRONG | 1536 | 20.87 | 75.41 |
| 42 | `gpqa_47` | A | None | WRONG | 1536 | 21.22 | 73.96 |
| 43 | `gpqa_131` | A | B | WRONG | 1536 | 20.34 | 77.80 |
| 44 | `gpqa_103` | B | B | CORRECT | 1536 | 20.57 | 76.58 |
| 45 | `gpqa_193` | D | None | WRONG | 2 | 30.14 | 2.02 |
| 46 | `gpqa_95` | D | None | WRONG | 1536 | 21.81 | 71.92 |
| 47 | `gpqa_144` | C | D | WRONG | 1536 | 21.26 | 73.47 |
| 48 | `gpqa_100` | D | None | WRONG | 1536 | 20.57 | 76.47 |
| 49 | `gpqa_142` | C | None | WRONG | 1536 | 21.74 | 73.53 |
| 50 | `gpqa_61` | B | None | WRONG | 1536 | 21.65 | 72.91 |
