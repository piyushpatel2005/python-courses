---
title: "Inspect labels and dtypes"
slug: inspect-table-labels
order: 3
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Read a DataFrame index, column names, and stored data types."
seo_title: "Inspect labels and dtypes | Pandas for beginners"
seo_description: "Read a DataFrame index, column names, and stored data types."
seo_keywords: ["pandas", "Python data analysis", "dataframe index columns and dtypes"]
---

Before editing a report, check how its rows and columns are labeled. `table.index` holds row labels, while `table.columns` holds column names. Calling `.tolist()` on either turns those labels into an ordinary Python list.

`table.dtypes` reports the stored type of each column. The `sold` counts are integers; `stall` contains text. Depending on the pandas version, that text column may show `object` or `str`. You do not need to memorize those spellings to correct a row label.

The starter prints the row labels, column names, and dtypes. None of these inspections changes the table.

## Your Task

1. Replace row label `unknown` with `late` in `table`, leaving the columns and values unchanged.

Edit `main.py` and **Run**. The row labels should become `['early', 'late']`; the columns should stay `['stall', 'sold']`. Then **Submit**.
