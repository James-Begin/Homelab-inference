# Homelab Inference writing style

Version 1 · 31 October 2026

This is the editorial contract for the README, technical notes, animation captions, and code examples. These rules describe the voice for this project; they are not a test for identifying AI authorship.

## Voice and reader

Write as the person who ran the experiments, explaining the code to another interested programmer. The reader can understand a loop and a benchmark table, but may never have used NUMA or a quantized inference kernel. A recruiter should understand the goal, hardware, contribution, and result from the opening three paragraphs.

The voice is technical, candid, and occasionally amused. Let the awkward result remain awkward: months of Qwen tuning, followed by better coding results from Flint at nearly the same decode rate. Do not turn that into a motivational story or imply the port happened by changing a filename.

Use first person for documented actions: “I compared,” “I patched,” “I added support.” State machine behavior directly: “A remote read crosses QPI.” Use “we” only when identifying an actual collaborator. Do not invent thoughts, conversations, frustration, breakthroughs, costs, late nights, or exact time spent. James has supplied the months-long Qwen effort; that detail is available to use.

## Rules for the README

1. **Open on the project.** Give the machine and the intended assistant before explaining the field. Mention the model-switch reversal once near the start. Do not add a bold synopsis that repeats the first paragraph.
2. **Follow decisions.** Sections should explain a configuration, a code change, a failure, or a comparison. Introduce only the background needed to follow it. Do not force an identical problem/solution/lesson template onto every section.
3. **Name the thing.** Prefer “exp42's punctuation loop” to “some unexpected challenges,” and “256 KiB L2” to “limited CPU resources.” Delete sentences that only announce that an investigation continued.
4. **Make ownership legible.** Credit upstream before showing an upstream implementation. Distinguish configuring a feature, testing it, modifying it, and implementing model support. Do not describe Q4_0_R8 or the speculation framework as original inventions here.
5. **Keep the failed attempt.** Include a failure when its code or output explains a decision. Do not manufacture a smooth optimization ladder from runs that change several variables.
6. **Keep qualifications local.** A source, result, and its material limit belong near each other. Combine related limits into one compact note. Do not hedge known hardware facts or attach the same disclaimer to every paragraph.
7. **End on the result.** Finish the technical story with actual output and the model comparison. No generic lesson about perseverance, innovation, or optimization.
8. **Use roughly 1,000–1,400 words of rendered prose.** Length is a budget for this README, not a target to pad toward. Keep the code and evidence needed to understand the work. Put secondary derivations in notes.

## Sentences and rhythm

Use active verbs and concrete subjects. “I tested two placement policies” is preferable to “A comprehensive exploration of locality was undertaken.” Use ordinary contractions when natural. Put technical names in code formatting only when they are identifiers, flags, filenames, or literal values.

Most paragraphs should contain two to four sentences. A short standalone sentence can mark a real surprise; do not make the whole page a sequence of dramatic fragments. Mix sentence lengths according to the explanation. Read it aloud and remove any line that sounds like a product launch or a narrator introducing a documentary.

Use plain descriptive headings that help someone find a mechanism or result. One mildly playful heading is enough. Avoid headings that congratulate the project or promise a revelation. No emoji headings, badge walls, decorative rules, blockquote manifestos, or bold introductory slogans. Bold is reserved for a few quantities that matter to the explanation.

Do not use repeated “not X, but Y” constructions, rhetorical questions immediately answered by the writer, forced groups of three, or a tidy moral at the end of each section. A technical distinction can be stated directly without becoming a slogan.

## Humor

Use at most three brief wry observations in the README. Each must refer to a documented result or the hardware actually used. The facts must still make sense if the joke is removed.

Good material here: generating punctuation quickly; Flint doing better while emitting tokens slightly more slowly; keeping the same old Xeons. Avoid fictional dialogue, memes pasted into explanations, jokes in source comments, and calling a model stupid. Do not add a comic sentence simply because a section has none.

“I had made punctuation very fast” belongs after the saved repetition failure. It does not belong next to the valid 21-token/s coding run as though all Qwen output were junk.

## Numbers and evidence

- Every performance number needs a metric, unit, configuration or run identity, and a nearby source. A pass count needs its denominator.
- Keep decode tokens/s, elapsed time per task, and test outcomes separate. Do not call all three “speed.” State when mean elapsed time includes failures.
- Use `KiB` and `MiB` for binary cache/layout quantities; use installed memory units as recorded. Preserve byte arithmetic when it makes the mechanism concrete.
- Describe a capacity comparison as a capacity comparison. It does not measure a miss rate, prove a runtime bottleneck, or require a whole expert to fit in L2.
- Describe a multi-change run as a configuration result. Do not assign its entire gain to a shown line of C++.
- For this comparison, HumanEval+ success requires both base and extra tests: **106/164** for Qwen and **148/164** for Flint. Extra-only totals are a different aggregation.
- Link exact code and saved records. Pin historical evidence to the commit that produced it; link current setup notes relatively. Do not link a claim to a broad document whose unsupported headline contradicts it.

## Code

Use actual source excerpts. Keep original identifiers and expression spelling; indentation may be normalized. Preserve source comments if needed to understand the code, but add no narrator comments, praise, section banners, emoji, or metaphors. Explain the snippet in the adjacent prose.

Usually show two to eight lines that expose the operation. Identify the source before or immediately after the block. A diff must show the actual old and new expression. Do not create a toy implementation and imply it was benchmarked.

Reserve the README's code blocks for James's engine changes, the model port, and revealing output examples. Explain NUMA placement briefly through prose and the diagram; keep launch commands in configuration records. Credit upstream mechanisms in prose and link their source. An upstream snippet belongs in the main page only when the explanation needs the actual expression.

Call command excerpts shortened, identify placeholders, and link the real manifest when presenting settings. Use ordinary syntax fences such as `cpp`, `bash`, `diff`, and `python`. Do not add custom syntax themes or HTML containers to make code look more substantial. Do not refactor working code just to satisfy the prose.

For new implementation code, comments should explain a constraint, invariant, unit, or non-obvious reason. Prefer the repository's existing naming and formatting. No generated abstractions, novelty class names, or ceremonial logging solely for presentation. Do not make claims about who wrote code that cannot be established from the record.

## Animation and layout

Use four main clips: memory paths and their speed labels, James's guarded prefetch in the AVX2 kernel, James's n-gram history-update change followed by verification, and the Qwen-to-Flint attention-graph comparison tied to the native port. Keep the upstream eight-row repack as an optional expandable explanation. The standalone L2 capacity diagram is removed. The paragraph before each clip supplies the reason to watch it. Nearby code explains the operation, with matching variables and labels.

Captions should identify the operation and state an essential interpretation limit. They must not contain timing directions, praise for the animation, or “as you can see.” Real geometry and flags may be exact while motion speed and acceptance examples remain illustrative; say so where it affects interpretation.

Use the exported media assets and keep render directions in the animation notes. The prose must remain understandable with media absent or paused.

The four main clips and optional repack are exported as ordinary GIF embeds, with PNG posters and MP4 masters alongside them. Preserve the short interpretation captions when replacing an export. Keep the browser preview's pause controls out of the Markdown itself. Memory labels must distinguish configured DIMM rates, Intel architectural references, and theoretical bus/packet ceilings; none should be presented as measured Talos read throughput.

Use ordinary GitHub Markdown. Tables are for comparisons, lists for genuinely parallel links or instructions. No decorative HTML, hand-styled callouts, or web-page components in the README.

## Editing examples

| Earlier wording | Revised wording | Reason |
| --- | --- | --- |
| “That gave the investigation a concrete direction.” | Delete it and start the next experiment. | The sentence reports no action or result. |
| “That model switch produced the funniest result.” | “Flint emitted tokens slightly more slowly and still finished tasks sooner.” | The measured mismatch supplies the humor. |
| “Smaller weight representations and better layouts address different costs.” | “Q4_0_R8 prepares eight rows for the vector kernel.” | Start with the implementation the reader is about to see. |
| “Some configurations produced repetitive output.” | “Experiment 42 includes a roughly 66-token/s result whose output falls into repeated punctuation.” | A named failure is inspectable. |
| “The engine work carried forward into that switch.” | Name the repacked kernels, merged up/gate path, and reused experiment tooling. | Give the reader the connection instead of asserting one. |

The examples are editing operations, not lines to repeat elsewhere.

## Terms to remove during review

Cut promotional adjectives such as “groundbreaking,” “robust,” “seamless,” “blazing-fast,” “production-grade,” and “industry-grade” unless a specific definition and evidence make the word necessary. Replace “leverage,” “delve,” “unlock,” “journey,” “testament,” “game-changer,” and “key takeaway” with the actual action or delete the phrase.

Also inspect ordinary-looking filler: “This highlighted the importance of,” “It became clear that,” “The investigation moved,” “What followed was,” “The real lesson,” and “Ultimately.” Removing a blacklist alone will not fix vague writing. Every surviving sentence still needs a job.

## Release check

- Can a new reader name the machine, purpose, contribution, and result after the opening?
- Does each explanation connect to a recorded choice, code path, output, or measurement?
- Does every first-person claim have support in the repo or James's account?
- Do the code excerpts match their sources, and do links reach the cited files?
- Are upstream credit, metric definitions, comparison limits, and animation limits present where needed?
- Are there at most three factual jokes, with no decorative prose in code?
- Does the story work without playing an animation?
- Have production notes, repeated premises, inflated adjectives, and closing morals been removed?
