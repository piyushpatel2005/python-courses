---
title: "Exercise: standardize workshop registrations"
slug: exercise-tidy-text
order: 10
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Clean text values, rename a column, and replace a short category code."
seo_title: "Exercise: standardize workshop registrations | Introduction to Pandas"
seo_description: "Clean text values, rename a column, and replace a short category code."
seo_keywords: [pandas, python, data cleaning]
---

The registration list uses `host_name` for the host and `dept` for the department. Return a new table with a `host` column of trimmed, lowercase names and a `dept` column where `arts` becomes `creative`. Do not drop other columns or change the caller's table.

## Your Tasks

1. Rename `host_name` to `host` and strip/lowercase its text values in `tidy_registrations(frame)`.
2. Replace `arts` with `creative` in `dept`, leaving other departments alone.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
