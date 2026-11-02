# 50-Question GPQA Diamond Report: Exp 60: Pre-Repacked Offline GGUF (IQ4_XS_R8 / Q4_0_R8) + Merged Experts (-muge) + Suffix Spec (n_max=8, match=5) + Prefix Cache Sharing (slot_prompt_similarity=0.20) + Native MTP + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp60_phys_pinning_28threads_repacked_iq4xs_muge_suffix_slot_similarity_q4kv`
- **Total Score (50Q):** **18 / 50 (36.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`20.97 tokens/second`**
- **Peak Generation Speed:** **`37.60 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 20.69 | 76.98 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 21.43 | 73.59 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 22.49 | 69.72 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 19.30 | 81.41 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 21.82 | 72.67 |
| 6 | `gpqa_12` | D | None | WRONG | 1536 | 37.60 | 43.23 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.65 | 75.76 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 18.76 | 83.37 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 20.92 | 90.52 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 20.40 | 77.11 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 24.07 | 65.28 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 21.36 | 73.76 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 20.68 | 75.58 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 21.82 | 75.66 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 21.88 | 71.80 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 20.41 | 77.01 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 19.76 | 79.42 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 20.15 | 77.68 |
| 19 | `gpqa_134` | D | B | WRONG | 1536 | 20.40 | 77.83 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 20.35 | 77.13 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 21.56 | 73.04 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 19.79 | 79.16 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 20.80 | 76.05 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 21.06 | 75.00 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.37 | 77.69 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 21.32 | 73.55 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 20.70 | 76.25 |
| 28 | `gpqa_126` | B | D | WRONG | 1536 | 19.00 | 82.36 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 21.11 | 74.60 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.22 | 78.83 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 20.10 | 78.70 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 20.91 | 75.53 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 19.56 | 79.71 |
| 34 | `gpqa_184` | C | C | CORRECT | 1185 | 20.34 | 59.81 |
| 35 | `gpqa_32` | B | None | WRONG | 1536 | 20.96 | 75.64 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.50 | 80.58 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 19.81 | 78.77 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 19.02 | 82.76 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 21.44 | 74.48 |
| 40 | `gpqa_60` | D | B | WRONG | 1536 | 19.66 | 79.96 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 19.31 | 81.33 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 19.41 | 80.69 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 19.77 | 79.89 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 20.79 | 75.65 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 20.82 | 75.70 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 20.75 | 75.64 |
| 47 | `gpqa_144` | C | C | CORRECT | 1536 | 18.73 | 83.08 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.05 | 82.33 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 26.48 | 60.72 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 21.12 | 74.75 |
