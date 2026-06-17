---

# 📐 COMPLEXITY ANALYSIS — THE COMPLETE FRAMEWORK
### Asymptotic Analysis · Big-O · Theta · Omega · Time · Space

---

## SECTION 1: PREREQUISITES

**From our last session — quick revision:**

> We learned that **Order of Growth** keeps only the dominant term and drops constants. `T(n) = 3n² + 7n + 42` becomes `n²` because at large n, only the dominant term matters.
>
> Today we formalize *exactly* what "at large n" means — and build the mathematical notation system that the entire DSA world uses.

**Math required:**
- Functions: f(n), g(n) — output depends on input n
- Inequalities: f(n) ≤ c · g(n)
- Limits (informal): "what happens as n → ∞"
- Absolute value: |f(n)|

**Programming required:**
- Understanding loops, recursion, memory allocation
- Stack frames, heap memory (briefly — we'll build this today)

---

## SECTION 2: THEORY — THE BIG PICTURE FIRST

Before diving into notation, understand **why** this entire framework exists.

### The Core Problem

You write two sorting algorithms. You benchmark them:

```
Algorithm A: takes 2.3 seconds on your laptop
Algorithm B: takes 1.1 seconds on your friend's PC
```

**Which is faster?** You cannot answer. Different machines, different CPUs, different memory speeds.

We need a **machine-independent** language to compare algorithms. That language is **Asymptotic Analysis**.

### The Core Idea

Instead of measuring seconds, we measure:

> "How does the number of operations grow as input size n grows toward infinity?"

We don't care about n = 5 or n = 10. We care about n = 10⁵, 10⁶, 10⁹. At that scale, the algorithm's mathematical shape reveals its true nature.

**Asymptotic** = relating to a value or curve that is approached but never reached as n → ∞.

---

## SECTION 3: REAL-WORLD INTUITION

### Part A — Real-Life Analogy

Think of three reviewers describing a restaurant's wait time:

- **The Pessimist (Big O):** "You'll wait *at most* 45 minutes." → Upper bound. Worst that can happen.
- **The Optimist (Omega Ω):** "You'll wait *at least* 5 minutes." → Lower bound. Best that can happen.
- **The Realist (Theta Θ):** "You'll wait *around* 20–25 minutes." → Tight bound. This is what usually happens.

All three describe the same restaurant. All three are *true*. But they tell you different things.

In algorithms:
- **Big O** = the promise "it won't get worse than this"
- **Omega** = the guarantee "it won't get better than this"
- **Theta** = the complete characterization "it grows exactly like this"

---

### Part B — Mental Model

```
Actual runtime T(n):         ≈ 3n² + 2n + 10
                              (messy, real)

                  c₂·n²  ─────────────────────────── ← Big O bound (upper)
                              /
                T(n)     ────                        ← Actual curve
                              \
                  c₁·n²  ─────────────────────────── ← Omega bound (lower)

All three curves grow at the same "speed" (n²)
→ T(n) = Θ(n²), O(n²), Ω(n²) simultaneously
```

```
Timeline view for ONE function T(n) = 3n² + 2n + 10:

n =    1  →   15    (10 is dominant at tiny n)
n =   10  →  320    (3n² starts winning)
n =  100  →  30210  (3n² completely dominates)
n = 1000  →  3,002,010  (lower terms are 0.07% of total)

Observation: After some threshold n₀, only the n² shape matters
```

---

### Part C — Guided Discovery

> Here's something to think about before we define anything formally:
>
> If `T(n) = 100n` and `g(n) = n²`, is T(n) ≤ g(n) for all large n?
>
> At n = 50:  T(50) = 5000,  g(50) = 2500  → T(n) > g(n). Hmm.
> At n = 100: T(100) = 10000, g(100) = 10000 → Equal.
> At n = 200: T(200) = 20000, g(200) = 40000 → T(n) < g(n). ✓
>
> **So from n = 100 onward, T(n) ≤ g(n).**
>
> This is the exact mechanism behind Big O. We find a threshold n₀ beyond which the relationship always holds. The behavior before n₀ doesn't matter.
>
> THIS is the "aha moment" of asymptotic analysis. We don't need the bound to hold everywhere — just eventually, for all large enough n.

---

## SECTION 4: PATTERN RECOGNITION

When does asymptotic analysis get tested?

```
If you see:
  — "Is this O(n) or O(n²)?"
  — "Prove that f(n) = O(g(n))"
  — "What's the tight bound of this algorithm?"
  — "Can this pass within the time limit for n = 10⁶?"
Then think → Apply the asymptotic framework
```

**The three questions to ask about any algorithm:**

```
1. What's the WORST it can do?    → Big O    (use for upper bound guarantees)
2. What's the BEST it can do?     → Omega    (use for lower bound / best case)
3. Is the bound TIGHT?            → Theta    (use when both bounds match)
```

**Pattern Recognition Checklist:**
- ☐ Does the problem ask "at most how slow?"  → Big O
- ☐ Does it ask "is this the theoretical minimum?"  → Omega
- ☐ Does the algorithm always behave the same regardless of input structure?  → Theta likely applies
- ☐ Does the algorithm behave differently on sorted vs unsorted?  → Big O and Omega will differ
- ☐ Do constraints say n ≤ 10⁵?  → You need O(n log n) or better
- ☐ Is someone claiming O(1) space for a recursive solution?  → Red flag — check the call stack

---

## SECTION 5: ASYMPTOTIC ANALYSIS — FORMAL FOUNDATION

### What "Asymptotic" Means Precisely

```
We study the behavior of T(n) as n → ∞

We IGNORE:
  ✗ Small values of n (they don't matter at scale)
  ✗ Constant multipliers (machine-dependent)
  ✗ Lower-order terms (dominated at large n)

We KEEP:
  ✓ The growth rate — the mathematical shape
  ✓ The dominant term
  ✓ The relationship between input size and operation count
```

### The Three Asymptotic Notations

```
┌─────────┬──────────────┬─────────────────┬──────────────────────┐
│Notation │ Bound Type   │ Math Meaning    │ Intuition            │
├─────────┼──────────────┼─────────────────┼──────────────────────┤
│ O(g(n)) │ Upper bound  │ T(n) ≤ c·g(n)  │ "at most this bad"   │
│ Ω(g(n)) │ Lower bound  │ T(n) ≥ c·g(n)  │ "at least this good" │
│ Θ(g(n)) │ Tight bound  │ both above hold │ "exactly this"       │
└─────────┴──────────────┴─────────────────┴──────────────────────┘
```

---

## SECTION 6: BIG-O NOTATION — UPPER BOUND

### Formal Definition

```
T(n) = O(g(n))

if and only if there exist positive constants c and n₀ such that:

    T(n) ≤ c · g(n)    for all n ≥ n₀
```

Read as: "T(n) is Big-O of g(n)"

In plain English: **After some point n₀, the function T(n) never exceeds c times g(n).**

### Visualized

```
Operations
^
|          c·g(n) ──────────────────────────────────
|                /          ↑ Big O upper bound
|          T(n) ────────────│──────────────────────
|              /            │ T(n) stays below c·g(n)
|             /             │ for all n ≥ n₀
|____________/______________|_________________________> n
                           n₀
```

### Worked Proof: T(n) = 4n + 3 is O(n)

**We must find c and n₀ such that: 4n + 3 ≤ c · n for all n ≥ n₀**

```
Step 1: Try c = 5
  Need: 4n + 3 ≤ 5n
  →     3 ≤ n
  →     This holds for all n ≥ 3

✓ Proof complete:
  c = 5, n₀ = 3
  For all n ≥ 3: 4n + 3 ≤ 5n
  Therefore T(n) = O(n)
```

**Verification at key values:**

```
n = 3:  4(3)+3 = 15,  5(3) = 15  ✓ (equal at boundary)
n = 5:  4(5)+3 = 23,  5(5) = 25  ✓
n = 100: 403 ≤ 500               ✓
```

### Worked Proof: T(n) = 3n² + 5n + 7 is O(n²)

```
Need: 3n² + 5n + 7 ≤ c · n² for all n ≥ n₀

Observation: for n ≥ 1:
  5n ≤ 5n²   (since n ≤ n²)
  7  ≤ 7n²   (since 1 ≤ n²)

So: 3n² + 5n + 7 ≤ 3n² + 5n² + 7n²
                  = 15n²

Choose c = 15, n₀ = 1
For all n ≥ 1: 3n² + 5n + 7 ≤ 15n²
Therefore: T(n) = O(n²)   ✓

Note: We could tighten this. But O just needs ANY valid c and n₀.
```

### Critical Property: Big O is NOT Unique

```
If T(n) = n, then ALL of these are true:
  T(n) = O(n)        ← tight and correct
  T(n) = O(n²)       ← true but loose
  T(n) = O(n³)       ← true but very loose
  T(n) = O(2ⁿ)       ← true but absurd

Convention: ALWAYS give the tightest Big O you can.
```

### Python Code Example — Deriving O(n²)

```python
def find_all_pairs(arr: list[int]) -> list[tuple]:
    """
    Returns all pairs (i, j) where i != j.
    
    Why O(n²)?
    Outer loop: n iterations
    Inner loop: n iterations for EACH outer iteration
    Total operations: n × n = n²
    """
    pairs = []
    
    for i in range(len(arr)):           # Runs n times
        for j in range(len(arr)):       # Runs n times FOR EACH i
            if i != j:
                pairs.append((arr[i], arr[j]))
    
    return pairs

# Dry run for arr = [1, 2, 3] (n = 3):
# i=0: j=0(skip), j=1→(1,2), j=2→(1,3)     [2 operations]
# i=1: j=0→(2,1), j=1(skip), j=2→(2,3)     [2 operations]
# i=2: j=0→(3,1), j=1→(3,2), j=2(skip)     [2 operations]
# Total: 6 operations = n(n-1) ≈ O(n²)      ✓
```

---

## SECTION 7: BIG-THETA NOTATION — TIGHT BOUND

### Formal Definition

```
T(n) = Θ(g(n))

if and only if there exist positive constants c₁, c₂, and n₀ such that:

    c₁ · g(n) ≤ T(n) ≤ c₂ · g(n)    for all n ≥ n₀
```

Read as: "T(n) is Theta of g(n)"

In plain English: **T(n) is sandwiched between two multiples of g(n). It grows exactly like g(n).**

### Visualized

```
Operations
^
|     c₂·g(n) ─────────────────────────────── ← upper fence
|                  ↑
|       T(n)  ───────────────────────────────  ← actual (trapped between)
|                  ↓
|     c₁·g(n) ─────────────────────────────── ← lower fence
|
|______________|______________________________> n
              n₀
```

### Key Insight: Θ = O AND Ω simultaneously

```
T(n) = Θ(g(n))
⟺ T(n) = O(g(n))   [upper bound holds]
  AND
  T(n) = Ω(g(n))   [lower bound holds]
```

### Worked Proof: T(n) = 2n² + 3n is Θ(n²)

```
Need to show: c₁·n² ≤ 2n² + 3n ≤ c₂·n² for all n ≥ n₀

UPPER BOUND (finding c₂):
  2n² + 3n ≤ 2n² + 3n²     [since n ≤ n² for n ≥ 1]
           = 5n²
  → c₂ = 5, works for n ≥ 1

LOWER BOUND (finding c₁):
  2n² + 3n ≥ 2n²            [since 3n is positive]
  → c₁ = 2, works for all n ≥ 0

CONCLUSION:
  c₁ = 2, c₂ = 5, n₀ = 1
  2n² ≤ 2n² + 3n ≤ 5n²    for all n ≥ 1
  Therefore: T(n) = Θ(n²)  ✓
```

**Dry run verification:**

```
n = 1:   c₁·1 = 2,    T(1) = 5,     c₂·1 = 5    ✓  (2 ≤ 5 ≤ 5)
n = 5:   c₁·25 = 50,  T(5) = 65,    c₂·25 = 125  ✓  (50 ≤ 65 ≤ 125)
n = 100: c₁·10000 = 20000, T(100) = 20300, c₂·10000 = 50000 ✓
```

### When Does Θ Exist?

Θ exists when best case = worst case in growth rate.

```
Linear Search:
  Best case:  Ω(1)   (found at position 0)
  Worst case: O(n)   (found at last position)
  → NO Theta — because O and Ω don't match

Merge Sort:
  Best case:  Ω(n log n)  (always divides and merges)
  Worst case: O(n log n)  (always divides and merges)
  → Θ(n log n) — because O and Ω match ✓
```

---

## SECTION 8: BIG-OMEGA NOTATION — LOWER BOUND

### Formal Definition

```
T(n) = Ω(g(n))

if and only if there exist positive constants c and n₀ such that:

    T(n) ≥ c · g(n)    for all n ≥ n₀
```

Read as: "T(n) is Omega of g(n)"

In plain English: **T(n) grows at least as fast as g(n). It will never be faster than this bound.**

### Visualized

```
Operations
^
|       T(n)  ─────────────────────────────────
|                   ↑ T(n) stays ABOVE c·g(n)
|       c·g(n)─────────────────────────────────  ← Omega lower bound
|
|______________|________________________________> n
              n₀
```

### Worked Proof: T(n) = 5n² + 3 is Ω(n²)

```
Need: T(n) ≥ c · n² for all n ≥ n₀

5n² + 3 ≥ 5n²   [since 3 is positive, this is obviously true]
→ c = 5, n₀ = 1

Therefore: T(n) = Ω(n²)  ✓
```

### Worked Proof: T(n) = 5n² + 3 is Ω(n) as well

```
5n² + 3 ≥ 5n²  ≥  5n · n  ≥  5n   [for n ≥ 1]
→ c = 5, n₀ = 1
T(n) = Ω(n) also holds!
```

> Notice: Like Big O, Omega is also not unique. The function is Ω(1), Ω(n), Ω(n²)...  
> **Convention:** Always give the tightest (largest) Omega you can.

### The Relationship Between All Three

```
For T(n) = 5n² + 3:

  Ω(n²) ← tightest lower bound (the largest function it beats)
     ↑
  Θ(n²) ← tight bound (exact growth rate)
     ↓
  O(n²) ← tightest upper bound (the smallest function that beats it)

All three point to n² → This is the "true" growth rate.
```

---

## SECTION 9: THE COMPLETE NOTATION TABLE

```
╔════════════════════════════════════════════════════════════════════╗
║              ASYMPTOTIC NOTATION MASTER TABLE                      ║
╠══════════╦═══════════════╦═══════════════════╦════════════════════╣
║ Notation ║ Bound         ║ Formal Condition   ║ Analogy            ║
╠══════════╬═══════════════╬═══════════════════╬════════════════════╣
║ O(g(n))  ║ Upper         ║ T(n) ≤ c·g(n)     ║ T(n) ≤ g(n) (≤)   ║
║ Ω(g(n))  ║ Lower         ║ T(n) ≥ c·g(n)     ║ T(n) ≥ g(n) (≥)   ║
║ Θ(g(n))  ║ Tight (both)  ║ c₁g ≤ T(n) ≤ c₂g ║ T(n) ≈ g(n) (=)   ║
╠══════════╬═══════════════╬═══════════════════╬════════════════════╣
║ o(g(n))  ║ Strict upper  ║ T(n)/g(n) → 0     ║ T(n) < g(n) (<)   ║
║ ω(g(n))  ║ Strict lower  ║ T(n)/g(n) → ∞     ║ T(n) > g(n) (>)   ║
╚══════════╩═══════════════╩═══════════════════╩════════════════════╝

Little-o and Little-omega: strict versions (not equal — strictly faster/slower)
Rarely used in interviews, but occasionally in theory courses.
```

### The Math Analogy (This Is Gold)

```
If f and g are numbers:

  f = O(g)  ←→  f ≤ g    (at most)
  f = Ω(g)  ←→  f ≥ g    (at least)
  f = Θ(g)  ←→  f = g    (exactly, up to constants)
  f = o(g)  ←→  f < g    (strictly less)
  f = ω(g)  ←→  f > g    (strictly greater)
```

---

## SECTION 10: TIME COMPLEXITY — DEEP ANALYSIS

Time complexity measures: **how does the number of basic operations grow with input size n?**

### What Counts as a "Basic Operation"?

```
✓ Counts as O(1):
  — Array index access: arr[i]
  — Arithmetic: +, -, *, /
  — Comparison: a > b
  — Assignment: x = 5
  — Dictionary lookup: d[key]  (average)
  — Function call overhead (not the function body)

✗ Does NOT count as O(1):
  — A loop (contains many operations)
  — A recursive call (contains subtree of operations)
  — String concatenation: a + b  (O(len(a) + len(b)))
  — List slicing: arr[i:j]  (O(j - i))
  — Sorting: arr.sort()  (O(n log n))
```

### Method 1: Counting Iterations Directly

```python
def example_1(n: int) -> None:
    # Single loop: runs exactly n times
    for i in range(n):          # ← n iterations
        print(i)                # ← O(1) work per iteration
    
    # Total: n × O(1) = O(n)
```

```python
def example_2(n: int) -> None:
    # Nested loops
    for i in range(n):          # ← n iterations
        for j in range(n):      # ← n iterations per outer
            print(i, j)         # ← O(1) work
    
    # Total: n × n × O(1) = O(n²)
```

```python
def example_3(n: int) -> None:
    # Loop where j grows multiplicatively, not additively
    j = 1
    while j < n:
        print(j)
        j *= 2                  # ← j doubles each time: 1, 2, 4, 8, ..., n
    
    # How many steps? 2^k = n → k = log₂(n)
    # Total: O(log n)
```

### Method 2: Tricky Loop Analysis — Dry Run Required

```python
def example_4(arr: list[int]) -> None:
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):    # Inner loop depends on i!
            print(arr[i], arr[j])
```

**Dry run for n = 5:**

```
i=0: j runs from 1 to 4  → 4 iterations
i=1: j runs from 2 to 4  → 3 iterations
i=2: j runs from 3 to 4  → 2 iterations
i=3: j runs from 4 to 4  → 1 iteration
i=4: j runs from 5 to 4  → 0 iterations

Total = 4 + 3 + 2 + 1 + 0 = 10 = n(n-1)/2
```

**Derivation:**

```
Total = Σ(i=0 to n-1) (n - 1 - i)
      = (n-1) + (n-2) + ... + 1 + 0
      = n(n-1)/2
      = (n² - n) / 2
Drop lower term (n) and constant (1/2):
→ O(n²)
```

### Method 3: Recursive Algorithm Analysis

This is where students struggle most. Let's derive carefully.

**Recursive Binary Search:**

```python
def binary_search_recursive(arr: list[int], target: int,
                             left: int, right: int) -> int:
    # Base case: search space exhausted
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        # Key: we only recurse on HALF the input
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

**Setting up the recurrence:**

```
Let T(n) = time for input of size n

T(n) = T(n/2) + O(1)
           ↑          ↑
     recurse on    comparison
     half input    at this level

Expanding:
T(n)   = T(n/2)   + c
T(n/2) = T(n/4)   + c
T(n/4) = T(n/8)   + c
...
T(2)   = T(1)     + c
T(1)   = O(1)

After k steps: T(n) = T(n/2^k) + k·c
Stop when n/2^k = 1 → k = log₂(n)
T(n) = O(1) + log₂(n) · c
     = O(log n)  ✓
```

**Recursive Merge Sort:**

```python
def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])     # T(n/2)
    right = merge_sort(arr[mid:])    # T(n/2)
    return merge(left, right)        # O(n) to merge
```

**Recurrence and solution:**

```
T(n) = 2·T(n/2) + O(n)
           ↑          ↑
    two recursive   merging takes
    calls, each     linear time
    on half input

Expanding via recursion tree:
Level 0: 1 call, cost n
Level 1: 2 calls, each cost n/2  → total n
Level 2: 4 calls, each cost n/4  → total n
...
Level k: 2^k calls, each cost n/2^k → total n

Number of levels = log₂(n)
Total cost = n × log₂(n)
→ O(n log n)  ✓
```

### Time Complexity Cheatsheet for Code Patterns

```
Code Pattern                              Time Complexity
─────────────────────────────────────────────────────────
Single loop 0 to n                        O(n)
Two nested loops 0 to n                   O(n²)
Three nested loops 0 to n                 O(n³)
Loop, halving each time (i //= 2)         O(log n)
Loop to n, inner loop to log n            O(n log n)
Recursive: T(n) = T(n-1) + O(1)          O(n)
Recursive: T(n) = T(n/2) + O(1)          O(log n)
Recursive: T(n) = 2T(n/2) + O(n)         O(n log n)
Recursive: T(n) = T(n-1) + O(n)          O(n²)
Recursive: T(n) = 2T(n-1) + O(1)         O(2ⁿ)
```

---

## SECTION 11: SPACE COMPLEXITY — COMPLETE ANALYSIS

Space complexity is the **total memory** an algorithm uses as a function of input size n.

### The Two Components

```
Total Space = Input Space + Auxiliary Space
                   ↑               ↑
           Space for the    Extra space the algorithm
           input itself     uses BEYOND the input
```

> **Key interview distinction:**
> - Space complexity = everything
> - Auxiliary space = extra space only (input not counted)
>
> When someone says "solve it in O(1) space", they mean **O(1) auxiliary space** — you can still use the input array, but no extra data structures.

### Type 1: O(1) Auxiliary Space — In-Place

```python
def find_max(arr: list[int]) -> int:
    """
    Space analysis:
    - Input arr: O(n)  ← this is INPUT space, not auxiliary
    - max_val: 1 integer = O(1)
    - Loop variable i: O(1)
    
    Auxiliary space = O(1)  ← only the extra variables we created
    Total space = O(n) + O(1) = O(n)
    """
    max_val = arr[0]            # O(1) extra space
    
    for val in arr:             # Loop variable: O(1)
        if val > max_val:
            max_val = val
    
    return max_val
```

### Type 2: O(n) Auxiliary Space — Extra Data Structure

```python
def two_sum(arr: list[int], target: int) -> tuple[int, int]:
    """
    Space analysis:
    - seen dict: at most n entries = O(n) auxiliary space
    
    This is the O(n) space, O(n) time tradeoff.
    We buy speed (O(n) time) at the cost of space (O(n) auxiliary).
    """
    seen = {}                   # O(n) auxiliary space in worst case
    
    for i, val in enumerate(arr):       # O(n) time
        complement = target - val
        
        if complement in seen:          # O(1) lookup
            return (seen[complement], i)
        
        seen[val] = i                   # Store: O(1) per operation
    
    return (-1, -1)
```

### Type 3: O(n) Space Due to Recursion — Call Stack

This is the **most commonly forgotten** space usage.

```python
def factorial_recursive(n: int) -> int:
    """
    SPACE ANALYSIS — The Hidden Stack Cost:
    
    factorial(5)
      → factorial(4)
           → factorial(3)
                → factorial(2)
                     → factorial(1)
                          → return 1
    
    At maximum depth, we have n frames on the call stack simultaneously.
    Each frame stores: n, return address, local variables = O(1) per frame
    Total stack space: n frames × O(1) = O(n) auxiliary space
    
    This is NOT O(1) space, even though each frame is simple!
    """
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)   # n frames deep → O(n) stack space
```

**Visualizing the call stack:**

```
Stack grows downward:

Call Stack at deepest point:
┌──────────────────────┐ ← Stack top
│ factorial(1)  n=1    │ ← Frame 5
├──────────────────────┤
│ factorial(2)  n=2    │ ← Frame 4
├──────────────────────┤
│ factorial(3)  n=3    │ ← Frame 3
├──────────────────────┤
│ factorial(4)  n=4    │ ← Frame 2
├──────────────────────┤
│ factorial(5)  n=5    │ ← Frame 1 (bottom)
└──────────────────────┘

n frames total → O(n) stack space
```

**Iterative version (O(1) space):**

```python
def factorial_iterative(n: int) -> int:
    """
    O(1) auxiliary space — no recursive call stack.
    Only constant number of variables regardless of n.
    """
    result = 1
    
    for i in range(2, n + 1):  # O(1) space — loop variable
        result *= i             # O(1) space — one variable
    
    return result
    # Auxiliary space: O(1) ✓
```

### Type 4: O(log n) Space — Balanced Recursion

```python
def binary_search_recursive(arr, target, left, right):
    """
    Recursion depth = log₂(n)  (input halves each call)
    Stack frames at max depth = log₂(n)
    → O(log n) auxiliary space
    
    Contrast with:
    - factorial (O(n) depth) → O(n) space
    - binary search iterative → O(1) space
    """
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

### Type 5: O(n) Space — Building Output

```python
def get_all_subsets(arr: list[int]) -> list[list[int]]:
    """
    Output itself has 2^n subsets.
    Even if we can't do better algorithmically,
    the output forces O(2^n) space.
    
    This is unavoidable — we MUST store 2^n subsets.
    Key distinction: Is the space for the OUTPUT or WORKING?
    """
    result = [[]]               # Start with empty subset
    
    for num in arr:
        # For each element, double the subsets
        new_subsets = [subset + [num] for subset in result]
        result.extend(new_subsets)
    
    return result
    # Space: O(2^n) — but this is the output, not wasteful auxiliary space
```

### Space Complexity Summary Table

```
Algorithm                      Time        Aux Space    Stack Space
──────────────────────────────────────────────────────────────────
find_max (loop)               O(n)         O(1)         O(1)
two_sum (hashmap)             O(n)         O(n)         O(1)
binary_search (iterative)     O(log n)     O(1)         O(1)
binary_search (recursive)     O(log n)     O(1)         O(log n)
merge_sort                    O(n log n)   O(n)         O(log n)
factorial (iterative)         O(n)         O(1)         O(1)
factorial (recursive)         O(n)         O(1)         O(n)
power_set                     O(2^n)       O(2^n)       O(n)
```

---

## SECTION 12: PYTHON MASTERY

### Python-Specific Space Costs

```python
# Lists
arr = [1, 2, 3, 4, 5]          # O(n) space
arr.copy()                      # O(n) — creates new list
arr[i:j]                        # O(j-i) — creates new list (NOT O(1)!)

# Strings (immutable)
s = "hello"
s + t                           # O(|s| + |t|) — creates new string
# String concat in a loop is O(n²) total!

# Dictionaries and Sets
d = {}                          # O(n) when full
s = set()                       # O(n) when full

# Recursive calls
# ALWAYS add O(depth) to space complexity for recursive algorithms
```

### Why Python's `sys.setrecursionlimit` Matters

```python
import sys
sys.setrecursionlimit(10000)    # Default is 1000 in Python

# Each recursive call uses ~100-500 bytes of stack frame
# Deep recursion (depth > 1000) → RecursionError in Python
# For large n, prefer iterative approaches in Python
```

### Counter, defaultdict — O(n) Space

```python
from collections import Counter, defaultdict

# Counter — O(n) space, builds frequency map
freq = Counter([1, 2, 2, 3, 3, 3])   # {3:3, 2:2, 1:1}
# Space: O(k) where k = unique elements ≤ n

# defaultdict — O(n) space
graph = defaultdict(list)              # Adjacency list
# Each key-value pair = O(1), but total = O(n + m) for n nodes, m edges
```

---

## SECTION 13: COMMON MISTAKES

### Mistake 1: Confusing O, Ω, Θ in Context

```
"Binary search is O(n)"     ← TRUE but misleading (O is upper bound)
"Binary search is O(log n)" ← TRUE and tight
"Binary search is Θ(log n)" ← MOST PRECISE

Always give the tightest bound.
```

### Mistake 2: Forgetting Call Stack Space

```python
# Students say this is O(1) space. It's NOT.
def sum_recursive(n):
    if n == 0: return 0
    return n + sum_recursive(n - 1)

# Call stack depth = n → O(n) auxiliary space
```

### Mistake 3: Treating Average Case as Worst Case

```
Quick Sort:
  Average case: O(n log n)  ← what most people say
  Worst case:   O(n²)       ← what you MUST mention in interviews

Interviews expect worst case unless specified otherwise.
```

### Mistake 4: List Slice is O(k), Not O(1)

```python
# This merge sort has HIDDEN space cost from slicing:
def merge_sort(arr):
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # arr[:mid] = O(n/2) copy!
    right = merge_sort(arr[mid:])  # arr[mid:] = O(n/2) copy!
    
# Total extra space: O(n log n) — worse than expected!
# In-place merge sort is harder but avoids this.
```

### Mistake 5: log₂ vs log₁₀ vs ln

```
In Big O: ALL logarithms are equivalent.
log₂(n) = log₁₀(n) × log₂(10) ≈ 3.32 × log₁₀(n)
The 3.32 is a constant → dropped in Big O.
Write O(log n) always, never O(log₂ n) or O(ln n).
```

### Edge Cases to Always Check:

- ☐ n = 0 → does the algorithm crash or return correctly?
- ☐ n = 1 → single element — does the loop/recursion work?
- ☐ All same elements → does this trigger worst case?
- ☐ Already sorted / reverse sorted → Quick sort worst case!
- ☐ Integer overflow: Python handles this natively, but in C++/Java: `mid = left + (right - left) // 2` not `(left + right) // 2`

---

## SECTION 14: HOW TO COMMUNICATE IN AN INTERVIEW

### Script: Presenting Complexity Analysis

> "Let me analyze this. The outer loop runs n times. For each iteration, I'm calling dictionary lookup which is O(1) average. So the time complexity is O(n). For space, I'm building a hash map that could hold at most n entries, so auxiliary space is O(n). Total space complexity is O(n) as well. Would you like me to optimize for space?"

---

### Script: When Asked "Which Notation?"

> "I'll give you the Big O — the worst-case upper bound — since that's what matters for system design and scalability. The tight bound here is actually Theta(n log n) since both best and worst case merge sort always divide and merge. But if you're asking strictly about upper bound guarantees: O(n log n)."

---

### The Tradeoff Conversation Template

> "We have two choices:
> - Option A: O(n²) time, O(1) auxiliary space — uses two nested loops, no extra memory
> - Option B: O(n) time, O(n) auxiliary space — uses a hash map
>
> Given n ≤ 10⁵ in the constraints, O(n²) would be 10¹⁰ operations — too slow. I'll go with Option B: O(n) time, O(n) space. If the interviewer says memory is constrained, I'd revisit Option A."

---

### What the Interviewer Is Checking

1. **Do you know the definitions** of O, Ω, Θ — not just vaguely?
2. **Can you derive**, not just guess, the complexity?
3. **Do you account for space** — especially recursive call stack?
4. **Do you know the difference** between auxiliary space and total space?
5. **Can you choose** the right notation for the right context?

---

## SECTION 15: INTERVIEW FOLLOW-UPS

**Q1: What is the difference between Big O and Theta?**
> Big O is an upper bound — T(n) could be faster. Theta is a tight bound — T(n) grows exactly at that rate. T(n) = n is O(n²) (true but loose) AND Θ(n) (tight). Always prefer Theta when the bounds match.

**Q2: Can an algorithm be both O(n) and O(n²)?**
> Yes. Big O is an upper bound, so any looser upper bound is also valid. If f(n) = n, then f(n) = O(n) and f(n) = O(n²) are both true. But we always state the tightest correct bound.

**Q3: Is a recursive solution always worse in space than iterative?**
> Yes, by O(depth) stack space. Recursive binary search is O(log n) space vs O(1) for iterative. Recursive factorial is O(n) space vs O(1) iterative. Tail call optimization (not available in Python) can eliminate this.

**Q4: What is amortized complexity?**
> Amortized complexity is the average cost per operation over a sequence. Python's `list.append()` is occasionally O(n) (when doubling), but amortized O(1) over n appends total. It's the "smoothed out" average.

**Q5: Is O(n log n) always better than O(n²)?**
> For large n, always. But for small n (say n ≤ 20), the constants matter and O(n²) with small constants can be faster. This is why Timsort uses insertion sort for small sub-arrays within merge sort.

**Q6: What's the space complexity of BFS vs DFS on a graph?**
> BFS stores all nodes at the current frontier in a queue: O(w) where w is max width. DFS uses the call stack (or explicit stack): O(d) where d is max depth. For balanced trees: BFS is O(n/2) ≈ O(n), DFS is O(log n). For skewed trees: DFS is O(n).

**Q7: If I have O(n) time and O(n) space, can I always reduce space to O(1)?**
> Not always. Sometimes O(n) space is inherent to the problem (building output, DP table). You can sometimes reduce with clever in-place tricks, but it often makes the code harder. In interviews, always mention the tradeoff.

**Q8: What does "tight bound" mean precisely?**
> A bound is tight when there exists an input that actually achieves it. Saying "binary search is O(n)" is true but not tight — no input causes binary search to run n comparisons. The tight bound is O(log n) because worst-case inputs (target not found) actually cause log n comparisons.

---

## SECTION 16: RELATED PROBLEMS / LEARNING GRAPH

```
Asymptotic Analysis (Foundation)
         ↓
Time Complexity of Loops
(Practice: count iterations on paper for any given code)
         ↓
Recurrence Relations
(T(n) = 2T(n/2) + n → solve for T(n))
         ↓
Master Theorem
(Shortcut for solving divide-and-conquer recurrences)
         ↓
Amortized Analysis
(Dynamic arrays, hash tables, Union-Find)
         ↓
Lower Bound Theory
(Can we prove no algorithm can beat Ω(n log n) for comparison sorting?)
         ↓
Algorithm Design via Complexity Targets
("I need O(n log n) — what techniques achieve this? Divide and conquer, heaps, sorting...")
```

---

## SECTION 17: TOPIC CONNECTION MAP

```
[Order of Growth — Session 1]
              ↓
[ASYMPTOTIC ANALYSIS · Big O · Theta · Omega]  ← YOU ARE HERE
              ↓
         ┌────┴────┐
         ↓         ↓
 [Time Complexity] [Space Complexity]
         ↓         ↓
         └────┬────┘
              ↓
    [Recurrence Relations]
    (formal way to derive O() for recursion)
              ↓
    [Master Theorem]
    (T(n) = aT(n/b) + f(n) → solved in one step)
              ↓
    [Sorting Algorithms]
    (every sort analyzed using this framework)
              ↓
    [Graph Algorithms]
    (BFS O(V+E), Dijkstra O(E log V) — all built on this)
              ↓
    [Dynamic Programming]
    (memoization converts O(2^n) → O(n) using O(n) space tradeoff)
              ↓
    [System Design]
    ("can this scale?" — always comes back to asymptotic analysis)
```

**Builds on most:** Order of Growth (Session 1) — today is the formal mathematical foundation of those intuitions.

**Future topic impossible without this:** Every single DSA topic. But immediately next: **Recurrence Relations and the Master Theorem** — you cannot correctly derive complexity of any recursive algorithm without today's foundation.

---

## SECTION 18: INTERVIEW REVISION NOTES

```
Pattern:             Asymptotic Notation — O, Ω, Θ

Big O:               T(n) ≤ c·g(n) for all n ≥ n₀  →  upper bound
Big Omega:           T(n) ≥ c·g(n) for all n ≥ n₀  →  lower bound
Big Theta:           c₁·g(n) ≤ T(n) ≤ c₂·g(n)      →  tight (O AND Ω)

Math analogy:        O = ≤,  Ω = ≥,  Θ = =

Time complexity:     Count dominant term in operation count expression
Space complexity:    Auxiliary space (extra) + Input space
Call stack:          Recursive depth × O(1) per frame → O(depth) stack space

Key rules:           Drop constants | Drop lower terms | Sum=max | Product=multiply
Python traps:        String concat in loop = O(n²) | slice = O(k) | dict lookup = O(1) avg

Constraint table:    n≤10²→O(n²) | n≤10⁵→O(n log n) | n≤10⁶→O(n) | n≥10⁷→O(log n)

Most common mistake: Forgetting recursive call stack space; not using tightest bound
One-line intuition:  "O = ceiling, Ω = floor, Θ = exact — after some threshold n₀"
```

---

## SECTION 19: DIFFICULTY AND FREQUENCY

```
Difficulty:    ■ Beginner (O/Ω/Θ definitions)
               ■ Intermediate (proving bounds, recurrences)
               □ Advanced (tight lower bounds, amortized)

Interview Frequency:
  FAANG overall:    ████████████  Asked in EVERY interview as follow-up
  Amazon:           ████████████  LP + technical — always asked
  Google:           ████████████  Extremely rigorous; expect formal proofs
  Microsoft:        ███████████   High; both time and space expected
  Meta:             ████████████  Scale focus — space especially important
  Startups:         █████████     High; they want to know you understand tradeoffs

Tested:  Practically (analyze this code) + Theoretically (prove this bound)
         Google uniquely asks: "Is O(n log n) tight here? Can you prove it?"
```

---

## SECTION 20: PRACTICE PROGRESSION

### Easy

**1. GFG — Time Complexity Quiz (Practice Section)**
- Why: Pure mechanical drill — read code snippets, state the complexity
- Focus: Nested loops, loops with multiplicative steps, simple recursion

**2. LeetCode 1 — Two Sum**
- Why: Classic O(n²) → O(n) improvement; practice space-time tradeoff
- Focus: Derive time AND space for BOTH approaches; explain why O(n) space is worth it

**3. LeetCode 704 — Binary Search**
- Why: First O(log n) time, O(1) vs O(log n) space comparison (iterative vs recursive)
- Focus: Write both versions; state exact space complexity for each

---

### Medium

**4. LeetCode 912 — Sort an Array (Implement Merge Sort)**
- Why: Derive O(n log n) from recursion tree; experience O(n) auxiliary space from merging
- Focus: Why does merge sort need O(n) extra space? Can we do better?

**5. LeetCode 347 — Top K Frequent Elements**
- Why: Compare O(n log n) sorting approach vs O(n log k) heap approach
- Focus: When is O(n log k) better than O(n log n)? Work through the math.

**6. LeetCode 239 — Sliding Window Maximum**
- Why: O(n²) naive vs O(n) deque; significant complexity reduction
- Focus: Prove the deque solution is O(n) — each element enters and exits at most once

---

### Hard

**7. LeetCode 4 — Median of Two Sorted Arrays**
- Why: O(log(min(m,n))) — prove why this is achievable; requires deep binary search insight
- Focus: Write the formal O() proof for why this is O(log(min(m,n))) not O(log(m+n))

**8. LeetCode 23 — Merge K Sorted Lists**
- Why: Multiple approaches with different complexities; derive each from scratch
- Focus: O(nk) naive vs O(n log k) heap — derive both; know why log k and not log n

**9. LeetCode 312 — Burst Balloons**
- Why: DP problem where the complexity proof is non-trivial — O(n³) must be argued carefully
- Focus: How many subproblems are there? How much work per subproblem? Derive O(n³).

---

## SECTION 21: PATTERN MEMORY SYSTEM

```
Pattern Name:       Asymptotic Analysis — Formal Complexity Framework

What makes it unique:
  The universal language of algorithm comparison; machine-independent;
  three notations that together fully characterize algorithm growth

Recognition signals:
  • "What's the complexity?" in any interview
  • n in constraints tells you the target complexity
  • Solution TLEs (Time Limit Exceeded) → your Big O is too large
  • Asked to "prove" an algorithm is efficient
  • Comparing two solutions that both work but differ in scale

Core tools:
  Big O (upper), Omega (lower), Theta (tight)
  Recurrence equations for recursive algorithms

Core observation that unlocks it:
  After threshold n₀, only the dominant term governs behavior;
  constants are machine-dependent and irrelevant to the shape

Typical complexity expressed:  O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ)

How to distinguish from similar ideas:
  O ≠ Θ: O(n²) for a linear function is valid but useless
  Time ≠ Space: O(n) time can have O(1) or O(n) space independently
  Auxiliary ≠ Total: recursive O(1) work per frame still costs O(n) stack

Problems that use exactly this pattern:
  Every DSA problem — this is the analytical lens,
  not the algorithm itself
```

---

> **Closing Thought:**
> You now have the complete mathematical language of algorithms. Big O, Omega, and Theta aren't just definitions — they're a *vocabulary* that lets you think clearly about problems at scale. Every algorithm you learn from this point is described in this language.
>
> The natural next topic is **Recurrence Relations and the Master Theorem** — which gives you a mechanical, formal way to derive the time complexity of any recursive algorithm without expanding the tree by hand.