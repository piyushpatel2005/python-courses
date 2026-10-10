---
title: 'Exercise: standardize workshop registrations'
slug: exercise-tidy-text
order: 10
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Clean text values, rename a column, and replace a short category code.
seo_title: 'Exercise: standardize workshop registrations | Introduction to Pandas'
seo_description: Clean text values, rename a column, and replace a short category code.
seo_keywords:
  - pandas
  - python
  - data cleaning
hints:
  - Assign the result of rename back to cleaned before selecting its new host column.
---

Workshop registrations need a consistent host column and readable department names. Make these changes one at a time inside the supplied function; it starts with a copy so the caller's table stays unchanged.

Renaming a column and cleaning its contents are separate operations. First rename host_name to host. Then strip whitespace from the ends of host values and lowercase them; keep missing names missing. Finally replace the exact dept value arts with creative. Leave other departments and columns alone.

Run already prints the returned table. After task 1, look for the new header. After task 2, names should be ada and ben. After task 3, departments should be creative and food.

## Your Tasks

1. Rename `host_name` to `host` in `tidy_registrations(frame)`.
2. Strip and lowercase the `host` values.
3. Replace `arts` with `creative` in `dept`, leaving other departments alone.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
