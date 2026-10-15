---
title: "Count halving work"
slug: count-halving-work
order: 7
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `halving_trace(n)` with repeated integer halving, returning the pre-reduction sizes and reduction count; reject negative n."
seo_title: "Count halving work | Python data structures"
seo_description: "Practice count halving work through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - count halving work
  - data structures practice
---

# Count halving work

A candidate region can sometimes be reduced by half at each step. Before applying that idea to searching, practice the shrinking loop itself. Record the remaining size so both progress and the stopping condition are visible.

## Shrink an integer region

`halving_trace(n)` accepts a nonnegative integer. While the current size is greater than one, record it, count one reduction, and replace it with its integer half. Python's `//` discards the fractional part for these nonnegative inputs. An odd size therefore rounds down. The final zero or one is not recorded because it causes no reduction.

For a region of size 13, the sizes before reductions are 13, 6, and 3. After the third reduction the size is 1, so the loop stops. Each transition must make the size smaller. Testing `size >= 1` instead would add an unwanted transition from one to zero; using ordinary `/` would change the state to floating-point values.

```python
size = 11
print(size // 2)  # 5
print(1 // 2)     # 0
```

## Growth is about repeated reduction

Doubling a positive starting size adds roughly one reduction rather than doubling the work. This is logarithmic growth, O(log n), for n greater than one. The small cases n = 0 and n = 1 take constant setup work and no loop iterations. We do not evaluate a logarithm of zero to handle them.

Return `(sizes, reductions)`, where `sizes` is the trace list. Trace storage is O(log n); the loop without a stored trace would need only O(1) auxiliary space. Reject negative n with `ValueError`, because a negative candidate count has no meaning in this model. Use a real `while` loop, not a logarithm formula: the rounding decisions and boundary are part of the practice. As before, the arithmetic cost model assumes bounded-size integers rather than arbitrarily enormous integers.

## Build in small steps

The loop condition and result tuple are supplied. Its temporary `break` prevents an unfinished loop from running forever. Record a size first; then replace the break with the progress updates. The first trace check needs only the initial entry, while the last check checks the complete sequence.

## Your Tasks

1. Raise `ValueError` when n is negative.
2. Append the current size before reducing it.
3. Replace the safe `break` with one count increment and one integer halving.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
