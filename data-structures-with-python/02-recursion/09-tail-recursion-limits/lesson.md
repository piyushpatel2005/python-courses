---
title: "Tail recursion still uses stack frames"
slug: tail-recursion-limits
order: 9
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `tail_sum(n, accumulated=0)` by returning a recursive call with updated accumulator; validate n and return accumulated at zero."
seo_title: "Tail recursion still uses stack frames | Python data structures"
seo_description: "Practice tail recursion limits through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - tail recursion limits
  - data structures practice
---

# Tail recursion still uses stack frames

A tail-recursive function returns its recursive call directly. It carries the completed work into the next call as an accumulator instead of waiting to combine a result afterward. That changes the shape of the function, but it does not give Python a constant-stack guarantee.

## Carry the answer so far

Implement `tail_sum(n, accumulated=0)` for the sum of the integers one through n plus an optional starting amount. When n is zero, return the accumulator. Otherwise move n into the accumulator and recurse with n - 1. The invariant is that the accumulator plus the still-unprocessed integers equals the requested final result.

For a starting amount of ten and n = 3, the states are `(3, 10)`, `(2, 13)`, `(1, 15)`, and `(0, 16)`. Nothing remains to add after the recursive call returns: its result can be returned directly. Contrast that with `n + recursive_call(n - 1)`, where addition is still waiting in each frame.

```python
remaining, completed = 4, 20
remaining, completed = remaining - 1, completed + remaining
print(remaining, completed)  # 3 24
```

This snippet demonstrates one state transition using the old remaining value. Your function repeats the transition through calls and handles the base case.

## Do not rely on optimization

Some languages can reuse a frame for a tail call. Python does not guarantee tail-call elimination. This function therefore still uses O(n) stack frames and O(n) calls, even though the call is the final action. A loop can carry the same two variables with constant auxiliary variable count and avoids recursion-depth limits.

This fresh variation is for recognizing the pattern, not for processing enormous inputs. Use the supplied `_check_n` to restrict n to integers from zero through 100, and keep the accumulator an integer. Return the caller's accumulator unchanged when n is zero. Do not reset it at recursive steps or ignore a nonzero initial amount. As in earlier lessons, numeric O(1) storage and arithmetic assumptions refer to bounded-size integers, not unlimited exact-integer bit costs.

## Build in small steps

The base-case condition is supplied. Test its return with nonzero accumulators before implementing the transition. The final change must return the recursive call itself, with no pending addition afterward.

## Your Tasks

1. Validate n with `_check_n(n)` before doing any work.
2. Return the current accumulator when n is zero.
3. Return the recursive call with n reduced and its value moved into the accumulator.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
