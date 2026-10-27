# Extreme Context Needle Retrieval Ladder: Exp83_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Calibrated_Temperature_Slot050_Ceiling4096_Q4KV

- **Timestamp:** `2026-10-13 07:13:35`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --slot-save-path /tmp/slots/ --slot-prompt-similarity 0.50 --spec-type suffix:n_max=4,suffix_min_match_len=5,suffix_max_depth=32 --spec-autotune -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,063 | **PASSED (100%)** | **`138.90 t/s`** | 173.2s | `16.23 t/s` | 21708.4 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.06 t/s`** | 470.9s | `14.52 t/s` | 21708.7 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.47 t/s`** | 1467.4s | `11.79 t/s` | 21708.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.96 t/s`** | 5060.0s | `8.56 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,063 tokens)
- **Expected Passkey:** `9679`
- **Decoded Snippet:** `The pass key is 9679.

The pass key is **9679

main: decoded 16 tokens in 1.01 s, speed: 15.80 t/s

llama_print_timings:        load time =  195718.29 ms
llama_print_timings:      sample time =`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `39641`
- **Decoded Snippet:** `The pass key is 39641.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.13 s, speed: 14.18 t/s

llama_print_timings:        load time =  494777.74 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `35192`
- **Decoded Snippet:** `The pass key is 35192. Remember it. 35192

main: decoded 16 tokens in 1.38 s, speed: 11.56 t/s

llama_print_timings:        load time = 1490555.45 ms
llama_print_timings:      sample time =       5.5`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `23777`
- **Decoded Snippet:** `The pass key is 23777.`
- **Status:** MATCH - ZERO REGRESSION

