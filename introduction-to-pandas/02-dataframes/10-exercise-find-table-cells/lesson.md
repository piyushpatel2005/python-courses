---
title: "Exercise: Look up table cells"
slug: exercise-find-table-cells
order: 10
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Handle cell requests expressed as labels or as positions."
seo_title: "Exercise: Look up table cells | Pandas for beginners"
seo_description: "Handle cell requests expressed as labels or as positions."
seo_keywords: ["pandas", "Python data analysis", "dataframe loc and iloc"]
---

A volunteer asks for the evening sold count by name. Another caller gives row and column positions. Write a separate lookup for each kind of request.

Both selectors take the row before the column. Use `.loc[...]` for `row_label` and `column_name`; use `.iloc[...]` for `row_number` and `column_number`. The test tables have unique labels, and each requested cell exists.

## Your Tasks

1. Make `labeled_cell(table, row_label, column_name)` return the cell selected with `loc`.
2. Make `positioned_cell(table, row_number, column_number)` return the cell selected with `iloc`.

Edit `main.py` and **Run** after each task. The first function should change the output to `8 None`; completing the second gives `8 2`. **Submit** also tries integer row labels that differ from positions.
