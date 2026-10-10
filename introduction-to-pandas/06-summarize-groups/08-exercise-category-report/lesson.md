---
title: 'Exercise: Name category measures'
slug: exercise-category-report
order: 8
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Build category revenue and entry-count columns with named aggregation."
seo_title: 'Exercise: Name category measures | Introduction to Pandas'
seo_description: "Build category revenue and entry-count columns with named aggregation."
seo_keywords:
  - pandas
  - exercise category report
  - community market data
hints:
  - 'Start with groupby("category").agg(revenue=("amount", "sum")), then add the entries keyword.'
---

# Exercise: Name category measures

The category report needs total revenue and an entry count. Use named aggregation to give the result columns those exact meanings.

Build `revenue` first with the sum of amount, then add `entries` using size. Keep the columns in that order and category labels as the index. Craft has revenue 5 and 2 entries in the preview, even though one amount is missing. A missing amount is not a reason to drop the entry.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Return a grouped report with a revenue column containing each category's amount sum.
2. Add an entries column containing each category's row count, after revenue.
