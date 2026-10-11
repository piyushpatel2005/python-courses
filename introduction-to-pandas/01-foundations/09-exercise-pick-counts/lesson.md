---
title: "Exercise: Find two counts"
slug: exercise-pick-counts
order: 9
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Write separate lookups for Series labels and positions."
seo_title: "Exercise: Find two counts | Pandas for beginners"
seo_description: "Write separate lookups for Series labels and positions."
seo_keywords: ["pandas", "Python data analysis", "series label and position selection"]
---

One caller asks for the `soap` stall; another asks for the first count in the card. Those requests need different selectors.

Use the supplied `label` with `.loc[...]` and the supplied `position` with `.iloc[...]`. Do not assume that a numeric label matches its position. These examples use labels that exist and positions within the card, so you can concentrate on selection.

## Your Tasks

1. Make `by_label(card, label)` return the value at the supplied index label using `loc`.
2. Make `by_position(card, position)` return the value at the supplied integer position using `iloc`.

Edit `main.py` and **Run** after each function. Finishing the first task gives `9 None`; finishing both gives `9 4`. **Submit** checks the two functions separately.
