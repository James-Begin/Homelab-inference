# Extreme Context Needle Retrieval Ladder: Exp94_Flint_ik_llama_MUGE_Repacked_Ngram_Mod_Slot050_Decoupled26_Ceiling4096_Q4KV

- **Timestamp:** `2026-10-25 07:32:31`
- **Model:** `/home/james/ik_llama.cpp/build/models/RecursiveSI_flint-Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 26 -ctk q4_0 -ctv q4_0 --numa numactl -muge`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,058 | **PASSED (100%)** | **`123.17 t/s`** | 195.3s | `14.60 t/s` | 29507.1 MB |
| **32K Context** | 48,058 | **PASSED (100%)** | **`84.46 t/s`** | 569.0s | `11.96 t/s` | 29507.2 MB |
| **64K Context** | 96,058 | **PASSED (100%)** | **`50.81 t/s`** | 1890.7s | `9.20 t/s` | 29507.3 MB |
| **128K Context** | 192,058 | **PASSED (100%)** | **`28.55 t/s`** | 6727.7s | `5.26 t/s` | 29508.7 MB |

## Detailed Needle Extractions

### 16K Context (24,058 tokens)
- **Expected Passkey:** `49465`
- **Decoded Snippet:** `The pass key is 49465. Remember it. 49465 is the pass key. The

main: decoded 16 tokens in 1.11 s, speed: 14.37 t/s

llama_print_timings:        load time =  225309.89 ms
llama_print_timings:      sa`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,058 tokens)
- **Expected Passkey:** `5742`
- **Decoded Snippet:** `The pass key is 5742. Remember it. 5742 is the pass key. The

main: decoded 16 tokens in 1.36 s, speed: 11.80 t/s

llama_print_timings:        load time =  599885.52 ms
llama_print_timings:      samp`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,058 tokens)
- **Expected Passkey:** `4216`
- **Decoded Snippet:** `The pass key is 4216. Remember it. 4216 is the pass key. The

main: decoded 16 tokens in 1.76 s, speed: 9.11 t/s

llama_print_timings:        load time = 1921711.51 ms
llama_print_timings:      sampl`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,058 tokens)
- **Expected Passkey:** `23603`
- **Decoded Snippet:** `The pass key is 23603. The grass is green. The sky is blue. The sun

main: decoded 16 tokens in 3.06 s, speed: 5.23 t/s

llama_print_timings:        load time = 6757836.08 ms
llama_print_timings:`
- **Status:** MATCH - ZERO REGRESSION

