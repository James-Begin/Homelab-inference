# GPQA (20 Questions) & Long-Context Report: Exp 9: Dual NUMA + AVX2 Prefetching Mega-Kernel (Pure Decode)

- **Timestamp:** `2026-09-06 15:18:54`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Command:** `numactl --interleave=all /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8085 -c 8192 -t 14 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa distribute -fa 1`
- **GPQA Score:** **5 / 20 (25.0%)**
- **Average Generation Speed:** **`15.96 t/s`**
- **Peak Generation Speed:** **`16.13 t/s`**
- **Average Prompt Speed:** **`140.57 t/s`**
- **4K Context Needle Passkey:** **PASSED (188.01 t/s)**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `15.73 t/s` | 384 |
| 2 | `gpqa_42` | **A** | `None` | FAILED | `15.98 t/s` | 384 |
| 3 | `gpqa_2` | **B** | `None` | FAILED | `16.00 t/s` | 384 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `15.91 t/s` | 384 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `15.96 t/s` | 384 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `15.94 t/s` | 384 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `16.04 t/s` | 384 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `16.07 t/s` | 384 |
| 9 | `gpqa_127` | **D** | `A` | FAILED | `15.42 t/s` | 384 |
| 10 | `gpqa_69` | **C** | `C` | PASSED | `15.99 t/s` | 384 |
| 11 | `gpqa_3` | **C** | `B` | FAILED | `16.05 t/s` | 384 |
| 12 | `gpqa_185` | **A** | `None` | FAILED | `16.05 t/s` | 384 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `16.10 t/s` | 384 |
| 14 | `gpqa_165` | **C** | `None` | FAILED | `15.86 t/s` | 384 |
| 15 | `gpqa_169` | **C** | `None` | FAILED | `16.07 t/s` | 384 |
| 16 | `gpqa_15` | **D** | `A` | FAILED | `16.03 t/s` | 384 |
| 17 | `gpqa_159` | **A** | `C` | FAILED | `16.08 t/s` | 384 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `15.98 t/s` | 384 |
| 19 | `gpqa_134` | **D** | `None` | FAILED | `15.90 t/s` | 384 |
| 20 | `gpqa_44` | **C** | `None` | FAILED | `16.13 t/s` | 384 |

| - | `passkey_4k` | **Match** | `Match` | PASSED | `188.01 t/s` | Needle |
