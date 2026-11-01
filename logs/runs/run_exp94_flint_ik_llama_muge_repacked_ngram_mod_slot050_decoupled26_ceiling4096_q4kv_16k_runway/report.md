# GPQA results: exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv

Saved run: `run_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_16k_runway`. Model: `RecursiveSI_flint-Q4_0_Repacked.gguf`. Ceiling: 16,384 output tokens.

Strict score: **23/50** (46.0%). Lenient audit: 29/50.

Mean saved decode rate: 15.99 tokens/s across 50 timing rows; 0 excluded. Rates must be finite and positive, with more than one generated token.

19/50 rows reached the recorded token ceiling or reported a length stop. 19/50 rows were recorded as having no final answer at truncation. These are different counts. Older rows lack raw stopping flags, so a below-ceiling response is not proof of a natural stop.

Regenerated from saved rows with `python3 benchmarks/summarize_runs.py --write`; recorded answers and grading flags are retained. Raw rows and manifests are unchanged.

| ID | Gold | Pred | Recorded status | Tokens | Decode tokens/s | Request s |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `gpqa_110` | A | - | no_answer_truncated | 16384 | 13.17 | 1245.26 |
| `gpqa_42` | A | - | no_answer_truncated | 16384 | 13.35 | 1228.69 |
| `gpqa_2` | B | B | correct | 630 | 19.82 | 33.4 |
| `gpqa_156` | A | A | correct | 222 | 19.96 | 12.26 |
| `gpqa_128` | A | B | wrong | 15923 | 13.19 | 1209.13 |
| `gpqa_12` | D | - | no_answer_truncated | 16384 | 13.29 | 1234.73 |
| `gpqa_79` | D | - | no_answer_truncated | 16384 | 15.53 | 1056.58 |
| `gpqa_13` | B | B | correct | 6029 | 16.62 | 364.2 |
| `gpqa_127` | D | - | no_answer_truncated | 16384 | 17.06 | 971.23 |
| `gpqa_69` | C | - | no_answer_truncated | 16384 | 13.3 | 1233.49 |
| `gpqa_3` | C | D | wrong | 555 | 19.98 | 29.45 |
| `gpqa_185` | A | - | no_answer_truncated | 16384 | 13.13 | 1248.46 |
| `gpqa_30` | B | - | no_answer_truncated | 16384 | 13.71 | 1196.6 |
| `gpqa_165` | C | A | wrong | 9701 | 16.25 | 601.06 |
| `gpqa_169` | C | C | correct | 2114 | 18.99 | 112.61 |
| `gpqa_15` | D | - | no_answer_truncated | 16384 | 13.72 | 1195.12 |
| `gpqa_159` | A | A | correct | 6043 | 16.34 | 371.59 |
| `gpqa_36` | B | - | no_answer_truncated | 16384 | 13.17 | 1245.12 |
| `gpqa_134` | D | D | correct | 4257 | 19.5 | 220.67 |
| `gpqa_44` | C | C | correct | 2390 | 18.38 | 131.2 |
| `gpqa_5` | C | C | correct | 2898 | 18.65 | 156.55 |
| `gpqa_53` | B | - | no_answer_truncated | 16384 | 12.7 | 1291.15 |
| `gpqa_84` | B | B | correct | 6642 | 17.29 | 386.21 |
| `gpqa_80` | D | D | correct | 11837 | 15.12 | 784.69 |
| `gpqa_64` | D | - | no_answer_truncated | 16384 | 14.04 | 1169.46 |
| `gpqa_73` | D | D | correct | 1124 | 19.36 | 59.76 |
| `gpqa_37` | A | A | correct | 13649 | 14.55 | 940.02 |
| `gpqa_126` | B | - | no_answer_truncated | 16384 | 13.28 | 1235.57 |
| `gpqa_122` | B | B | correct | 3062 | 18.13 | 170.82 |
| `gpqa_78` | A | A | correct | 11249 | 15.04 | 749.93 |
| `gpqa_160` | A | C | wrong | 12134 | 14.15 | 859.51 |
| `gpqa_66` | C | C | correct | 814 | 19.64 | 43.58 |
| `gpqa_45` | C | - | no_answer_truncated | 16384 | 13.42 | 1221.53 |
| `gpqa_184` | C | C | correct | 257 | 20.87 | 14.11 |
| `gpqa_32` | B | - | no_answer_truncated | 16384 | 13.35 | 1229.14 |
| `gpqa_52` | D | D | correct | 8038 | 16.07 | 501.88 |
| `gpqa_192` | C | B | wrong | 1137 | 19.51 | 59.41 |
| `gpqa_174` | B | D | wrong | 659 | 21.09 | 32.46 |
| `gpqa_10` | B | - | no_answer_truncated | 16384 | 14.2 | 1155.93 |
| `gpqa_60` | D | D | correct | 7656 | 15.99 | 480.6 |
| `gpqa_170` | C | B | wrong | 12813 | 14.26 | 900.04 |
| `gpqa_47` | A | - | no_answer_truncated | 16384 | 13.16 | 1246.99 |
| `gpqa_131` | A | - | no_answer_truncated | 16384 | 13.33 | 1231.45 |
| `gpqa_103` | B | B | correct | 2286 | 18.54 | 125.31 |
| `gpqa_193` | D | D | correct | 945 | 19.86 | 48.78 |
| `gpqa_95` | D | D | correct | 2704 | 18.78 | 144.92 |
| `gpqa_144` | C | C | correct | 9066 | 15.76 | 575.94 |
| `gpqa_100` | D | - | no_answer_truncated | 16384 | 12.84 | 1277.69 |
| `gpqa_142` | C | D | wrong | 12020 | 14.51 | 831.14 |
| `gpqa_61` | B | B | correct | 15781 | 13.43 | 1177.49 |
