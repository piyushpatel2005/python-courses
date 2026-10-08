---
title: "Choose columns for a stall card"
slug: choose-columns
order: 1
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Select one Series or several DataFrame columns from a market roster."
seo_title: "Choose columns for a stall card | Introduction to Pandas"
seo_description: "Select one Series or several DataFrame columns from a market roster."
seo_keywords: [pandas, python, data selection]
---

The stall directory has more details than a printed card needs. `roster["stall"]` returns one column as a Series; `roster[["stall", "zone"]]` returns a two-column DataFrame. The inner brackets hold a list of column names, in the order you want them.

The starter already selects one column. Change just the column list assigned to `result` so the card also includes `zone`.

## Your Tasks

1. Change `result` to select both `stall` and `zone`, in that order.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
