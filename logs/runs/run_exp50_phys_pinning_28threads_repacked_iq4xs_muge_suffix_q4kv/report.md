# GPQA results: exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv

Saved run: `run_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv`. Model: `Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`. Ceiling: 8,192 output tokens.

Strict score: **13/50** (26.0%). Lenient audit: 20/50.

Mean saved decode rate: 19.18 tokens/s across 50 timing rows; 0 excluded. Rates must be finite and positive, with more than one generated token.

37/50 rows reached the recorded token ceiling or reported a length stop. 27/50 rows were recorded as having no final answer at truncation. These are different counts. Older rows lack raw stopping flags, so a below-ceiling response is not proof of a natural stop.

Regenerated from saved rows with `python3 benchmarks/summarize_runs.py --write`; recorded answers and grading flags are retained. Raw rows and manifests are unchanged.

| ID | Gold | Pred | Recorded status | Tokens | Decode tokens/s | Request s |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `gpqa_110` | A | - | no_answer_truncated | 8192 | 18.67 | 441.42 |
| `gpqa_42` | A | - | no_answer_truncated | 8192 | 18.89 | 435.77 |
| `gpqa_2` | B | B | correct | 2457 | 22.6 | 110.52 |
| `gpqa_156` | A | A | correct | 1795 | 20.85 | 88.01 |
| `gpqa_128` | A | - | no_answer_truncated | 8192 | 18.51 | 445.03 |
| `gpqa_12` | D | - | no_answer_format | 8192 | 19.42 | 424.43 |
| `gpqa_79` | D | - | no_answer_format | 8192 | 18.77 | 438.04 |
| `gpqa_13` | B | B | correct | 1638 | 19.63 | 85.1 |
| `gpqa_127` | D | - | no_answer_truncated | 8192 | 17.88 | 475.78 |
| `gpqa_69` | C | - | no_answer_truncated | 8192 | 19.47 | 422.83 |
| `gpqa_3` | C | C | correct | 2027 | 21.53 | 95.91 |
| `gpqa_185` | A | - | no_answer_format | 8192 | 18.43 | 446.37 |
| `gpqa_30` | B | - | no_answer_truncated | 8192 | 19.13 | 429.85 |
| `gpqa_165` | C | C | correct | 2154 | 19.28 | 118.3 |
| `gpqa_169` | C | C | correct | 2167 | 22.74 | 96.97 |
| `gpqa_15` | D | - | no_answer_format | 8192 | 18.26 | 450.74 |
| `gpqa_159` | A | A | correct | 1209 | 22.37 | 55.83 |
| `gpqa_36` | B | - | no_answer_format | 8192 | 18.52 | 444.14 |
| `gpqa_134` | D | D | correct | 1138 | 21.88 | 54.61 |
| `gpqa_44` | C | C | correct | 5781 | 20.01 | 290.7 |
| `gpqa_5` | C | C | correct | 1946 | 22.81 | 87.32 |
| `gpqa_53` | B | - | no_answer_truncated | 8192 | 18.51 | 444.6 |
| `gpqa_84` | B | B | correct | 5957 | 19.35 | 310.4 |
| `gpqa_80` | D | - | no_answer_truncated | 8192 | 19.08 | 431.61 |
| `gpqa_64` | D | - | no_answer_truncated | 8192 | 19.5 | 422.75 |
| `gpqa_73` | D | - | no_answer_truncated | 8192 | 18.8 | 437.41 |
| `gpqa_37` | A | - | no_answer_truncated | 8192 | 18.0 | 457.62 |
| `gpqa_126` | B | - | no_answer_truncated | 8192 | 19.55 | 420.66 |
| `gpqa_122` | B | B | correct | 5978 | 19.75 | 304.74 |
| `gpqa_78` | A | - | no_answer_truncated | 8192 | 17.95 | 459.26 |
| `gpqa_160` | A | A | correct | 6681 | 18.63 | 360.97 |
| `gpqa_66` | C | - | no_answer_truncated | 8192 | 18.47 | 445.54 |
| `gpqa_45` | C | - | no_answer_format | 8192 | 18.49 | 444.38 |
| `gpqa_184` | C | - | no_answer_truncated | 8192 | 18.54 | 443.78 |
| `gpqa_32` | B | - | no_answer_format | 8192 | 17.84 | 461.67 |
| `gpqa_52` | D | - | no_answer_truncated | 8192 | 18.26 | 450.87 |
| `gpqa_192` | C | - | no_answer_truncated | 8192 | 18.26 | 450.37 |
| `gpqa_174` | B | - | no_answer_truncated | 8192 | 18.05 | 455.82 |
| `gpqa_10` | B | - | no_answer_truncated | 8192 | 18.04 | 456.99 |
| `gpqa_60` | D | - | no_answer_truncated | 8192 | 17.89 | 459.93 |
| `gpqa_170` | C | - | no_answer_format | 8192 | 17.95 | 458.76 |
| `gpqa_47` | A | - | no_answer_truncated | 8192 | 19.3 | 426.29 |
| `gpqa_131` | A | - | no_answer_format | 8192 | 18.17 | 453.47 |
| `gpqa_103` | B | - | no_answer_truncated | 8192 | 18.36 | 448.38 |
| `gpqa_193` | D | - | no_answer_truncated | 8192 | 18.6 | 442.61 |
| `gpqa_95` | D | - | no_answer_truncated | 8192 | 19.02 | 432.57 |
| `gpqa_144` | C | - | no_answer_truncated | 8192 | 18.42 | 446.28 |
| `gpqa_100` | D | - | no_answer_truncated | 8192 | 18.96 | 434.21 |
| `gpqa_142` | C | - | no_answer_format | 8192 | 19.18 | 430.02 |
| `gpqa_61` | B | - | no_answer_truncated | 8192 | 18.18 | 452.85 |
