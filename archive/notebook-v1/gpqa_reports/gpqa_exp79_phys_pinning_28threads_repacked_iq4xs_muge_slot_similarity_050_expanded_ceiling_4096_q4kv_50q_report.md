# 50-Question GPQA Diamond Report: Exp 79: Pre-Repacked Offline GGUF + Merged Experts (-muge) + High-Threshold Persistent Slot Cache (--slot-save-path /tmp/slots/ --slot-prompt-similarity 0.50) + Constrained Draft + MTP + 4K Ceiling

- **Experiment ID:** `exp79_phys_pinning_28threads_repacked_iq4xs_muge_slot_similarity_050_expanded_ceiling_4096_q4kv`
- **Total Score (50Q):** **9 / 50 (18.0%)**
- **Standard 20Q Subset:** **4 / 20 (20.0%)**
- **Average Generation Speed:** **`22.76 tokens/second`**
- **Peak Generation Speed:** **`41.10 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 20.82 | 199.19 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 21.82 | 189.72 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 22.97 | 179.93 |
| 4 | `gpqa_156` | A | A | CORRECT | 1212 | 22.24 | 56.21 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 20.70 | 199.98 |
| 6 | `gpqa_12` | D | C | WRONG | 4096 | 26.70 | 155.92 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 20.57 | 200.49 |
| 8 | `gpqa_13` | B | B | CORRECT | 977 | 19.59 | 51.34 |
| 9 | `gpqa_127` | D | C | WRONG | 4096 | 36.39 | 272.09 |
| 10 | `gpqa_69` | C | None | WRONG | 4096 | 28.96 | 143.21 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 21.45 | 192.38 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 19.74 | 209.38 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 20.32 | 203.30 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 21.09 | 199.28 |
| 15 | `gpqa_169` | C | None | WRONG | 4096 | 23.34 | 177.11 |
| 16 | `gpqa_15` | D | C | WRONG | 4096 | 20.92 | 197.58 |
| 17 | `gpqa_159` | A | A | CORRECT | 3524 | 19.99 | 177.92 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 24.18 | 170.82 |
| 19 | `gpqa_134` | D | A | WRONG | 2320 | 21.60 | 110.15 |
| 20 | `gpqa_44` | C | None | WRONG | 4096 | 24.09 | 171.61 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 21.97 | 188.11 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 20.13 | 204.97 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 21.18 | 195.53 |
| 24 | `gpqa_80` | D | None | WRONG | 4096 | 37.68 | 110.67 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 20.31 | 203.92 |
| 26 | `gpqa_73` | D | None | WRONG | 4096 | 22.31 | 185.38 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 30.48 | 136.46 |
| 28 | `gpqa_126` | B | None | WRONG | 4096 | 20.61 | 200.25 |
| 29 | `gpqa_122` | B | B | CORRECT | 4096 | 20.74 | 199.54 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 20.88 | 198.96 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 20.00 | 207.15 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 20.21 | 204.52 |
| 33 | `gpqa_45` | C | C | CORRECT | 4096 | 20.87 | 403.28 |
| 34 | `gpqa_184` | C | None | WRONG | 4096 | 20.86 | 198.13 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 41.10 | 101.93 |
| 36 | `gpqa_52` | D | None | WRONG | 4096 | 19.47 | 212.26 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 20.36 | 202.78 |
| 38 | `gpqa_174` | B | None | WRONG | 4096 | 20.06 | 206.04 |
| 39 | `gpqa_10` | B | None | WRONG | 4096 | 19.31 | 214.68 |
| 40 | `gpqa_60` | D | B | WRONG | 3254 | 19.70 | 167.10 |
| 41 | `gpqa_170` | C | A | WRONG | 4096 | 19.47 | 212.37 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 31.17 | 133.11 |
| 43 | `gpqa_131` | A | C | WRONG | 4096 | 19.82 | 209.00 |
| 44 | `gpqa_103` | B | B | CORRECT | 3072 | 20.58 | 151.32 |
| 45 | `gpqa_193` | D | None | WRONG | 2 | 30.84 | 1.87 |
| 46 | `gpqa_95` | D | D | CORRECT | 4096 | 20.83 | 198.23 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 20.20 | 406.23 |
| 48 | `gpqa_100` | D | B | WRONG | 4096 | 19.16 | 215.59 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 20.33 | 204.23 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 20.13 | 205.60 |
