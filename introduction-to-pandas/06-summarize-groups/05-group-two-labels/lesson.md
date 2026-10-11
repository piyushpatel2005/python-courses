---
title: Group on two labels
slug: group-two-labels
order: 5
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Sum donations separately for each observed zone and day pair."
seo_title: Group on two labels | Introduction to Pandas
seo_description: "Sum donations separately for each observed zone and day pair."
seo_keywords:
  - pandas
  - group two labels
  - community market data
hints:
  - 'Pass the two grouping column names as one list, in zone-then-day order.'
---

# Group on two labels

A zone total hides which day a donation arrived. Pass a list of column names to `groupby` to keep the zone and day together as the group key.

`["zone", "day"]` produces a two-level index, also called a MultiIndex: each result is labeled by a pair such as (North, Fri). The printed output may leave a repeated zone label blank to save space; that row still belongs to the zone above it.

After the change, North has separate totals of 5 for Friday and 7 for Saturday instead of one total of 12. South has only Friday. With `observed=True`, grouping includes combinations present in the data, not invented zero rows for every possible pair.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Change the grouping key in `daily_gifts` to `["zone", "day"]`.
