---
title: "Echo Tower: Tune the Frequencies"
slug: lambda-map-filter-demo
order: 3
language: python
lesson_type: coding
runtime: pyodide
summary: Use lambda, map, and filter to tune beacon frequencies.
seo_title: "Echo Tower: Tune the Frequencies | Python Basics"
seo_description: Use lambda, map, and filter to tune beacon frequencies.
seo_keywords: [python lambda, map, filter, Echo Tower]
---

Ari's receiver adds a small adjustment to each frequency, then keeps frequencies above the tower's threshold. A `lambda` is a short unnamed function. `map(function, items)` transforms each item; `filter(function, items)` keeps those meeting a condition. Both return iterators, so `list(...)` lets you see the values.

In `main.py`, change **only** the adjustment inside the `map` lambda from `1` to `2`. Run to see `Tuned: [5, 7, 9]` and `Strong: [7, 9]`, then Submit. A loop or comprehension is often clearer for a larger operation; the next exercise uses this compact pattern on different beacon data.

## Your Task

1. Change the `map` lambda to add `2` to every frequency, leaving the `filter` rule unchanged.
