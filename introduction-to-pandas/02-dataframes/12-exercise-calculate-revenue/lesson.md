---
title: "Exercise: Calculate market revenue"
slug: exercise-calculate-revenue
order: 12
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Build a derived column for a community market data desk."
seo_title: "Exercise: Calculate market revenue | Pandas for beginners"
seo_description: "Build a derived column for a community market data desk."
seo_keywords: ["pandas", "Python data analysis", "build a derived column"]
---
Finish the market desk’s first table report. Add a `revenue` column by multiplying the supplied `sold` and `price` columns row by row. Return the table with its existing columns and row labels intact; do not hard-code sample totals.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your work.

## Your Task

1. Make `with_revenue(table)` return a table with a `revenue` column equal to `sold * price` for each row.
