# 50-Question GPQA Diamond Report: Exp 85: Corpus-Backed Constrained Suffix with High-Threshold Slot Cache (suffix_corpus + slot_similarity=0.50 + Autotune + MTP + 4K Ceiling)

- **Experiment ID:** `exp85_phys_pinning_28threads_repacked_iq4xs_muge_corpus_suffix_slot050_ceiling4096_q4kv`
- **Total Score (50Q):** **6 / 50 (12.0%)**
- **Standard 20Q Subset:** **3 / 20 (15.0%)**
- **Average Generation Speed:** **`21.34 tokens/second`**
- **Peak Generation Speed:** **`35.15 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 20.83 | 199.27 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 21.90 | 189.15 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 23.17 | 178.46 |
| 4 | `gpqa_156` | A | A | CORRECT | 1522 | 21.96 | 71.13 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 20.75 | 199.45 |
| 6 | `gpqa_12` | D | C | WRONG | 4096 | 26.79 | 155.24 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 20.38 | 202.40 |
| 8 | `gpqa_13` | B | B | CORRECT | 977 | 19.72 | 50.92 |
| 9 | `gpqa_127` | D | A | WRONG | 4096 | 19.21 | 229.81 |
| 10 | `gpqa_69` | C | None | WRONG | 4096 | 29.26 | 141.80 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 21.58 | 191.36 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 21.27 | 194.16 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 19.53 | 211.26 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 20.65 | 203.56 |
| 15 | `gpqa_169` | C | None | WRONG | 4096 | 22.27 | 185.36 |
| 16 | `gpqa_15` | D | None | WRONG | 4096 | 19.97 | 207.00 |
| 17 | `gpqa_159` | A | B | WRONG | 3671 | 21.05 | 383.63 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 20.64 | 199.95 |
| 19 | `gpqa_134` | D | None | WRONG | 4096 | 35.15 | 119.04 |
| 20 | `gpqa_44` | C | None | WRONG | 4096 | 20.93 | 197.30 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 22.55 | 183.63 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 21.48 | 192.44 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 20.34 | 203.69 |
| 24 | `gpqa_80` | D | None | WRONG | 4096 | 20.86 | 198.30 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 20.24 | 204.70 |
| 26 | `gpqa_73` | D | None | WRONG | 4096 | 22.59 | 182.90 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 19.97 | 207.32 |
| 28 | `gpqa_126` | B | None | WRONG | 4096 | 20.46 | 201.74 |
| 29 | `gpqa_122` | B | B | CORRECT | 4096 | 20.31 | 203.48 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 20.96 | 402.71 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 19.78 | 209.40 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 20.35 | 203.28 |
| 33 | `gpqa_45` | C | None | WRONG | 4096 | 21.40 | 192.63 |
| 34 | `gpqa_184` | C | None | WRONG | 4096 | 21.18 | 194.97 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 20.26 | 204.37 |
| 36 | `gpqa_52` | D | A | WRONG | 4096 | 19.56 | 211.44 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 20.56 | 200.78 |
| 38 | `gpqa_174` | B | None | WRONG | 4096 | 19.36 | 213.36 |
| 39 | `gpqa_10` | B | None | WRONG | 4096 | 19.85 | 208.91 |
| 40 | `gpqa_60` | D | A | WRONG | 4096 | 19.17 | 215.53 |
| 41 | `gpqa_170` | C | A | WRONG | 4096 | 19.37 | 213.31 |
| 42 | `gpqa_47` | A | None | WRONG | 14 | 16.27 | 2.70 |
| 43 | `gpqa_131` | A | A | CORRECT | 4096 | 19.68 | 210.24 |
| 44 | `gpqa_103` | B | A | WRONG | 3344 | 20.28 | 166.74 |
| 45 | `gpqa_193` | D | None | WRONG | 2 | 30.87 | 1.89 |
| 46 | `gpqa_95` | D | None | WRONG | 4096 | 21.39 | 192.76 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 19.23 | 214.28 |
| 48 | `gpqa_100` | D | None | WRONG | 4096 | 19.43 | 212.72 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 21.45 | 193.51 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 20.61 | 200.91 |
