---
title: "Add a calculated column"
slug: add-a-calculated-column
order: 11
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "DataFrame new columns for a community market data desk."
seo_title: "Add a calculated column | Pandas for beginners"
seo_description: "DataFrame new columns for a community market data desk."
seo_keywords: ["pandas", "Python data analysis", "dataframe new columns"]
---
A new column can be calculated from existing columns. Assigning `table["total"] = table["sold"] * table["price"]` multiplies each row’s values. Correct the price of the second stall and see its new total.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your work.

## Your Task

1. Change the second `price` from 2 to 4 so the second `total` becomes 24.
