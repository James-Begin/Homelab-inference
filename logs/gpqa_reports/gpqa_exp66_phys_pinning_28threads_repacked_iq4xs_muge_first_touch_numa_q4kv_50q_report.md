# 50-Question GPQA Diamond Report: Exp 66: Pre-Repacked Offline GGUF + Merged Experts (-muge) + First-Touch Local NUMA Allocation (numactl --localalloc) + Direct NUMA Map Pinning (--numa numactl) + Suffix (n_max=8, match=5) + Confidence MTP (p_min=0.15) + Q4_0 KV + SER 2,0.5

- **Experiment ID:** `exp66_phys_pinning_28threads_repacked_iq4xs_muge_first_touch_numa_q4kv`
- **Total Score (50Q):** **2 / 50 (4.0%)**
- **Standard 20Q Subset:** **1 / 20 (5.0%)**
- **Average Generation Speed:** **`13.67 tokens/second`**
- **Peak Generation Speed:** **`25.26 tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | A | A | CORRECT | 1536 | 12.86 | 122.24 |
| 2 | `gpqa_42` | A | None | WRONG | 1536 | 13.64 | 114.75 |
| 3 | `gpqa_2` | B | None | WRONG | 1536 | 14.60 | 106.94 |
| 4 | `gpqa_156` | A | None | WRONG | 1536 | 12.54 | 124.38 |
| 5 | `gpqa_128` | A | None | WRONG | 1536 | 14.11 | 111.22 |
| 6 | `gpqa_12` | D | None | WRONG | 1536 | 25.26 | 63.50 |
| 7 | `gpqa_79` | D | None | WRONG | 1536 | 13.27 | 117.25 |
| 8 | `gpqa_13` | B | None | WRONG | 1536 | 12.01 | 129.40 |
| 9 | `gpqa_127` | D | A | WRONG | 1536 | 13.88 | 127.52 |
| 10 | `gpqa_69` | C | None | WRONG | 1536 | 13.18 | 118.27 |
| 11 | `gpqa_3` | C | None | WRONG | 1536 | 15.79 | 98.88 |
| 12 | `gpqa_185` | A | None | WRONG | 1536 | 14.09 | 110.95 |
| 13 | `gpqa_30` | B | None | WRONG | 1536 | 13.29 | 117.10 |
| 14 | `gpqa_165` | C | None | WRONG | 1536 | 14.42 | 112.03 |
| 15 | `gpqa_169` | C | None | WRONG | 1536 | 14.20 | 109.81 |
| 16 | `gpqa_15` | D | None | WRONG | 1536 | 13.09 | 119.23 |
| 17 | `gpqa_159` | A | None | WRONG | 1536 | 12.84 | 121.54 |
| 18 | `gpqa_36` | B | None | WRONG | 1536 | 13.27 | 117.50 |
| 19 | `gpqa_134` | D | None | WRONG | 1536 | 13.24 | 118.67 |
| 20 | `gpqa_44` | C | None | WRONG | 1536 | 13.30 | 117.21 |
| 21 | `gpqa_5` | C | None | WRONG | 1536 | 14.52 | 107.69 |
| 22 | `gpqa_53` | B | None | WRONG | 1536 | 12.83 | 121.45 |
| 23 | `gpqa_84` | B | None | WRONG | 1536 | 13.37 | 117.13 |
| 24 | `gpqa_80` | D | None | WRONG | 1536 | 13.77 | 113.60 |
| 25 | `gpqa_64` | D | None | WRONG | 1536 | 13.35 | 117.36 |
| 26 | `gpqa_73` | D | None | WRONG | 1536 | 13.91 | 112.17 |
| 27 | `gpqa_37` | A | None | WRONG | 1536 | 13.52 | 115.88 |
| 28 | `gpqa_126` | B | D | WRONG | 1536 | 12.41 | 125.32 |
| 29 | `gpqa_122` | B | None | WRONG | 1536 | 13.85 | 112.84 |
| 30 | `gpqa_78` | A | None | WRONG | 1536 | 13.22 | 119.09 |
| 31 | `gpqa_160` | A | None | WRONG | 1536 | 13.12 | 119.52 |
| 32 | `gpqa_66` | C | None | WRONG | 1536 | 13.61 | 114.94 |
| 33 | `gpqa_45` | C | None | WRONG | 1536 | 12.61 | 123.05 |
| 34 | `gpqa_184` | C | C | CORRECT | 1185 | 12.87 | 93.84 |
| 35 | `gpqa_32` | B | None | WRONG | 1536 | 13.59 | 115.53 |
| 36 | `gpqa_52` | D | A | WRONG | 1536 | 12.60 | 124.00 |
| 37 | `gpqa_192` | C | None | WRONG | 1536 | 12.85 | 121.05 |
| 38 | `gpqa_174` | B | None | WRONG | 1536 | 12.41 | 125.67 |
| 39 | `gpqa_10` | B | A | WRONG | 1536 | 13.86 | 113.58 |
| 40 | `gpqa_60` | D | B | WRONG | 1536 | 12.63 | 123.56 |
| 41 | `gpqa_170` | C | None | WRONG | 1536 | 12.64 | 123.46 |
| 42 | `gpqa_47` | A | None | WRONG | 1536 | 12.80 | 121.58 |
| 43 | `gpqa_131` | A | None | WRONG | 1536 | 12.94 | 121.10 |
| 44 | `gpqa_103` | B | None | WRONG | 1536 | 13.49 | 115.91 |
| 45 | `gpqa_193` | D | None | WRONG | 1536 | 13.69 | 114.53 |
| 46 | `gpqa_95` | D | None | WRONG | 1536 | 13.40 | 116.21 |
| 47 | `gpqa_144` | C | None | WRONG | 1536 | 12.24 | 126.77 |
| 48 | `gpqa_100` | D | A | WRONG | 1536 | 12.58 | 123.99 |
| 49 | `gpqa_142` | C | None | WRONG | 1536 | 18.14 | 87.56 |
| 50 | `gpqa_61` | B | None | WRONG | 1536 | 13.87 | 112.85 |
