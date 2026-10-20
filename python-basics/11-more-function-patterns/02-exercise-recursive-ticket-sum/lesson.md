---
title: "Add daily deliveries recursively"
slug: exercise-recursive-ticket-sum
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: Sum a short list of daily delivery counts with a recursive function.
seo_title: "Recursive List Sum Exercise | Python Basics"
seo_description: Write a recursive sum that stops at an empty list and adds each daily delivery count.
seo_keywords: [python recursive sum, list slicing, base case]
---

A coordinator records how many supply boxes arrive each day. To total a short list recursively, add the first day's count to the total for the remaining days. An empty list contributes zero and stops the calls: `[4, 2]` becomes `4 + 2 + 0`.

Use `[0]` to read the first count and `[1:]` to pass along a shorter list. This makes a useful recursion exercise; for a large list, a loop or `sum()` avoids making many calls and copies.

## Your Task

1. Complete `delivery_total(daily_deliveries)` so an empty list returns `0`; otherwise return the first count plus `delivery_total(daily_deliveries[1:])`.

Edit `main.py`, press **Run** to check for `Boxes delivered: 6`, and then **Submit**.
