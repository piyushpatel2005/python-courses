---
title: "Exercise: Read the table card"
slug: exercise-table-metadata
order: 4
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Index column names and dtypes for a community market data desk."
seo_title: "Exercise: Read the table card | Pandas for beginners"
seo_description: "Index column names and dtypes for a community market data desk."
seo_keywords: ["pandas", "Python data analysis", "index column names and dtypes"]
---
Before changing a table, inspect its structure. Return its row labels and column names as lists; for the chosen column, return its dtype object. Do not assume the market always has the same columns.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your work.

## Your Tasks

1. Make `table_labels(table)` return a pair of lists `(row_labels, column_names)`.
2. Make `column_dtype(table, column)` return the dtype of the named column.
