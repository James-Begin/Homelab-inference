# Benchmark Report: Exp 94: Recursive Flint 40B MoE on ik_llama.cpp (Merged Up/Gate -muge 1 + AVX2 64-Byte Repacking Q4_0_R8 + N-Gram Mod Speculation n_max=4, match=4 + Slot Cache 0.50 + Decoupled Prefill -tb 26)
- **Run ID:** `run_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_16k_runway`
- **Protocol:** Protocol C-gpqa-v2
- **Model:** `RecursiveSI_flint-Q4_0_Repacked.gguf`
- **Token Ceiling (max_tokens):** 16384 tokens
- **Strict Score:** **23/50** (46.0%)
- **Lenient Score:** 29/50 (58.0%)
- **Mid-Thought Truncations:** 19 (38.0%)
- **Average Decode Speed:** 15.99 tokens/sec

## Detailed Question Rows
| ID | Gold | Pred | Strict Status | Tokens | Decode Speed | Wall Time |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: |
| `gpqa_110` | A | - | `no_answer_truncated` | 16384 | 13.17 t/s | 1245.26s |
| `gpqa_42` | A | - | `no_answer_truncated` | 16384 | 13.35 t/s | 1228.69s |
| `gpqa_2` | B | B | `correct` | 630 | 19.82 t/s | 33.4s |
| `gpqa_156` | A | A | `correct` | 222 | 19.96 t/s | 12.26s |
| `gpqa_128` | A | B | `wrong` | 15923 | 13.19 t/s | 1209.13s |
| `gpqa_12` | D | - | `no_answer_truncated` | 16384 | 13.29 t/s | 1234.73s |
| `gpqa_79` | D | - | `no_answer_truncated` | 16384 | 15.53 t/s | 1056.58s |
| `gpqa_13` | B | B | `correct` | 6029 | 16.62 t/s | 364.2s |
| `gpqa_127` | D | - | `no_answer_truncated` | 16384 | 17.06 t/s | 971.23s |
| `gpqa_69` | C | - | `no_answer_truncated` | 16384 | 13.3 t/s | 1233.49s |
| `gpqa_3` | C | D | `wrong` | 555 | 19.98 t/s | 29.45s |
| `gpqa_185` | A | - | `no_answer_truncated` | 16384 | 13.13 t/s | 1248.46s |
| `gpqa_30` | B | - | `no_answer_truncated` | 16384 | 13.71 t/s | 1196.6s |
| `gpqa_165` | C | A | `wrong` | 9701 | 16.25 t/s | 601.06s |
| `gpqa_169` | C | C | `correct` | 2114 | 18.99 t/s | 112.61s |
| `gpqa_15` | D | - | `no_answer_truncated` | 16384 | 13.72 t/s | 1195.12s |
| `gpqa_159` | A | A | `correct` | 6043 | 16.34 t/s | 371.59s |
| `gpqa_36` | B | - | `no_answer_truncated` | 16384 | 13.17 t/s | 1245.12s |
| `gpqa_134` | D | D | `correct` | 4257 | 19.5 t/s | 220.67s |
| `gpqa_44` | C | C | `correct` | 2390 | 18.38 t/s | 131.2s |
| `gpqa_5` | C | C | `correct` | 2898 | 18.65 t/s | 156.55s |
| `gpqa_53` | B | - | `no_answer_truncated` | 16384 | 12.7 t/s | 1291.15s |
| `gpqa_84` | B | B | `correct` | 6642 | 17.29 t/s | 386.21s |
| `gpqa_80` | D | D | `correct` | 11837 | 15.12 t/s | 784.69s |
| `gpqa_64` | D | - | `no_answer_truncated` | 16384 | 14.04 t/s | 1169.46s |
| `gpqa_73` | D | D | `correct` | 1124 | 19.36 t/s | 59.76s |
| `gpqa_37` | A | A | `correct` | 13649 | 14.55 t/s | 940.02s |
| `gpqa_126` | B | - | `no_answer_truncated` | 16384 | 13.28 t/s | 1235.57s |
| `gpqa_122` | B | B | `correct` | 3062 | 18.13 t/s | 170.82s |
| `gpqa_78` | A | A | `correct` | 11249 | 15.04 t/s | 749.93s |
| `gpqa_160` | A | C | `wrong` | 12134 | 14.15 t/s | 859.51s |
| `gpqa_66` | C | C | `correct` | 814 | 19.64 t/s | 43.58s |
| `gpqa_45` | C | - | `no_answer_truncated` | 16384 | 13.42 t/s | 1221.53s |
| `gpqa_184` | C | C | `correct` | 257 | 20.87 t/s | 14.11s |
| `gpqa_32` | B | - | `no_answer_truncated` | 16384 | 13.35 t/s | 1229.14s |
| `gpqa_52` | D | D | `correct` | 8038 | 16.07 t/s | 501.88s |
| `gpqa_192` | C | B | `wrong` | 1137 | 19.51 t/s | 59.41s |
| `gpqa_174` | B | D | `wrong` | 659 | 21.09 t/s | 32.46s |
| `gpqa_10` | B | - | `no_answer_truncated` | 16384 | 14.2 t/s | 1155.93s |
| `gpqa_60` | D | D | `correct` | 7656 | 15.99 t/s | 480.6s |
| `gpqa_170` | C | B | `wrong` | 12813 | 14.26 t/s | 900.04s |
| `gpqa_47` | A | - | `no_answer_truncated` | 16384 | 13.16 t/s | 1246.99s |
| `gpqa_131` | A | - | `no_answer_truncated` | 16384 | 13.33 t/s | 1231.45s |
| `gpqa_103` | B | B | `correct` | 2286 | 18.54 t/s | 125.31s |
| `gpqa_193` | D | D | `correct` | 945 | 19.86 t/s | 48.78s |
| `gpqa_95` | D | D | `correct` | 2704 | 18.78 t/s | 144.92s |
| `gpqa_144` | C | C | `correct` | 9066 | 15.76 t/s | 575.94s |
| `gpqa_100` | D | - | `no_answer_truncated` | 16384 | 12.84 t/s | 1277.69s |
| `gpqa_142` | C | D | `wrong` | 12020 | 14.51 t/s | 831.14s |
| `gpqa_61` | B | B | `correct` | 15781 | 13.43 t/s | 1177.49s |
