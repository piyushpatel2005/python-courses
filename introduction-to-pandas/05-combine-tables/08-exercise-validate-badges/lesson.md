---
title: 'Exercise: Validate badges'
slug: exercise-validate-badges
order: 8
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Check-ins should have one row per badge in each roster.
seo_title: 'Exercise: Validate badges | Introduction to Pandas'
seo_description: Check-ins should have one row per badge in each roster.
seo_keywords:
- pandas
- exercise validate badges
- community market data
---

# Exercise: Validate badges

Check-ins should have one row per badge in each roster. A one-to-one merge rejects duplicates on either side instead of silently multiplying rows.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.

## Your Tasks

1. Complete `audit_badges(a, b)` with an inner merge on `badge` and `validate="one_to_one"`.
