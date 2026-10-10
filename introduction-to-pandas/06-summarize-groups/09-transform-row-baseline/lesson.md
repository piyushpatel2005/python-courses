---
title: Return a baseline per row
slug: transform-row-baseline
order: 9
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Repeat each zone mean at its original rows with transform."
seo_title: Return a baseline per row | Introduction to Pandas
seo_description: "Repeat each zone mean at its original rows with transform."
seo_keywords:
  - pandas
  - transform row baseline
  - community market data
hints:
  - 'Use transform rather than mean() alone when you need one result per original row.'
---

# Return a baseline per row

A summary gives one result per zone. This report instead needs a comparison value beside every original sale. `transform("mean")` calculates each group mean and repeats it at the rows that belong to that group. The returned Series keeps the original index and row order.

North amounts 4 and 8 have a mean of 6, so the first two rows both receive 6. South receives 9. The starter currently repeats the group sum, giving 12 for each North row. Change the operation and compare those two rows. You will subtract this kind of baseline in the next exercise.

![North mean 6 returns to rows 0 and 1, and South mean 9 returns to row 2](group-mean-per-row.svg)

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Change the operation in `zone_baseline` from `sum` to `mean`.
