---
title: "Recursive binary search from sorted halves"
slug: recursive-binary-search
order: 10
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `binary_search_recursive(values, target)` with recursive half-open interval halving; return any matching index or `None`."
seo_title: "Recursive binary search from sorted halves | Python data structures"
seo_description: "Practice recursive binary search through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - recursive binary search
  - data structures practice
---

# Recursive binary search from sorted halves

A sorted sequence lets you rule out many positions with one comparison. Binary search maintains a candidate interval, inspects its middle value, and searches only the half that could still contain the target. This lesson teaches the search itself; you do not need a later search module to implement it.

## Why sorted order matters

Use an ascending, nondecreasing list of integers. If its middle value is smaller than the target, every value to the left is also too small. If the middle value is larger, every value to the right is too large. Equality ends the search. An unsorted input does not justify either conclusion, so sorted input is a precondition, not something the function fixes by sorting.

Keep half-open bounds `[low, high)`: low is included and high is excluded. Start at zero and the list length. An interval is empty when low is at least high. Check that base case before reading the middle. Otherwise choose `(low + high) // 2`, then recurse into `[mid + 1, high)` or `[low, mid)`. Excluding mid after a miss guarantees progress, including for a one-element interval.

```python
catalog = [3, 8, 12, 19, 27]
low, high = 0, len(catalog)
middle = (low + high) // 2
print(middle, catalog[middle])  # 2 12
```

Searching this example for 19 discards the middle and everything before it. You still use original-list indices; slicing would create a new list and make indices harder to interpret.

![Recursive binary search for 17 in \[2,5,8,11,14,17,20\] probes index 3 in \[0,7), then index 5 in \[4,7), and returns 5. Empty intervals return None without reading a cell.](recursion-recursive-binary-search-trace.svg)

Discarding the first midpoint moves the included left boundary to index 4 while the excluded right boundary stays at 7.

## Return a location or a clear miss

Write a fresh function `binary_search_recursive(values, target)` returning an index whose value equals the target, or `None` if absent. With duplicates, any matching index is valid. A nested helper can keep the list and target in scope while receiving only low and high. Do not sort, scan, use `index`, or slice: implement the recursive halving algorithm.

At most one half is searched per call, so comparisons and stack space are O(log n), with constant work for empty input. This assumes bounded-cost integer comparisons and list indexing. Input sortedness is not checked inside the function because a full validation scan would add O(n) work. The caller must provide sorted data, and the function leaves that data unchanged.

## Build in small steps

The helper, midpoint calculation, comparisons, and initial bounds are supplied. Complete the empty case and equality case before the two directional recursive returns. Each direction has its own check; the final check also covers misses and duplicates.

## Your Tasks

1. Return `None` when the candidate interval is empty.
2. Return `mid` when its value equals the target.
3. Recurse into `[low, mid)` when the midpoint is too large.
4. Recurse into `[mid + 1, high)` when the midpoint is too small.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
