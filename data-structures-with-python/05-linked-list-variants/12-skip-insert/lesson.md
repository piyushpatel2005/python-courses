---
title: "Insert one tower at its supplied height"
slug: "skip-insert"
order: 12
language: "python"
runtime: pyodide
lesson_type: "coding"
summary: "Implement `insert(key, height)` with real forward-link splices at every level below height; return `True` for a new integer key and `False` for a duplicate, maintaining size and tail. Validate height first and raise `ValueError` for invalid heights without mutation."
seo_title: "Insert one tower at its supplied height | Python data structures"
seo_description: "Implement `insert(key, height)` with real forward-link splices at every level below height; return `True` for a new integer key and `False` for a duplicate, maintaining size and tail. Validate height first and raise `ValueError` for invalid heights without mutation."
seo_keywords:
  - "Python"
  - "skip insert"
  - "data structures"
---

# Insert one tower at its supplied height

The skip list now gains general insertion in any key order. Heights are explicit inputs, not random values generated during grading. This makes the exact tower arrangement reproducible and lets you check upper-level links directly.

Validate height before touching the structure: it must be a non-boolean integer between one and max_level inclusive. Then obtain the predecessor array. If the base successor already has the requested key, return False without replacing its node, changing its height, or changing size. An invalid height still raises even when the key is a duplicate because validation comes first.

For a new key, allocate one node with the requested number of forward slots. At each participating level, save the predecessor's old successor into the new node's slot before redirecting the predecessor to the new node. This is the same splice pattern as singly linked insertion, repeated across one tower. Levels at or above the node's height remain unchanged.

If the new node has no level-zero successor, it is the new tail. This also handles insertion into an empty list. Size increases once per key, not once per level. The sentinel remains the head regardless of which real key becomes smallest.

Do not store a parallel collection of keys as the implementation. Python lists here hold link slots and predecessor references; the ordered data itself lives in the linked nodes. Search must discover inserted keys through those links.

## Trace it first

Start with keys 14(h1) and 43(h2). Insert 28(h3). Level zero becomes 14,28,43; level one becomes 28,43; level two becomes 28 alone. All references to 28 on those levels lead to one node. Inserting 28 again with height one leaves that original tower unchanged.

## Cost

Insertion costs predecessor search plus O(h) splicing for height h. Worst-case time is O(n+L), with O(L) search space and O(h) new storage. Expected O(log n) time requires randomized geometric heights and a level cap suitable for n.

## Operation contract

Implement `insert(key, height)` with real forward-link splices at every level below height; return `True` for a new integer key and `False` for a duplicate, maintaining size and tail. Validate height first and raise `ValueError` for invalid heights without mutation.

![Skip insert. Fixed level data before: L0 (4,9,15,22), L1 (9,22), L2 (22). Insert 12 with height 2: update(0) = 9; update(1) = 9; level 2 stays unchanged. L0: 9 → 12 → 15; L1: 9 → 12 → 22. Return True. First insertion also sets tail; duplicate returns False.](linked-list-variants-skip-insert-trace.svg)

Skip insert. Fixed level data before: L0 [4,9,15,22], L1 [9,22], L2 [22]. Insert 12 with height 2: update[0] = 9; update[1] = 9; level 2 stays unchanged. L0: 9 → 12 → 15; L1: 9 → 12 → 22. Return True. First insertion also sets tail; duplicate returns False.

## Your Tasks

1. Reject heights outside `1..max_level`, including booleans and non-integers, before searching.
2. Return `False` for an existing key without replacing its tower or changing the list.
3. Splice a new node at each level below its height; update tail and size, then return `True`.

## Run and check

Edit `SkipList.insert` in `main.py`. The predecessor lookup and candidate are supplied; the final `return True` is only a placeholder until task 3. Complete each task in order and Submit after each change. The earlier definitions and Run probe are supplied. Run the completed operation to see:

```text
3 24 39
```

Press **Submit** to check the tasks on additional inputs and boundary cases.
