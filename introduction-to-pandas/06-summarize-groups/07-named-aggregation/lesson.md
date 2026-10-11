---
title: Name grouped results
slug: named-aggregation
order: 7
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Name grouped report columns and distinguish an average from a sum."
seo_title: Name grouped results | Introduction to Pandas
seo_description: "Name grouped report columns and distinguish an average from a sum."
seo_keywords:
  - pandas
  - named aggregation
  - community market data
hints:
  - 'In the average tuple, change the operation string without changing the input column.'
---

# Name grouped results

The desk wants one table with readable column headings instead of several separate Series. `.agg()` can calculate named results in one call. In `average=("total", "mean")`, `average` is the output column name, `total` is the input column, and `mean` is the operation.

The starter incorrectly sums the amounts under a heading called average. Lark has amounts 4 and 10, so its average should be 7, not 14. Change that operation and leave `orders=("total", "size")` alone: it counts rows even if a total is missing. The result has vendor labels as its index and average and orders as columns.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Change `average=("total", "sum")` to use `mean`.
