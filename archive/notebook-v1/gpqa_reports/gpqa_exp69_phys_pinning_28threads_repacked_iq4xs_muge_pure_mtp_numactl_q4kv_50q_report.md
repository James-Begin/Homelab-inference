# 50-Question GPQA Diamond Report: Exp 69: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Pure MTP Speculation (No Suffix) + Direct NUMA Map Pinning (--numa numactl) + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp69_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_numactl_q4kv`
- **Total Score (50Q):** **8 / 50 (16.0%)**
- **Standard 20Q Subset:** **5 / 20 (25.0%)**
- **Average Generation Speed:** **`22.36 tokens/second`**
- **Peak Generation Speed:** **`24.03 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 21.96 | 72.60 |
| 2 | `gpqa_42` | A | None | WRONG | 1536 | 23.15 | 68.43 |
| 3 | `gpqa_2` | B | None | WRONG | 1536 | 24.03 | 65.47 |
| 4 | `gpqa_156` | A | A | CORRECT | 704 | 21.95 | 33.67 |
| 5 | `gpqa_128` | A | None | WRONG | 1536 | 21.86 | 72.26 |
| 6 | `gpqa_12` | D | None | WRONG | 1536 | 22.38 | 71.20 |
| 7 | `gpqa_79` | D | None | WRONG | 1536 | 22.28 | 70.19 |
| 8 | `gpqa_13` | B | B | CORRECT | 1494 | 20.15 | 75.45 |
| 9 | `gpqa_127` | D | D | CORRECT | 1536 | 19.55 | 94.90 |
| 10 | `gpqa_69` | C | None | WRONG | 1536 | 22.27 | 70.44 |
| 11 | `gpqa_3` | C | None | WRONG | 1536 | 23.11 | 67.86 |
| 12 | `gpqa_185` | A | None | WRONG | 1536 | 22.83 | 68.85 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 21.72 | 72.07 |
| 14 | `gpqa_165` | C | None | WRONG | 1536 | 21.04 | 78.25 |
| 15 | `gpqa_169` | C | C | CORRECT | 1536 | 23.68 | 66.26 |
| 16 | `gpqa_15` | D | None | WRONG | 1536 | 22.19 | 70.85 |
| 17 | `gpqa_159` | A | None | WRONG | 1536 | 23.52 | 66.89 |
| 18 | `gpqa_36` | B | None | WRONG | 1536 | 22.27 | 70.37 |
| 19 | `gpqa_134` | D | A | WRONG | 1536 | 22.57 | 70.54 |
| 20 | `gpqa_44` | C | A | WRONG | 1536 | 23.41 | 67.38 |
| 21 | `gpqa_5` | C | None | WRONG | 1536 | 23.64 | 66.58 |
| 22 | `gpqa_53` | B | None | WRONG | 1536 | 22.49 | 69.82 |
| 23 | `gpqa_84` | B | None | WRONG | 1536 | 22.73 | 69.66 |
| 24 | `gpqa_80` | D | A | WRONG | 1536 | 21.35 | 73.97 |
| 25 | `gpqa_64` | D | None | WRONG | 1536 | 21.96 | 72.36 |
| 26 | `gpqa_73` | D | None | WRONG | 1536 | 23.37 | 67.48 |
| 27 | `gpqa_37` | A | None | WRONG | 1536 | 22.57 | 70.07 |
| 28 | `gpqa_126` | B | C | WRONG | 1536 | 22.77 | 68.78 |
| 29 | `gpqa_122` | B | None | WRONG | 1536 | 22.86 | 68.93 |
| 30 | `gpqa_78` | A | None | WRONG | 1536 | 23.14 | 69.00 |
| 31 | `gpqa_160` | A | None | WRONG | 1536 | 22.37 | 70.92 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 23.18 | 68.30 |
| 33 | `gpqa_45` | C | C | CORRECT | 1536 | 21.82 | 71.46 |
| 34 | `gpqa_184` | C | C | CORRECT | 1536 | 23.54 | 66.76 |
| 35 | `gpqa_32` | B | None | WRONG | 1536 | 22.21 | 71.66 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 22.29 | 70.68 |
| 37 | `gpqa_192` | C | None | WRONG | 1536 | 22.17 | 70.78 |
| 38 | `gpqa_174` | B | None | WRONG | 1536 | 22.46 | 70.07 |
| 39 | `gpqa_10` | B | B | CORRECT | 1536 | 20.35 | 78.16 |
| 40 | `gpqa_60` | D | None | WRONG | 1536 | 21.94 | 71.88 |
| 41 | `gpqa_170` | C | None | WRONG | 1536 | 21.55 | 72.95 |
| 42 | `gpqa_47` | A | None | WRONG | 1536 | 22.27 | 70.40 |
| 43 | `gpqa_131` | A | None | WRONG | 1536 | 22.00 | 71.94 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 22.56 | 69.84 |
| 46 | `gpqa_95` | D | None | WRONG | 1536 | 23.33 | 67.35 |
| 47 | `gpqa_144` | C | None | WRONG | 1536 | 23.05 | 67.69 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 21.93 | 71.70 |
| 49 | `gpqa_142` | C | None | WRONG | 1536 | 22.29 | 71.72 |
| 50 | `gpqa_61` | B | None | WRONG | 1536 | 22.14 | 71.22 |
| 50 | `gpqa_61` | B | None | WRONG | 1536 | 21.92 | 72.12 |
