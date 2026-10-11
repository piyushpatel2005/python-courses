---
title: "Pick a label or a position"
slug: pick-label-or-position
order: 8
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Choose the first Series value by position, even with numeric labels."
seo_title: "Pick a label or a position | Pandas for beginners"
seo_description: "Choose the first Series value by position, even with numeric labels."
seo_keywords: ["pandas", "Python data analysis", "series loc and iloc"]
---

This card has labels `20`, `10`, and `30`, but its positions are still `0`, `1`, and `2`.

Use `.loc[label]` to ask for a label and `.iloc[position]` to ask for a position. Both use square brackets. On this card, `card.loc[20]` is `7`, while `card.iloc[1]` is `14`. An integer label is still a label: `20` does not mean the twenty-first row.

The supplied function currently picks the second value. Change its position so it picks the first, even when a different card is passed in.

## Your Task

1. Change `first_count(values)` to return the first value by position using `iloc`.

Edit `main.py`, then **Run**. The printed value should change from `14` to `7`. **Submit** tries other values and label orders.
