# 50-Question GPQA Diamond Report: Exp 70: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Suffix Speculation (n_max=6, match=4) + Spec Autotune + Direct NUMA Map Pinning (--numa numactl) + Confidence MTP (p_min=0.15) + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp70_phys_pinning_28threads_repacked_iq4xs_muge_suffix_autotune_numactl_q4kv`
- **Total Score (50Q):** **3 / 50 (6.0%)**
- **Standard 20Q Subset:** **1 / 20 (5.0%)**
- **Average Generation Speed:** **`21.13 tokens/second`**
- **Peak Generation Speed:** **`38.02 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 21.21 | 75.18 |
| 2 | `gpqa_42` | A | None | WRONG | 1536 | 20.60 | 76.47 |
| 3 | `gpqa_2` | B | None | WRONG | 1536 | 23.10 | 67.96 |
| 4 | `gpqa_156` | A | None | WRONG | 1536 | 19.39 | 80.86 |
| 5 | `gpqa_128` | A | None | WRONG | 1536 | 20.55 | 76.88 |
| 6 | `gpqa_12` | D | None | WRONG | 1536 | 38.02 | 42.91 |
| 7 | `gpqa_79` | D | None | WRONG | 1536 | 27.60 | 57.01 |
| 8 | `gpqa_13` | B | C | WRONG | 1536 | 18.63 | 83.87 |
| 9 | `gpqa_127` | D | None | WRONG | 1536 | 25.03 | 77.77 |
| 10 | `gpqa_69` | C | None | WRONG | 1536 | 21.00 | 74.76 |
| 11 | `gpqa_3` | C | None | WRONG | 1536 | 20.67 | 75.77 |
| 12 | `gpqa_185` | A | None | WRONG | 1536 | 19.49 | 80.47 |
| 13 | `gpqa_30` | B | D | WRONG | 1536 | 20.56 | 76.09 |
| 14 | `gpqa_165` | C | None | WRONG | 1536 | 20.13 | 81.39 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 22.61 | 69.43 |
| 16 | `gpqa_15` | D | None | WRONG | 1536 | 20.07 | 78.37 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 20.15 | 77.91 |
| 18 | `gpqa_36` | B | None | WRONG | 1536 | 19.87 | 78.85 |
| 19 | `gpqa_134` | D | C | WRONG | 1536 | 21.29 | 74.58 |
| 20 | `gpqa_44` | C | None | WRONG | 1536 | 20.27 | 77.36 |
| 21 | `gpqa_5` | C | None | WRONG | 1536 | 23.01 | 68.57 |
| 22 | `gpqa_53` | B | None | WRONG | 1536 | 20.06 | 78.12 |
| 23 | `gpqa_84` | B | None | WRONG | 1536 | 19.83 | 79.55 |
| 24 | `gpqa_80` | D | D | CORRECT | 1536 | 20.36 | 77.44 |
| 25 | `gpqa_64` | D | None | WRONG | 1536 | 19.08 | 82.66 |
| 26 | `gpqa_73` | D | None | WRONG | 1536 | 20.66 | 76.06 |
| 27 | `gpqa_37` | A | None | WRONG | 1536 | 20.46 | 77.37 |
| 28 | `gpqa_126` | B | C | WRONG | 1536 | 21.17 | 73.94 |
| 29 | `gpqa_122` | B | None | WRONG | 1536 | 20.60 | 76.43 |
| 30 | `gpqa_78` | A | None | WRONG | 1536 | 20.33 | 78.04 |
| 31 | `gpqa_160` | A | None | WRONG | 1536 | 19.29 | 81.93 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 20.36 | 77.29 |
| 33 | `gpqa_45` | C | None | WRONG | 1536 | 18.71 | 83.22 |
| 34 | `gpqa_184` | C | C | CORRECT | 1042 | 20.60 | 52.12 |
| 35 | `gpqa_32` | B | None | WRONG | 1536 | 34.11 | 47.30 |
| 36 | `gpqa_52` | D | B | WRONG | 1536 | 19.70 | 79.77 |
| 37 | `gpqa_192` | C | None | WRONG | 1536 | 19.51 | 80.16 |
| 38 | `gpqa_174` | B | None | WRONG | 1536 | 18.45 | 85.16 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 20.75 | 76.51 |
| 40 | `gpqa_60` | D | None | WRONG | 1536 | 19.69 | 79.88 |
| 41 | `gpqa_170` | C | None | WRONG | 1536 | 19.71 | 79.78 |
| 42 | `gpqa_47` | A | None | WRONG | 1536 | 18.67 | 83.81 |
| 43 | `gpqa_131` | A | None | WRONG | 1536 | 19.84 | 79.58 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 19.83 | 79.31 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 23.38 | 67.51 |
| 46 | `gpqa_95` | D | None | WRONG | 1536 | 19.58 | 79.85 |
| 47 | `gpqa_144` | C | None | WRONG | 1536 | 19.59 | 79.66 |
| 48 | `gpqa_100` | D | B | WRONG | 1536 | 19.60 | 80.18 |
| 49 | `gpqa_142` | C | None | WRONG | 1536 | 19.67 | 80.69 |
| 50 | `gpqa_61` | B | None | WRONG | 1536 | 19.75 | 79.86 |
