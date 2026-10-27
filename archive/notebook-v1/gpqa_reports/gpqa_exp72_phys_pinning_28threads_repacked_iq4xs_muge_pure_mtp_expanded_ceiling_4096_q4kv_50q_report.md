# 50-Question GPQA Diamond Report: Exp 72: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Pure Native MTP (No Suffix) + Expanded Token Ceiling (max_tokens=4096) + Direct NUMA Pinning (--numa numactl) + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp72_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_expanded_ceiling_4096_q4kv`
- **Total Score (50Q):** **11 / 50 (22.0%)**
- **Standard 20Q Subset:** **5 / 20 (25.0%)**
- **Average Generation Speed:** **`21.17 tokens/second`**
- **Peak Generation Speed:** **`23.14 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 20.32 | 204.33 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 21.37 | 193.88 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 22.22 | 185.94 |
| 4 | `gpqa_156` | A | A | CORRECT | 704 | 22.12 | 33.38 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 20.67 | 200.26 |
| 6 | `gpqa_12` | D | None | WRONG | 4096 | 22.05 | 188.00 |
| 7 | `gpqa_79` | D | A | WRONG | 4096 | 21.36 | 193.04 |
| 8 | `gpqa_13` | B | B | CORRECT | 1494 | 20.28 | 74.93 |
| 9 | `gpqa_127` | D | D | CORRECT | 4096 | 19.82 | 223.51 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 21.36 | 193.36 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 21.50 | 192.06 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 20.49 | 201.28 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 19.93 | 210.64 |
| 15 | `gpqa_169` | C | C | CORRECT | 2175 | 23.14 | 95.43 |
| 16 | `gpqa_15` | D | None | WRONG | 4096 | 20.57 | 200.85 |
| 17 | `gpqa_159` | A | None | WRONG | 4096 | 21.54 | 191.79 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 21.60 | 191.23 |
| 19 | `gpqa_134` | D | A | WRONG | 1572 | 22.49 | 72.26 |
| 20 | `gpqa_44` | C | A | WRONG | 2063 | 23.05 | 91.01 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 21.89 | 188.91 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 21.07 | 195.84 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 21.35 | 193.90 |
| 24 | `gpqa_80` | D | A | WRONG | 4096 | 20.08 | 206.10 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 20.24 | 204.33 |
| 26 | `gpqa_73` | D | None | WRONG | 4096 | 21.97 | 188.27 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 21.13 | 195.85 |
| 28 | `gpqa_126` | B | A | WRONG | 4096 | 21.13 | 195.44 |
| 29 | `gpqa_122` | B | C | WRONG | 3963 | 21.36 | 187.20 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 21.35 | 194.36 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 20.83 | 198.83 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 21.55 | 192.24 |
| 34 | `gpqa_184` | C | C | CORRECT | 2279 | 22.75 | 101.83 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 21.00 | 197.32 |
| 36 | `gpqa_52` | D | A | WRONG | 4096 | 20.77 | 199.00 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 21.03 | 196.03 |
| 38 | `gpqa_174` | B | None | WRONG | 4096 | 20.42 | 202.26 |
| 39 | `gpqa_10` | B | B | CORRECT | 4096 | 19.68 | 211.05 |
| 40 | `gpqa_60` | D | None | WRONG | 4096 | 20.42 | 202.69 |
| 41 | `gpqa_170` | C | C | CORRECT | 4096 | 20.18 | 204.72 |
| 42 | `gpqa_47` | A | C | WRONG | 4096 | 20.72 | 199.25 |
| 43 | `gpqa_131` | A | A | CORRECT | 4096 | 20.70 | 200.09 |
| 44 | `gpqa_103` | B | B | CORRECT | 1739 | 22.47 | 79.14 |
| 46 | `gpqa_95` | D | A | WRONG | 4096 | 22.13 | 186.56 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 21.74 | 189.67 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 20.42 | 203.30 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 20.80 | 199.05 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 21.70 | 189.89 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 20.44 | 203.19 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 20.72 | 199.52 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 20.76 | 199.10 |
