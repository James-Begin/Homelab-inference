# 50-Question GPQA Diamond Report: Exp 74: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Speculative Autotuning (--spec-autotune) + Constrained Suffix (n_max=4) + Confidence MTP (p_min=0.15) + Direct NUMA Pinning + Expanded Ceiling (max_tokens=4096)

- **Experiment ID:** `exp74_phys_pinning_28threads_repacked_iq4xs_muge_suffix_autotune_expanded_ceiling_4096_q4kv`
- **Total Score (50Q):** **9 / 50 (18.0%)**
- **Standard 20Q Subset:** **4 / 20 (20.0%)**
- **Average Generation Speed:** **`22.67 tokens/second`**
- **Peak Generation Speed:** **`41.05 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 20.66 | 201.00 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 21.70 | 190.85 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 22.78 | 181.40 |
| 4 | `gpqa_156` | A | A | CORRECT | 1212 | 22.10 | 56.50 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 20.57 | 201.30 |
| 6 | `gpqa_12` | D | C | WRONG | 4096 | 26.56 | 156.55 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 20.50 | 201.08 |
| 8 | `gpqa_13` | B | B | CORRECT | 977 | 19.50 | 51.51 |
| 9 | `gpqa_127` | D | C | WRONG | 4096 | 36.28 | 273.50 |
| 10 | `gpqa_69` | C | None | WRONG | 4096 | 28.77 | 144.02 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 21.35 | 193.50 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 19.65 | 210.05 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 20.35 | 202.95 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 21.08 | 199.45 |
| 15 | `gpqa_169` | C | None | WRONG | 4096 | 23.25 | 177.73 |
| 16 | `gpqa_15` | D | C | WRONG | 4096 | 20.87 | 198.20 |
| 17 | `gpqa_159` | A | A | CORRECT | 3524 | 19.93 | 178.38 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 24.05 | 171.65 |
| 19 | `gpqa_134` | D | A | WRONG | 2320 | 21.51 | 110.41 |
| 20 | `gpqa_44` | C | None | WRONG | 4096 | 23.99 | 172.26 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 21.86 | 189.31 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 19.95 | 206.82 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 21.08 | 196.75 |
| 24 | `gpqa_80` | D | None | WRONG | 4096 | 37.33 | 111.60 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 20.11 | 206.08 |
| 26 | `gpqa_73` | D | None | WRONG | 4096 | 22.08 | 187.30 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 30.12 | 137.99 |
| 28 | `gpqa_126` | B | None | WRONG | 4096 | 20.42 | 202.21 |
| 29 | `gpqa_122` | B | B | CORRECT | 4096 | 20.54 | 201.52 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 20.69 | 200.86 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 19.82 | 209.06 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 20.23 | 204.68 |
| 33 | `gpqa_45` | C | C | CORRECT | 4096 | 20.90 | 402.22 |
| 34 | `gpqa_184` | C | None | WRONG | 4096 | 20.89 | 197.94 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 41.05 | 102.08 |
| 36 | `gpqa_52` | D | None | WRONG | 4096 | 19.54 | 211.66 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 20.40 | 202.26 |
| 38 | `gpqa_174` | B | None | WRONG | 4096 | 20.11 | 205.49 |
| 39 | `gpqa_10` | B | None | WRONG | 4096 | 19.38 | 213.99 |
| 40 | `gpqa_60` | D | B | WRONG | 3254 | 19.79 | 166.17 |
| 41 | `gpqa_170` | C | A | WRONG | 4096 | 19.57 | 211.24 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 31.11 | 133.13 |
| 43 | `gpqa_131` | A | C | WRONG | 4096 | 19.85 | 208.72 |
| 44 | `gpqa_103` | B | B | CORRECT | 3072 | 20.60 | 150.93 |
| 45 | `gpqa_193` | D | None | WRONG | 2 | 30.44 | 2.04 |
| 46 | `gpqa_95` | D | D | CORRECT | 4096 | 20.70 | 199.47 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 20.05 | 409.62 |
| 48 | `gpqa_100` | D | B | WRONG | 4096 | 19.00 | 217.34 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 20.19 | 205.86 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 20.19 | 204.94 |
