# Extreme Context Needle Retrieval Ladder: Exp86_Phys_Pinning_28decode_26batch_Repacked_IQ4XS_MUGE_Triple_Champion_Ceiling4096_Q4KV

- **Timestamp:** `2026-10-22 23:33:48`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 26 --slot-save-path /tmp/slots/ --slot-prompt-similarity 0.50 --spec-type suffix:n_max=4,suffix_min_match_len=5,suffix_max_depth=32 --spec-autotune -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`140.98 t/s`** | 170.7s | `16.38 t/s` | 21708.6 MB |
| **32K Context** | 48,063 | **PASSED (100%)** | **`105.03 t/s`** | 457.6s | `14.35 t/s` | 21708.7 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`69.72 t/s`** | 1377.9s | `11.21 t/s` | 21708.7 MB |
| **128K Context** | 192,061 | **PASSED (100%)** | **`41.01 t/s`** | 4683.1s | `8.50 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `49001`
- **Decoded Snippet:** `The pass key is 49001.`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,063 tokens)
- **Expected Passkey:** `8622`
- **Decoded Snippet:** `The pass key is 8622. Remember it. 8622 is the

main: decoded 16 tokens in 1.14 s, speed: 14.02 t/s

llama_print_timings:        load time =  481003.99 ms
llama_print_timings:      sample time =`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `11687`
- **Decoded Snippet:** `The pass key is 11687.



main: decoded 8 tokens in 0.73 s, speed: 11.00 t/s

llama_print_timings:        load time = 1401338.09 ms
llama_print_timings:      sample time =       2.98 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,061 tokens)
- **Expected Passkey:** `885`
- **Decoded Snippet:** `The pass key is 885.

<think>

</think>

The pass key is 8

main: decoded 16 tokens in 1.91 s, speed: 8.39 t/s

llama_print_timings:        load time = 4706941.26 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

