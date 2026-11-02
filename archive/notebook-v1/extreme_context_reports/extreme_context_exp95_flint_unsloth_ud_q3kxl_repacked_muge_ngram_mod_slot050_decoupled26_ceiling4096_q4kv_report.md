# Extreme Context Needle Retrieval Ladder: Exp95_Flint_Unsloth_UD_Q3KXL_Repacked_MUGE_Ngram_Mod_Slot050_Decoupled26_Ceiling4096_Q4KV

- **Timestamp:** `2026-10-25 13:05:54`
- **Model:** `/home/james/ik_llama.cpp/build/models/flint-UD-Q3_K_XL_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 26 -ctk q4_0 -ctv q4_0 --numa numactl -muge`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,058 | **PASSED (100%)** | **`116.27 t/s`** | 206.9s | `13.13 t/s` | 25351.6 MB |
| **32K Context** | 48,058 | **PASSED (100%)** | **`81.66 t/s`** | 588.5s | `11.55 t/s` | 25351.7 MB |
| **64K Context** | 96,058 | **PASSED (100%)** | **`49.02 t/s`** | 1959.4s | `8.43 t/s` | 25351.8 MB |
| **128K Context** | 192,058 | **PASSED (100%)** | **`28.12 t/s`** | 6829.6s | `5.18 t/s` | 25353.0 MB |

## Detailed Needle Extractions

### 16K Context (24,058 tokens)
- **Expected Passkey:** `42057`
- **Decoded Snippet:** `The pass key is 42057. Remember it. 42057 is the pass key. The

main: decoded 16 tokens in 1.24 s, speed: 12.95 t/s

llama_print_timings:        load time =  231836.90 ms
llama_print_timings:      sa`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,058 tokens)
- **Expected Passkey:** `39288`
- **Decoded Snippet:** `The pass key is 39288. Remember it. The grass is green. The sky is blue

main: decoded 16 tokens in 1.40 s, speed: 11.40 t/s

llama_print_timings:        load time =  613758.15 ms
llama_print_timings`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,058 tokens)
- **Expected Passkey:** `12024`
- **Decoded Snippet:** `The pass key is 12024. Remember it. The pass key is 12024. The

main: decoded 16 tokens in 1.92 s, speed: 8.35 t/s

llama_print_timings:        load time = 1984220.33 ms
llama_print_timings:      sam`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,058 tokens)
- **Expected Passkey:** `48616`
- **Decoded Snippet:** `The pass key is 48616. The grass is green. The sky is blue. The sun

main: decoded 16 tokens in 3.11 s, speed: 5.15 t/s

llama_print_timings:        load time = 6855489.30 ms
llama_print_timings:`
- **Status:** MATCH - ZERO REGRESSION

