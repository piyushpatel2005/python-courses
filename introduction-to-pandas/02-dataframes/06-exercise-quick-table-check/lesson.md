---
title: "Exercise: Check the new delivery"
slug: exercise-quick-table-check
order: 6
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Table previews and summaries for a community market data desk."
seo_title: "Exercise: Check the new delivery | Pandas for beginners"
seo_description: "Table previews and summaries for a community market data desk."
seo_keywords: ["pandas", "Python data analysis", "table previews and summaries"]
---
A fresh delivery table can have any number of rows. The front and back previews keep their original row labels. For an overview, return the numerical summary that `describe()` produces; `info()` is for a quick printed check, not the returned summary.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your work.

## Your Tasks

1. Make `ends(table, amount)` return `(table.head(amount), table.tail(amount))`.
2. Make `numeric_summary(table)` return the DataFrame produced by `table.describe()` for its numeric columns.
