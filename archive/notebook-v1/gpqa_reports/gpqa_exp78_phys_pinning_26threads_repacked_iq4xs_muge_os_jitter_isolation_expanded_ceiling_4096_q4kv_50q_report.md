# 50-Question GPQA Diamond Report: Exp 78: Pre-Repacked Offline GGUF + Merged Experts (-muge) + OS Jitter Isolation (26 Physical Compute Threads, 2 Cores Reserved for IO/OS) + Spec Autotune + MTP + 4K Ceiling

- **Experiment ID:** `exp78_phys_pinning_26threads_repacked_iq4xs_muge_os_jitter_isolation_expanded_ceiling_4096_q4kv`
- **Total Score (50Q):** **8 / 50 (16.0%)**
- **Standard 20Q Subset:** **5 / 20 (25.0%)**
- **Average Generation Speed:** **`19.47 tokens/second`**
- **Peak Generation Speed:** **`34.14 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | None | WRONG | 4096 | 18.04 | 229.42 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 19.15 | 215.89 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 19.91 | 207.38 |
| 4 | `gpqa_156` | A | A | CORRECT | 2465 | 18.83 | 132.60 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 18.01 | 229.54 |
| 6 | `gpqa_12` | D | None | WRONG | 4096 | 34.14 | 122.36 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 18.58 | 221.77 |
| 8 | `gpqa_13` | B | C | WRONG | 2190 | 18.42 | 120.27 |
| 9 | `gpqa_127` | D | D | CORRECT | 4096 | 31.39 | 147.73 |
| 10 | `gpqa_69` | C | None | WRONG | 4096 | 19.61 | 210.60 |
| 11 | `gpqa_3` | C | C | CORRECT | 1865 | 21.27 | 89.37 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 18.33 | 225.14 |
| 13 | `gpqa_30` | B | B | CORRECT | 4096 | 17.65 | 233.59 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 19.01 | 220.92 |
| 15 | `gpqa_169` | C | None | WRONG | 4096 | 22.29 | 185.47 |
| 16 | `gpqa_15` | D | D | CORRECT | 2331 | 19.98 | 118.55 |
| 17 | `gpqa_159` | A | C | WRONG | 3915 | 18.80 | 209.97 |
| 18 | `gpqa_36` | B | C | WRONG | 4096 | 18.55 | 222.33 |
| 19 | `gpqa_134` | D | None | WRONG | 4096 | 18.62 | 222.73 |
| 20 | `gpqa_44` | C | None | WRONG | 4096 | 18.71 | 220.52 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 19.79 | 208.72 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 19.23 | 214.82 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 18.18 | 227.39 |
| 24 | `gpqa_80` | D | None | WRONG | 4096 | 18.38 | 224.81 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 17.87 | 231.56 |
| 26 | `gpqa_73` | D | None | WRONG | 4096 | 19.57 | 210.98 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 18.97 | 439.49 |
| 28 | `gpqa_126` | B | A | WRONG | 4096 | 18.62 | 221.45 |
| 29 | `gpqa_122` | B | None | WRONG | 4096 | 18.57 | 222.59 |
| 30 | `gpqa_78` | A | A | CORRECT | 4096 | 17.33 | 239.28 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 18.11 | 228.26 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 18.54 | 222.98 |
| 33 | `gpqa_45` | C | None | WRONG | 4096 | 18.32 | 224.89 |
| 34 | `gpqa_184` | C | None | WRONG | 4096 | 19.00 | 217.39 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 28.51 | 146.16 |
| 36 | `gpqa_52` | D | None | WRONG | 4096 | 17.66 | 233.94 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 18.37 | 224.47 |
| 38 | `gpqa_174` | B | A | WRONG | 4096 | 17.56 | 235.09 |
| 39 | `gpqa_10` | B | None | WRONG | 4096 | 19.18 | 216.22 |
| 40 | `gpqa_60` | D | A | WRONG | 4096 | 17.35 | 237.92 |
| 41 | `gpqa_170` | C | None | WRONG | 4096 | 17.50 | 235.85 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 18.84 | 219.15 |
| 43 | `gpqa_131` | A | B | WRONG | 4096 | 18.22 | 227.11 |
| 44 | `gpqa_103` | B | B | CORRECT | 2847 | 19.25 | 149.69 |
| 45 | `gpqa_193` | D | A | WRONG | 4096 | 19.32 | 213.93 |
| 46 | `gpqa_95` | D | None | WRONG | 4096 | 19.25 | 214.35 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 17.62 | 233.64 |
| 48 | `gpqa_100` | D | None | WRONG | 4096 | 17.79 | 232.18 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 18.98 | 218.78 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 18.10 | 228.47 |
