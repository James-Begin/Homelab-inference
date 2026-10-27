# Extreme Context Needle Retrieval Ladder: Exp93_Flint_Dense_Drafter_Qwen08B_Slot050_Decoupled26_Ceiling4096_Q4KV

- **Timestamp:** `2026-10-25 01:12:09`
- **Model:** `/home/james/ik_llama.cpp/build/models/RecursiveSI_flint-Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 26 -ctk q4_0 -ctv q4_0 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 25,000 | **FAILED** | **`0.00 t/s`** | 782.3s | `0.00 t/s` | 43579.7 MB |
| **32K Context** | 50,000 | **FAILED** | **`0.00 t/s`** | 2587.7s | `0.00 t/s` | 43619.2 MB |
| **64K Context** | 0 | **FAILED** | **`0.00 t/s`** | 0.0s | `0.00 t/s` | 0.0 MB |
| **128K Context** | 0 | **FAILED** | **`0.00 t/s`** | 0.0s | `0.00 t/s` | 0.0 MB |

## Detailed Needle Extractions

### 16K Context (25,000 tokens)
- **Expected Passkey:** `30887`
- **Decoded Snippet:** `The pass key is12.55.418.341 I main: decoded 16 tokens in 3.08 s, speed: 5.20 t/s
	Command being timed: "numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15`
- **Status:** MISMATCH

### 32K Context (50,000 tokens)
- **Expected Passkey:** `30887`
- **Decoded Snippet:** `The pass key is43.05.480.351 I main: decoded 16 tokens in 4.12 s, speed: 3.89 t/s
	Command being timed: "numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15`
- **Status:** MISMATCH

### 64K Context (0 tokens)
- **Expected Passkey:** `None`
- **Decoded Snippet:** `ERROR`
- **Status:** MISMATCH

### 128K Context (0 tokens)
- **Expected Passkey:** `None`
- **Decoded Snippet:** `ERROR`
- **Status:** MISMATCH
