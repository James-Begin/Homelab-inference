# Extreme Context Needle Retrieval Ladder: Exp89_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Slot_Similarity_070_Ceiling4096_Q4KV

- **Timestamp:** `2026-10-23 14:29:06`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --slot-save-path /tmp/slots/ --slot-prompt-similarity 0.70 --spec-type suffix:n_max=4,suffix_min_match_len=5,suffix_max_depth=32 --spec-autotune -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.29 t/s`** | 174.0s | `16.62 t/s` | 21707.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`101.72 t/s`** | 472.5s | `14.62 t/s` | 21708.7 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.16 t/s`** | 1474.3s | `11.69 t/s` | 21708.8 MB |
| **128K Context** | 192,063 | **PASSED (100%)** | **`36.32 t/s`** | 5288.5s | `8.51 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `23567`
- **Decoded Snippet:** `The pass key is 23567.`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `20477`
- **Decoded Snippet:** `The pass key is 20477.

<think>

The user asks me to identify

main: decoded 16 tokens in 1.12 s, speed: 14.28 t/s

llama_print_timings:        load time =  496111.15 ms
llama_print_timings:      sam`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `13100`
- **Decoded Snippet:** `The pass key is 13100.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.39 s, speed: 11.47 t/s

llama_print_timings:        load time = 1497633.64 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,063 tokens)
- **Expected Passkey:** `3458`
- **Decoded Snippet:** `The pass key is 3458.

The pass key is 3458

main: decoded 16 tokens in 1.91 s, speed: 8.39 t/s

llama_print_timings:        load time = 5312093.82 ms
llama_print_timings:      sample time =       5.`
- **Status:** MATCH - ZERO REGRESSION

