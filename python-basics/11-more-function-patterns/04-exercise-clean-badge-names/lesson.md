---
title: "Echo Tower: Select Beacon Labels"
slug: exercise-clean-badge-names
order: 4
language: python
lesson_type: coding
runtime: pyodide
summary: Use map and filter to prepare beacon labels.
seo_title: "Echo Tower: Select Beacon Labels | Python Basics"
seo_description: Use map and filter to prepare beacon labels.
seo_keywords: [python map filter exercise, beacon labels]
---

Prepare labels for the tower display. It uses uppercase text and accepts labels with at least four characters, including labels of exactly four.

Apply the previous pattern to strings: use `map` to uppercase the labels, then `filter` on that transformed list. Wrap each result in `list(...)` so the supplied printout can show it.

Edit `main.py`, Run to compare the two lists, then Submit. These compact tools are optional; you can use ordinary functions and loops in the final mission.

## Your Tasks

1. Set `upper_labels` to `list(map(...))` using a lambda that uppercases each item in `beacon_labels`.
2. Set `long_labels` to `list(filter(...))` using a lambda that keeps labels of at least four characters from `upper_labels`.
