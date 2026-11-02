# GPQA results: exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv

Saved run: `run_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv_16k_runway`. Model: `Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`. Ceiling: 16,384 output tokens.

Strict score: **19/50** (38.0%). Lenient audit: 23/50.

Mean saved decode rate: 17.6 tokens/s across 50 timing rows; 0 excluded. Rates must be finite and positive, with more than one generated token.

25/50 rows reached the recorded token ceiling or reported a length stop. 21/50 rows were recorded as having no final answer at truncation. These are different counts. Older rows lack raw stopping flags, so a below-ceiling response is not proof of a natural stop.

Regenerated from saved rows with `python3 benchmarks/summarize_runs.py --write`; recorded answers and grading flags are retained. Raw rows and manifests are unchanged.

| ID | Gold | Pred | Recorded status | Tokens | Decode tokens/s | Request s |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `gpqa_110` | A | - | no_answer_truncated | 16384 | 16.52 | 994.53 |
| `gpqa_42` | A | - | no_answer_truncated | 16384 | 16.15 | 1016.46 |
| `gpqa_2` | B | B | correct | 2457 | 22.51 | 110.93 |
| `gpqa_156` | A | A | correct | 1795 | 20.74 | 88.39 |
| `gpqa_128` | A | - | no_answer_truncated | 16384 | 16.44 | 999.26 |
| `gpqa_12` | D | - | no_answer_format | 16384 | 16.71 | 983.27 |
| `gpqa_79` | D | B | wrong | 9246 | 18.35 | 505.5 |
| `gpqa_13` | B | B | correct | 1638 | 19.6 | 85.23 |
| `gpqa_127` | D | - | no_answer_truncated | 16384 | 15.41 | 1080.78 |
| `gpqa_69` | C | - | no_answer_truncated | 16384 | 16.76 | 979.83 |
| `gpqa_3` | C | C | correct | 2027 | 21.43 | 96.47 |
| `gpqa_185` | A | C | wrong | 10248 | 17.49 | 587.79 |
| `gpqa_30` | B | - | no_answer_truncated | 16384 | 16.6 | 988.44 |
| `gpqa_165` | C | C | correct | 2154 | 19.25 | 117.68 |
| `gpqa_169` | C | C | correct | 2167 | 22.7 | 97.19 |
| `gpqa_15` | D | C | wrong | 10230 | 17.54 | 585.37 |
| `gpqa_159` | A | A | correct | 1209 | 22.35 | 56.27 |
| `gpqa_36` | B | D | wrong | 9765 | 18.03 | 543.17 |
| `gpqa_134` | D | D | correct | 1138 | 21.89 | 54.94 |
| `gpqa_44` | C | C | correct | 5781 | 20.05 | 290.12 |
| `gpqa_5` | C | C | correct | 1946 | 22.83 | 87.36 |
| `gpqa_53` | B | - | no_answer_truncated | 16384 | 16.3 | 1006.66 |
| `gpqa_84` | B | B | correct | 5957 | 19.37 | 310.08 |
| `gpqa_80` | D | - | no_answer_truncated | 16384 | 16.63 | 987.46 |
| `gpqa_64` | D | - | no_answer_truncated | 16384 | 16.67 | 985.14 |
| `gpqa_73` | D | D | correct | 14713 | 16.46 | 895.83 |
| `gpqa_37` | A | - | no_answer_truncated | 16384 | 15.61 | 1052.06 |
| `gpqa_126` | B | - | no_answer_truncated | 16384 | 16.83 | 975.19 |
| `gpqa_122` | B | B | correct | 5978 | 19.8 | 304.11 |
| `gpqa_78` | A | C | wrong | 9235 | 17.62 | 527.17 |
| `gpqa_160` | A | A | correct | 6681 | 18.72 | 359.61 |
| `gpqa_66` | C | - | no_answer_truncated | 16384 | 15.78 | 1040.11 |
| `gpqa_45` | C | - | no_answer_format | 16384 | 15.64 | 1049.15 |
| `gpqa_184` | C | C | correct | 11994 | 17.16 | 701.02 |
| `gpqa_32` | B | B | correct | 10400 | 17.04 | 613.09 |
| `gpqa_52` | D | - | no_answer_truncated | 16384 | 15.63 | 1050.71 |
| `gpqa_192` | C | - | no_answer_truncated | 16384 | 15.6 | 1052.21 |
| `gpqa_174` | B | - | no_answer_truncated | 16384 | 15.59 | 1053.5 |
| `gpqa_10` | B | - | no_answer_truncated | 16384 | 16.1 | 1020.58 |
| `gpqa_60` | D | - | no_answer_format | 16384 | 15.31 | 1072.44 |
| `gpqa_170` | C | C | correct | 10268 | 17.35 | 594.09 |
| `gpqa_47` | A | - | no_answer_truncated | 16384 | 16.83 | 975.19 |
| `gpqa_131` | A | D | wrong | 15599 | 15.92 | 982.79 |
| `gpqa_103` | B | B | correct | 15777 | 15.95 | 991.23 |
| `gpqa_193` | D | - | no_answer_truncated | 16384 | 15.79 | 1039.64 |
| `gpqa_95` | D | - | no_answer_truncated | 16384 | 16.31 | 1006.23 |
| `gpqa_144` | C | - | no_answer_truncated | 16384 | 15.56 | 1054.45 |
| `gpqa_100` | D | - | no_answer_truncated | 16384 | 16.67 | 985.27 |
| `gpqa_142` | C | - | no_answer_format | 16384 | 16.55 | 992.97 |
| `gpqa_61` | B | B | correct | 14900 | 15.86 | 942.06 |
