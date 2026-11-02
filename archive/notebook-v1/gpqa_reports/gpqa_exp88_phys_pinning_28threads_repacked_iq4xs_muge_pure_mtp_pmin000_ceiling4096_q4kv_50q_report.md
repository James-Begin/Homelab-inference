# 50-Question GPQA Diamond Report: Exp 88: Unconstrained Pure Native MTP (p_min=0.0, Zero Threshold, No Suffix) + Direct NUMA Pinning + 4K Ceiling

- **Experiment ID:** `exp88_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_pmin000_ceiling4096_q4kv`
- **Total Score (50Q):** **11 / 50 (22.0%)**
- **Standard 20Q Subset:** **5 / 20 (25.0%)**
- **Average Generation Speed:** **`21.40 tokens/second`**
- **Peak Generation Speed:** **`23.36 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 20.49 | 202.55 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 21.56 | 191.87 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 22.29 | 185.30 |
| 4 | `gpqa_156` | A | A | CORRECT | 704 | 22.22 | 33.56 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 20.74 | 199.60 |
| 6 | `gpqa_12` | D | None | WRONG | 4096 | 22.13 | 187.35 |
| 7 | `gpqa_79` | D | A | WRONG | 4096 | 21.48 | 191.98 |
| 8 | `gpqa_13` | B | B | CORRECT | 1494 | 20.43 | 74.38 |
| 9 | `gpqa_127` | D | D | CORRECT | 4096 | 19.89 | 222.40 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 21.41 | 192.79 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 21.55 | 191.61 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 20.53 | 201.11 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 19.97 | 210.19 |
| 15 | `gpqa_169` | C | C | CORRECT | 2175 | 23.36 | 94.51 |
| 16 | `gpqa_15` | D | None | WRONG | 4096 | 20.81 | 198.53 |
| 17 | `gpqa_159` | A | None | WRONG | 4096 | 21.79 | 189.54 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 21.85 | 188.85 |
| 19 | `gpqa_134` | D | A | WRONG | 1572 | 22.73 | 71.50 |
| 20 | `gpqa_44` | C | A | WRONG | 2063 | 23.34 | 89.89 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 22.14 | 186.64 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 21.32 | 193.65 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 21.65 | 191.30 |
| 24 | `gpqa_80` | D | A | WRONG | 4096 | 20.22 | 204.38 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 20.37 | 203.41 |
| 26 | `gpqa_73` | D | None | WRONG | 4096 | 22.12 | 186.87 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 21.28 | 194.75 |
| 28 | `gpqa_126` | B | A | WRONG | 4096 | 21.32 | 193.41 |
| 29 | `gpqa_122` | B | C | WRONG | 3963 | 21.68 | 184.53 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 21.80 | 190.41 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 21.20 | 195.70 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 21.92 | 188.73 |
| 34 | `gpqa_184` | C | C | CORRECT | 2279 | 23.23 | 99.79 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 21.43 | 193.36 |
| 36 | `gpqa_52` | D | A | WRONG | 4096 | 20.18 | 204.73 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 21.19 | 195.36 |
| 38 | `gpqa_174` | B | None | WRONG | 4096 | 20.86 | 198.03 |
| 39 | `gpqa_10` | B | B | CORRECT | 4096 | 20.06 | 206.70 |
| 40 | `gpqa_60` | D | None | WRONG | 4096 | 20.83 | 198.43 |
| 41 | `gpqa_170` | C | C | CORRECT | 4096 | 20.58 | 200.93 |
| 42 | `gpqa_47` | A | C | WRONG | 4096 | 21.14 | 195.34 |
| 43 | `gpqa_131` | A | A | CORRECT | 4096 | 21.12 | 196.12 |
| 44 | `gpqa_103` | B | B | CORRECT | 1739 | 22.93 | 77.51 |
| 46 | `gpqa_95` | D | A | WRONG | 4096 | 22.42 | 184.23 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 22.02 | 187.23 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 20.68 | 200.49 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 21.05 | 196.74 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 21.87 | 188.57 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 20.99 | 197.56 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 21.28 | 194.59 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 20.79 | 199.14 |
