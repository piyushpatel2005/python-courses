---
title: "Exercise: Clean Badge Names"
slug: exercise-clean-badge-names
order: 4
language: python
lesson_type: coding
runtime: pyodide
summary: Use map and filter for a short badge-name pipeline.
seo_title: "Exercise: Clean Badge Names | Python Basics"
seo_description: Use map and filter for a short badge-name pipeline.
seo_keywords: [python lambda map filter exercise, badge names]
---

The demo changed prices; this job cleans attendee badge names. First transform each name to uppercase with `map` and a lambda. Then keep only names of length at least four with `filter` and another lambda. Convert each result to a list to display it. These are optional compact patterns, not requirements for the final workshop project.

Edit `main.py`, Run to inspect both lists, then Submit. The two tasks have separate checkpoints; `badge_names` is already supplied.

## Your Tasks

1. Set `upper_names` to `list(map(...))` using a lambda that uppercases each name in `badge_names`.
2. Set `long_names` to `list(filter(...))` using a lambda that keeps names with at least four characters from `upper_names`.
