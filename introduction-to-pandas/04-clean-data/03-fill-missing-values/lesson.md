---
title: Fill an absent attendance count
slug: fill-missing-values
order: 3
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Use fillna for an explicitly chosen fallback without changing the input.
seo_title: Fill an absent attendance count | Introduction to Pandas
seo_description: Use fillna for an explicitly chosen fallback without changing the input.
seo_keywords:
  - pandas
  - python
  - data cleaning
hints:
  - Change the value paired with attendees, not the column name or the whole table.
---

The attendance report has an unrecorded count for Repair. For this display, the coordinator has chosen zero as a fallback. That is a reporting decision, not evidence that nobody attended; the source table should retain the missing count.

A dictionary passed to fillna names exactly which column to fill: `sessions.fillna({"attendees": 0})`. Existing counts are unchanged, and missing comments stay missing. Save the returned table in result.

Change the supplied fallback from -1 to 0. Run should show Repair with zero attendees while Music and Seed swap keep 12 and 8. Counts may display with decimal points because the original column contains a missing number.

## Your Tasks

1. Fill missing `attendees` with 0 in `result`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
