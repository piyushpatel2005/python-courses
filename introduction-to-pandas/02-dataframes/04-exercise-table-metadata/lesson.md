---
title: "Exercise: Read the table card"
slug: exercise-table-metadata
order: 4
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Return a table's labels and inspect one column's dtype."
seo_title: "Exercise: Read the table card | Pandas for beginners"
seo_description: "Return a table's labels and inspect one column's dtype."
seo_keywords: ["pandas", "Python data analysis", "index column names and dtypes"]
---

A new delivery table may have unfamiliar column names. Read its labels from the table instead of returning the names in the example.

For the first function, use `.index.tolist()` and `.columns.tolist()`. Python can return both lists as a tuple: `return first_list, second_list`.

For the second function, `table.dtypes` is itself a Series, indexed by column name. Select the requested entry with `.loc[column]` to get its dtype object. Return that object, not a string describing it. We will select columns directly in a later lesson.

## Your Tasks

1. Make `table_labels(table)` return `(row_labels, column_names)`, with both sets of labels converted to lists.
2. Make `column_dtype(table, column)` return the dtype object for the named column.

Edit `main.py` and **Run** after each function. The example's labels are `(['morning'], ['stall', 'sold'])`, and `sold` has an integer dtype. **Submit** checks other labels and column types.
