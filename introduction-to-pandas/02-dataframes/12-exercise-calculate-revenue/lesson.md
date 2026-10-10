---
title: "Exercise: Calculate market revenue"
slug: exercise-calculate-revenue
order: 12
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Return a market table with revenue calculated for every row."
seo_title: "Exercise: Calculate market revenue | Pandas for beginners"
seo_description: "Return a market table with revenue calculated for every row."
seo_keywords: ["pandas", "Python data analysis", "build a derived column"]
---

Finish the desk's first table report by adding revenue for each stall. Multiply the supplied `sold` and `price` columns rather than typing the example's totals into your function.

Return the table with its original columns, values, and row labels still present. You may add the column directly to `table`. If you prefer to leave the caller's table untouched, start with `result = table.copy()`, add the column to `result`, then return it. `.copy()` makes a separate table for this calculation; the reference solution uses that approach. Either approach is accepted here.

## Your Task

1. Make `with_revenue(table)` return a DataFrame with a `revenue` column equal to `sold * price` for each row, preserving the existing data and labels.

Edit `main.py`, **Run**, and look for revenue `6` for tea and `20` for jam. **Submit** checks other counts, prices, and extra columns.

After the quiz, you will choose which rows and columns belong in a report rather than returning the whole table.
