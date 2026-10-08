---
title: "Exercise: repair case quantities"
slug: exercise-convert-numbers
order: 8
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Convert numeric strings with errors coerced to missing nullable integers."
seo_title: "Exercise: repair case quantities | Introduction to Pandas"
seo_description: "Convert numeric strings with errors coerced to missing nullable integers."
seo_keywords: [pandas, python, data cleaning]
---

The inventory clerk enters case counts as text. Some rows contain `"unknown"` or an empty field. Return a copy whose `cases` column holds nullable integers: valid counts are numbers and invalid entries are missing. Do not replace invalid entries with zero, because zero cases is a different fact.

## Your Tasks

1. In `numeric_cases(frame)`, convert `cases` with invalid text coerced to missing values and store it as nullable `Int64`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
