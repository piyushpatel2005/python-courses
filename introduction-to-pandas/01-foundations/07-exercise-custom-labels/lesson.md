---
title: "Exercise: Label a shift"
slug: exercise-custom-labels
order: 7
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Construct a labeled Series for a community market data desk."
seo_title: "Exercise: Label a shift | Pandas for beginners"
seo_description: "Construct a labeled Series for a community market data desk."
seo_keywords: ["pandas", "Python data analysis", "construct a labeled series"]
---
The shift leader supplies names and sign-in counts separately. A Series keeps them paired in the same order. Pass `index=names` when building it; mismatched lengths are invalid rather than silently dropping an entry.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your work.

## Your Task

1. Make `shift_card(names, counts)` return a Series whose index is `names` and whose values are `counts`.
