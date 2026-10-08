---
title: "Match a list of categories"
slug: match-categories
order: 9
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Use isin for several allowed labels and query for a compact expression."
seo_title: "Match a list of categories | Introduction to Pandas"
seo_description: "Use isin for several allowed labels and query for a compact expression."
seo_keywords: [pandas, python, data selection]
---

The weekly list contains several produce categories. `.isin(["fruit", "bakery"])` builds a mask for any of those labels. For simple column names, `frame.query("category == 'fruit'")` is another readable filter; `.isin` is especially convenient when the allowed choices arrive as a variable.

The starter's `result` keeps just fruit. Add `"bakery"` to the allowed list in that expression. The separate `fruit_only` line shows the equivalent single-category query.

## Your Tasks

1. Add `bakery` to the categories selected in `result`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
