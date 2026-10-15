---
title: "Base and recursive cases"
slug: base-and-recursive-cases
order: 1
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `steps_to_zero(n)` with a base case at zero and recursion on n - 1; validate with the supplied `_check_n`."
seo_title: "Base and recursive cases | Python data structures"
seo_description: "Practice base and recursive cases through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - base and recursive cases
  - data structures practice
---

# Base and recursive cases

A recursive function solves a problem by calling itself with a smaller problem. Build a function that counts how many one-step reductions separate a nonnegative integer from zero. The answer is familiar; the purpose is to make the calls and returns correct.

## Stop before calling again

Every recursive algorithm needs a base case with a direct answer and a recursive case that moves toward it. Here zero needs zero reductions. A positive value needs one reduction, followed by however many reductions the smaller value needs. The smaller argument must be n - 1, not n, or the function would keep repeating the same problem.

For an input of three, the pending questions are "one plus the answer for two," "one plus the answer for one," and "one plus the answer for zero." Zero returns directly. The waiting additions then finish in reverse order. Each function call has its own local n; changing an argument for a new call does not overwrite the caller's local variable.

```python
def describe_base(value: int) -> str:
    if value == 0:
        return "stop here"
    return "a smaller problem is needed"

print(describe_base(0))  # stop here
```

![Base and recursive cases: count(3): wait for 1 + count(2); count(2): wait for 1 + count(1); count(1): wait for 1 + count(0); count(0): return 0 (base). Unwind: return 0, return 1, return 2, return 3. Nonnegative integer contract: every call reduces n by one; n = 0 stops.](recursion-base-and-recursive-cases-trace.svg)

The illustrative `count` calls follow the same reduction as `steps_to_zero`: the zero base answer lets each waiting addition finish.

## A small, safe first recursion

Complete `steps_to_zero(n)` using a recursive call, rather than simply returning n or using a loop. The supplied `_check_n` helper accepts integers from zero through 100, raises `TypeError` for other types, and raises `ValueError` outside that range. Call it before choosing a case. This deliberate bound keeps the exercise well below typical stack limits; it is not a mathematical restriction on counting.

There are n + 1 calls, including the base case. Runtime is O(n) and the call stack uses O(n) space even though each call has only a small amount of local state. Python does not guarantee tail-call elimination, so recursive calls are not free jumps. Keep the examples small and do not change the recursion limit. The next lesson will make entry and return order visible.

## Build in small steps

The base-case branch is already placed before the recursive case. Each task changes one part of the function: validation, the direct base answer, then the smaller recursive call and its combination.

## Your Tasks

1. Validate n with `_check_n(n)` before doing any work.
2. Return zero reductions for n = 0.
3. Return one plus the recursive answer for n - 1.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
