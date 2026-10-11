---
title: "Exercise: Pack a report view"
slug: exercise-select-columns
order: 8
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Return one named field or an ordered selection of report columns."
seo_title: "Exercise: Pack a report view | Pandas for beginners"
seo_description: "Return one named field or an ordered selection of report columns."
seo_keywords: ["pandas", "Python data analysis", "select one or multiple columns"]
---

One caller wants a single field as a Series. Another wants a small table whose columns appear in a particular order. Use the requested names rather than assuming every caller wants `sold`.

In `report_fields`, the `names` parameter is already a Python list. You can pass that list directly between the table's selection brackets; do not put another list around it. A list with one name must still give a DataFrame.

## Your Tasks

1. Make `one_field(table, name)` return the named column as a Series, keeping its row labels.
2. Make `report_fields(table, names)` return a DataFrame with exactly those columns in the requested order, keeping its row labels.

Edit `main.py`, **Run**, and then **Submit**. The sample report should put `sold` before `stall`, even though the original table uses the opposite order.
