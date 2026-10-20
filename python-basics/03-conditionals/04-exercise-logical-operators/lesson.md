---
title: "Exercise: Check Store Stock"
slug: exercise-logical-operators
order: 4
language: python
lesson_type: coding
summary: "Combine grocery-stock and store-opening checks with and, or, and not."
seo_title: "Python Logical Operators Exercise | Python Basics"
seo_description: "Use and, or, and not to check flour, milk, and whether a store is open."
seo_keywords: [python logical operators exercise, boolean expressions, grocery stock]
---

The grocery store can take an order only when it has enough flour **and** at least one milk carton. It also needs to know when either item needs restocking. The supplied `store_closed` boolean records whether the shop is shut.

In `main.py`, the quantities are counts of bags and cartons. `enough_flour` is already calculated. Replace the other three placeholders with expressions that depend on the supplied values; the tests will also try different stock levels and opening states.

## Your Tasks

1. Set `can_take_order` using `and` with `enough_flour` and `milk_cartons >= 1`.
2. Set `needs_restock` using `or` with `flour_bags < 4` and `milk_cartons == 0`.
3. Set `store_open` using `not` to reverse `store_closed`.

Press **Run** and then **Submit**. With the supplied values, the four lines (including `enough_flour`) print `True`, `True`, `False`, `False`. Each completed expression can pass on its own. The next lesson uses `if` to act on a check.
