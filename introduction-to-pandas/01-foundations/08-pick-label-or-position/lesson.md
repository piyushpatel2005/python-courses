---
title: "Pick a label or a position"
slug: pick-label-or-position
order: 8
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Series loc and iloc for a community market data desk."
seo_title: "Pick a label or a position | Pandas for beginners"
seo_description: "Series loc and iloc for a community market data desk."
seo_keywords: ["pandas", "Python data analysis", "series loc and iloc"]
---
`loc` asks for an index **label**; `iloc` asks for an integer **position**. In this card, label `20` belongs to the first value, so `card.loc[20]` and `card.iloc[1]` select different counts. Change the lookup in `first_count` to inspect the first count in any supplied Series, regardless of its labels.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your work.

## Your Task

1. Change `first_count(values)` to select the first value by position with `iloc`.
