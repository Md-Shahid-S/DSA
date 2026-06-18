# Generate Subsets — Complete Dry Run

**Input:** `[2, 3, 1]`  
**Expected output:** All 2³ = 8 subsets

---

## THE BIG PICTURE FIRST

Before anything — understand the **two choices at every element:**

```
For each element in arr, you ask ONE question:
"Do I include this element in my current subset, or not?"

arr = [2,    3,    1  ]
       ↑     ↑     ↑
    include  include  include
      OR       OR       OR
    exclude  exclude  exclude

Total combinations = 2 × 2 × 2 = 8 subsets
```

**The key mechanism — `current` list:**
```
current is a SHARED list — one list, mutated and un-mutated as we go.

INCLUDE → append to current → recurse → pop from current (backtrack)
EXCLUDE → recurse WITHOUT touching current

current always shows "what subset am I building RIGHT NOW"
```

---

## THE DECISION TREE (Full Picture)

```
                        index=0, current=[]
                       /                    \
               EXCLUDE 2                  INCLUDE 2
                  /                            \
       index=1, current=[]          index=1, current=[2]
            /        \                   /              \
      EXCL 3        INCL 3          EXCL 3            INCL 3
         /              \               \                   \
index=2,[]    index=2,[3]    index=2,[2]    index=2,[2,3]
    /    \        /    \        /    \          /       \
EXCL1  INCL1  EXCL1  INCL1  EXCL1  INCL1  EXCL1     INCL1
  |      |      |      |      |      |      |           |
 []    [1]    [3]   [3,1]   [2]   [2,1]  [2,3]      [2,3,1]

OUTPUT (left to right): [[], [1], [3], [3,1], [2], [2,1], [2,3], [2,3,1]]
```

---

## FULL CALL-BY-CALL DRY RUN

I'll track every call with:
- Call number
- `index` value
- `current` list state
- What happens

---

### CALL 1 — Entry Point

```
generate_subsets([2,3,1], index=0, current=None)

current = None → current = []     ← initialized here

index=0, len(arr)=3 → 0 != 3 → NOT base case

results = []

Next: TWO recursive calls happen
  First:  EXCLUDE arr[0]=2  → Call 2
  Second: INCLUDE arr[0]=2  → Call 8  (will happen AFTER Call 2 fully returns)
```

---

### ── EXCLUDE 2 BRANCH ──

---

#### CALL 2

```
generate_subsets([2,3,1], index=1, current=[])
                                    ↑
                            unchanged — we excluded 2

index=1 != 3 → NOT base case
results = []

Next:
  First:  EXCLUDE arr[1]=3  → Call 3
  Second: INCLUDE arr[1]=3  → Call 6
```

---

##### CALL 3

```
generate_subsets([2,3,1], index=2, current=[])
                                    ↑
                            still empty — excluded 2 and 3

index=2 != 3 → NOT base case
results = []

Next:
  First:  EXCLUDE arr[2]=1  → Call 4
  Second: INCLUDE arr[2]=1  → Call 5
```

---

###### CALL 4 — BASE CASE ✓

```
generate_subsets([2,3,1], index=3, current=[])
                                    ↑
                            excluded 2, 3, and 1

index=3 == len(arr)=3 → BASE CASE

return [current[:]]
     = [[]]           ← copy of empty list

✓ Returns: [[]]
```

---

Back in **Call 3:**

```
results.extend([[]])   →   results = [[]]

Now: INCLUDE arr[2]=1
current.append(1)      →   current = [1]
```

---

###### CALL 5 — BASE CASE ✓

```
generate_subsets([2,3,1], index=3, current=[1])
                                    ↑
                            excluded 2, 3 but INCLUDED 1

index=3 == 3 → BASE CASE

return [current[:]]
     = [[1]]          ← copy of [1]

✓ Returns: [[1]]
```

---

Back in **Call 3:**

```
results.extend([[1]])  →   results = [[], [1]]

current.pop()          →   current = []   ← BACKTRACK, undo the append(1)

return [[], [1]]
```

---

Back in **Call 2:**

```
results.extend([[], [1]])   →   results = [[], [1]]

Now: INCLUDE arr[1]=3
current.append(3)           →   current = [3]
```

---

##### CALL 6

```
generate_subsets([2,3,1], index=2, current=[3])
                                    ↑
                            excluded 2, INCLUDED 3

index=2 != 3 → NOT base case
results = []

Next:
  First:  EXCLUDE arr[2]=1  → Call 7
  Second: INCLUDE arr[2]=1  → Call 8... 
  
  wait — let me renumber cleanly
```

---

###### CALL 7 — BASE CASE ✓

```
generate_subsets([2,3,1], index=3, current=[3])
                                    ↑
                            excluded 2, included 3, excluded 1

index=3 == 3 → BASE CASE

return [current[:]]
     = [[3]]

✓ Returns: [[3]]
```

---

Back in **Call 6:**

```
results.extend([[3]])  →   results = [[3]]

Now: INCLUDE arr[2]=1
current.append(1)      →   current = [3, 1]
```

---

###### CALL 8 — BASE CASE ✓

```
generate_subsets([2,3,1], index=3, current=[3,1])
                                    ↑
                            excluded 2, included 3, included 1

index=3 == 3 → BASE CASE

return [current[:]]
     = [[3, 1]]

✓ Returns: [[3, 1]]
```

---

Back in **Call 6:**

```
results.extend([[3,1]])  →   results = [[3], [3,1]]

current.pop()            →   current = [3]   ← undo append(1)

return [[3], [3,1]]
```

---

Back in **Call 2:**

```
results.extend([[3],[3,1]])   →   results = [[], [1], [3], [3,1]]

current.pop()                 →   current = []   ← undo append(3)

return [[], [1], [3], [3,1]]
```

---

Back in **Call 1:**

```
results.extend([[], [1], [3], [3,1]])

results = [[], [1], [3], [3,1]]

Now: INCLUDE arr[0]=2
current.append(2)    →    current = [2]
```

---

### ── INCLUDE 2 BRANCH ──

---

#### CALL 9

```
generate_subsets([2,3,1], index=1, current=[2])
                                    ↑
                            INCLUDED 2

index=1 != 3 → NOT base case
results = []

Next:
  First:  EXCLUDE arr[1]=3  → Call 10
  Second: INCLUDE arr[1]=3  → Call 13
```

---

##### CALL 10

```
generate_subsets([2,3,1], index=2, current=[2])
                                    ↑
                            included 2, excluded 3

index=2 != 3 → NOT base case
results = []

Next:
  First:  EXCLUDE arr[2]=1  → Call 11
  Second: INCLUDE arr[2]=1  → Call 12
```

---

###### CALL 11 — BASE CASE ✓

```
generate_subsets([2,3,1], index=3, current=[2])
                                    ↑
                            included 2, excluded 3, excluded 1

index=3 == 3 → BASE CASE

return [current[:]]
     = [[2]]

✓ Returns: [[2]]
```

---

Back in **Call 10:**

```
results.extend([[2]])   →   results = [[2]]

current.append(1)       →   current = [2, 1]
```

---

###### CALL 12 — BASE CASE ✓

```
generate_subsets([2,3,1], index=3, current=[2,1])
                                    ↑
                            included 2, excluded 3, included 1

index=3 == 3 → BASE CASE

return [current[:]]
     = [[2, 1]]

✓ Returns: [[2, 1]]
```

---

Back in **Call 10:**

```
results.extend([[2,1]])   →   results = [[2], [2,1]]

current.pop()             →   current = [2]   ← undo append(1)

return [[2], [2,1]]
```

---

Back in **Call 9:**

```
results.extend([[2],[2,1]])   →   results = [[2], [2,1]]

current.append(3)             →   current = [2, 3]
```

---

##### CALL 13

```
generate_subsets([2,3,1], index=2, current=[2,3])
                                    ↑
                            included 2, included 3

index=2 != 3 → NOT base case
results = []

Next:
  First:  EXCLUDE arr[2]=1  → Call 14
  Second: INCLUDE arr[2]=1  → Call 15
```

---

###### CALL 14 — BASE CASE ✓

```
generate_subsets([2,3,1], index=3, current=[2,3])
                                    ↑
                            included 2, included 3, excluded 1

index=3 == 3 → BASE CASE

return [current[:]]
     = [[2, 3]]

✓ Returns: [[2, 3]]
```

---

Back in **Call 13:**

```
results.extend([[2,3]])   →   results = [[2,3]]

current.append(1)         →   current = [2, 3, 1]
```

---

###### CALL 15 — BASE CASE ✓

```
generate_subsets([2,3,1], index=3, current=[2,3,1])
                                    ↑
                            included 2, included 3, included 1

index=3 == 3 → BASE CASE

return [current[:]]
     = [[2, 3, 1]]

✓ Returns: [[2, 3, 1]]
```

---

Back in **Call 13:**

```
results.extend([[2,3,1]])   →   results = [[2,3], [2,3,1]]

current.pop()               →   current = [2,3]   ← undo append(1)

return [[2,3], [2,3,1]]
```

---

Back in **Call 9:**

```
results.extend([[2,3],[2,3,1]])

results = [[2], [2,1], [2,3], [2,3,1]]

current.pop()   →   current = [2]   ← undo append(3)

return [[2], [2,1], [2,3], [2,3,1]]
```

---

Back in **Call 1:**

```
results.extend([[2],[2,1],[2,3],[2,3,1]])

results = [[], [1], [3], [3,1], [2], [2,1], [2,3], [2,3,1]]

current.pop()   →   current = []   ← undo append(2)

return [[], [1], [3], [3,1], [2], [2,1], [2,3], [2,3,1]]
```

---

## FINAL ANSWER

```
generate_subsets([2, 3, 1])

= [[], [1], [3], [3,1], [2], [2,1], [2,3], [2,3,1]]
```

All **2³ = 8 subsets** ✓

---

## THE BACKTRACKING MECHANISM — Zoomed In

This is the most important thing to understand. `current` is **one single list** shared across all calls. Watch how it changes:

```
STATE OF current AT EVERY BASE CASE HIT:

Call 4  hits base: current = []        → records []
Call 5  hits base: current = [1]       → records [1]
                   current.pop() → []  ← UNDO

Call 7  hits base: current = [3]       → records [3]
Call 8  hits base: current = [3,1]     → records [3,1]
                   current.pop() → [3] ← UNDO

Call 11 hits base: current = [2]       → records [2]
Call 12 hits base: current = [2,1]     → records [2,1]
                   current.pop() → [2] ← UNDO

Call 14 hits base: current = [2,3]     → records [2,3]
Call 15 hits base: current = [2,3,1]   → records [2,3,1]
                   current.pop() → [2,3] ← UNDO
```

```
current grows and shrinks like a STACK:

Timeline:
[]
[2] ← append
[2,3] ← append
[2,3,1] ← append → RECORD
[2,3] ← pop
[2,3] → RECORD
[2] ← pop
[2,1] ← append → RECORD
[2] ← pop
[2] → RECORD
[] ← pop
... and so on
```

---

## WHY `current[:]` MATTERS

```python
return [current[:]]    # ← this copy is CRITICAL
```

```
Without copy:
  current = [1]
  result.append(current)    →  result = [[1]]
  current.pop()             →  current = []
  Now result = [[]]  ← WRONG! The list in result got modified!

With copy (current[:]):
  current = [1]
  snapshot = current[:]     →  snapshot = [1]  (new independent list)
  result.append(snapshot)   →  result = [[1]]
  current.pop()             →  current = []
  result is still [[1]]     ✓  snapshot is unaffected
```

---

## CALL ORDER SUMMARY

```
Call  1: index=0, current=[]      → branches into exclude/include 2
Call  2: index=1, current=[]      → exclude 2 path
Call  3: index=2, current=[]      → exclude 2, exclude 3 path
Call  4: index=3, current=[]      → BASE → returns [[]]
Call  5: index=3, current=[1]     → BASE → returns [[1]]
Call  6: index=2, current=[3]     → exclude 2, include 3 path
Call  7: index=3, current=[3]     → BASE → returns [[3]]
Call  8: index=3, current=[3,1]   → BASE → returns [[3,1]]
Call  9: index=1, current=[2]     → include 2 path
Call 10: index=2, current=[2]     → include 2, exclude 3 path
Call 11: index=3, current=[2]     → BASE → returns [[2]]
Call 12: index=3, current=[2,1]   → BASE → returns [[2,1]]
Call 13: index=2, current=[2,3]   → include 2, include 3 path
Call 14: index=3, current=[2,3]   → BASE → returns [[2,3]]
Call 15: index=3, current=[2,3,1] → BASE → returns [[2,3,1]]

Total calls = 15 = 2^(n+1) - 1 = 2⁴ - 1  ✓
Base cases  =  8 = 2^n = 2³                ✓
```