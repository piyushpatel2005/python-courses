---
title: "Recursive sum without slicing"
slug: recursive-sum
order: 3
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `recursive_sum(values)` using an index-based recursive helper, no slices or `sum`; reject inputs longer than 100."
seo_title: "Recursive sum without slicing | Python data structures"
seo_description: "Practice recursive sum through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - recursive sum
  - data structures practice
---

# Recursive sum without slicing

A recursive sum can separate the next reading from the remaining readings. Use an index to describe the remaining region instead of creating a new sliced list at every call. This keeps the representation small and leaves the caller's list unchanged.

## Describe a suffix by its start

The public function `recursive_sum(values)` receives a reference to the input. Inside it, define `total_from(index)` to mean "the sum from this index through the end." When index equals the list length, the remaining region is empty and its sum is zero. Otherwise combine the current value with the answer starting one position later.

For `[6, -2, 5]`, the first call waits for the sum of `[-2, 5]`, but no new list is needed. The next index identifies that suffix within the same list. The last real value waits for the empty suffix; then returns combine 5, -2, and 6 in reverse call order.

```python
readings = [9, 4, -1]
start = 1
print(readings[start])       # 4
print(start == len(readings))  # False
```

A valid index can equal the length only as a stopping boundary; reading `values[len(values)]` would fail. Test that boundary before indexing. The nested helper can read `values` from its enclosing function, just as the previous helper shared its event list.

![Recursive sum: sum_at(0): wait for 6 + sum_at(1); sum_at(1): wait for 2 + sum_at(2); sum_at(2): wait for 5 + sum_at(3); sum_at(3): return 0 (i = length). Unwind: return 0, 5 + 0 = 5, 2 + 5 = 7, 6 + 7 = 13. Input \[6, 2, 5\] is unchanged. Index-based recursion: no slices are copied.](recursion-recursive-sum-trace.svg)

Here `sum_at` illustrates your `total_from` helper on different readings, with each return completing one waiting addition.

## The cost of the representation

There are n + 1 helper calls and one addition per element, giving O(n) time under the bounded-integer cost model. Stack space is O(n). Slicing `values[1:]` at each level would copy progressively shorter lists and add quadratic total copying work, so use indices instead. Do not call `sum` or replace recursion with iteration in this exercise.

Accept lists of integers, including negatives and duplicates. Empty input returns zero. Reject lists longer than 100 with `ValueError` so practice stays within a small safe recursion depth. This is a fresh standalone implementation, not an extension of the tracing function. The same "base before access" habit will matter when a later recursive search has an empty candidate interval.

## Build in small steps

The helper definition, end-boundary condition, and initial helper call are supplied. Reject oversized input first, give the empty suffix its base answer next, and only then implement the recursive combination. The validation check never needs a completed sum.

## Your Tasks

1. Raise `ValueError` if the list has more than 100 values.
2. Return zero when the helper reaches the end boundary.
3. Add the current value to the recursive sum starting one index later.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
