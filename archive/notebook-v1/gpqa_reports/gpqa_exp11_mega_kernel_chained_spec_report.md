# GPQA (20 Questions) & Long-Context Report: Exp 11: Dual NUMA + AVX2 Prefetching Mega-Kernel + Chained Speculation

- **Timestamp:** `2026-09-06 15:37:50`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Command:** `numactl --interleave=all /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8085 -c 8192 -t 14 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa distribute -fa 1 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type ngram-mod:n_max=16,n_min=3,ngram_size_n=4 --spec-type mtp:n_max=1,p_min=0.0`
- **GPQA Score:** **6 / 20 (30.0%)**
- **Average Generation Speed:** **`17.14 t/s`**
- **Peak Generation Speed:** **`31.69 t/s`**
- **Average Prompt Speed:** **`125.46 t/s`**
- **4K Context Needle Passkey:** **PASSED (167.57 t/s)**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `18.23 t/s` | 384 |
| 2 | `gpqa_42` | **A** | `None` | FAILED | `15.46 t/s` | 384 |
| 3 | `gpqa_2` | **B** | `C` | FAILED | `15.21 t/s` | 384 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `16.34 t/s` | 384 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `16.50 t/s` | 384 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `14.61 t/s` | 384 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `16.44 t/s` | 384 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `14.82 t/s` | 384 |
| 9 | `gpqa_127` | **D** | `None` | FAILED | `31.69 t/s` | 384 |
| 10 | `gpqa_69` | **C** | `C` | PASSED | `18.79 t/s` | 384 |
| 11 | `gpqa_3` | **C** | `B` | FAILED | `15.92 t/s` | 384 |
| 12 | `gpqa_185` | **A** | `None` | FAILED | `17.19 t/s` | 384 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `16.94 t/s` | 384 |
| 14 | `gpqa_165` | **C** | `None` | FAILED | `15.49 t/s` | 384 |
| 15 | `gpqa_169` | **C** | `None` | FAILED | `15.70 t/s` | 384 |
| 16 | `gpqa_15` | **D** | `A` | FAILED | `16.14 t/s` | 384 |
| 17 | `gpqa_159` | **A** | `A` | PASSED | `16.61 t/s` | 384 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `16.47 t/s` | 384 |
| 19 | `gpqa_134` | **D** | `None` | FAILED | `16.46 t/s` | 384 |
| 20 | `gpqa_44` | **C** | `None` | FAILED | `17.87 t/s` | 384 |

| - | `passkey_4k` | **Match** | `Match` | PASSED | `167.57 t/s` | Needle |
