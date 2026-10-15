---
title: "Reverse with two inward pointers"
slug: reverse-two-pointers
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `reverse_in_place(values)` with two inward-moving indices and swaps, returning the original list without slicing or reversal built-ins."
seo_title: "Reverse with two inward pointers | Python data structures"
seo_description: "Practice reverse two pointers through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - reverse two pointers
  - data structures practice
---

# Reverse with two inward pointers

Reverse a route's list of stops without creating a second list. Two indices can identify the next unmatched pair: one begins at the left edge and the other at the right. Swapping that pair puts both values into their final positions.

## A new sequence exercise

The modeled array project is complete. This lesson starts a fresh function over an ordinary Python list rather than extending `Array`. `reverse_in_place(values)` must mutate the caller's list and return that same list. The function accepts integer values, including duplicates and negatives; positions, not value uniqueness, determine the swaps.

Maintain the invariant that positions outside the two indices are already correct. Swap the two current values, advance the left index, and retreat the right index. Stop when the indices meet or cross. For an odd-length list, the middle value needs no swap. For an empty list, the initial right index is -1, so the loop must not enter.

```python
stops = ["gate", "pond", "hill"]
stops[0], stops[2] = stops[2], stops[0]
print(stops)  # ['hill', 'pond', 'gate']
```

Parallel assignment preserves both old values until the swap is complete. A temporary variable is equally valid. Two ordinary assignments without a saved value would overwrite one endpoint and lose it. The example has only one pair; your loop must handle every pair for arbitrary list lengths.

![Reverse \[3,7,4,8,2\] by swapping indices 0 and 4, then 1 and 3. States are \[2,7,4,8,3\] and \[2,8,4,7,3\]. Pointers meet at the unchanged middle value.](arrays-and-sequences-reverse-two-pointers-trace.svg)

Each inward step settles two positions, and the pointers stop when they reach the unchanged middle value.

## Mutation and cost

A caller may hold another reference to the list. That alias must see the reversed order because the original object changes. Returning a reversed copy would print the expected values but violate this contract. Leave empty and singleton lists as the same objects, not newly created replacements.

The loop makes floor(n/2) swaps, so time is O(n) and auxiliary space is O(1). Do not use `reverse`, `reversed`, sorting, or slicing in this exercise; those would hide the pointer movement or allocate another container. The two-pointer pattern will recur in later problems whenever each step can settle work at opposite ends of a region.

## Build in small steps

The initial indices, loop condition, and same-list return are supplied. First implement one swap. The temporary break keeps an unfinished loop safe; replace it with pointer movement only after the swap works.

## Your Tasks

1. Swap the values at the current left and right indices.
2. Replace the safe `break` with inward updates to both indices.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
