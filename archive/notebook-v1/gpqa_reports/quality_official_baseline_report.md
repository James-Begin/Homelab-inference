# Quality & Performance Verification Report: Official Baseline

- **Timestamp:** `2026-09-02 16:45:14`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Command:** `numactl --cpunodebind=0 --membind=0 /home/james/ik_llama.cpp/build/bin/llama-server -m /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf --port 8082 -c 8192 -t 10 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa isolate -fa 1 `
- **Summary Score:** **6 / 6 Tests Passed** (ALL PASSED - PERFECT FIDELITY)
- **Average Token Generation Speed:** **`11.32 t/s`**
- **Average Prompt Processing Speed:** **`91.18 t/s`**

## Test Breakdown

| Test ID | Category | Status | Generation Speed | Prompt Speed |
| :--- | :--- | :---: | :---: | :---: |
| `code_toposort` | Coding & Algorithmic Correctness | PASSED | `11.38 t/s` | `93.99 t/s` |
| `code_lru` | Concurrency & System Design | PASSED | `11.38 t/s` | `84.12 t/s` |
| `math_multistep` | Mathematical Reasoning | PASSED | `11.06 t/s` | `89.77 t/s` |
| `knowledge_facts` | Factual Knowledge & Anti-Hallucination | PASSED | `11.30 t/s` | `94.39 t/s` |
| `logic_puzzle` | Logic & Constraint Satisfaction | PASSED | `11.47 t/s` | `93.62 t/s` |
| `long_context_passkey` | Long Context Retrieval (Needle-In-A-Haystack) | PASSED | `135.54 t/s` | `135.54 t/s` |

## Detailed Outputs

### Coding & Algorithmic Correctness (`code_toposort`)
**Prompt:** *Write a clean C++ function `topologicalSort` that performs topological sorting on a directed graph represented as `std::vector<std::vector<int>>& adj`. If a cycle is detected, return an empty vector. Only return valid C++ code with minimal comments.*

**Result:** PASSED

```text
<think>

</think>

```cpp
#include <vector>
#include <stack>
#include <algorithm>

std::vector<int> topologicalSort(std::vector<std::vector<int>>& adj) {
    int n = adj.size();
    std::vector<int> inDegree(n, 0);
    for (int i = 0; i < n; ++i) {
        for (int neighbor : adj[i]) {
            inDegree[neighbor]++;
        }
    }

    std::vector<int> queue;
    for (int i = 0; i < n; ++i) {
        if (inDegree[i] == 0) {
            queue.push_back(i);
        }
    }

    std::vector<int> result;
    int head = 0;
    while (head < queue.size()) {
        int node = queue[head++];
        result.push_back(node);
        for (int neighbor : adj[node]) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] == 0) {
                queue.push_back(neighbor);
            }
        }
    }

    if (result.size() != n) {
        return {};
    }

    return result;
}
```
```

### Concurrency & System Design (`code_lru`)
**Prompt:** *Implement a thread-safe LRU cache class `ThreadSafeLRUCache` in C++ with `get(int key)` and `put(int key, int value)`. Use `std::mutex`. Provide the implementation.*

**Result:** PASSED

```text
<think>
Here's a thinking process:

1.  **Understand User Request:**
   - **Class Name:** `ThreadSafeLRUCache`
   - **Language:** C++
   - **Methods:** `get(int key)`, `put(int key, int value)`
   - **Concurrency:** Thread-safe using `std::mutex`
   - **Data Structure:** LRU (Least Recently Used) Cache
   - **Output:** Complete implementation

2.  **Identify Core Requirements:**
   - LRU Cache typically requires O(1) `get` and `put` operations.
   - Standard approach: Hash map + Doubly linked list.
   - Thread safety: Protect shared state with a mutex (or read-write lock, but `std::mutex` is explicitly requested).
   - Need to handle cache capacity, eviction of least recently used item when full.
   - Standard C++11 or later is assumed (given `std::mutex`, `std::unordered_map`, etc.).

3.  **Design the Data Structures:**
   - **Doubly Linked List Node:** Stores `key`, `value`, `prev`, `next`.
   - **Hash Map:** `std::unordered_map<int, std::shared_ptr<Node>>` or raw pointers. `std::shared_ptr` is safer for ownership, but raw pointers or `std::unique_ptr` with custom deleters are also fine. I'll use `std::shared_ptr` for simplicity and safety, or just raw pointers with a custom node manager. Actually, raw pointers with explicit `new`/`delete` or `std::unique_ptr` in a container is fine. Let's stick to raw pointers for the list nodes but manage them carefully, or use `std::shared_ptr` for simplicity. Given it's a cache, performance matters, so I'll use a custom node class with raw pointers but ensure proper cleanup, or just use `std::unique_ptr` with a custom deleter. Actually, raw pointers are standard for this pattern. I'll use `std::shared_ptr` for simplicity and safety, or just raw pointers with a `std::list`? No, `std::list` doesn't give O(1) erase by iterator in all cases without C++11's `splice` or similar. Better to implement a simple doubly linked list with a dummy head/tail for O(1) operations.
   - Let
```

### Mathematical Reasoning (`math_multistep`)
**Prompt:** *Solve this carefully step by step:
A factory produces 1,500 widgets per day. 12% are rejected during quality inspection. The remaining widgets are packed into boxes of 22 widgets each. Any remaining widgets that cannot fill a full box are recycled. How many full boxes are packed, and how many widgets are recycled?*

**Result:** PASSED

```text
<think>

</think>

Here is the step-by-step solution to the problem.

### Step 1: Calculate the number of rejected widgets
First, we determine how many widgets are rejected during quality inspection. The factory produces 1,500 widgets per day, and 12% are rejected.

$$ \text{Rejected Widgets} = 1,500 \times 0.12 $$

Calculation:
$$ 1,500 \times 0.10 = 150 $$
$$ 1,500 \times 0.02 = 30 $$
$$ 150 + 30 = 180 $$

So, **180** widgets are rejected.

### Step 2: Calculate the number of widgets remaining for packing
Next, we subtract the rejected widgets from the total production to find out how many widgets are available to be packed.

$$ \text{Remaining Widgets} = \text{Total Production} - \text{Rejected Widgets} $$
$$ \text{Remaining Widgets} = 1,500 - 180 $$
$$ \text{Remaining Widgets} = 1,320 $$

There are **1,320** widgets available for packing.

### Step 3: Calculate the number of full boxes
The remaining widgets are packed into boxes of 22 widgets each. To find the number of full boxes, we divide the total remaining widgets by the box capacity.

$$ \text{Number of Boxes} = 1,320 / 22 $$

Let's perform the division:
1. $132 / 22 = 6$ (since $22 \times 6 = 132$)
2. Bring down the 0: $0 / 22 = 0$

So,
$$ 1,320 / 22 = 60 $$

There are exactly **60** full boxes.

### Step 4: Calculate the number of recycled widgets
The problem states that any remaining widgets that cannot fill a full box are recycled. We must check if there is a remainder from the division in Step 3.

$$ 60 \text{ boxes} \times 22 \text{ widgets/box} = 1,320 \text{ widgets used} $$

Now, calculate the
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
   - *Speed of light in vacuum:* Exactly 299,792,458 m/s. (Correct, by definition)

3.  **Format Output:**
   - Keep it strict and concise as requested.
   - Structure clearly for each question.

   Draft:
   1. Symbol: W, Atomic Number: 74
   2. 1969
   3. 299,792,458 m/s

4.  **Check Constraints:**
   - Strictly and concisely? Yes.
   - Answers all three? Yes.
   - Factual accuracy? Verified.
   - Exact integer for speed of light? Yes, 299792458 (I'll format it with or without commas, but the prompt says "exact integer", so I'll provide just the number or with standard formatting).

   I will present it clearly numbered to match the prompt.

   Final check of the prompt: "strictly and concisely"
   I'll keep it to one line per answer or a simple list.

   Refined:
   1. Symbol: W, Atomic Number: 74
   2. 1969
   3. 299,792,458 m/s

   All good. Output matches.✅
   Note: I'll make sure the formatting exactly matches the request style if needed, but a simple numbered list is fine. I'll stick to the refined version.✅
   Proceed. 
   Output Generation. 
   Self-Correction/Verification during thought: 
   - Speed of light is exactly
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
   - Remaining people: Alice, Bob
   - Remaining fruits: Apple, Banana
   - From "Alice does not have the banana": Since the only remaining fruits are Apple and Banana, and Alice ≠ Banana, then Alice must have the Apple. So, Alice = Apple.
   - From "Bob does not have the apple": This is consistent with our current assignment (Alice has Apple, Charlie has Orange), so Bob must have the remaining fruit: Banana. So, Bob = Banana.
   - Check constraints:
     - Alice ≠ Banana? Yes, she has Apple.
     - Bob ≠ Apple? Yes, he has Banana.
     - Charlie = Orange? Yes.
     - All different? Yes (Apple, Banana, Orange).
   - All constraints satisfied.

3.  **Formulate Output:**
   - State the logical steps clearly but concisely.
   - Provide the final assignment clearly as requested.
   - Structure: Step-by-step deduction followed by a clear final answer.

   Draft:
   Let's solve this step-by-step:
   1. We know Charlie has the orange.
   2. This leaves the apple and the banana for Alice and Bob.
   3. We're told Alice does not have the banana, so Alice must have the apple.
   4. That leaves the banana for Bob.
   5. (Checking the constraint "Bob does not have the apple" confirms this, as he has the banana.)
   
   Final Assignment:
   - Alice: Apple
   - Bob: Banana
   - Charlie: Orange

4.  **Self-Correction/Verification:**
   - Does it match all conditions? Yes.
   - Is it clear? Yes.
   - Any logical fallacies? No.
   - The constraint "Bob does not have the apple
```

### Long Context Retrieval (Needle-In-A-Haystack) (`long_context_passkey`)
**Prompt:** *llama-passkey 4096 tokens insertion/retrieval*

**Result:** PASSED

```text
: 10.40 t/s

llama_print_timings:        load time =   62236.28 ms
llama_print_timings:      sample time =       5.53 ms /    17 runs   (    0.33 ms per token,  3073.03 tokens per second)
llama_print_timings: prompt eval time =   44745.48 ms /  6065 tokens (    7.38 ms per token,   135.54 tokens per second)
llama_print_timings:        eval time =    1511.09 ms /    16 runs   (   94.44 ms per token,    10.59 tokens per second)
llama_print_timings:       total time =   63773.92 ms /  6081 tokens


```

