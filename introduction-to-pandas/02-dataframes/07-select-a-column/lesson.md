---
title: "Select a column"
slug: select-a-column
order: 7
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "See why a column name returns a Series but a list returns a DataFrame."
seo_title: "Select a column | Pandas for beginners"
seo_description: "See why a column name returns a Series but a list returns a DataFrame."
seo_keywords: ["pandas", "Python data analysis", "dataframe single and multiple column selection"]
---

The desk needs sold counts on their own. Selecting `table["sold"]` returns that column as a Series, with the table's row index still attached.

A list of column names keeps the result as a DataFrame. In `table[["stall", "sold"]]`, the inner brackets make a Python list; the outer brackets select those columns. Even a one-name list, `table[["sold"]]`, returns a DataFrame. The difference is the kind of selector, not how many values the result contains.

![Selecting sold by name returns a Series; selecting a list containing sold returns a one-column DataFrame](column-selection-types.svg)

## Your Task

1. Change `chosen` to select the `sold` column from `table` as a Series.

Edit `main.py` and **Run**. The first output should contain counts `3` and `9`, with `Name: sold` beneath them. The second output remains a two-column table. Then **Submit**.
