# Benchmark Report: Exp 50: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Pre-Repacked Offline GGUF (IQ4_XS_R8 / Q4_0_R8) + Merged Up/Gate Experts (-muge) + Native MTP + Q4_0 KV + SER 2,0.5
- **Run ID:** `run_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv_16k_runway`
- **Protocol:** Protocol C-gpqa-v2
- **Model:** `Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Token Ceiling (max_tokens):** 16384 tokens
- **Strict Score:** **19/50** (38.0%)
- **Lenient Score:** 13/50 (26.0%)
- **Mid-Thought Truncations:** 21 (42.0%)
- **Average Decode Speed:** 17.6 tokens/sec

## Detailed Question Rows
| ID | Gold | Pred | Strict Status | Tokens | Decode Speed | Wall Time |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: |
| `gpqa_110` | A | - | `no_answer_truncated` | 16384 | 16.52 t/s | 994.53s |
| `gpqa_42` | A | - | `no_answer_truncated` | 16384 | 16.15 t/s | 1016.46s |
| `gpqa_2` | B | B | `correct` | 2457 | 22.51 t/s | 110.93s |
| `gpqa_156` | A | A | `correct` | 1795 | 20.74 t/s | 88.39s |
| `gpqa_128` | A | - | `no_answer_truncated` | 16384 | 16.44 t/s | 999.26s |
| `gpqa_12` | D | - | `no_answer_format` | 16384 | 16.71 t/s | 983.27s |
| `gpqa_79` | D | B | `wrong` | 9246 | 18.35 t/s | 505.5s |
| `gpqa_13` | B | B | `correct` | 1638 | 19.6 t/s | 85.23s |
| `gpqa_127` | D | - | `no_answer_truncated` | 16384 | 15.41 t/s | 1080.78s |
| `gpqa_69` | C | - | `no_answer_truncated` | 16384 | 16.76 t/s | 979.83s |
| `gpqa_3` | C | C | `correct` | 2027 | 21.43 t/s | 96.47s |
| `gpqa_185` | A | C | `wrong` | 10248 | 17.49 t/s | 587.79s |
| `gpqa_30` | B | - | `no_answer_truncated` | 16384 | 16.6 t/s | 988.44s |
| `gpqa_165` | C | C | `correct` | 2154 | 19.25 t/s | 117.68s |
| `gpqa_169` | C | C | `correct` | 2167 | 22.7 t/s | 97.19s |
| `gpqa_15` | D | C | `wrong` | 10230 | 17.54 t/s | 585.37s |
| `gpqa_159` | A | A | `correct` | 1209 | 22.35 t/s | 56.27s |
| `gpqa_36` | B | D | `wrong` | 9765 | 18.03 t/s | 543.17s |
| `gpqa_134` | D | D | `correct` | 1138 | 21.89 t/s | 54.94s |
| `gpqa_44` | C | C | `correct` | 5781 | 20.05 t/s | 290.12s |
| `gpqa_5` | C | C | `correct` | 1946 | 22.83 t/s | 87.36s |
| `gpqa_53` | B | - | `no_answer_truncated` | 16384 | 16.3 t/s | 1006.66s |
| `gpqa_84` | B | B | `correct` | 5957 | 19.37 t/s | 310.08s |
| `gpqa_80` | D | - | `no_answer_truncated` | 16384 | 16.63 t/s | 987.46s |
| `gpqa_64` | D | - | `no_answer_truncated` | 16384 | 16.67 t/s | 985.14s |
| `gpqa_73` | D | D | `correct` | 14713 | 16.46 t/s | 895.83s |
| `gpqa_37` | A | - | `no_answer_truncated` | 16384 | 15.61 t/s | 1052.06s |
| `gpqa_126` | B | - | `no_answer_truncated` | 16384 | 16.83 t/s | 975.19s |
| `gpqa_122` | B | B | `correct` | 5978 | 19.8 t/s | 304.11s |
| `gpqa_78` | A | C | `wrong` | 9235 | 17.62 t/s | 527.17s |
| `gpqa_160` | A | A | `correct` | 6681 | 18.72 t/s | 359.61s |
| `gpqa_66` | C | - | `no_answer_truncated` | 16384 | 15.78 t/s | 1040.11s |
| `gpqa_45` | C | - | `no_answer_format` | 16384 | 15.64 t/s | 1049.15s |
| `gpqa_184` | C | C | `correct` | 11994 | 17.16 t/s | 701.02s |
| `gpqa_32` | B | B | `correct` | 10400 | 17.04 t/s | 613.09s |
| `gpqa_52` | D | - | `no_answer_truncated` | 16384 | 15.63 t/s | 1050.71s |
| `gpqa_192` | C | - | `no_answer_truncated` | 16384 | 15.6 t/s | 1052.21s |
| `gpqa_174` | B | - | `no_answer_truncated` | 16384 | 15.59 t/s | 1053.5s |
| `gpqa_10` | B | - | `no_answer_truncated` | 16384 | 16.1 t/s | 1020.58s |
| `gpqa_60` | D | - | `no_answer_format` | 16384 | 15.31 t/s | 1072.44s |
| `gpqa_170` | C | C | `correct` | 10268 | 17.35 t/s | 594.09s |
| `gpqa_47` | A | - | `no_answer_truncated` | 16384 | 16.83 t/s | 975.19s |
| `gpqa_131` | A | D | `wrong` | 15599 | 15.92 t/s | 982.79s |
| `gpqa_103` | B | B | `correct` | 15777 | 15.95 t/s | 991.23s |
| `gpqa_193` | D | - | `no_answer_truncated` | 16384 | 15.79 t/s | 1039.64s |
| `gpqa_95` | D | - | `no_answer_truncated` | 16384 | 16.31 t/s | 1006.23s |
| `gpqa_144` | C | - | `no_answer_truncated` | 16384 | 15.56 t/s | 1054.45s |
| `gpqa_100` | D | - | `no_answer_truncated` | 16384 | 16.67 t/s | 985.27s |
| `gpqa_142` | C | - | `no_answer_format` | 16384 | 16.55 t/s | 992.97s |
| `gpqa_61` | B | B | `correct` | 14900 | 15.86 t/s | 942.06s |
