# Extreme Context Needle Retrieval Ladder: Exp81_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Unified_Champion_Steering_Slot050_Ceiling4096_Q4KV

- **Timestamp:** `2026-10-12 21:19:32`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --slot-save-path /tmp/slots/ --slot-prompt-similarity 0.50 --spec-type suffix:n_max=4,suffix_min_match_len=5,suffix_max_depth=32 --spec-autotune -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.72 t/s`** | 173.5s | `16.58 t/s` | 21709.0 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.33 t/s`** | 469.7s | `14.78 t/s` | 21709.1 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.43 t/s`** | 1468.1s | `11.70 t/s` | 21708.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.94 t/s`** | 5062.4s | `8.47 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `12371`
- **Decoded Snippet:** `The pass key is 12371.`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `37218`
- **Decoded Snippet:** `The pass key is 37218.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `26857`
- **Decoded Snippet:** `The pass key is 26857.

main: decoded 7 tokens in 0.61 s, speed: 11.46 t/s

llama_print_timings:        load time = 1490826.62 ms
llama_print_timings:      sample time =       2.57 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `23916`
- **Decoded Snippet:** `The pass key is 23916.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.91 s, speed: 8.36 t/s

llama_print_timings:        load time = 5085439.37 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

