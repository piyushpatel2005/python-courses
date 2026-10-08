---
title: Count values and rows
slug: count-vs-size
order: 1
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: The desk compares receipts by zone.
seo_title: Count values and rows | Introduction to Pandas
seo_description: The desk compares receipts by zone.
seo_keywords:
- pandas
- count vs size
- community market data
---

# Count values and rows

The desk compares receipts by zone. `mean` averages known amounts; `sum` totals them; `count` counts nonmissing amounts; `size` counts all rows. The printed fixture has one unrecorded amount.

![Count skips missing amounts; size retains rows](count-size.svg)

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.

## Your Tasks

1. Change the second calculation in `zone_counts` from `count()` to `size()`.
