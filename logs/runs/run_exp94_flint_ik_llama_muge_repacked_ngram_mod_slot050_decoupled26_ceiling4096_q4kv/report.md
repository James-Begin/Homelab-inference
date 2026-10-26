# Benchmark Report: Exp 94: Recursive Flint 40B MoE (ik_llama.cpp, -muge 1, Repacked Q4_0_R8, N-gram spec)
- **Run ID:** `run_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv`
- **Protocol:** Protocol C-gpqa-v2
- **Model:** `RecursiveSI_flint-Q4_0_Repacked.gguf`
- **Token Ceiling (max_tokens):** 8192 tokens
- **Strict Score:** **18/50** (36.0%)
- **Lenient Score:** 23/50 (46.0%)
- **Mid-Thought Truncations:** 0
- **Average Decode Speed:** 17.14 tokens/sec

## Detailed Question Rows
| ID | Gold | Pred | Strict Status | Tokens | Decode Speed | Wall Time |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: |
| `gpqa_110` | A | - | `no_answer_format` | 8192 | 16.18 t/s | 508.41s |
| `gpqa_42` | A | - | `no_answer_format` | 8192 | 15.93 t/s | 515.84s |
| `gpqa_2` | B | B | `correct` | 591 | 19.19 t/s | 32.17s |
| `gpqa_156` | A | A | `correct` | 204 | 20.48 t/s | 11.33s |
| `gpqa_128` | A | - | `no_answer_format` | 8192 | 15.69 t/s | 523.51s |
| `gpqa_12` | D | - | `no_answer_format` | 8192 | 16.13 t/s | 509.96s |
| `gpqa_79` | D | - | `no_answer_format` | 8192 | 15.78 t/s | 520.22s |
| `gpqa_13` | B | B | `correct` | 6029 | 16.74 t/s | 361.39s |
| `gpqa_127` | D | - | `no_answer_format` | 8192 | 20.4 t/s | 412.53s |
| `gpqa_69` | C | - | `no_answer_format` | 8192 | 16.01 t/s | 513.43s |
| `gpqa_3` | C | D | `wrong` | 555 | 19.87 t/s | 29.34s |
| `gpqa_185` | A | - | `no_answer_format` | 8192 | 15.94 t/s | 515.04s |
| `gpqa_30` | B | - | `no_answer_format` | 8192 | 15.88 t/s | 517.33s |
| `gpqa_165` | C | - | `no_answer_format` | 8192 | 16.56 t/s | 498.75s |
| `gpqa_169` | C | C | `correct` | 1605 | 19.08 t/s | 85.39s |
| `gpqa_15` | D | - | `no_answer_format` | 8192 | 16.56 t/s | 495.9s |
| `gpqa_159` | A | A | `correct` | 6043 | 16.22 t/s | 374.22s |
| `gpqa_36` | B | - | `no_answer_format` | 8192 | 15.89 t/s | 516.67s |
| `gpqa_134` | D | D | `correct` | 4257 | 19.25 t/s | 223.04s |
| `gpqa_44` | C | C | `correct` | 2390 | 18.21 t/s | 132.37s |
| `gpqa_5` | C | C | `correct` | 2898 | 18.44 t/s | 158.45s |
| `gpqa_53` | B | - | `no_answer_format` | 8192 | 15.85 t/s | 517.86s |
| `gpqa_84` | B | B | `correct` | 6642 | 17.03 t/s | 392.02s |
| `gpqa_80` | D | - | `no_answer_format` | 8192 | 16.32 t/s | 503.58s |
| `gpqa_64` | D | - | `no_answer_format` | 8192 | 16.92 t/s | 486.02s |
| `gpqa_73` | D | D | `correct` | 1124 | 19.29 t/s | 59.69s |
| `gpqa_37` | A | - | `no_answer_format` | 8192 | 16.35 t/s | 502.78s |
| `gpqa_126` | B | - | `no_answer_format` | 8192 | 16.15 t/s | 508.65s |
| `gpqa_122` | B | B | `correct` | 5284 | 16.97 t/s | 313.05s |
| `gpqa_78` | A | - | `no_answer_format` | 8192 | 16.08 t/s | 511.24s |
| `gpqa_160` | A | - | `no_answer_format` | 8192 | 15.65 t/s | 525.61s |
| `gpqa_66` | C | C | `correct` | 814 | 19.34 t/s | 44.03s |
| `gpqa_45` | C | - | `no_answer_format` | 8192 | 15.92 t/s | 515.28s |
| `gpqa_184` | C | C | `correct` | 257 | 20.69 t/s | 13.68s |
| `gpqa_32` | B | - | `no_answer_format` | 8192 | 16.75 t/s | 490.49s |
| `gpqa_52` | D | D | `correct` | 8038 | 15.85 t/s | 508.62s |
| `gpqa_192` | C | B | `wrong` | 1540 | 18.93 t/s | 82.55s |
| `gpqa_174` | B | D | `wrong` | 866 | 19.51 t/s | 45.68s |
| `gpqa_10` | B | - | `no_answer_format` | 8192 | 16.92 t/s | 485.96s |
| `gpqa_60` | D | D | `correct` | 7656 | 15.76 t/s | 487.35s |
| `gpqa_170` | C | - | `no_answer_format` | 8192 | 15.71 t/s | 522.98s |
| `gpqa_47` | A | - | `no_answer_format` | 8192 | 15.55 t/s | 528.41s |
| `gpqa_131` | A | - | `no_answer_format` | 8192 | 16.16 t/s | 509.06s |
| `gpqa_103` | B | B | `correct` | 2286 | 18.67 t/s | 124.26s |
| `gpqa_193` | D | D | `correct` | 945 | 19.62 t/s | 49.36s |
| `gpqa_95` | D | D | `correct` | 2704 | 18.29 t/s | 148.87s |
| `gpqa_144` | C | - | `no_answer_format` | 8192 | 15.78 t/s | 519.96s |
| `gpqa_100` | D | - | `no_answer_format` | 8192 | 15.67 t/s | 524.56s |
| `gpqa_142` | C | - | `no_answer_format` | 8192 | 15.73 t/s | 523.3s |
| `gpqa_61` | B | - | `no_answer_format` | 8192 | 15.32 t/s | 536.57s |

