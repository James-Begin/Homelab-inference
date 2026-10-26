# Benchmark Report: Exp 50: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Pre-Repacked Offline GGUF (IQ4_XS_R8 / Q4_0_R8) + Merged Up/Gate Experts (-muge) + Precision Suffix Speculation (n_max=8, match=5) + Native MTP + Q4_0 KV + SER 2,0.5
- **Run ID:** `run_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv`
- **Protocol:** Protocol C-gpqa-v2
- **Model:** `Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Token Ceiling (max_tokens):** 8192 tokens
- **Strict Score:** **10/50** (20.0%)
- **Lenient Score:** 12/50 (24.0%)
- **Mid-Thought Truncations:** 29 (58.0%)
- **Average Decode Speed:** 21.36 tokens/sec

## Detailed Question Rows
| ID | Gold | Pred | Strict Status | Tokens | Decode Speed | Wall Time |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: |
| `gpqa_110` | A | - | `no_answer_truncated` | 8192 | 18.66 t/s | 441.91s |
| `gpqa_42` | A | - | `no_answer_truncated` | 8192 | 18.79 t/s | 438.3s |
| `gpqa_2` | B | B | `correct` | 1239 | 23.34 t/s | 54.96s |
| `gpqa_156` | A | A | `correct` | 2228 | 19.58 t/s | 115.74s |
| `gpqa_128` | A | - | `no_answer_truncated` | 8192 | 36.2 t/s | 228.55s |
| `gpqa_12` | D | - | `no_answer_format` | 8192 | 37.88 t/s | 218.79s |
| `gpqa_79` | D | - | `no_answer_truncated` | 8192 | 22.18 t/s | 371.03s |
| `gpqa_13` | B | - | `no_answer_truncated` | 8192 | 28.94 t/s | 284.85s |
| `gpqa_127` | D | - | `no_answer_truncated` | 8192 | 42.07 t/s | 212.61s |
| `gpqa_69` | C | - | `no_answer_format` | 8192 | 21.65 t/s | 380.07s |
| `gpqa_3` | C | - | `no_answer_format` | 8192 | 19.25 t/s | 427.38s |
| `gpqa_185` | A | - | `no_answer_format` | 8192 | 19.44 t/s | 423.29s |
| `gpqa_30` | B | - | `no_answer_truncated` | 8192 | 20.89 t/s | 393.93s |
| `gpqa_165` | C | C | `correct` | 6813 | 17.92 t/s | 385.82s |
| `gpqa_169` | C | C | `correct` | 2125 | 24.36 t/s | 88.83s |
| `gpqa_15` | D | D | `correct` | 6956 | 18.57 t/s | 376.66s |
| `gpqa_159` | A | C | `wrong` | 1961 | 19.86 t/s | 100.64s |
| `gpqa_36` | B | - | `no_answer_truncated` | 8192 | 37.94 t/s | 217.56s |
| `gpqa_134` | D | D | `correct` | 1649 | 21.23 t/s | 80.64s |
| `gpqa_44` | C | - | `no_answer_truncated` | 8192 | 20.94 t/s | 393.0s |
| `gpqa_5` | C | C | `correct` | 1665 | 21.72 t/s | 78.72s |
| `gpqa_53` | B | - | `no_answer_format` | 8192 | 17.76 t/s | 463.07s |
| `gpqa_84` | B | - | `no_answer_format` | 8192 | 17.82 t/s | 462.38s |
| `gpqa_80` | D | - | `no_answer_truncated` | 8192 | 23.9 t/s | 344.96s |
| `gpqa_64` | D | - | `no_answer_truncated` | 8192 | 17.64 t/s | 466.76s |
| `gpqa_73` | D | D | `correct` | 2115 | 21.97 t/s | 98.26s |
| `gpqa_37` | A | - | `no_answer_truncated` | 8192 | 21.17 t/s | 389.14s |
| `gpqa_126` | B | - | `no_answer_truncated` | 8192 | 26.11 t/s | 315.62s |
| `gpqa_122` | B | B | `correct` | 5307 | 18.68 t/s | 286.35s |
| `gpqa_78` | A | - | `no_answer_truncated` | 8192 | 18.48 t/s | 446.16s |
| `gpqa_160` | A | - | `no_answer_truncated` | 8192 | 18.69 t/s | 441.04s |
| `gpqa_66` | C | - | `no_answer_truncated` | 8192 | 19.83 t/s | 415.6s |
| `gpqa_45` | C | - | `no_answer_format` | 8192 | 28.16 t/s | 292.3s |
| `gpqa_184` | C | - | `no_answer_truncated` | 8192 | 18.24 t/s | 451.26s |
| `gpqa_32` | B | - | `no_answer_format` | 8192 | 18.37 t/s | 448.5s |
| `gpqa_52` | D | - | `no_answer_truncated` | 8192 | 16.33 t/s | 503.52s |
| `gpqa_192` | C | - | `no_answer_truncated` | 8192 | 18.46 t/s | 445.32s |
| `gpqa_174` | B | - | `no_answer_truncated` | 8192 | 16.24 t/s | 506.75s |
| `gpqa_10` | B | - | `no_answer_truncated` | 8192 | 17.91 t/s | 460.47s |
| `gpqa_60` | D | - | `no_answer_truncated` | 8192 | 16.6 t/s | 495.63s |
| `gpqa_170` | C | C | `correct` | 4389 | 18.08 t/s | 245.12s |
| `gpqa_47` | A | - | `no_answer_truncated` | 8192 | 17.41 t/s | 472.39s |
| `gpqa_131` | A | - | `no_answer_format` | 8192 | 16.24 t/s | 507.44s |
| `gpqa_103` | B | - | `no_answer_truncated` | 8192 | 18.26 t/s | 450.93s |
| `gpqa_193` | D | - | `no_answer_truncated` | 8192 | 18.69 t/s | 440.49s |
| `gpqa_95` | D | - | `no_answer_truncated` | 8192 | 17.96 t/s | 457.95s |
| `gpqa_144` | C | - | `no_answer_truncated` | 8192 | 16.4 t/s | 500.93s |
| `gpqa_100` | D | - | `no_answer_truncated` | 8192 | 22.58 t/s | 800.48s |
| `gpqa_142` | C | - | `no_answer_truncated` | 8192 | 21.15 t/s | 390.25s |
| `gpqa_61` | B | - | `no_answer_format` | 8192 | 17.31 t/s | 475.55s |
