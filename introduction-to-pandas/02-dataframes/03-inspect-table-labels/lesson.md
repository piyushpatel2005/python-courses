---
title: "Inspect labels and dtypes"
slug: inspect-table-labels
order: 3
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "DataFrame index columns and dtypes for a community market data desk."
seo_title: "Inspect labels and dtypes | Pandas for beginners"
seo_description: "DataFrame index columns and dtypes for a community market data desk."
seo_keywords: ["pandas", "Python data analysis", "dataframe index columns and dtypes"]
---
`table.index` names rows and `table.columns` names columns. `table.dtypes` reports each column’s stored type; integer counts and text stall names differ. Set the missing row label in `index=` and watch the row heading change without changing any values.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your work.

## Your Task

1. Replace row label `unknown` with `late` in `table`.
