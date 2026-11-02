# 50-Question GPQA Diamond Report: Exp 77: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Pure Native MTP (p_min=0.05, No Suffix) + Expanded Ceiling (max_tokens=4096) + Direct NUMA Pinning

- **Experiment ID:** `exp77_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_pmin005_expanded_ceiling_4096_q4kv`
- **Total Score (50Q):** **11 / 50 (22.0%)**
- **Standard 20Q Subset:** **5 / 20 (25.0%)**
- **Average Generation Speed:** **`21.26 tokens/second`**
- **Peak Generation Speed:** **`23.23 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 20.47 | 202.51 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 21.57 | 191.90 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 22.14 | 186.53 |
| 4 | `gpqa_156` | A | A | CORRECT | 704 | 22.08 | 33.60 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 20.63 | 200.69 |
| 6 | `gpqa_12` | D | None | WRONG | 4096 | 22.02 | 188.61 |
| 7 | `gpqa_79` | D | A | WRONG | 4096 | 21.29 | 193.69 |
| 8 | `gpqa_13` | B | B | CORRECT | 1494 | 20.21 | 75.17 |
| 9 | `gpqa_127` | D | D | CORRECT | 4096 | 19.74 | 223.96 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 21.36 | 193.24 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 21.50 | 192.09 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 20.52 | 201.01 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 19.90 | 210.88 |
| 15 | `gpqa_169` | C | C | CORRECT | 2175 | 23.23 | 95.09 |
| 16 | `gpqa_15` | D | None | WRONG | 4096 | 20.69 | 199.66 |
| 17 | `gpqa_159` | A | None | WRONG | 4096 | 21.64 | 190.92 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 21.69 | 190.22 |
| 19 | `gpqa_134` | D | A | WRONG | 1572 | 22.60 | 72.34 |
| 20 | `gpqa_44` | C | A | WRONG | 2063 | 23.16 | 90.61 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 22.01 | 188.06 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 21.18 | 195.21 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 21.47 | 192.89 |
| 24 | `gpqa_80` | D | A | WRONG | 4096 | 20.08 | 205.83 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 20.23 | 204.80 |
| 26 | `gpqa_73` | D | None | WRONG | 4096 | 21.97 | 188.22 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 21.14 | 195.90 |
| 28 | `gpqa_126` | B | A | WRONG | 4096 | 21.18 | 194.78 |
| 29 | `gpqa_122` | B | C | WRONG | 3963 | 21.45 | 186.48 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 21.42 | 193.75 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 20.89 | 198.58 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 21.60 | 191.79 |
| 34 | `gpqa_184` | C | C | CORRECT | 2279 | 22.96 | 100.85 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 21.18 | 195.49 |
| 36 | `gpqa_52` | D | A | WRONG | 4096 | 20.95 | 197.66 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 21.22 | 194.34 |
| 38 | `gpqa_174` | B | None | WRONG | 4096 | 20.61 | 200.73 |
| 39 | `gpqa_10` | B | B | CORRECT | 4096 | 19.84 | 208.93 |
| 40 | `gpqa_60` | D | None | WRONG | 4096 | 20.58 | 200.94 |
| 41 | `gpqa_170` | C | C | CORRECT | 4096 | 20.34 | 203.10 |
| 42 | `gpqa_47` | A | C | WRONG | 4096 | 20.89 | 197.51 |
| 43 | `gpqa_131` | A | A | CORRECT | 4096 | 20.70 | 200.09 |
| 44 | `gpqa_103` | B | B | CORRECT | 1739 | 22.46 | 79.08 |
| 46 | `gpqa_95` | D | A | WRONG | 4096 | 22.15 | 186.05 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 21.79 | 189.25 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 20.67 | 200.93 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 20.96 | 197.29 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 21.84 | 188.59 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 20.82 | 199.58 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 21.11 | 195.90 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 20.90 | 197.90 |
