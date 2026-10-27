# GPQA (50 Questions, 1536 Tokens) Report: Exp 6 / 11: Dual NUMA + Chained Speculation (Unfiltered N-Gram + MTP)

- **Timestamp:** `2026-09-08 02:19:32`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Command:** `numactl --interleave=all /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8085 -c 8192 -t 14 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa distribute -fa 1 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type ngram-mod:n_max=16,n_min=3,ngram_size_n=4 --spec-type mtp:n_max=1,p_min=0.0`
- **GPQA 50Q Score:** **20 / 50 (40.0%)**
- **GPQA 20Q Baseline Subset Score:** **10 / 20 (50.0%)**
- **Average Generation Speed:** **`14.60 t/s`**
- **Peak Generation Speed:** **`22.47 t/s`**
- **Average Prompt Speed:** **`124.81 t/s`**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `14.40 t/s` | 1536 |
| 2 | `gpqa_42` | **A** | `A` | PASSED | `13.37 t/s` | 1536 |
| 3 | `gpqa_2` | **B** | `C` | FAILED | `14.01 t/s` | 1536 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `15.81 t/s` | 517 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `14.65 t/s` | 1536 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `14.06 t/s` | 1536 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `15.99 t/s` | 1536 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `14.45 t/s` | 1536 |
| 9 | `gpqa_127` | **D** | `A` | FAILED | `22.47 t/s` | 1536 |
| 10 | `gpqa_69` | **C** | `C` | PASSED | `19.52 t/s` | 1536 |
| 11 | `gpqa_3` | **C** | `C` | PASSED | `14.67 t/s` | 1536 |
| 12 | `gpqa_185` | **A** | `A` | PASSED | `13.86 t/s` | 1536 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `14.41 t/s` | 1536 |
| 14 | `gpqa_165` | **C** | `A` | FAILED | `14.70 t/s` | 1536 |
| 15 | `gpqa_169` | **C** | `C` | PASSED | `15.09 t/s` | 1144 |
| 16 | `gpqa_15` | **D** | `A` | FAILED | `14.67 t/s` | 1536 |
| 17 | `gpqa_159` | **A** | `A` | PASSED | `14.72 t/s` | 1536 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `14.30 t/s` | 1536 |
| 19 | `gpqa_134` | **D** | `A` | FAILED | `14.15 t/s` | 1255 |
| 20 | `gpqa_44` | **C** | `None` | FAILED | `14.00 t/s` | 1536 |
| 21 | `gpqa_5` | **C** | `C` | PASSED | `15.18 t/s` | 1536 |
| 22 | `gpqa_53` | **B** | `None` | FAILED | `13.37 t/s` | 1536 |
| 23 | `gpqa_84` | **B** | `B` | PASSED | `15.31 t/s` | 1350 |
| 24 | `gpqa_80` | **D** | `A` | FAILED | `15.69 t/s` | 1536 |
| 25 | `gpqa_64` | **D** | `C` | FAILED | `14.51 t/s` | 1536 |
| 26 | `gpqa_73` | **D** | `A` | FAILED | `13.55 t/s` | 1536 |
| 27 | `gpqa_37` | **A** | `A` | PASSED | `14.12 t/s` | 1536 |
| 28 | `gpqa_126` | **B** | `A` | FAILED | `14.61 t/s` | 1536 |
| 29 | `gpqa_122` | **B** | `A` | FAILED | `14.21 t/s` | 1536 |
| 30 | `gpqa_78` | **A** | `A` | PASSED | `14.89 t/s` | 1536 |
| 31 | `gpqa_160` | **A** | `A` | PASSED | `13.17 t/s` | 1536 |
| 32 | `gpqa_66` | **C** | `A` | FAILED | `12.37 t/s` | 1536 |
| 33 | `gpqa_45` | **C** | `C` | PASSED | `14.27 t/s` | 1536 |
| 34 | `gpqa_184` | **C** | `C` | PASSED | `15.03 t/s` | 730 |
| 35 | `gpqa_32` | **B** | `A` | FAILED | `14.83 t/s` | 1536 |
| 36 | `gpqa_52` | **D** | `A` | FAILED | `14.55 t/s` | 1536 |
| 37 | `gpqa_192` | **C** | `C` | PASSED | `12.95 t/s` | 1536 |
| 38 | `gpqa_174` | **B** | `A` | FAILED | `13.55 t/s` | 1536 |
| 39 | `gpqa_10` | **B** | `A` | FAILED | `14.58 t/s` | 1536 |
| 40 | `gpqa_60` | **D** | `C` | FAILED | `13.76 t/s` | 1536 |
| 41 | `gpqa_170` | **C** | `A` | FAILED | `14.62 t/s` | 1536 |
| 42 | `gpqa_47` | **A** | `A` | PASSED | `13.82 t/s` | 1536 |
| 43 | `gpqa_131` | **A** | `None` | FAILED | `14.28 t/s` | 1536 |
| 44 | `gpqa_103` | **B** | `None` | FAILED | `14.44 t/s` | 1536 |
| 45 | `gpqa_193` | **D** | `D` | PASSED | `13.97 t/s` | 1536 |
| 46 | `gpqa_95` | **D** | `A` | FAILED | `14.62 t/s` | 1536 |
| 47 | `gpqa_144` | **C** | `A` | FAILED | `14.55 t/s` | 1536 |
| 48 | `gpqa_100` | **D** | `A` | FAILED | `13.73 t/s` | 1536 |
| 49 | `gpqa_142` | **C** | `A` | FAILED | `13.62 t/s` | 1536 |
| 50 | `gpqa_61` | **B** | `A` | FAILED | `14.39 t/s` | 1536 |
