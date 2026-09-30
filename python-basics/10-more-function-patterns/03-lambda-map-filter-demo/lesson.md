---
title: Lambda, Map, and Filter Demo
slug: lambda-map-filter-demo
order: 3
language: python
lesson_type: coding
runtime: pyodide
summary: Edit a short lambda used to transform prices.
seo_title: "Lambda, Map, and Filter Demo | Python Basics"
seo_description: Edit a short lambda used to transform prices.
seo_keywords: [python lambda, map, filter, iterators]
---

A `lambda` is a small unnamed function: `lambda price: price + 2` takes a price and returns one value. `map(function, items)` applies that function to each item; `filter(function, items)` keeps items for which it returns `True`. Both produce iterators, so `list(...)` makes their results visible. A list comprehension or loop often reads better for complex work.

The complete demo adds a fee to snack prices, then keeps prices over a threshold. Edit `main.py`: change only the fee inside the `map` lambda from `1` to `2`. Run to see `[5, 7, 9]` and `[7, 9]`, then Submit. The following exercise uses different data.

## Your Task

1. Change the `map` lambda to add `2` to each price; keep the `filter` rule unchanged.
