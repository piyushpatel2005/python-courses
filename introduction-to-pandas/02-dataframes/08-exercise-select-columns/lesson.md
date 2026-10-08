---
title: "Exercise: Pack a report view"
slug: exercise-select-columns
order: 8
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Select one or multiple columns for a community market data desk."
seo_title: "Exercise: Pack a report view | Pandas for beginners"
seo_description: "Select one or multiple columns for a community market data desk."
seo_keywords: ["pandas", "Python data analysis", "select one or multiple columns"]
---
A caller may ask for one field or a short report of several fields. The first request returns a Series; the second returns a DataFrame even if its list contains only one name. Preserve the requested column order.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your work.

## Your Tasks

1. Make `one_field(table, name)` return the named column as a Series.
2. Make `report_fields(table, names)` return a DataFrame with precisely those columns in the requested order.
