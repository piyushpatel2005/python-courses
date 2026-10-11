---
title: "Add a calculated column"
slug: add-a-calculated-column
order: 11
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Calculate a new column from two existing numeric columns."
seo_title: "Add a calculated column | Pandas for beginners"
seo_description: "Calculate a new column from two existing numeric columns."
seo_keywords: ["pandas", "Python data analysis", "dataframe new columns"]
---

The report needs a total for each stall: units sold multiplied by price. Selecting `table["sold"]` and `table["price"]` gives two Series with the same index, so multiplying them pairs values from the same rows.

Assigning that result to `table["total"]` adds a new column. Unlike the previews you returned earlier, this assignment changes `table` itself. The starter already contains the calculation; you only need to correct one input price.

## Your Task

1. Change the second value in the `price` input list from `2` to `4`, leaving the calculated-column expression in place.

Edit `main.py` and **Run**. The first total stays `15`; the second becomes `24`, because `6 * 4 = 24`. Then **Submit**.
