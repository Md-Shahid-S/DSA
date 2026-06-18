# Merge Sort — Complete Dry Run

**Input:** `[1, 2, 3, 3, 6, 7, 3, 3, 7, 4, 2, 8, 3, 5, 2]`

That's 15 elements. Let me trace every single call.

---

## THE BIG PICTURE FIRST

Before diving in, understand the **two phases**:

```
PHASE 1 — DIVIDE (going down):
  Keep splitting arrays in half until every piece has 1 element
  1 element = already sorted (base case)

PHASE 2 — MERGE (coming back up):
  Combine sorted pieces into larger sorted pieces
  Work happens HERE, not during splitting
```

```
Think of it like this:

[1,2,3,3,6,7,3,3,7,4,2,8,3,5,2]     ← START: unsorted, size 15
            ↓ SPLIT
    [1,2,3,3,6,7,3]  [3,7,4,2,8,3,5,2] ← wait, let me show exact splits
```

---

## EXACT SPLITS (mid = len // 2)

```
len=15, mid=7  → left=arr[:7],  right=arr[7:]
len=7,  mid=3  → left=arr[:3],  right=arr[3:]
len=8,  mid=4  → left=arr[:4],  right=arr[4:]
... and so on
```

---

## PHASE 1: THE COMPLETE SPLIT TREE

I'll number each call so we can track them.

```
CALL 1: merge_sort([1,2,3,3,6,7,3, | 3,7,4,2,8,3,5,2])
                   mid=7
                  /                  \
CALL 2:          /                    \ CALL 3:
merge_sort([1,2,3,3,6,7,3])       merge_sort([3,7,4,2,8,3,5,2])
           mid=3                              mid=4
          /         \                        /              \
CALL 4:  /           \ CALL 5:    CALL 6:   /                \ CALL 7:
ms([1,2,3])    ms([3,6,7,3])    ms([3,7,4,2])          ms([8,3,5,2])
   mid=1           mid=2            mid=2                   mid=2
   /    \          /    \           /     \                 /      \
C8:/ \C9: C10:/  \C11:  C12:/  \C13:   C14:/  \C15:
ms([1]) ms([2,3]) ms([3,6]) ms([7,3]) ms([3,7]) ms([4,2]) ms([8,3]) ms([5,2])
BASE    mid=1     mid=1     mid=1     mid=1     mid=1     mid=1     mid=1
        / \       / \       / \       / \       / \       / \       / \
      C16 C17   C18 C19   C20 C21   C22 C23   C24 C25   C26 C27   C28 C29
      [2] [3]   [3] [6]   [7] [3]   [3] [7]   [4] [2]   [8] [3]   [5] [2]
      BASE BASE BASE BASE BASE BASE BASE BASE BASE BASE BASE BASE BASE BASE
```

Every **BASE** is a single element → returned immediately, no work done.

---

## PHASE 2: MERGING — WHERE THE MAGIC HAPPENS

Now we travel **back up** the tree, merging at each step.

I'll show every `_merge()` call in detail.

---

### LEVEL 3 MERGES (size 1 + 1 → size 2)

These are the first merges to happen — the deepest level.

---

#### Merge C16+C17: `[2]` and `[3]`  (from Call 9)

```
left=[2],  right=[3]
i=0, j=0

Step 1: left[0]=2  vs  right[0]=3
        2 < 3  → take from left
        result=[2],  i=1

Step 2: i=1 = len(left) → left exhausted
        extend right[0:] = [3]
        result=[2,3]

✓ Returns: [2, 3]
```

---

#### Merge C18+C19: `[3]` and `[6]`  (from Call 10)

```
left=[3],  right=[6]
i=0, j=0

Step 1: left[0]=3  vs  right[0]=6
        3 < 6  → take from left
        result=[3],  i=1

Step 2: left exhausted → extend right → result=[3,6]

✓ Returns: [3, 6]
```

---

#### Merge C20+C21: `[7]` and `[3]`  (from Call 11)

```
left=[7],  right=[3]
i=0, j=0

Step 1: left[0]=7  vs  right[0]=3
        7 > 3  → take from RIGHT
        result=[3],  j=1

Step 2: right exhausted → extend left[0:] = [7]
        result=[3, 7]

✓ Returns: [3, 7]
```

---

#### Merge C22+C23: `[3]` and `[7]`  (from Call 12)

```
left=[3],  right=[7]

Step 1: 3 < 7 → take left → result=[3], i=1
Step 2: left exhausted → extend [7] → result=[3,7]

✓ Returns: [3, 7]
```

---

#### Merge C24+C25: `[4]` and `[2]`  (from Call 13)

```
left=[4],  right=[2]

Step 1: 4 > 2 → take right → result=[2], j=1
Step 2: right exhausted → extend [4] → result=[2,4]

✓ Returns: [2, 4]
```

---

#### Merge C26+C27: `[8]` and `[3]`  (from Call 14)

```
left=[8],  right=[3]

Step 1: 8 > 3 → take right → result=[3], j=1
Step 2: right exhausted → extend [8] → result=[3,8]

✓ Returns: [3, 8]
```

---

#### Merge C28+C29: `[5]` and `[2]`  (from Call 15)

```
left=[5],  right=[2]

Step 1: 5 > 2 → take right → result=[2], j=1
Step 2: right exhausted → extend [5] → result=[2,5]

✓ Returns: [2, 5]
```

---

### LEVEL 2 MERGES (size 2 + 1 or 2 + 2 → size 3 or 4)

Now we use the results from Level 3.

---

#### Merge Call 8 + Call 9's result: `[1]` and `[2,3]`  (→ Call 4's left)

```
left=[1],  right=[2,3]
i=0, j=0

Step 1: left[0]=1  vs  right[0]=2
        1 < 2  → take left
        result=[1],  i=1

Step 2: left exhausted → extend right[0:] = [2,3]
        result=[1, 2, 3]

✓ Returns: [1, 2, 3]
```

---

#### Merge Call 10's result + Call 11's result: `[3,6]` and `[3,7]`  (→ Call 5)

```
left=[3,6],  right=[3,7]
i=0, j=0

Step 1: left[0]=3  vs  right[0]=3
        3 == 3 → LEFT wins (≤ condition)
        result=[3],  i=1

Step 2: left[1]=6  vs  right[0]=3
        6 > 3  → take right
        result=[3,3],  j=1

Step 3: left[1]=6  vs  right[1]=7
        6 < 7  → take left
        result=[3,3,6],  i=2

Step 4: i=2 = len(left) → left exhausted
        extend right[1:] = [7]
        result=[3, 3, 6, 7]

✓ Returns: [3, 3, 6, 7]
```

> 🔍 **Notice:** When elements are equal (both 3), we take from LEFT (`left[i] <= right[j]`). This preserves **stability** — equal elements maintain their original relative order.

---

#### Merge Call 12's result + Call 13's result: `[3,7]` and `[2,4]`  (→ Call 6's left)

```
left=[3,7],  right=[2,4]
i=0, j=0

Step 1: left[0]=3  vs  right[0]=2
        3 > 2  → take right
        result=[2],  j=1

Step 2: left[0]=3  vs  right[1]=4
        3 < 4  → take left
        result=[2,3],  i=1

Step 3: left[1]=7  vs  right[1]=4
        7 > 4  → take right
        result=[2,3,4],  j=2

Step 4: j=2 = len(right) → right exhausted
        extend left[1:] = [7]
        result=[2, 3, 4, 7]

✓ Returns: [2, 3, 4, 7]
```

---

#### Merge Call 14's result + Call 15's result: `[3,8]` and `[2,5]`  (→ Call 7's right... wait)

Actually Call 7 = `merge_sort([8,3,5,2])`, mid=2:
- left = `[8,3]` → sorted to `[3,8]`  (Call 14)
- right = `[5,2]` → sorted to `[2,5]`  (Call 15)

```
left=[3,8],  right=[2,5]
i=0, j=0

Step 1: left[0]=3  vs  right[0]=2
        3 > 2  → take right
        result=[2],  j=1

Step 2: left[0]=3  vs  right[1]=5
        3 < 5  → take left
        result=[2,3],  i=1

Step 3: left[1]=8  vs  right[1]=5
        8 > 5  → take right
        result=[2,3,5],  j=2

Step 4: right exhausted → extend left[1:] = [8]
        result=[2, 3, 5, 8]

✓ Returns: [2, 3, 5, 8]
```

---

### LEVEL 1 MERGES (size 3 + 4 → size 7, and size 4 + 4 → size 8)

Now merging the bigger pieces.

---

#### Merge Call 4's result + Call 5's result: `[1,2,3]` and `[3,3,6,7]`  (→ Call 2)

```
left=[1,2,3],  right=[3,3,6,7]
i=0, j=0

Step 1: left[0]=1  vs  right[0]=3  →  1<3, take left
        result=[1],  i=1

Step 2: left[1]=2  vs  right[0]=3  →  2<3, take left
        result=[1,2],  i=2

Step 3: left[2]=3  vs  right[0]=3  →  3==3, take LEFT (stability)
        result=[1,2,3],  i=3

Step 4: i=3 = len(left) → left exhausted
        extend right[0:] = [3,3,6,7]
        result=[1, 2, 3, 3, 3, 6, 7]

✓ Returns: [1, 2, 3, 3, 3, 6, 7]
```

---

#### Merge Call 6's result + Call 7's result: `[2,3,4,7]` and `[2,3,5,8]`  (→ Call 3)

```
left=[2,3,4,7],  right=[2,3,5,8]
i=0, j=0

Step 1: left[0]=2  vs  right[0]=2  →  equal, take LEFT
        result=[2],  i=1

Step 2: left[1]=3  vs  right[0]=2  →  3>2, take right
        result=[2,2],  j=1

Step 3: left[1]=3  vs  right[1]=3  →  equal, take LEFT
        result=[2,2,3],  i=2

Step 4: left[2]=4  vs  right[1]=3  →  4>3, take right
        result=[2,2,3,3],  j=2

Step 5: left[2]=4  vs  right[2]=5  →  4<5, take left
        result=[2,2,3,3,4],  i=3

Step 6: left[3]=7  vs  right[2]=5  →  7>5, take right
        result=[2,2,3,3,4,5],  j=3

Step 7: left[3]=7  vs  right[3]=8  →  7<8, take left
        result=[2,2,3,3,4,5,7],  i=4

Step 8: i=4 = len(left) → left exhausted
        extend right[3:] = [8]
        result=[2, 2, 3, 3, 4, 5, 7, 8]

✓ Returns: [2, 2, 3, 3, 4, 5, 7, 8]
```

---

### FINAL MERGE (Call 1): `[1,2,3,3,3,6,7]` and `[2,2,3,3,4,5,7,8]`

This is the **root merge** — combines everything into the final answer.

```
left  = [1, 2, 3, 3, 3, 6, 7]        (size 7)
right = [2, 2, 3, 3, 4, 5, 7, 8]     (size 8)
i=0, j=0

Step  1: l[0]=1  vs r[0]=2  → 1<2, take LEFT   result=[1]           i=1
Step  2: l[1]=2  vs r[0]=2  → equal, take LEFT  result=[1,2]         i=2
Step  3: l[2]=3  vs r[0]=2  → 3>2, take RIGHT   result=[1,2,2]       j=1
Step  4: l[2]=3  vs r[1]=2  → 3>2, take RIGHT   result=[1,2,2,2]     j=2
Step  5: l[2]=3  vs r[2]=3  → equal, take LEFT  result=[1,2,2,2,3]   i=3
Step  6: l[3]=3  vs r[2]=3  → equal, take LEFT  result=[1,2,2,2,3,3] i=4
Step  7: l[4]=3  vs r[2]=3  → equal, take LEFT  result=[...,3]       i=5
Step  8: l[5]=6  vs r[2]=3  → 6>3, take RIGHT   result=[...,3]       j=3
Step  9: l[5]=6  vs r[3]=3  → 6>3, take RIGHT   result=[...,3]       j=4
Step 10: l[5]=6  vs r[4]=4  → 6>4, take RIGHT   result=[...,4]       j=5
Step 11: l[5]=6  vs r[5]=5  → 6>5, take RIGHT   result=[...,5]       j=6
Step 12: l[5]=6  vs r[6]=7  → 6<7, take LEFT    result=[...,6]       i=6
Step 13: l[6]=7  vs r[6]=7  → equal, take LEFT  result=[...,7]       i=7
Step 14: i=7 = len(left) → left exhausted
         extend right[6:] = [7, 8]
         result=[..., 7, 8]
```

**Full result built step by step:**

```
After step  1:  [1]
After step  2:  [1, 2]
After step  3:  [1, 2, 2]
After step  4:  [1, 2, 2, 2]
After step  5:  [1, 2, 2, 2, 3]
After step  6:  [1, 2, 2, 2, 3, 3]
After step  7:  [1, 2, 2, 2, 3, 3, 3]
After step  8:  [1, 2, 2, 2, 3, 3, 3, 3]
After step  9:  [1, 2, 2, 2, 3, 3, 3, 3, 3]
After step 10:  [1, 2, 2, 2, 3, 3, 3, 3, 3, 4]
After step 11:  [1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5]
After step 12:  [1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 6]
After step 13:  [1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7]
After step 14:  [1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7, 7, 8]

✓ FINAL ANSWER: [1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7, 7, 8]
```

---

## THE COMPLETE PICTURE — All Merges Together

```
ORIGINAL:  [1, 2, 3, 3, 6, 7, 3, 3, 7, 4, 2, 8, 3, 5, 2]
                          SPLIT DOWN
                          ↓
Singles:   [1][2][3][3][6][7][3] [3][7][4][2][8][3][5][2]
                          MERGE UP
                          ↓
Size 2:    [1][2,3][3,6][3,7]    [3,7][2,4][3,8][2,5]
                          ↓
Size 3/4:  [1,2,3][3,3,6,7]      [2,3,4,7][2,3,5,8]
                          ↓
Size 7/8:  [1,2,3,3,3,6,7]       [2,2,3,3,4,5,7,8]
                          ↓
FINAL:     [1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7, 7, 8]
```

---

## THREE KEY INSIGHTS FROM THIS DRY RUN

**Insight 1 — Work happens on the way UP, not down:**
```
Going DOWN = just splitting indices, O(1) per level (ignoring slices)
Going UP   = actual comparisons happen in _merge()
The split phase is setup; the merge phase is the algorithm.
```

**Insight 2 — Duplicates are handled cleanly:**
```
Input had: five 3s, two 2s, two 7s
The (left[i] <= right[j]) condition handles ties by
taking from the LEFT — this is what makes merge sort STABLE.
All five 3s end up together: [...3, 3, 3, 3, 3...]  ✓
```

**Insight 3 — The `extend` at the end is not just cleanup:**
```python
result.extend(left[i:])   # Handles remaining left elements
result.extend(right[j:])  # Handles remaining right elements
```
```
In the final merge, right had [7, 8] remaining.
extend() added both in O(1) call instead of two loop iterations.
One of these will always be empty — both can't have remainders.
```