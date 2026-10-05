# 50-Question GPQA Diamond Report: Exp 73: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Corpus-Backed Suffix Speculation (suffix_corpus, n_max=4) + Confidence MTP (p_min=0.15) + Direct NUMA Pinning + Expanded Ceiling (max_tokens=4096)

- **Experiment ID:** `exp73_phys_pinning_28threads_repacked_iq4xs_muge_corpus_suffix_expanded_ceiling_4096_q4kv`
- **Total Score (50Q):** **6 / 50 (12.0%)**
- **Standard 20Q Subset:** **3 / 20 (15.0%)**
- **Average Generation Speed:** **`20.87 tokens/second`**
- **Peak Generation Speed:** **`34.14 tokens/second`**
- **Token Ceiling:** 4096 tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 4096 | 20.36 | 203.71 |
| 2 | `gpqa_42` | A | None | WRONG | 4096 | 21.29 | 194.58 |
| 3 | `gpqa_2` | B | None | WRONG | 4096 | 22.41 | 184.50 |
| 4 | `gpqa_156` | A | A | CORRECT | 1522 | 21.19 | 73.61 |
| 5 | `gpqa_128` | A | None | WRONG | 4096 | 20.09 | 206.05 |
| 6 | `gpqa_12` | D | C | WRONG | 4096 | 25.97 | 160.07 |
| 7 | `gpqa_79` | D | None | WRONG | 4096 | 19.69 | 209.34 |
| 8 | `gpqa_13` | B | B | CORRECT | 977 | 19.17 | 52.44 |
| 9 | `gpqa_127` | D | A | WRONG | 4096 | 18.66 | 236.02 |
| 10 | `gpqa_69` | C | None | WRONG | 4096 | 28.21 | 146.98 |
| 11 | `gpqa_3` | C | None | WRONG | 4096 | 20.87 | 197.93 |
| 12 | `gpqa_185` | A | None | WRONG | 4096 | 20.65 | 200.30 |
| 13 | `gpqa_30` | B | None | WRONG | 4096 | 18.94 | 217.66 |
| 14 | `gpqa_165` | C | None | WRONG | 4096 | 20.02 | 209.95 |
| 15 | `gpqa_169` | C | None | WRONG | 4096 | 21.63 | 190.91 |
| 16 | `gpqa_15` | D | None | WRONG | 4096 | 19.27 | 214.33 |
| 17 | `gpqa_159` | A | B | WRONG | 3671 | 20.32 | 397.29 |
| 18 | `gpqa_36` | B | None | WRONG | 4096 | 20.11 | 205.39 |
| 19 | `gpqa_134` | D | None | WRONG | 4096 | 34.14 | 122.62 |
| 20 | `gpqa_44` | C | None | WRONG | 4096 | 20.43 | 202.29 |
| 21 | `gpqa_5` | C | None | WRONG | 4096 | 21.93 | 188.50 |
| 22 | `gpqa_53` | B | None | WRONG | 4096 | 20.78 | 198.59 |
| 23 | `gpqa_84` | B | B | CORRECT | 4096 | 19.66 | 210.53 |
| 24 | `gpqa_80` | D | None | WRONG | 4096 | 20.42 | 202.72 |
| 25 | `gpqa_64` | D | None | WRONG | 4096 | 19.84 | 208.72 |
| 26 | `gpqa_73` | D | None | WRONG | 4096 | 22.21 | 186.16 |
| 27 | `gpqa_37` | A | None | WRONG | 4096 | 19.59 | 211.32 |
| 28 | `gpqa_126` | B | None | WRONG | 4096 | 20.01 | 205.96 |
| 29 | `gpqa_122` | B | B | CORRECT | 4096 | 19.87 | 207.88 |
| 30 | `gpqa_78` | A | None | WRONG | 4096 | 20.50 | 411.94 |
| 31 | `gpqa_160` | A | None | WRONG | 4096 | 19.37 | 213.67 |
| 32 | `gpqa_66` | C | None | WRONG | 4096 | 20.08 | 205.95 |
| 33 | `gpqa_45` | C | None | WRONG | 4096 | 21.02 | 195.96 |
| 34 | `gpqa_184` | C | None | WRONG | 4096 | 20.90 | 197.62 |
| 35 | `gpqa_32` | B | None | WRONG | 4096 | 20.15 | 205.52 |
| 36 | `gpqa_52` | D | A | WRONG | 4096 | 19.43 | 212.63 |
| 37 | `gpqa_192` | C | None | WRONG | 4096 | 20.49 | 201.25 |
| 38 | `gpqa_174` | B | None | WRONG | 4096 | 19.35 | 213.36 |
| 39 | `gpqa_10` | B | None | WRONG | 4096 | 19.77 | 209.76 |
| 40 | `gpqa_60` | D | A | WRONG | 4096 | 19.11 | 216.36 |
| 41 | `gpqa_170` | C | A | WRONG | 4096 | 19.27 | 214.33 |
| 42 | `gpqa_47` | A | None | WRONG | 14 | 16.19 | 2.44 |
| 43 | `gpqa_131` | A | A | CORRECT | 4096 | 19.31 | 214.47 |
| 44 | `gpqa_103` | B | A | WRONG | 3344 | 19.90 | 170.02 |
| 45 | `gpqa_193` | D | None | WRONG | 2 | 30.39 | 1.97 |
| 46 | `gpqa_95` | D | None | WRONG | 4096 | 20.97 | 196.73 |
| 47 | `gpqa_144` | C | None | WRONG | 4096 | 18.85 | 218.50 |
| 48 | `gpqa_100` | D | None | WRONG | 4096 | 19.11 | 216.14 |
| 49 | `gpqa_142` | C | None | WRONG | 4096 | 21.15 | 196.47 |
| 50 | `gpqa_61` | B | None | WRONG | 4096 | 20.20 | 204.91 |
