# 50-Question GPQA Diamond Report: Exp 83: Calibrated Sampling Dynamics (T=0.3, top_p=0.95 + Persistent Slot Cache similarity=0.50 + Autotune + Suffix n_max=4 + MTP + 4K Ceiling)

- **Experiment ID:** `exp83_phys_pinning_28threads_repacked_iq4xs_muge_calibrated_temperature_slot050_ceiling4096_q4kv`
- **Total Score (50Q):** **7 / 50 (14.0%)**
- **Standard 20Q Subset:** **4 / 20 (20.0%)**
- **Average Generation Speed:** **`21.43 tokens/second`**
- **Peak Generation Speed:** **`34.05 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 20.45 | 203.16 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 21.41 | 193.22 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 22.39 | 184.57 |
| 4 | `gpqa_156` | A | A | CORRECT | 2163 | 22.10 | 99.64 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 20.18 | 205.02 |
| 6 | `gpqa_12` | D | None | WRONG | 4096 | 32.42 | 128.65 |
| 7 | `gpqa_79` | D | B | WRONG | 4096 | 20.69 | 199.42 |
| 8 | `gpqa_13` | B | C | WRONG | 2192 | 19.16 | 115.67 |
| 9 | `gpqa_127` | D | D | CORRECT | 4096 | 34.05 | 136.71 |
| 10 | `gpqa_69` | C | None | WRONG | 4096 | 27.57 | 150.20 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 20.59 | 200.58 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 19.93 | 207.42 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 18.97 | 217.36 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 20.98 | 200.33 |
| 15 | `gpqa_169` | C | C | CORRECT | 1289 | 22.94 | 57.74 |
| 16 | `gpqa_15` | D | None | WRONG | 4096 | 19.54 | 211.31 |
| 17 | `gpqa_159` | A | B | WRONG | 4096 | 19.44 | 422.40 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 21.23 | 194.66 |
| 19 | `gpqa_134` | D | A | WRONG | 1988 | 21.44 | 95.18 |
| 20 | `gpqa_44` | C | None | WRONG | 4096 | 27.04 | 153.07 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 21.77 | 190.09 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 19.78 | 208.72 |
| 23 | `gpqa_84` | B | B | CORRECT | 4078 | 19.99 | 206.13 |
| 24 | `gpqa_80` | D | A | WRONG | 4096 | 19.85 | 410.95 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 19.37 | 213.86 |
| 26 | `gpqa_73` | D | None | WRONG | 4096 | 21.24 | 194.32 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 19.85 | 418.61 |
| 28 | `gpqa_126` | B | C | WRONG | 4096 | 20.07 | 205.51 |
| 29 | `gpqa_122` | B | B | CORRECT | 3722 | 20.21 | 186.04 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 19.67 | 210.76 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 19.21 | 215.64 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 20.42 | 202.59 |
| 33 | `gpqa_45` | C | None | WRONG | 4096 | 20.97 | 608.53 |
| 34 | `gpqa_184` | C | None | WRONG | 4096 | 20.67 | 199.73 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 20.29 | 204.04 |
| 36 | `gpqa_52` | D | A | WRONG | 4096 | 19.75 | 209.47 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 19.36 | 413.43 |
| 38 | `gpqa_174` | B | None | WRONG | 4096 | 19.47 | 212.33 |
| 39 | `gpqa_10` | B | A | WRONG | 3806 | 19.40 | 198.91 |
| 40 | `gpqa_60` | D | B | WRONG | 3997 | 19.73 | 204.35 |
| 41 | `gpqa_170` | C | A | WRONG | 4096 | 19.11 | 216.49 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 28.31 | 146.33 |
| 43 | `gpqa_131` | A | A | CORRECT | 4096 | 20.14 | 205.94 |
| 44 | `gpqa_103` | B | A | WRONG | 1666 | 21.52 | 79.15 |
| 45 | `gpqa_193` | D | None | WRONG | 2 | 30.88 | 1.95 |
| 46 | `gpqa_95` | D | A | WRONG | 4096 | 20.43 | 201.99 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 19.17 | 215.00 |
| 48 | `gpqa_100` | D | A | WRONG | 4096 | 19.49 | 212.09 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 19.12 | 217.24 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 19.53 | 211.63 |
