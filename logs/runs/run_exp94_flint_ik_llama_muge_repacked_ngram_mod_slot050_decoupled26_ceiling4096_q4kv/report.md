# GPQA results: exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv

Saved run: `run_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv`. Model: `RecursiveSI_flint-Q4_0_Repacked.gguf`. Ceiling: 8,192 output tokens.

Strict score: **18/50** (36.0%). Lenient audit: 22/50.

Mean saved decode rate: 17.14 tokens/s across 50 timing rows; 0 excluded. Rates must be finite and positive, with more than one generated token.

29/50 rows reached the recorded token ceiling or reported a length stop. 0/50 rows were recorded as having no final answer at truncation. These are different counts. Older rows lack raw stopping flags, so a below-ceiling response is not proof of a natural stop.

Regenerated from saved rows with `python3 benchmarks/summarize_runs.py --write`; recorded answers and grading flags are retained. Raw rows and manifests are unchanged.

| ID | Gold | Pred | Recorded status | Tokens | Decode tokens/s | Request s |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `gpqa_110` | A | - | no_answer_format | 8192 | 16.18 | 508.41 |
| `gpqa_42` | A | - | no_answer_format | 8192 | 15.93 | 515.84 |
| `gpqa_2` | B | B | correct | 591 | 19.19 | 32.17 |
| `gpqa_156` | A | A | correct | 204 | 20.48 | 11.33 |
| `gpqa_128` | A | - | no_answer_format | 8192 | 15.69 | 523.51 |
| `gpqa_12` | D | - | no_answer_format | 8192 | 16.13 | 509.96 |
| `gpqa_79` | D | - | no_answer_format | 8192 | 15.78 | 520.22 |
| `gpqa_13` | B | B | correct | 6029 | 16.74 | 361.39 |
| `gpqa_127` | D | - | no_answer_format | 8192 | 20.4 | 412.53 |
| `gpqa_69` | C | - | no_answer_format | 8192 | 16.01 | 513.43 |
| `gpqa_3` | C | D | wrong | 555 | 19.87 | 29.34 |
| `gpqa_185` | A | - | no_answer_format | 8192 | 15.94 | 515.04 |
| `gpqa_30` | B | - | no_answer_format | 8192 | 15.88 | 517.33 |
| `gpqa_165` | C | - | no_answer_format | 8192 | 16.56 | 498.75 |
| `gpqa_169` | C | C | correct | 1605 | 19.08 | 85.39 |
| `gpqa_15` | D | - | no_answer_format | 8192 | 16.56 | 495.9 |
| `gpqa_159` | A | A | correct | 6043 | 16.22 | 374.22 |
| `gpqa_36` | B | - | no_answer_format | 8192 | 15.89 | 516.67 |
| `gpqa_134` | D | D | correct | 4257 | 19.25 | 223.04 |
| `gpqa_44` | C | C | correct | 2390 | 18.21 | 132.37 |
| `gpqa_5` | C | C | correct | 2898 | 18.44 | 158.45 |
| `gpqa_53` | B | - | no_answer_format | 8192 | 15.85 | 517.86 |
| `gpqa_84` | B | B | correct | 6642 | 17.03 | 392.02 |
| `gpqa_80` | D | - | no_answer_format | 8192 | 16.32 | 503.58 |
| `gpqa_64` | D | - | no_answer_format | 8192 | 16.92 | 486.02 |
| `gpqa_73` | D | D | correct | 1124 | 19.29 | 59.69 |
| `gpqa_37` | A | - | no_answer_format | 8192 | 16.35 | 502.78 |
| `gpqa_126` | B | - | no_answer_format | 8192 | 16.15 | 508.65 |
| `gpqa_122` | B | B | correct | 5284 | 16.97 | 313.05 |
| `gpqa_78` | A | - | no_answer_format | 8192 | 16.08 | 511.24 |
| `gpqa_160` | A | - | no_answer_format | 8192 | 15.65 | 525.61 |
| `gpqa_66` | C | C | correct | 814 | 19.34 | 44.03 |
| `gpqa_45` | C | - | no_answer_format | 8192 | 15.92 | 515.28 |
| `gpqa_184` | C | C | correct | 257 | 20.69 | 13.68 |
| `gpqa_32` | B | - | no_answer_format | 8192 | 16.75 | 490.49 |
| `gpqa_52` | D | D | correct | 8038 | 15.85 | 508.62 |
| `gpqa_192` | C | B | wrong | 1540 | 18.93 | 82.55 |
| `gpqa_174` | B | D | wrong | 866 | 19.51 | 45.68 |
| `gpqa_10` | B | - | no_answer_format | 8192 | 16.92 | 485.96 |
| `gpqa_60` | D | D | correct | 7656 | 15.76 | 487.35 |
| `gpqa_170` | C | - | no_answer_format | 8192 | 15.71 | 522.98 |
| `gpqa_47` | A | - | no_answer_format | 8192 | 15.55 | 528.41 |
| `gpqa_131` | A | - | no_answer_format | 8192 | 16.16 | 509.06 |
| `gpqa_103` | B | B | correct | 2286 | 18.67 | 124.26 |
| `gpqa_193` | D | D | correct | 945 | 19.62 | 49.36 |
| `gpqa_95` | D | D | correct | 2704 | 18.29 | 148.87 |
| `gpqa_144` | C | - | no_answer_format | 8192 | 15.78 | 519.96 |
| `gpqa_100` | D | - | no_answer_format | 8192 | 15.67 | 524.56 |
| `gpqa_142` | C | - | no_answer_format | 8192 | 15.73 | 523.3 |
| `gpqa_61` | B | - | no_answer_format | 8192 | 15.32 | 536.57 |
