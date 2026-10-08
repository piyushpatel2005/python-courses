---
title: Return a baseline per row
slug: transform-row-baseline
order: 9
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: The desk compares each sale with its zone baseline.
seo_title: Return a baseline per row | Introduction to Pandas
seo_description: The desk compares each sale with its zone baseline.
seo_keywords:
- pandas
- transform row baseline
- community market data
---

# Return a baseline per row

The desk compares each sale with its zone baseline. Aggregation shrinks groups; `transform("mean")` broadcasts each group mean to its original rows, retaining the row index.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.

## Your Tasks

1. Change the operation in `zone_baseline` from `sum` to `mean`.
