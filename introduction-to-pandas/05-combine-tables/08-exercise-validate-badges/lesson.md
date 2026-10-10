---
title: 'Exercise: Validate badges'
slug: exercise-validate-badges
order: 8
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Match badge records while checking uniqueness on both sides."
seo_title: 'Exercise: Validate badges | Introduction to Pandas'
seo_description: "Match badge records while checking uniqueness on both sides."
seo_keywords:
  - pandas
  - exercise validate badges
  - community market data
hints:
  - 'Combine how="inner" with validate="one_to_one"; validation and row retention are separate choices.'
---

# Exercise: Validate badges

Each badge should identify one check-in and one person. Unlike repeat product orders, a duplicate badge on either side is an error for this report.

Use `validate="one_to_one"` when merging on `badge`. This checks uniqueness on both sides, but it does not require every badge to match. The requested inner merge includes only badges found in both tables. With the supplied data, E1 matches Dee and E2 matches Bo despite the reversed roster order.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Complete `audit_badges(a, b)` with an inner merge on `badge` and `validate="one_to_one"`.
