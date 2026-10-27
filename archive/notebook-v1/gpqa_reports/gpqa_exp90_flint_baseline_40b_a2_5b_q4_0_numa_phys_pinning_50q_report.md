# 50-Question GPQA Diamond Report: Exp 90: Recursive Flint 40B MoE (A2.5B Active) Q4_0 Baseline (Pure Dual-Socket NUMA Interleave, 28 Physical Cores, Flash Attention, 4K Ceiling)

- **Experiment ID:** `exp90_flint_baseline_40b_a2_5b_q4_0_numa_phys_pinning`
- **Total Score (50Q):** **17 / 50 (34.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`9.97 tokens/second`**
- **Peak Generation Speed:** **`10.93 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | None | WRONG | 4096 | 9.83 | 419.52 |
| 2 | `gpqa_42` | A | A | CORRECT | 4096 | 9.91 | 415.23 |
| 3 | `gpqa_2` | B | B | CORRECT | 613 | 10.77 | 58.46 |
| 4 | `gpqa_156` | A | A | CORRECT | 373 | 10.83 | 36.32 |
| 5 | `gpqa_128` | A | C | WRONG | 4096 | 9.93 | 414.58 |
| 6 | `gpqa_12` | D | C | WRONG | 4096 | 9.88 | 417.07 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 9.99 | 411.27 |
| 8 | `gpqa_13` | B | C | WRONG | 4096 | 9.93 | 413.84 |
| 9 | `gpqa_127` | D | A | WRONG | 4096 | 9.19 | 468.86 |
| 10 | `gpqa_69` | C | A | WRONG | 4096 | 9.75 | 421.77 |
| 11 | `gpqa_3` | C | C | CORRECT | 4096 | 9.79 | 419.86 |
| 12 | `gpqa_185` | A | C | WRONG | 4096 | 9.76 | 421.27 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 9.83 | 418.18 |
| 14 | `gpqa_165` | C | A | WRONG | 4096 | 9.58 | 434.30 |
| 15 | `gpqa_169` | C | C | CORRECT | 1907 | 10.22 | 188.00 |
| 16 | `gpqa_15` | D | None | WRONG | 4096 | 9.77 | 421.21 |
| 17 | `gpqa_159` | A | A | CORRECT | 1629 | 10.26 | 160.50 |
| 18 | `gpqa_36` | B | C | WRONG | 4096 | 9.82 | 418.61 |
| 19 | `gpqa_134` | D | D | CORRECT | 1723 | 10.23 | 171.04 |
| 20 | `gpqa_44` | C | C | CORRECT | 2955 | 10.04 | 295.99 |
| 21 | `gpqa_5` | C | C | CORRECT | 1452 | 10.31 | 142.65 |
| 22 | `gpqa_53` | B | A | WRONG | 4096 | 9.81 | 419.08 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 9.78 | 421.14 |
| 24 | `gpqa_80` | D | A | WRONG | 4096 | 9.75 | 422.14 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 9.74 | 422.82 |
| 26 | `gpqa_73` | D | D | CORRECT | 2134 | 10.13 | 212.10 |
| 27 | `gpqa_37` | A | B | WRONG | 4096 | 9.77 | 421.92 |
| 28 | `gpqa_126` | B | None | WRONG | 4096 | 9.84 | 417.63 |
| 29 | `gpqa_122` | B | B | CORRECT | 3019 | 10.02 | 303.04 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 9.73 | 424.12 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 9.75 | 422.82 |
| 32 | `gpqa_66` | C | C | CORRECT | 1191 | 10.30 | 117.71 |
| 33 | `gpqa_45` | C | None | WRONG | 4096 | 9.83 | 417.67 |
| 34 | `gpqa_184` | C | C | CORRECT | 225 | 10.93 | 22.09 |
| 35 | `gpqa_32` | B | C | WRONG | 4096 | 9.76 | 422.15 |
| 36 | `gpqa_52` | D | None | WRONG | 4096 | 9.77 | 421.07 |
| 37 | `gpqa_192` | C | B | WRONG | 455 | 10.65 | 44.05 |
| 38 | `gpqa_174` | B | D | WRONG | 1264 | 10.29 | 124.70 |
| 39 | `gpqa_10` | B | C | WRONG | 4096 | 9.76 | 422.99 |
| 40 | `gpqa_60` | D | None | WRONG | 4096 | 9.78 | 420.64 |
| 41 | `gpqa_170` | C | A | WRONG | 4096 | 9.73 | 422.87 |
| 42 | `gpqa_47` | A | C | WRONG | 4096 | 9.79 | 419.90 |
| 43 | `gpqa_131` | A | None | WRONG | 4096 | 9.71 | 424.63 |
| 44 | `gpqa_103` | B | B | CORRECT | 949 | 10.47 | 92.56 |
| 45 | `gpqa_193` | D | D | CORRECT | 769 | 10.49 | 75.12 |
| 46 | `gpqa_95` | D | D | CORRECT | 1990 | 10.21 | 196.27 |
| 47 | `gpqa_144` | C | A | WRONG | 4096 | 9.81 | 418.64 |
| 48 | `gpqa_100` | D | None | WRONG | 4096 | 9.79 | 420.05 |
| 49 | `gpqa_142` | C | B | WRONG | 4096 | 9.74 | 423.64 |
| 50 | `gpqa_61` | B | A | WRONG | 4096 | 9.77 | 421.12 |
