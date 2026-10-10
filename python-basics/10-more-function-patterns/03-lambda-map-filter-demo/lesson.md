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

The receiver adjusts each frequency, then keeps only strong signals. The starter uses a lambda, a short function written as a single expression. In `lambda value: value + 1`, `value` is the input and the expression after the colon supplies the result.

`map(function, items)` applies the function to each item. `filter(function, items)` keeps an item when the function returns a true value. Both produce iterators; wrapping them in `list(...)` collects their values so you can print them.

In `main.py`, change only the adjustment in the `map` lambda from `1` to `2`. Run should show `Tuned: [5, 7, 9]` and `Strong: [7, 9]`. Leave the filter rule unchanged, then Submit. For a longer operation, a regular function or loop may be easier to read.

## Your Task

1. Change the `map` lambda to add `2` to every frequency, leaving the `filter` rule unchanged.
