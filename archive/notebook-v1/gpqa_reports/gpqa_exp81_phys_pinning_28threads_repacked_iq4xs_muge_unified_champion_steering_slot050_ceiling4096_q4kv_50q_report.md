# 50-Question GPQA Diamond Report: Exp 81: Unified Champion (Persistent Slot Cache similarity=0.50 + Concise Reasoning Steering 600 Words + Autotune + Constrained Suffix n_max=4 + MTP + 4K Ceiling)

- **Experiment ID:** `exp81_phys_pinning_28threads_repacked_iq4xs_muge_unified_champion_steering_slot050_ceiling4096_q4kv`
- **Total Score (50Q):** **11 / 50 (22.0%)**
- **Standard 20Q Subset:** **2 / 20 (10.0%)**
- **Average Generation Speed:** **`21.82 tokens/second`**
- **Peak Generation Speed:** **`36.93 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | B | WRONG | 4096 | 19.92 | 415.91 |
| 2 | `gpqa_42` | A | A | CORRECT | 4096 | 20.93 | 197.61 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 21.90 | 188.74 |
| 4 | `gpqa_156` | A | D | WRONG | 660 | 21.15 | 32.91 |
| 5 | `gpqa_128` | A | A | CORRECT | 4096 | 20.04 | 206.58 |
| 6 | `gpqa_12` | D | None | WRONG | 4096 | 36.93 | 113.30 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 28.20 | 146.86 |
| 8 | `gpqa_13` | B | None | WRONG | 4096 | 19.34 | 213.13 |
| 9 | `gpqa_127` | D | None | WRONG | 4096 | 36.29 | 257.24 |
| 10 | `gpqa_69` | C | None | WRONG | 4096 | 31.21 | 133.02 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 21.50 | 191.94 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 25.30 | 163.56 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 19.93 | 392.95 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 20.46 | 205.39 |
| 15 | `gpqa_169` | C | None | WRONG | 4096 | 22.13 | 186.78 |
| 16 | `gpqa_15` | D | None | WRONG | 4096 | 20.37 | 203.19 |
| 17 | `gpqa_159` | A | B | WRONG | 3168 | 20.86 | 153.86 |
| 18 | `gpqa_36` | B | C | WRONG | 4096 | 25.85 | 160.19 |
| 19 | `gpqa_134` | D | A | WRONG | 1333 | 20.88 | 66.51 |
| 20 | `gpqa_44` | C | None | WRONG | 4096 | 22.02 | 187.63 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 23.33 | 177.37 |
| 22 | `gpqa_53` | B | A | WRONG | 4096 | 20.91 | 197.61 |
| 23 | `gpqa_84` | B | B | CORRECT | 2703 | 21.15 | 129.88 |
| 24 | `gpqa_80` | D | None | WRONG | 4096 | 21.37 | 193.62 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 25.16 | 165.03 |
| 26 | `gpqa_73` | D | D | CORRECT | 3407 | 22.17 | 155.33 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 22.10 | 187.46 |
| 28 | `gpqa_126` | B | None | WRONG | 4096 | 19.99 | 206.44 |
| 29 | `gpqa_122` | B | None | WRONG | 4096 | 20.50 | 202.05 |
| 30 | `gpqa_78` | A | A | CORRECT | 4096 | 19.57 | 212.23 |
| 31 | `gpqa_160` | A | A | CORRECT | 3777 | 19.39 | 196.96 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 20.27 | 203.98 |
| 33 | `gpqa_45` | C | C | CORRECT | 3634 | 19.49 | 187.70 |
| 34 | `gpqa_184` | C | None | WRONG | 4096 | 20.91 | 197.69 |
| 35 | `gpqa_32` | B | B | CORRECT | 4096 | 19.83 | 209.04 |
| 36 | `gpqa_52` | D | A | WRONG | 4096 | 18.91 | 218.55 |
| 37 | `gpqa_192` | C | C | CORRECT | 3630 | 21.90 | 167.10 |
| 38 | `gpqa_174` | B | A | WRONG | 2216 | 19.63 | 114.81 |
| 39 | `gpqa_10` | B | A | WRONG | 3301 | 19.85 | 168.86 |
| 40 | `gpqa_60` | D | None | WRONG | 4096 | 19.42 | 212.98 |
| 41 | `gpqa_170` | C | None | WRONG | 4096 | 19.04 | 217.36 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 19.25 | 214.46 |
| 43 | `gpqa_131` | A | None | WRONG | 4096 | 20.77 | 199.71 |
| 44 | `gpqa_103` | B | B | CORRECT | 2065 | 21.69 | 97.14 |
| 45 | `gpqa_193` | D | D | CORRECT | 1871 | 23.08 | 82.85 |
| 46 | `gpqa_95` | D | None | WRONG | 10 | 16.79 | 2.15 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 19.45 | 211.92 |
| 48 | `gpqa_100` | D | None | WRONG | 4096 | 20.08 | 205.90 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 19.98 | 207.91 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 20.03 | 206.79 |
