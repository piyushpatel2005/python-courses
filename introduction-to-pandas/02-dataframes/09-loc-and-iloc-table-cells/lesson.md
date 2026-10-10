---
title: "Find a row and column"
slug: loc-and-iloc-table-cells
order: 9
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Select a single DataFrame cell by row and column position."
seo_title: "Find a row and column | Pandas for beginners"
seo_description: "Select a single DataFrame cell by row and column position."
seo_keywords: ["pandas", "Python data analysis", "dataframe loc iloc rows and columns"]
---

You used `loc` and `iloc` to select a Series value. A DataFrame has two directions to specify: row first, then column, separated by a comma inside the brackets.

`table.loc[20, "sold"]` asks for row label `20` and column name `sold`, giving `5`. `table.iloc[0, 1]` reaches the same cell by position: first row, second column. Positions start at zero in both directions.

For the next lookup, keep the second column but move to the second row. Its row label is `10`; its row position is `1`.

## Your Task

1. Set `chosen` to the second row's `sold` count using `iloc`.

Edit `main.py` and **Run**. The first printed value should become `11`; the label-based lookup below it should still print `5`. **Submit** checks the positional lookup.
