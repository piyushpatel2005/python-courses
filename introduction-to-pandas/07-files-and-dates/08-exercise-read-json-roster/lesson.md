---
title: 'Exercise: load a JSON roster'
slug: exercise-read-json-roster
order: 8
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Write a function that loads variable JSON records into a DataFrame.
seo_title: 'Exercise: load a JSON roster | Introduction to Pandas'
seo_description: Write a function that loads variable JSON records into a DataFrame.
seo_keywords:
  - pandas
  - read_json
  - roster JSON
hints:
  - "Use orient=\"records\" because the top-level JSON list contains one object per row."
---

# Exercise: load a JSON roster

The volunteer desk sends a JSON roster with `name` and `shift` keys. This time you need the whole table, not a single column. Each record supplies one volunteer's row.

Edit `load_roster` in `main.py`. The imports are supplied; use the incoming `text` to create a fresh `StringIO` buffer and read it with records orientation. Return the DataFrame itself.

Run should show Mara on the morning shift and Luis on the evening shift. Submit uses a different roster as well, so avoid constructing those two rows by hand.

## Your Tasks

1. Implement `load_roster(text)` to return a DataFrame with `name` and `shift` columns from the supplied JSON list of records.
