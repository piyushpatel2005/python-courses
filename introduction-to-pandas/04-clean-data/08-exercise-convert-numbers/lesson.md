---
title: 'Exercise: repair case quantities'
slug: exercise-convert-numbers
order: 8
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Convert numeric strings with errors coerced to missing nullable integers.
seo_title: 'Exercise: repair case quantities | Introduction to Pandas'
seo_description: Convert numeric strings with errors coerced to missing nullable integers.
seo_keywords:
  - pandas
  - python
  - data cleaning
hints:
  - Assign the converted Series to the cases column of a copy, using astype("Int64").
---

The inventory clerk records case counts as text, but unknown is not the same as zero. Preserve that distinction: valid whole-number text becomes an integer and invalid or absent text becomes missing.

Start with a copy of frame. Replace its cases column with `pd.to_numeric(..., errors="coerce").astype("Int64")`, then return the copy. The capital I in "Int64" selects Pandas' nullable integer dtype, which can hold numbers and pd.NA together. Do not fill missing values in this exercise. Other columns and labels should remain unchanged.

Run should show Jam with 3, Rice with a missing value, and Tea with a genuine 0. Inputs here contain whole-number text or invalid entries; handling fractional counts is outside this task.

## Your Tasks

1. In `numeric_cases(frame)`, convert `cases` with invalid text coerced to missing values and store it as nullable `Int64`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
