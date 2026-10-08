---
title: "Find a row and column"
slug: loc-and-iloc-table-cells
order: 9
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "DataFrame loc iloc rows and columns for a community market data desk."
seo_title: "Find a row and column | Pandas for beginners"
seo_description: "DataFrame loc iloc rows and columns for a community market data desk."
seo_keywords: ["pandas", "Python data analysis", "dataframe loc iloc rows and columns"]
---
For a DataFrame, `loc[row_label, column_name]` finds a cell by labels; `iloc[row_position, column_position]` uses positions. Here the first row carries label `20`, not `0`. Change the positional expression to read the second row’s sold count.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your work.

## Your Task

1. Set `chosen` to the second row’s `sold` count using `iloc`.
