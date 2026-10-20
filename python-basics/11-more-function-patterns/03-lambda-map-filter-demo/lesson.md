---
title: "Adjust prices with map and filter"
slug: lambda-map-filter-demo
order: 3
language: python
lesson_type: coding
runtime: pyodide
summary: Adjust delivery prices with a lambda, then filter the resulting prices.
seo_title: "Python Lambda, Map, and Filter | Python Basics"
seo_description: Use a short lambda to adjust each price with map and select prices with filter.
seo_keywords: [python lambda, map, filter, price list]
---

A shop adds a delivery fee to each listed price, then checks which totals exceed $6. A `lambda` is a short function written as one expression: in `lambda price: price + 1`, `price` is the input and the expression after the colon gives the result.

`map(function, items)` applies a function to every item. `filter(function, items)` keeps an item if the function returns a true value. Both return iterators; `list(...)` collects the results for printing. Here the filter reads the **adjusted** prices, not the original ones.

## Your Task

1. Change the fee in the `map` lambda from $1 to $2. Leave the filter rule unchanged.

Edit `main.py`, press **Run**, and check for `With delivery: [5, 7, 9]` and `Over $6: [7, 9]`. Then **Submit**. For a longer calculation, an ordinary function or loop may be easier to read.
