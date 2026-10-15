---
title: "Count linear work"
slug: count-linear-work
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `sum_with_work(values)` with an explicit loop, returning `(total, visits)` with one visit per processed value."
seo_title: "Count linear work | Python data structures"
seo_description: "Practice count linear work through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - count linear work
  - data structures practice
---

# Count linear work

A sensor report adds every reading, but a total alone hides how much work it did. Return a work counter beside the total so you can connect a loop to its growth rate. The counter measures a chosen operation, not elapsed seconds.

## Define the unit before counting

Count one visit whenever the loop processes an input element. Start the total and visit count at zero. On each iteration add the reading to the running total and increase the count once. The invariant is that the total equals the sum of readings already visited, and the counter equals the number of those readings.

```python
visits = 0
for color in ["blue", "gold", "white"]:
    visits += 1
print(visits)  # 3
```

The strings are irrelevant to this example's work count: three entries cause three visits. In the exercise, a negative reading changes the sum but still costs one visit. Empty input requires no visits and has total zero. Duplicates also count separately because they occupy separate positions.

## From counts to Big O

For n readings, the body runs n times. Loop setup and the final return add fixed work, so a model such as `a*n + b` describes the total. O(n), pronounced "order n," describes an upper growth bound after ignoring constant factors and fixed overhead. It is not the number you return from this function. Return the measured integer count, not the text `"O(n)"`.

Use an explicit loop rather than `sum` plus `len`; the exercise is to connect the counter to the work you perform. Do not mutate the readings. The algorithm needs only a running total and a counter, so auxiliary space is O(1), excluding the input. Arithmetic is treated as constant work here for bounded-size numbers. Python integers can grow arbitrarily large, and their addition cost depends on their size when that assumption does not hold. A single exponentiation expression can also perform substantial work; one written operator is not automatically one constant-time operation.

The parameter hint `Iterable[int]` means an object that yields integers in a loop, such as a list or iterator. It is imported from `collections.abc`; the operation does not need indexed access or a known length.

## Build in small steps

The zeroed accumulators, loop, and tuple return are supplied. First make the total correct; then count the visits in the same loop. Returning both fields is setup, not an extra task.

## Your Tasks

1. Add each visited value to `total`.
2. Increase `visits` once per loop iteration.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
