---
title: "Exercise: Write a stock summary"
slug: exercise-write-receipt
order: 4
language: python
lesson_type: coding
runtime: pyodide
summary: "Label stock counts and total the units in a dictionary."
seo_title: "Exercise: Write a stock summary | Python Basics"
seo_description: "Label stock counts and total the units in a dictionary."
seo_keywords: [python basics, python collections, beginner python]
---

A stock sheet records how many units of each item are available. Make one readable line per product, then add up the units. This is a count of physical items, not a price in dollars.

Use `stock_counts.items()` for the lines: each pair supplies a product name and its count. Use `stock_counts.values()` for the total. The starter supplies an empty `lines` list and a zero total. Edit `main.py`, **Run** to inspect both results, then **Submit**.

## Your Tasks

1. In the first loop, append a `<product>: <count> in stock` string for each entry to `lines`.
2. In the second loop, add each count to `total_units`.
