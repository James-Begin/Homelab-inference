# 50-Question GPQA Diamond Report: Exp 75: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Persistent Slot Cache (--slot-save-path /tmp/slots/ --slot-prompt-similarity 0.20) + Constrained Draft (n_max=4) + Direct NUMA Pinning + MTP (p_min=0.15) + Q4_0 KV + SER 2,0.5 + Expanded Ceiling (max_tokens=4096)

- **Experiment ID:** `exp75_phys_pinning_28threads_repacked_iq4xs_muge_persistent_slot_cache_expanded_ceiling_4096_q4kv`
- **Total Score (50Q):** **9 / 50 (18.0%)**
- **Standard 20Q Subset:** **4 / 20 (20.0%)**
- **Average Generation Speed:** **`22.49 tokens/second`**
- **Peak Generation Speed:** **`40.20 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 20.51 | 202.29 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 21.64 | 191.45 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 22.71 | 181.87 |
| 4 | `gpqa_156` | A | A | CORRECT | 1212 | 21.97 | 56.82 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 20.44 | 202.52 |
| 6 | `gpqa_12` | D | C | WRONG | 4096 | 26.42 | 157.58 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 20.40 | 202.01 |
| 8 | `gpqa_13` | B | B | CORRECT | 977 | 19.44 | 51.65 |
| 9 | `gpqa_127` | D | C | WRONG | 4096 | 36.21 | 274.00 |
| 10 | `gpqa_69` | C | None | WRONG | 4096 | 28.69 | 144.33 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 21.25 | 194.28 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 19.57 | 211.22 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 20.26 | 203.54 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 20.96 | 200.46 |
| 15 | `gpqa_169` | C | None | WRONG | 4096 | 23.01 | 179.50 |
| 16 | `gpqa_15` | D | C | WRONG | 4096 | 20.73 | 199.41 |
| 17 | `gpqa_159` | A | A | CORRECT | 3524 | 19.85 | 179.44 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 23.99 | 172.27 |
| 19 | `gpqa_134` | D | A | WRONG | 2320 | 21.42 | 110.87 |
| 20 | `gpqa_44` | C | None | WRONG | 4096 | 23.90 | 172.91 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 21.79 | 189.79 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 19.86 | 207.79 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 21.01 | 197.09 |
| 24 | `gpqa_80` | D | None | WRONG | 4096 | 37.02 | 112.45 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 19.86 | 208.32 |
| 26 | `gpqa_73` | D | None | WRONG | 4096 | 21.79 | 189.77 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 29.71 | 139.87 |
| 28 | `gpqa_126` | B | None | WRONG | 4096 | 20.31 | 203.12 |
| 29 | `gpqa_122` | B | B | CORRECT | 4096 | 20.46 | 202.00 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 20.47 | 202.79 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 18.63 | 222.09 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 20.30 | 203.67 |
| 33 | `gpqa_45` | C | C | CORRECT | 4096 | 20.63 | 406.08 |
| 34 | `gpqa_184` | C | None | WRONG | 4096 | 20.62 | 200.52 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 40.20 | 104.44 |
| 36 | `gpqa_52` | D | None | WRONG | 4096 | 19.12 | 216.28 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 19.99 | 206.28 |
| 38 | `gpqa_174` | B | None | WRONG | 4096 | 19.71 | 209.82 |
| 39 | `gpqa_10` | B | None | WRONG | 4096 | 18.98 | 218.37 |
| 40 | `gpqa_60` | D | B | WRONG | 3254 | 19.57 | 168.08 |
| 41 | `gpqa_170` | C | A | WRONG | 4096 | 19.37 | 213.28 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 30.97 | 133.83 |
| 43 | `gpqa_131` | A | C | WRONG | 4096 | 19.72 | 210.10 |
| 44 | `gpqa_103` | B | B | CORRECT | 3072 | 20.47 | 152.18 |
| 45 | `gpqa_193` | D | None | WRONG | 2 | 30.45 | 1.83 |
| 46 | `gpqa_95` | D | D | CORRECT | 4096 | 20.56 | 200.52 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 20.04 | 409.69 |
| 48 | `gpqa_100` | D | B | WRONG | 4096 | 19.01 | 217.30 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 20.21 | 205.21 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 20.18 | 204.76 |
