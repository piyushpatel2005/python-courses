---
title: "Find supplies within a budget"
slug: exercise-clean-badge-names
order: 4
language: python
lesson_type: coding
runtime: pyodide
summary: Apply a $1 coupon with map and filter the resulting supply prices by budget.
seo_title: "Map and Filter Price Exercise | Python Basics"
seo_description: Practice map and filter by discounting supply prices and selecting those within a budget.
seo_keywords: [python map filter exercise, lambda prices, budget]
---

A community workshop has a $1 coupon for each supply item. After the discount, the coordinator wants a list of prices at or below $8. Unlike the delivery-fee example, this calculation lowers each price before filtering it.

Use `map` with a lambda to apply the coupon, then `filter` with another lambda on the discounted list. Wrap each result in `list(...)`; otherwise you would hold an iterator rather than the printable list requested here. An item costing exactly $8 after the coupon belongs in the result.

## Your Tasks

1. Set `discounted_prices` with `list(map(...))` and a lambda that subtracts `1` from each price in `supply_prices`.
2. Set `within_budget` with `list(filter(...))` and a lambda that keeps values at or below `8` from `discounted_prices`.

Edit `main.py`, press **Run** to compare both lists, then **Submit**. You can use ordinary loops instead of these optional patterns in the final project.
