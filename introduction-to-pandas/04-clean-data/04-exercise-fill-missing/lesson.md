---
title: 'Exercise: complete inspection ratings'
slug: exercise-fill-missing
order: 4
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Fill only the chosen rating column with a supplied fallback.
seo_title: 'Exercise: complete inspection ratings | Introduction to Pandas'
seo_description: Fill only the chosen rating column with a supplied fallback.
seo_keywords:
  - pandas
  - python
  - data cleaning
hints:
  - 'Pass {"rating": fallback} to fillna and return the result.'
---

Inspection ratings and inspector notes have different meanings. The coordinator supplies a numeric fallback rating for the report, but a missing note must remain missing. Use a column-to-value dictionary so the replacement cannot spill into other columns.

Replace the copy-only placeholder with a returned table whose missing ratings use fallback. Preserve existing ratings, row labels, and all other columns. Leave frame unchanged so the original inspection record remains available.

Run should show Bee with rating 3 and leave Oak and Fern at 4 and 5. Trying a different fallback should change only Bee's rating.

## Your Tasks

1. Fill missing `rating` values with the supplied `fallback` in `complete_ratings(frame, fallback)`, preserving all other columns.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
