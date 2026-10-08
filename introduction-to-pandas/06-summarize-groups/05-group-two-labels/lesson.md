---
title: Group on two labels
slug: group-two-labels
order: 5
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: The desk already totals donations by zone.
seo_title: Group on two labels | Introduction to Pandas
seo_description: The desk already totals donations by zone.
seo_keywords:
- pandas
- group two labels
- community market data
---

# Group on two labels

The desk already totals donations by zone. Grouping on `["zone", "day"]` creates a group for every observed combination and a two-level index; grouping on zone alone blends days.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.

## Your Tasks

1. Change the grouping key in `daily_gifts` to `["zone", "day"]`.
