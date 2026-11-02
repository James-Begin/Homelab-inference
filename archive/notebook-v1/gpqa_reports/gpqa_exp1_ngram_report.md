# GPQA (20 Questions) & Long-Context Report: Exp 1: N-Gram Speculation

- **Timestamp:** `2026-09-02 17:40:22`
- **Command:** `numactl --cpunodebind=0 --membind=0 /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8085 -c 8192 -t 10 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa isolate -fa 1 --spec-type ngram-mod:n_max=5,ngram_size_n=8`
- **GPQA Score:** **5 / 20 (25.0%)**
- **Average Generation Speed:** **`12.19 t/s`**
- **Average Prompt Speed:** **`125.66 t/s`**
- **4K Context Needle Passkey:** **PASSED**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `14.26 t/s` | 384 |
| 2 | `gpqa_42` | **A** | `None` | FAILED | `11.47 t/s` | 384 |
| 3 | `gpqa_2` | **B** | `None` | FAILED | `11.81 t/s` | 384 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `11.36 t/s` | 384 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `12.70 t/s` | 384 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `11.09 t/s` | 384 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `11.45 t/s` | 384 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `11.57 t/s` | 384 |
| 9 | `gpqa_127` | **D** | `A` | FAILED | `17.06 t/s` | 384 |
| 10 | `gpqa_69` | **C** | `A` | FAILED | `11.91 t/s` | 384 |
| 11 | `gpqa_3` | **C** | `B` | FAILED | `11.83 t/s` | 384 |
| 12 | `gpqa_185` | **A** | `A` | PASSED | `12.77 t/s` | 384 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `11.50 t/s` | 384 |
| 14 | `gpqa_165` | **C** | `A` | FAILED | `12.18 t/s` | 384 |
| 15 | `gpqa_169` | **C** | `None` | FAILED | `12.00 t/s` | 384 |
| 16 | `gpqa_15` | **D** | `A` | FAILED | `12.67 t/s` | 384 |
| 17 | `gpqa_159` | **A** | `C` | FAILED | `11.53 t/s` | 384 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `11.32 t/s` | 384 |
| 19 | `gpqa_134` | **D** | `None` | FAILED | `11.44 t/s` | 384 |
| 20 | `gpqa_44` | **C** | `None` | FAILED | `11.92 t/s` | 384 |

| - | `passkey_4k` | **Match** | `Match` | PASSED | `135.89 t/s` | Needle |
