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
- Use the example above the task and check the printed result before submitting.
---

# Exercise: load a JSON roster

The volunteer desk sends records with `name` and `shift` keys. Unlike the registry example, you need the whole DataFrame so you can inspect shifts later. The JSON is supplied as a string parameter; wrap it in `StringIO` before reading.

Edit `main.py`, Run to see the roster table, then Submit to test a different roster.

## Your Tasks

1. Implement `load_roster(text)` to return a DataFrame with `name` and `shift` columns from the supplied JSON list of records.
