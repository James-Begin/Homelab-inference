# 50-Question GPQA Diamond Report: Exp 67: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Corpus-Backed Suffix Speculation (suffix_corpus) + Confidence MTP (p_min=0.15) + Direct NUMA Map Pinning (--numa numactl) + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp67_phys_pinning_28threads_repacked_iq4xs_muge_corpus_suffix_spec_q4kv`
- **Total Score (50Q):** **4 / 50 (8.0%)**
- **Standard 20Q Subset:** **1 / 20 (5.0%)**
- **Average Generation Speed:** **`21.47 tokens/second`**
- **Peak Generation Speed:** **`38.79 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 20.93 | 75.98 |
| 2 | `gpqa_42` | A | None | WRONG | 1536 | 21.79 | 72.49 |
| 3 | `gpqa_2` | B | None | WRONG | 1536 | 22.99 | 68.28 |
| 4 | `gpqa_156` | A | None | WRONG | 1536 | 19.69 | 79.72 |
| 5 | `gpqa_128` | A | None | WRONG | 1536 | 22.35 | 70.84 |
| 6 | `gpqa_12` | D | None | WRONG | 1536 | 38.79 | 41.86 |
| 7 | `gpqa_79` | D | None | WRONG | 1536 | 21.33 | 73.42 |
| 8 | `gpqa_13` | B | None | WRONG | 1536 | 19.35 | 80.76 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 21.41 | 88.41 |
| 10 | `gpqa_69` | C | None | WRONG | 1536 | 20.88 | 75.37 |
| 11 | `gpqa_3` | C | None | WRONG | 1536 | 24.60 | 63.88 |
| 12 | `gpqa_185` | A | None | WRONG | 1536 | 21.83 | 72.21 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 21.11 | 74.16 |
| 14 | `gpqa_165` | C | None | WRONG | 1536 | 22.23 | 74.20 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 22.22 | 70.69 |
| 16 | `gpqa_15` | D | None | WRONG | 1536 | 20.73 | 75.79 |
| 17 | `gpqa_159` | A | None | WRONG | 1536 | 20.08 | 78.36 |
| 18 | `gpqa_36` | B | None | WRONG | 1536 | 20.48 | 76.36 |
| 19 | `gpqa_134` | D | None | WRONG | 1536 | 20.73 | 76.53 |
| 20 | `gpqa_44` | C | None | WRONG | 1536 | 20.69 | 75.78 |
| 21 | `gpqa_5` | C | None | WRONG | 1536 | 21.89 | 72.03 |
| 22 | `gpqa_53` | B | None | WRONG | 1536 | 20.93 | 75.06 |
| 23 | `gpqa_84` | B | None | WRONG | 1536 | 21.08 | 74.92 |
| 24 | `gpqa_80` | D | None | WRONG | 1536 | 22.05 | 71.71 |
| 25 | `gpqa_64` | D | None | WRONG | 1536 | 20.42 | 77.28 |
| 26 | `gpqa_73` | D | None | WRONG | 1536 | 21.86 | 71.95 |
| 27 | `gpqa_37` | A | None | WRONG | 1536 | 20.61 | 76.70 |
| 28 | `gpqa_126` | B | None | WRONG | 1536 | 21.12 | 151.87 |
| 29 | `gpqa_122` | B | None | WRONG | 1536 | 21.06 | 74.73 |
| 30 | `gpqa_78` | A | None | WRONG | 1536 | 20.90 | 75.99 |
| 31 | `gpqa_160` | A | None | WRONG | 1536 | 20.31 | 77.71 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 21.06 | 74.88 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 19.98 | 78.07 |
| 34 | `gpqa_184` | C | C | CORRECT | 1075 | 21.20 | 52.23 |
| 35 | `gpqa_32` | B | None | WRONG | 1536 | 21.60 | 73.21 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 20.52 | 76.62 |
| 37 | `gpqa_192` | C | None | WRONG | 1536 | 20.49 | 76.40 |
| 38 | `gpqa_174` | B | None | WRONG | 1536 | 19.46 | 80.57 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 21.74 | 73.42 |
| 40 | `gpqa_60` | D | A | WRONG | 1536 | 19.75 | 79.56 |
| 41 | `gpqa_170` | C | None | WRONG | 1536 | 20.77 | 75.76 |
| 42 | `gpqa_47` | A | None | WRONG | 1536 | 19.56 | 79.99 |
| 43 | `gpqa_131` | A | None | WRONG | 1536 | 19.38 | 81.42 |
| 44 | `gpqa_103` | B | B | CORRECT | 1536 | 20.18 | 77.99 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 23.81 | 66.45 |
| 46 | `gpqa_95` | D | C | WRONG | 1536 | 21.37 | 73.41 |
| 47 | `gpqa_144` | C | None | WRONG | 1536 | 19.41 | 80.31 |
| 48 | `gpqa_100` | D | None | WRONG | 1536 | 19.85 | 79.01 |
| 49 | `gpqa_142` | C | None | WRONG | 1536 | 26.26 | 61.10 |
| 50 | `gpqa_61` | B | None | WRONG | 1536 | 20.79 | 75.95 |
