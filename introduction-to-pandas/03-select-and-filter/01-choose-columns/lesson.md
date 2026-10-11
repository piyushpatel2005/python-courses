---
title: Choose columns for a stall card
slug: choose-columns
order: 1
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Select one Series or several DataFrame columns from a market roster.
seo_title: Choose columns for a stall card | Introduction to Pandas
seo_description: Select one Series or several DataFrame columns from a market roster.
seo_keywords:
  - pandas
  - python
  - data selection
hints:
  - Use a list of column names inside the selection brackets.
---

The previous report added a revenue column. A printed stall card needs fewer columns, so this time you will choose what to show without changing the roster.

`roster["stall"]` returns a Series: one labeled column. `roster[["stall", "zone"]]` returns a DataFrame: a table with two columns. The inner brackets make a Python list of names; their order becomes the output column order. Even a list with one name returns a DataFrame.

The starter supplies both forms. Edit only the list in `result`. After Run, look for Fern/east and Bee/west, with no fee column.

## Your Tasks

1. Change `result` to select both `stall` and `zone`, in that order.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
