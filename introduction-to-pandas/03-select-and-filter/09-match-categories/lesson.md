---
title: Match a list of categories
slug: match-categories
order: 9
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Use isin for several allowed labels and query for a compact expression.
seo_title: Match a list of categories | Introduction to Pandas
seo_description: Use isin for several allowed labels and query for a compact expression.
seo_keywords:
  - pandas
  - python
  - data selection
hints:
  - Add the second string to the existing list passed to isin.
---

The weekly list needs both fruit and bakery stalls. Rather than writing one equality comparison for every category, use `.isin(["fruit", "bakery"])`. It produces a True/False Series for membership in that collection; `.loc` uses the Series to select rows. Matching is exact, including spelling and case.

The supplied `fruit_only` line also shows `query("category == 'fruit'")`. Inside that expression, category refers to a column. You do not need to change it; the task practices isin, which works conveniently with a list of allowed names.

Add bakery to the list used by `result`. Run should still print Pear alone first, followed by Pear and Loaf. Soap remains outside the selected categories.

## Your Tasks

1. Add `bakery` to the categories selected in `result`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
