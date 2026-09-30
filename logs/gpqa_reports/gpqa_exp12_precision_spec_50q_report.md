# GPQA (50 Questions, 1536 Tokens) Report: Exp 12: Dual NUMA + MegaKernel + Precision Chained Speculation (ngram_min_hits=2 + MTP)

- **Timestamp:** `2026-09-07 22:22:41`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Command:** `numactl --interleave=all /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8085 -c 8192 -t 14 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa distribute -fa 1 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type ngram-map-k:n_max=16,ngram_min_hits=2,ngram_size_n=8 --spec-type mtp:n_max=1,p_min=0.0`
- **GPQA 50Q Score:** **17 / 50 (34.0%)**
- **GPQA 20Q Baseline Subset Score:** **9 / 20 (45.0%)**
- **Average Generation Speed:** **`18.74 t/s`**
- **Peak Generation Speed:** **`26.35 t/s`**
- **Average Prompt Speed:** **`123.01 t/s`**

## Question Breakdown

| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `gpqa_110` | **A** | `A` | PASSED | `19.22 t/s` | 1536 |
| 2 | `gpqa_42` | **A** | `A` | PASSED | `19.51 t/s` | 1536 |
| 3 | `gpqa_2` | **B** | `None` | FAILED | `19.62 t/s` | 1536 |
| 4 | `gpqa_156` | **A** | `A` | PASSED | `18.84 t/s` | 498 |
| 5 | `gpqa_128` | **A** | `A` | PASSED | `18.43 t/s` | 1536 |
| 6 | `gpqa_12` | **D** | `C` | FAILED | `18.54 t/s` | 1536 |
| 7 | `gpqa_79` | **D** | `A` | FAILED | `19.17 t/s` | 1536 |
| 8 | `gpqa_13` | **B** | `B` | PASSED | `16.71 t/s` | 1536 |
| 9 | `gpqa_127` | **D** | `A` | FAILED | `26.35 t/s` | 1536 |
| 10 | `gpqa_69` | **C** | `C` | PASSED | `19.88 t/s` | 1536 |
| 11 | `gpqa_3` | **C** | `A` | FAILED | `18.61 t/s` | 1536 |
| 12 | `gpqa_185` | **A** | `A` | PASSED | `19.18 t/s` | 1536 |
| 13 | `gpqa_30` | **B** | `A` | FAILED | `17.91 t/s` | 1536 |
| 14 | `gpqa_165` | **C** | `A` | FAILED | `17.62 t/s` | 1536 |
| 15 | `gpqa_169` | **C** | `C` | PASSED | `20.36 t/s` | 1086 |
| 16 | `gpqa_15` | **D** | `C` | FAILED | `18.15 t/s` | 1536 |
| 17 | `gpqa_159` | **A** | `C` | FAILED | `19.43 t/s` | 1199 |
| 18 | `gpqa_36` | **B** | `C` | FAILED | `19.16 t/s` | 1536 |
| 19 | `gpqa_134` | **D** | `A` | FAILED | `18.98 t/s` | 1536 |
| 20 | `gpqa_44` | **C** | `C` | PASSED | `18.99 t/s` | 1536 |
| 21 | `gpqa_5` | **C** | `A` | FAILED | `17.12 t/s` | 1536 |
| 22 | `gpqa_53` | **B** | `C` | FAILED | `18.27 t/s` | 1536 |
| 23 | `gpqa_84` | **B** | `A` | FAILED | `20.04 t/s` | 1536 |
| 24 | `gpqa_80` | **D** | `A` | FAILED | `18.01 t/s` | 1536 |
| 25 | `gpqa_64` | **D** | `A` | FAILED | `19.04 t/s` | 1536 |
| 26 | `gpqa_73` | **D** | `None` | FAILED | `18.99 t/s` | 1536 |
| 27 | `gpqa_37` | **A** | `A` | PASSED | `17.59 t/s` | 1536 |
| 28 | `gpqa_126` | **B** | `C` | FAILED | `18.76 t/s` | 1536 |
| 29 | `gpqa_122` | **B** | `A` | FAILED | `18.20 t/s` | 1536 |
| 30 | `gpqa_78` | **A** | `A` | PASSED | `17.72 t/s` | 1536 |
| 31 | `gpqa_160` | **A** | `C` | FAILED | `18.87 t/s` | 1536 |
| 32 | `gpqa_66` | **C** | `C` | PASSED | `18.65 t/s` | 1536 |
| 33 | `gpqa_45` | **C** | `C` | PASSED | `17.93 t/s` | 1536 |
| 34 | `gpqa_184` | **C** | `B` | FAILED | `19.94 t/s` | 1021 |
| 35 | `gpqa_32` | **B** | `A` | FAILED | `17.70 t/s` | 1536 |
| 36 | `gpqa_52` | **D** | `A` | FAILED | `18.27 t/s` | 1536 |
| 37 | `gpqa_192` | **C** | `C` | PASSED | `18.47 t/s` | 1536 |
| 38 | `gpqa_174` | **B** | `A` | FAILED | `17.77 t/s` | 1536 |
| 39 | `gpqa_10` | **B** | `A` | FAILED | `17.70 t/s` | 1536 |
| 40 | `gpqa_60` | **D** | `A` | FAILED | `18.07 t/s` | 1536 |
| 41 | `gpqa_170` | **C** | `A` | FAILED | `18.47 t/s` | 1536 |
| 42 | `gpqa_47` | **A** | `A` | PASSED | `17.69 t/s` | 1536 |
| 43 | `gpqa_131` | **A** | `A` | PASSED | `17.85 t/s` | 1536 |
| 44 | `gpqa_103` | **B** | `A` | FAILED | `19.00 t/s` | 1536 |
| 45 | `gpqa_193` | **D** | `A` | FAILED | `19.36 t/s` | 1536 |
| 46 | `gpqa_95` | **D** | `D` | PASSED | `19.60 t/s` | 1529 |
| 47 | `gpqa_144` | **C** | `None` | FAILED | `19.27 t/s` | 1536 |
| 48 | `gpqa_100` | **D** | `A` | FAILED | `17.74 t/s` | 1536 |
| 49 | `gpqa_142` | **C** | `A` | FAILED | `17.94 t/s` | 1536 |
| 50 | `gpqa_61` | **B** | `A` | FAILED | `18.45 t/s` | 1536 |
