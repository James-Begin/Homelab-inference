# 50-Question GPQA Diamond Report: Exp 57: Pre-Repacked Offline GGUF (IQ4_XS_R8 / Q4_0_R8) + Merged Experts (-muge) + Calibrated Precision Suffix (n_max=8, match=5) + Confidence-Gated MTP (n_max=1, p_min=0.15) + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp57_phys_pinning_28threads_repacked_iq4xs_muge_suffix_mtp_pmin015_q4kv`
- **Total Score (50Q):** **18 / 50 (36.0%)**
- **Standard 20Q Subset:** **8 / 20 (40.0%)**
- **Average Generation Speed:** **`21.10 tokens/second`**
- **Peak Generation Speed:** **`37.99 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 19.85 | 80.33 |
| 2 | `gpqa_42` | A | A | CORRECT | 1536 | 20.91 | 75.57 |
| 3 | `gpqa_2` | B | B | CORRECT | 1536 | 22.74 | 69.07 |
| 4 | `gpqa_156` | A | A | CORRECT | 1536 | 19.53 | 80.45 |
| 5 | `gpqa_128` | A | A | CORRECT | 1536 | 22.07 | 71.69 |
| 6 | `gpqa_12` | D | None | WRONG | 1536 | 37.99 | 42.90 |
| 7 | `gpqa_79` | D | A | WRONG | 1536 | 20.90 | 74.83 |
| 8 | `gpqa_13` | B | B | CORRECT | 1536 | 17.97 | 87.11 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 19.88 | 95.98 |
| 10 | `gpqa_69` | C | A | WRONG | 1536 | 20.45 | 76.68 |
| 11 | `gpqa_3` | C | A | WRONG | 1536 | 24.32 | 64.62 |
| 12 | `gpqa_185` | A | A | CORRECT | 1536 | 20.95 | 75.25 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 20.82 | 75.04 |
| 14 | `gpqa_165` | C | A | WRONG | 1536 | 22.06 | 74.92 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 22.09 | 70.90 |
| 16 | `gpqa_15` | D | A | WRONG | 1536 | 20.60 | 76.29 |
| 17 | `gpqa_159` | A | B | WRONG | 1536 | 19.96 | 78.94 |
| 18 | `gpqa_36` | B | C | WRONG | 1536 | 20.34 | 77.08 |
| 19 | `gpqa_134` | D | B | WRONG | 1536 | 20.59 | 77.18 |
| 20 | `gpqa_44` | C | C | CORRECT | 1536 | 20.57 | 76.34 |
| 21 | `gpqa_5` | C | C | CORRECT | 1536 | 21.74 | 72.57 |
| 22 | `gpqa_53` | B | A | WRONG | 1536 | 19.99 | 78.51 |
| 23 | `gpqa_84` | B | A | WRONG | 1536 | 21.03 | 75.20 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 21.28 | 74.05 |
| 25 | `gpqa_64` | D | A | WRONG | 1536 | 20.60 | 76.60 |
| 26 | `gpqa_73` | D | D | CORRECT | 1536 | 21.52 | 73.06 |
| 27 | `gpqa_37` | A | A | CORRECT | 1536 | 20.89 | 75.65 |
| 28 | `gpqa_126` | B | D | WRONG | 1536 | 19.19 | 81.48 |
| 29 | `gpqa_122` | B | A | WRONG | 1536 | 21.32 | 73.98 |
| 30 | `gpqa_78` | A | A | CORRECT | 1536 | 20.41 | 78.10 |
| 31 | `gpqa_160` | A | A | CORRECT | 1536 | 20.35 | 77.61 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 21.16 | 74.52 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 19.80 | 78.64 |
| 34 | `gpqa_184` | C | C | CORRECT | 1185 | 20.60 | 59.12 |
| 35 | `gpqa_32` | B | None | WRONG | 1536 | 21.18 | 74.63 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 19.76 | 79.56 |
| 37 | `gpqa_192` | C | A | WRONG | 1536 | 20.06 | 77.79 |
| 38 | `gpqa_174` | B | A | WRONG | 1536 | 19.25 | 81.43 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 21.70 | 73.70 |
| 40 | `gpqa_60` | D | B | WRONG | 1536 | 19.94 | 78.83 |
| 41 | `gpqa_170` | C | A | WRONG | 1536 | 19.57 | 80.35 |
| 42 | `gpqa_47` | A | A | CORRECT | 1536 | 19.67 | 79.73 |
| 43 | `gpqa_131` | A | A | CORRECT | 1536 | 20.01 | 79.20 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 21.05 | 74.73 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 21.05 | 74.91 |
| 46 | `gpqa_95` | D | A | WRONG | 1536 | 21.03 | 74.61 |
| 47 | `gpqa_144` | C | C | CORRECT | 1536 | 18.94 | 82.29 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 19.29 | 81.44 |
| 49 | `gpqa_142` | C | A | WRONG | 1536 | 26.80 | 60.04 |
| 50 | `gpqa_61` | B | A | WRONG | 1536 | 21.37 | 73.99 |
