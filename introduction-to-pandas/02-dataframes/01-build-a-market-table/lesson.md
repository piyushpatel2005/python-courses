---
title: "Build a market table"
slug: build-a-market-table
order: 1
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "DataFrame columns and records for a community market data desk."
seo_title: "Build a market table | Pandas for beginners"
seo_description: "DataFrame columns and records for a community market data desk."
seo_keywords: ["pandas", "Python data analysis", "dataframe columns and records"]
---
A **DataFrame** is a table with row labels and column names. One way to build it is a dictionary whose keys become columns; each list supplies a column of the same length. A list of row dictionaries also works: each dictionary supplies one record. Change the second stall count in both versions so they still represent the same table.

The picture shows the starting table. Read each row across to pair a stall with its visitor count.

![DataFrame columns and records diagram showing labeled data](dataframe-grid.svg)

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your work.

## Your Task

1. Change the bread visitor count from 6 to 9 in both `stalls` and `records`.
