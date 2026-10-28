# Benchmark Report: Exp 50: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Pre-Repacked Offline GGUF (IQ4_XS_R8 / Q4_0_R8) + Merged Up/Gate Experts (-muge) + Native MTP + Q4_0 KV + SER 2,0.5
- **Run ID:** `run_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv`
- **Protocol:** Protocol C-gpqa-v2
- **Model:** `Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Token Ceiling (max_tokens):** 8192 tokens
- **Strict Score:** **13/50** (26.0%)
- **Lenient Score:** 10/50 (20.0%)
- **Mid-Thought Truncations:** 27 (54.0%)
- **Average Decode Speed:** 19.18 tokens/sec

## Detailed Question Rows
| ID | Gold | Pred | Strict Status | Tokens | Decode Speed | Wall Time |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: |
| `gpqa_110` | A | - | `no_answer_truncated` | 8192 | 18.67 t/s | 441.42s |
| `gpqa_42` | A | - | `no_answer_truncated` | 8192 | 18.89 t/s | 435.77s |
| `gpqa_2` | B | B | `correct` | 2457 | 22.6 t/s | 110.52s |
| `gpqa_156` | A | A | `correct` | 1795 | 20.85 t/s | 88.01s |
| `gpqa_128` | A | - | `no_answer_truncated` | 8192 | 18.51 t/s | 445.03s |
| `gpqa_12` | D | - | `no_answer_format` | 8192 | 19.42 t/s | 424.43s |
| `gpqa_79` | D | - | `no_answer_format` | 8192 | 18.77 t/s | 438.04s |
| `gpqa_13` | B | B | `correct` | 1638 | 19.63 t/s | 85.1s |
| `gpqa_127` | D | - | `no_answer_truncated` | 8192 | 17.88 t/s | 475.78s |
| `gpqa_69` | C | - | `no_answer_truncated` | 8192 | 19.47 t/s | 422.83s |
| `gpqa_3` | C | C | `correct` | 2027 | 21.53 t/s | 95.91s |
| `gpqa_185` | A | - | `no_answer_format` | 8192 | 18.43 t/s | 446.37s |
| `gpqa_30` | B | - | `no_answer_truncated` | 8192 | 19.13 t/s | 429.85s |
| `gpqa_165` | C | C | `correct` | 2154 | 19.28 t/s | 118.3s |
| `gpqa_169` | C | C | `correct` | 2167 | 22.74 t/s | 96.97s |
| `gpqa_15` | D | - | `no_answer_format` | 8192 | 18.26 t/s | 450.74s |
| `gpqa_159` | A | A | `correct` | 1209 | 22.37 t/s | 55.83s |
| `gpqa_36` | B | - | `no_answer_format` | 8192 | 18.52 t/s | 444.14s |
| `gpqa_134` | D | D | `correct` | 1138 | 21.88 t/s | 54.61s |
| `gpqa_44` | C | C | `correct` | 5781 | 20.01 t/s | 290.7s |
| `gpqa_5` | C | C | `correct` | 1946 | 22.81 t/s | 87.32s |
| `gpqa_53` | B | - | `no_answer_truncated` | 8192 | 18.51 t/s | 444.6s |
| `gpqa_84` | B | B | `correct` | 5957 | 19.35 t/s | 310.4s |
| `gpqa_80` | D | - | `no_answer_truncated` | 8192 | 19.08 t/s | 431.61s |
| `gpqa_64` | D | - | `no_answer_truncated` | 8192 | 19.5 t/s | 422.75s |
| `gpqa_73` | D | - | `no_answer_truncated` | 8192 | 18.8 t/s | 437.41s |
| `gpqa_37` | A | - | `no_answer_truncated` | 8192 | 18.0 t/s | 457.62s |
| `gpqa_126` | B | - | `no_answer_truncated` | 8192 | 19.55 t/s | 420.66s |
| `gpqa_122` | B | B | `correct` | 5978 | 19.75 t/s | 304.74s |
| `gpqa_78` | A | - | `no_answer_truncated` | 8192 | 17.95 t/s | 459.26s |
| `gpqa_160` | A | A | `correct` | 6681 | 18.63 t/s | 360.97s |
| `gpqa_66` | C | - | `no_answer_truncated` | 8192 | 18.47 t/s | 445.54s |
| `gpqa_45` | C | - | `no_answer_format` | 8192 | 18.49 t/s | 444.38s |
| `gpqa_184` | C | - | `no_answer_truncated` | 8192 | 18.54 t/s | 443.78s |
| `gpqa_32` | B | - | `no_answer_format` | 8192 | 17.84 t/s | 461.67s |
| `gpqa_52` | D | - | `no_answer_truncated` | 8192 | 18.26 t/s | 450.87s |
| `gpqa_192` | C | - | `no_answer_truncated` | 8192 | 18.26 t/s | 450.37s |
| `gpqa_174` | B | - | `no_answer_truncated` | 8192 | 18.05 t/s | 455.82s |
| `gpqa_10` | B | - | `no_answer_truncated` | 8192 | 18.04 t/s | 456.99s |
| `gpqa_60` | D | - | `no_answer_truncated` | 8192 | 17.89 t/s | 459.93s |
| `gpqa_170` | C | - | `no_answer_format` | 8192 | 17.95 t/s | 458.76s |
| `gpqa_47` | A | - | `no_answer_truncated` | 8192 | 19.3 t/s | 426.29s |
| `gpqa_131` | A | - | `no_answer_format` | 8192 | 18.17 t/s | 453.47s |
| `gpqa_103` | B | - | `no_answer_truncated` | 8192 | 18.36 t/s | 448.38s |
| `gpqa_193` | D | - | `no_answer_truncated` | 8192 | 18.6 t/s | 442.61s |
| `gpqa_95` | D | - | `no_answer_truncated` | 8192 | 19.02 t/s | 432.57s |
| `gpqa_144` | C | - | `no_answer_truncated` | 8192 | 18.42 t/s | 446.28s |
| `gpqa_100` | D | - | `no_answer_truncated` | 8192 | 18.96 t/s | 434.21s |
| `gpqa_142` | C | - | `no_answer_format` | 8192 | 19.18 t/s | 430.02s |
| `gpqa_61` | B | - | `no_answer_truncated` | 8192 | 18.18 t/s | 452.85s |
