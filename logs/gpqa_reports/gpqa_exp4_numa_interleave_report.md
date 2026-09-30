# GPQA (20 Questions) & Long-Context Report: Exp 4: Dual-Socket NUMA Memory Bandwidth Scaling

- **Timestamp:** `2026-09-02 18:14:57`
- **Command:** `numactl --interleave=all /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8085 -c 8192 -t 14 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa distribute -fa 1`
- **GPQA Score:** **5 / 20 (25.0%)**
- **Average Generation Speed:** **`16.00 t/s`**
- **Average Prompt Speed:** **`142.77 t/s`**
- **4K Context Needle Passkey:** **PASSED**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `15.22 t/s` | 384 |
| 2 | `gpqa_42` | **A** | `None` | FAILED | `16.57 t/s` | 384 |
| 3 | `gpqa_2` | **B** | `None` | FAILED | `16.46 t/s` | 384 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `16.47 t/s` | 384 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `16.26 t/s` | 384 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `15.96 t/s` | 384 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `16.18 t/s` | 384 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `15.35 t/s` | 384 |
| 9 | `gpqa_127` | **D** | `A` | FAILED | `15.46 t/s` | 384 |
| 10 | `gpqa_69` | **C** | `C` | PASSED | `16.07 t/s` | 384 |
| 11 | `gpqa_3` | **C** | `B` | FAILED | `16.17 t/s` | 384 |
| 12 | `gpqa_185` | **A** | `None` | FAILED | `15.99 t/s` | 384 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `16.05 t/s` | 384 |
| 14 | `gpqa_165` | **C** | `None` | FAILED | `15.83 t/s` | 384 |
| 15 | `gpqa_169` | **C** | `None` | FAILED | `15.55 t/s` | 384 |
| 16 | `gpqa_15` | **D** | `A` | FAILED | `16.05 t/s` | 384 |
| 17 | `gpqa_159` | **A** | `C` | FAILED | `16.09 t/s` | 384 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `16.13 t/s` | 384 |
| 19 | `gpqa_134` | **D** | `None` | FAILED | `16.09 t/s` | 384 |
| 20 | `gpqa_44` | **C** | `None` | FAILED | `16.13 t/s` | 384 |

| - | `passkey_4k` | **Match** | `Match` | PASSED | `167.59 t/s` | Needle |
