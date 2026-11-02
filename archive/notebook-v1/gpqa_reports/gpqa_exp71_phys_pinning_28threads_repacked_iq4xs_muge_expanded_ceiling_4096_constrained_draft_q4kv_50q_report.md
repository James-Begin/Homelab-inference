# 50-Question GPQA Diamond Report: Exp 71: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Expanded Token Ceiling (max_tokens=4096) + Constrained Draft Depth (n_max=4, depth=32) + Direct NUMA Pinning (--numa numactl) + Confidence MTP (p_min=0.15) + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp71_phys_pinning_28threads_repacked_iq4xs_muge_expanded_ceiling_4096_constrained_draft_q4kv`
- **Total Score (50Q):** **9 / 50 (18.0%)**
- **Standard 20Q Subset:** **4 / 20 (20.0%)**
- **Average Generation Speed:** **`22.43 tokens/second`**
- **Peak Generation Speed:** **`40.32 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 20.44 | 203.03 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 21.56 | 192.15 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 22.64 | 182.54 |
| 4 | `gpqa_156` | A | A | CORRECT | 1212 | 21.84 | 57.13 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 20.40 | 202.95 |
| 6 | `gpqa_12` | D | C | WRONG | 4096 | 26.36 | 157.64 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 20.30 | 203.24 |
| 8 | `gpqa_13` | B | B | CORRECT | 977 | 19.30 | 51.99 |
| 9 | `gpqa_127` | D | C | WRONG | 4096 | 36.06 | 275.85 |
| 10 | `gpqa_69` | C | None | WRONG | 4096 | 28.50 | 145.49 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 21.06 | 196.18 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 19.37 | 213.12 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 20.11 | 205.18 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 20.77 | 202.43 |
| 15 | `gpqa_169` | C | None | WRONG | 4096 | 22.85 | 180.97 |
| 16 | `gpqa_15` | D | C | WRONG | 4096 | 20.50 | 201.67 |
| 17 | `gpqa_159` | A | A | CORRECT | 3524 | 19.60 | 181.67 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 23.79 | 173.53 |
| 19 | `gpqa_134` | D | A | WRONG | 2320 | 21.34 | 111.26 |
| 20 | `gpqa_44` | C | None | WRONG | 4096 | 23.81 | 173.69 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 21.71 | 190.34 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 19.80 | 208.61 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 20.88 | 198.29 |
| 24 | `gpqa_80` | D | None | WRONG | 4096 | 37.00 | 112.80 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 19.95 | 207.52 |
| 26 | `gpqa_73` | D | None | WRONG | 4096 | 21.90 | 188.63 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 29.82 | 139.64 |
| 28 | `gpqa_126` | B | None | WRONG | 4096 | 20.23 | 203.92 |
| 29 | `gpqa_122` | B | B | CORRECT | 4096 | 20.36 | 203.32 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 20.50 | 202.40 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 19.63 | 210.82 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 20.04 | 206.37 |
| 33 | `gpqa_45` | C | C | CORRECT | 4096 | 20.64 | 407.32 |
| 34 | `gpqa_184` | C | None | WRONG | 4096 | 20.65 | 200.01 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 40.32 | 103.77 |
| 36 | `gpqa_52` | D | None | WRONG | 4096 | 19.35 | 213.39 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 20.22 | 204.17 |
| 38 | `gpqa_174` | B | None | WRONG | 4096 | 19.94 | 207.40 |
| 39 | `gpqa_10` | B | None | WRONG | 4096 | 19.20 | 215.81 |
| 40 | `gpqa_60` | D | B | WRONG | 3254 | 19.46 | 169.00 |
| 41 | `gpqa_170` | C | A | WRONG | 4096 | 19.27 | 214.42 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 30.78 | 134.55 |
| 43 | `gpqa_131` | A | C | WRONG | 4096 | 19.62 | 211.02 |
| 44 | `gpqa_103` | B | B | CORRECT | 3072 | 20.35 | 152.95 |
| 45 | `gpqa_193` | D | None | WRONG | 2 | 30.32 | 1.83 |
| 46 | `gpqa_95` | D | D | CORRECT | 4096 | 20.44 | 201.84 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 19.77 | 415.00 |
| 48 | `gpqa_100` | D | B | WRONG | 4096 | 18.78 | 220.16 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 19.96 | 207.90 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 19.95 | 207.45 |
