---
title: "Exercise: Look up table cells"
slug: exercise-find-table-cells
order: 10
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "DataFrame loc and iloc for a community market data desk."
seo_title: "Exercise: Look up table cells | Pandas for beginners"
seo_description: "DataFrame loc and iloc for a community market data desk."
seo_keywords: ["pandas", "Python data analysis", "dataframe loc and iloc"]
---
The desk gets one request with row and column labels, and another with row and column positions. Apply the matching selector to each request. The row labels may be strings or integers that do not match their positions.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your work.

## Your Tasks

1. Make `labeled_cell(table, row_label, column_name)` return the cell selected with `loc`.
2. Make `positioned_cell(table, row_number, column_number)` return the cell selected with `iloc`.
