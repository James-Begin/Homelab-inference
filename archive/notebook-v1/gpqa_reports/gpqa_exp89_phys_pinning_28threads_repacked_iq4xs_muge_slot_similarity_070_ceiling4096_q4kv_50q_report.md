# 50-Question GPQA Diamond Report: Exp 89: Ultra-Selective Persistent Slot Cache (similarity=0.70, /tmp/slots/) + Constrained Draft + Autotune + MTP + 4K Ceiling

- **Experiment ID:** `exp89_phys_pinning_28threads_repacked_iq4xs_muge_slot_similarity_070_ceiling4096_q4kv`
- **Total Score (50Q):** **9 / 50 (18.0%)**
- **Standard 20Q Subset:** **4 / 20 (20.0%)**
- **Average Generation Speed:** **`22.58 tokens/second`**
- **Peak Generation Speed:** **`40.66 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 20.64 | 201.02 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 21.68 | 191.05 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 22.76 | 181.62 |
| 4 | `gpqa_156` | A | A | CORRECT | 1212 | 22.24 | 56.23 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 20.41 | 202.70 |
| 6 | `gpqa_12` | D | C | WRONG | 4096 | 26.35 | 158.03 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 20.55 | 200.79 |
| 8 | `gpqa_13` | B | B | CORRECT | 977 | 19.14 | 52.59 |
| 9 | `gpqa_127` | D | C | WRONG | 4096 | 35.87 | 275.95 |
| 10 | `gpqa_69` | C | None | WRONG | 4096 | 28.71 | 144.38 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 21.41 | 192.81 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 19.62 | 210.67 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 20.41 | 202.04 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 20.90 | 201.04 |
| 15 | `gpqa_169` | C | None | WRONG | 4096 | 23.31 | 177.25 |
| 16 | `gpqa_15` | D | C | WRONG | 4096 | 20.74 | 199.45 |
| 17 | `gpqa_159` | A | A | CORRECT | 3524 | 19.78 | 180.08 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 24.10 | 171.34 |
| 19 | `gpqa_134` | D | A | WRONG | 2320 | 21.44 | 110.96 |
| 20 | `gpqa_44` | C | None | WRONG | 4096 | 23.92 | 172.86 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 21.81 | 189.48 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 19.71 | 209.40 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 20.87 | 198.60 |
| 24 | `gpqa_80` | D | None | WRONG | 4096 | 36.94 | 112.72 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 19.89 | 208.30 |
| 26 | `gpqa_73` | D | None | WRONG | 4096 | 21.79 | 189.50 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 29.80 | 139.48 |
| 28 | `gpqa_126` | B | None | WRONG | 4096 | 20.39 | 202.34 |
| 29 | `gpqa_122` | B | B | CORRECT | 4096 | 20.37 | 203.17 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 20.33 | 203.99 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 19.61 | 211.09 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 20.22 | 204.63 |
| 33 | `gpqa_45` | C | C | CORRECT | 4096 | 20.62 | 406.48 |
| 34 | `gpqa_184` | C | None | WRONG | 4096 | 20.74 | 199.40 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 40.66 | 103.03 |
| 36 | `gpqa_52` | D | None | WRONG | 4096 | 19.58 | 211.08 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 20.37 | 202.67 |
| 38 | `gpqa_174` | B | None | WRONG | 4096 | 20.12 | 205.49 |
| 39 | `gpqa_10` | B | None | WRONG | 4096 | 19.33 | 214.56 |
| 40 | `gpqa_60` | D | B | WRONG | 3254 | 19.78 | 166.27 |
| 41 | `gpqa_170` | C | A | WRONG | 4096 | 19.38 | 213.32 |
| 42 | `gpqa_47` | A | None | WRONG | 4096 | 31.09 | 133.34 |
| 43 | `gpqa_131` | A | C | WRONG | 4096 | 19.88 | 208.22 |
| 44 | `gpqa_103` | B | B | CORRECT | 3072 | 20.56 | 151.49 |
| 45 | `gpqa_193` | D | None | WRONG | 2 | 30.97 | 1.99 |
| 46 | `gpqa_95` | D | D | CORRECT | 4096 | 20.70 | 199.34 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 20.03 | 409.67 |
| 48 | `gpqa_100` | D | B | WRONG | 4096 | 19.03 | 217.29 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 20.14 | 206.07 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 20.11 | 205.55 |
