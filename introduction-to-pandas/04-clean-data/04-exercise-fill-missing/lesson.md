---
title: "Exercise: complete inspection ratings"
slug: exercise-fill-missing
order: 4
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Fill only the chosen rating column with a supplied fallback."
seo_title: "Exercise: complete inspection ratings | Introduction to Pandas"
seo_description: "Fill only the chosen rating column with a supplied fallback."
seo_keywords: [pandas, python, data cleaning]
---

A stall inspection ledger has missing ratings and missing inspector notes. The coordinator supplies the fallback rating for each report; the note must remain untouched. Return a new table and leave the incoming one unchanged.

## Your Tasks

1. Fill missing `rating` values with the supplied `fallback` in `complete_ratings(frame, fallback)`, preserving all other columns.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
