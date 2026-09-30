# Quality & Performance Verification Report: Exp2: Native MTP (n_max=1)

- **Timestamp:** `2026-09-02 16:55:11`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Command:** `numactl --cpunodebind=0 --membind=0 /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8082 -c 8192 -t 10 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa isolate -fa 1 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1`
- **Summary Score:** **6 / 6 Tests Passed** (ALL PASSED - PERFECT FIDELITY)
- **Average Token Generation Speed:** **`14.58 t/s`**
- **Average Prompt Processing Speed:** **`75.49 t/s`**

## Test Breakdown

| Test ID | Category | Status | Generation Speed | Prompt Speed |
| :--- | :--- | :---: | :---: | :---: |
| `code_toposort` | Coding & Algorithmic Correctness | PASSED | `14.41 t/s` | `75.90 t/s` |
| `code_lru` | Concurrency & System Design | PASSED | `13.97 t/s` | `64.31 t/s` |
| `math_multistep` | Mathematical Reasoning | PASSED | `14.93 t/s` | `78.75 t/s` |
| `knowledge_facts` | Factual Knowledge & Anti-Hallucination | PASSED | `14.90 t/s` | `80.36 t/s` |
| `logic_puzzle` | Logic & Constraint Satisfaction | PASSED | `14.71 t/s` | `78.14 t/s` |
| `long_context_passkey` | Long Context Retrieval (Needle-In-A-Haystack) | PASSED | `117.25 t/s` | `117.25 t/s` |

## Detailed Outputs

### Coding & Algorithmic Correctness (`code_toposort`)
**Prompt:** *Write a clean C++ function `topologicalSort` that performs topological sorting on a directed graph represented as `std::vector<std::vector<int>>& adj`. If a cycle is detected, return an empty vector. Only return valid C++ code with minimal comments.*

**Result:** PASSED

```text
<think>
Here's a thinking process:

1.  **Understand the Goal**: The user wants a C++ function `topologicalSort` that takes a directed graph represented as an adjacency list (`std::vector<std::vector<int>>& adj`) and returns a topological ordering as a `std::vector<int>`. If the graph contains a cycle, it should return an empty vector. The code should be clean, minimal comments, and valid C++.

2.  **Key Requirements**:
   - Input: `std::vector<std::vector<int>>& adj`
   - Output: `std::vector<int>` (topological order or empty vector on cycle)
   - Algorithm: Topological sort (Kahn's algorithm or DFS-based). Kahn's algorithm (BFS with in-degrees) is often simpler to implement iteratively and naturally detects cycles (if the result doesn't contain all nodes, there's a cycle). DFS-based is also fine but requires recursion stack tracking. I'll go with Kahn's algorithm for its iterative nature and straightforward cycle detection.
   - Constraints/Assumptions: Nodes are typically 0-indexed or 1-indexed. I'll assume 0 to n-1 where n = adj.size(). If the graph nodes are not contiguous from 0 to n-1, the problem usually specifies, but standard competitive programming assumes 0 to n-1. I'll stick with 0 to n-1.
   - Return: `std::vector<int>`

3.  **Algorithm Selection (Kahn's Algorithm)**:
   - Calculate in-degrees for all nodes.
   - Push all nodes with in-degree 0 into a queue.
   - While queue is not empty:
     - Pop front, add to result.
     - For each neighbor, decrement in-degree. If in-degree becomes 0, push to queue.
   - After processing, if result size equals number of nodes, return result. Otherwise, return empty vector (cycle detected).

4.  **Edge Cases**:
   - Empty graph: `adj.size() == 0` -> return empty vector or `{}`.
   - Disconnected components: Handled correctly by Kahn's.
   - Self-loops: Handled (in-degree won't drop to 0 for that node until cycle is resolved, but self-loop means in-degree never drops, so cycle detected correctly).
   - Multiple valid orders: Any valid
```

### Concurrency & System Design (`code_lru`)
**Prompt:** *Implement a thread-safe LRU cache class `ThreadSafeLRUCache` in C++ with `get(int key)` and `put(int key, int value)`. Use `std::mutex`. Provide the implementation.*

**Result:** PASSED

```text
<think>
Here's a thinking process:

1.  **Understand User Request:**
   - **Goal:** Implement a thread-safe LRU (Least Recently Used) cache in C++.
   - **Class Name:** `ThreadSafeLRUCache`
   - **Methods:** `get(int key)` and `put(int key, int value)`
   - **Concurrency:** Must be thread-safe using `std::mutex`
   - **Language:** C++

2.  **Identify Core Requirements:**
   - LRU Cache needs O(1) `get` and `put` operations.
   - Standard approach: Hash map + Doubly linked list.
   - Thread-safety: Protect shared state with a mutex (RAII style with `std::lock_guard` or `std::unique_lock`).
   - C++11 or later is assumed (standard for modern C++).

3.  **Design the Data Structures:**
   - **Hash Map:** `std::unordered_map<int, std::shared_ptr<Node>>` or `std::unordered_map<int, std::list<std::pair<int, int>>::iterator>` (C++14/17) or just store iterators to a doubly linked list. Actually, `std::list` doesn't give O(1) erase/insert with iterators in all cases, but we can use `std::list<std::pair<int, int>>` and store iterators. Wait, `std::list` iterators are stable, so storing `std::list<std::pair<int, int>>::iterator` in the hash map works.
   - Alternatively, use `std::forward_list`? No, doubly linked list is better for LRU (need to move to front on access/update).
   - Let's use `std::list<std::pair<int, int>>` (key-value pairs) and `std::unordered_map<int, std::list<std::pair<int, int>>::iterator>`.
   - Actually, `std::list` doesn't provide `erase` by value in O(1), but we have the iterator from the map, so `list.erase(it)` is O(1).
   - Wait, `std::list::erase` takes an iterator and returns the next iterator. That's fine.
   - Let's stick to `std::list<std::pair<int, int>>` and `std::unordered_map<int, std::list<std::
```

### Mathematical Reasoning (`math_multistep`)
**Prompt:** *Solve this carefully step by step:
A factory produces 1,500 widgets per day. 12% are rejected during quality inspection. The remaining widgets are packed into boxes of 22 widgets each. Any remaining widgets that cannot fill a full box are recycled. How many full boxes are packed, and how many widgets are recycled?*

**Result:** PASSED

```text
<think>
Here's a thinking process:

1.  **Understand the Goal:** The user wants to solve a word problem step-by-step. The problem involves calculating the number of full boxes packed and the number of recycled widgets based on daily production, a rejection rate, and box capacity.

2.  **Identify Given Information:**
   - Daily production: 1,500 widgets
   - Rejection rate: 12%
   - Box capacity: 22 widgets per box
   - Recycling rule: Remaining widgets that don't fill a full box are recycled.

3.  **Step 1: Calculate the number of rejected widgets.**
   - Rejected = 12% of 1,500
   - Calculation: $0.12 \times 1500 = 180$
   - Check: $10\% = 150$, $2\% = 30$, so $150+30=180$. Correct.

4.  **Step 2: Calculate the number of accepted widgets (to be packed).**
   - Accepted = Total - Rejected
   - Calculation: $1500 - 180 = 1320$
   - Check: $1500 \times 0.88 = 1320$. Correct.

5.  **Step 3: Calculate the number of full boxes.**
   - Each box holds 22 widgets.
   - Full boxes = $\lfloor 1320 / 22 \rfloor$
   - Calculation: $1320 \div 22$
   - Let's do the division: $22 \times 60 = 1320$. Exactly 60.
   - So, 60 full boxes.

6.  **Step 4: Calculate the number of recycled widgets.**
   - Recycled = Accepted - (Full boxes $\times$ Box capacity)
   - Calculation: $1320 - (60 \times 22) = 1320 - 1320 = 0$
   - Wait, is it exactly 0? Let me double-check the division.
   - $22 \times 60 = 1320$. Yes, exactly.
```

### Factual Knowledge & Anti-Hallucination (`knowledge_facts`)
**Prompt:** *Answer the following three questions strictly and concisely:
1. What is the chemical symbol and atomic number of Tungsten?
2. In which year did the Apollo 11 mission land humans on the Moon?
3. What is the speed of light in a vacuum in meters per second (exact integer)?*

**Result:** PASSED

```text
<think>
Here's a thinking process:

1.  **Analyze User Input:**
   - **Question 1:** Chemical symbol and atomic number of Tungsten?
   - **Question 2:** Year of Apollo 11 Moon landing?
   - **Question 3:** Speed of light in a vacuum in m/s (exact integer)?
   - **Constraints:** Strictly and concisely answer all three.

2.  **Verify Facts:**
   - *Tungsten:* Symbol = W, Atomic Number = 74. (Correct)
   - *Apollo 11:* Landed on the Moon on July 20, 1969. (Correct)
   - *Speed of light in vacuum:* Exactly 299,792,458 m/s. (Correct, by definition of the meter)

3.  **Format Output:**
   - Keep it strict and concise as requested.
   - Number the answers to match the questions.
   - Ensure exact phrasing matches the prompt's request.

   Draft:
   1. Symbol: W, Atomic Number: 74
   2. 1969
   3. 299,792,458 m/s

4.  **Check Constraints:**
   - Strictly and concisely? Yes.
   - All three answered? Yes.
   - Factual accuracy? Yes.
   - Exact integer for speed of light? Yes, 299792458 (I'll omit commas for strict integer format, or keep them for readability; the prompt says "exact integer", I'll provide just the number or with commas, both are fine. I'll stick to the exact number: 299792458).

   Refined:
   1. Symbol: W, Atomic Number: 74
   2. 1969
   3. 299792458 m/s

   All good. Output matches refined version.✅
   Note: I'll make sure the formatting exactly matches the request style. I'll list them 1-3. No extra fluff.✅
   Proceed. 
   Output Generation. 
   Self-Correction/Verification during thought: 
   - Speed of light exact integer: 299
```

### Logic & Constraint Satisfaction (`logic_puzzle`)
**Prompt:** *Solve this logic problem:
Alice, Bob, and Charlie each have a different fruit: an apple, an orange, and a banana. Alice does not have the banana. Bob does not have the apple. Charlie has the orange. Who has which fruit? State the final assignment clearly.*

**Result:** PASSED

```text
<think>
Here's a thinking process:

1.  **Analyze User Input:**
   - **People:** Alice, Bob, Charlie
   - **Fruits:** Apple, Orange, Banana
   - **Constraints:**
     - Each person has a different fruit.
     - Alice ≠ Banana
     - Bob ≠ Apple
     - Charlie = Orange
   - **Goal:** Determine who has which fruit. State final assignment clearly.

2.  **Deconstruct Constraints & Deduce:**
   - From "Charlie has the orange": Charlie = Orange.
   - Since each person has a different fruit, the remaining fruits are Apple and Banana.
   - Remaining people: Alice and Bob.
   - Constraint: Alice ≠ Banana. Since the only remaining fruits are Apple and Banana, and she can't have Banana, she must have the Apple. So, Alice = Apple.
   - That leaves Bob with the only remaining fruit: Banana. So, Bob = Banana.
   - Check against constraints:
     - Alice ≠ Banana? Yes, she has Apple.
     - Bob ≠ Apple? Yes, he has Banana.
     - Charlie = Orange? Yes.
     - All different? Yes (Alice: Apple, Bob: Banana, Charlie: Orange).
   - All constraints satisfied.

3.  **Formulate Output:**
   - State the logical steps clearly but concisely.
   - Provide the final assignment as requested.
   - Format: 
     - Alice: Apple
     - Bob: Banana
     - Charlie: Orange
   - Add a brief explanation if helpful, but keep it direct.

   Draft:
   Based on the clues:
   - Charlie has the orange.
   - That leaves the apple and banana for Alice and Bob.
   - Since Alice does not have the banana, she must have the apple.
   - This leaves Bob with the banana.
   
   Final assignment:
   - **Alice:** Apple
   - **Bob:** Banana
   - **Charlie:** Orange

4.  **Self-Correction/Verification:**
   - Check logic: Charlie=Orange (given). Remaining: Apple, Banana. Alice≠Banana → Alice=Apple. Bob gets remaining → Bob=Banana. Bob≠Apple? Yes, he has Banana. All good.
   - Matches constraints exactly.
   - Output matches request. Ready.✅
```

### Long Context Retrieval (Needle-In-A-Haystack) (`long_context_passkey`)
**Prompt:** *llama-passkey 4096 tokens insertion/retrieval*

**Result:** PASSED

```text
: 10.30 t/s

llama_print_timings:        load time =   69528.20 ms
llama_print_timings:      sample time =       5.54 ms /    17 runs   (    0.33 ms per token,  3070.81 tokens per second)
llama_print_timings: prompt eval time =   51727.64 ms /  6065 tokens (    8.53 ms per token,   117.25 tokens per second)
llama_print_timings:        eval time =    1527.66 ms /    16 runs   (   95.48 ms per token,    10.47 tokens per second)
llama_print_timings:       total time =   71081.77 ms /  6081 tokens


```

