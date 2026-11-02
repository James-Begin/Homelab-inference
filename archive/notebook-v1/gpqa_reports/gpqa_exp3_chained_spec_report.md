# GPQA (20 Questions) & Long-Context Report: Exp 3: Chained Speculation (N-Gram + MTP)

- **Timestamp:** `2026-09-02 18:04:45`
- **Command:** `numactl --cpunodebind=0 --membind=0 /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8085 -c 8192 -t 10 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa isolate -fa 1 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type ngram-mod:n_max=16,n_min=3,ngram_size_n=4 --spec-type mtp:n_max=1,p_min=0.0`
- **GPQA Score:** **6 / 20 (30.0%)**
- **Average Generation Speed:** **`13.15 t/s`**
- **Average Prompt Speed:** **`103.18 t/s`**
- **4K Context Needle Passkey:** **PASSED**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `13.75 t/s` | 384 |
| 2 | `gpqa_42` | **A** | `None` | FAILED | `12.04 t/s` | 384 |
| 3 | `gpqa_2` | **B** | `C` | FAILED | `11.81 t/s` | 384 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `12.24 t/s` | 384 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `12.67 t/s` | 384 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `11.28 t/s` | 384 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `12.32 t/s` | 384 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `11.47 t/s` | 384 |
| 9 | `gpqa_127` | **D** | `None` | FAILED | `25.53 t/s` | 384 |
| 10 | `gpqa_69` | **C** | `C` | PASSED | `14.40 t/s` | 384 |
| 11 | `gpqa_3` | **C** | `B` | FAILED | `12.17 t/s` | 384 |
| 12 | `gpqa_185` | **A** | `None` | FAILED | `13.22 t/s` | 384 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `12.73 t/s` | 384 |
| 14 | `gpqa_165` | **C** | `None` | FAILED | `11.95 t/s` | 384 |
| 15 | `gpqa_169` | **C** | `None` | FAILED | `12.18 t/s` | 384 |
| 16 | `gpqa_15` | **D** | `A` | FAILED | `12.24 t/s` | 384 |
| 17 | `gpqa_159` | **A** | `A` | PASSED | `12.51 t/s` | 384 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `12.46 t/s` | 384 |
| 19 | `gpqa_134` | **D** | `None` | FAILED | `12.60 t/s` | 384 |
| 20 | `gpqa_44` | **C** | `None` | FAILED | `13.48 t/s` | 384 |

| - | `passkey_4k` | **Match** | `Match` | PASSED | `116.60 t/s` | Needle |
