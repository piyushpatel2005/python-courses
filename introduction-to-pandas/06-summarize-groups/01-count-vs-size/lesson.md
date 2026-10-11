---
title: Count values and rows
slug: count-vs-size
order: 1
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Compare known-value counts with row counts after grouping by zone."
seo_title: Count values and rows | Introduction to Pandas
seo_description: "Compare known-value counts with row counts after grouping by zone."
seo_keywords:
  - pandas
  - count vs size
  - community market data
hints:
  - 'Keep the first count() call; use size() for the second result.'
---

# Count values and rows

The Community Data Desk can now combine records. To compare zones, it needs fewer rows: one summary per zone. `a.groupby("zone")` collects rows with the same zone label. Selecting `["amount"]` chooses what to measure; calling a method such as `.sum()` computes one result for each group. This is often called split, apply, combine.

For North, the amounts are 10 and a missing value. `sum()` gives 10 and `mean()` gives 10, because both use the known amounts. `count()` gives 1 known amount, while `size()` gives 2 rows. South has one row with amount 6.

The function returns a pair of Series: known-value counts first, row counts second. Change only the second calculation. Both Series use zone labels as their index, sorted by default.

Our examples use observed groups (`observed=True`) and omit missing grouping keys (`dropna=True`). A missing amount is different from a missing zone: it still belongs to a group. A categorical column has a predefined set of possible labels; observed=True leaves unused labels out of these summaries. Setting this explicitly keeps that choice consistent across pandas versions.

![Count skips missing amounts; size retains rows](count-size.svg)

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Change the second calculation in `zone_counts` from `count()` to `size()`.

## Learn more

The pandas [grouping guide](https://pandas.pydata.org/docs/user_guide/groupby.html) gives the full argument details and more examples.
