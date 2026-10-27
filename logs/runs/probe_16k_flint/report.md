# Targeted 16K Runway Probe Report: Recursive Flint 40B MoE
- **Target Questions:** 5 candidate questions that timed out at the 8K ceiling in Exp 94
- **Token Runway Ceiling:** 16,384 tokens (`-c 24576`)
- **Strict Score Achieved:** **2/5** (40.0%)
- **Questions Exceeding 8,192 Tokens:** 5/5
- **Correct Answers Enabled by >8K Runway:** **2 questions**

## Question-by-Question Results
| ID | Gold | Pred (16K) | Strict Status | Tokens Used | Wall Time | Exceeded 8K? | Rescued? |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| `gpqa_42` | A | A | `correct` | 14435 | 1031.17s | Yes | **RESCUED** |
| `gpqa_128` | A | - | `no_answer_format` | 16384 | 1285.09s | Yes | **Failed** |
| `gpqa_160` | A | - | `no_answer_format` | 16384 | 1277.88s | Yes | **Failed** |
| `gpqa_10` | B | B | `correct` | 15459 | 1076.21s | Yes | **RESCUED** |
| `gpqa_144` | C | - | `no_answer_format` | 16384 | 724.64s | Yes | **Failed** |

