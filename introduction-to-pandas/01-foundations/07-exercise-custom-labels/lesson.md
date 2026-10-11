---
title: "Exercise: Label a shift"
slug: exercise-custom-labels
order: 7
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Pair the names and counts supplied to a shift-card function."
seo_title: "Exercise: Label a shift | Pandas for beginners"
seo_description: "Pair the names and counts supplied to a shift-card function."
seo_keywords: ["pandas", "Python data analysis", "construct a labeled series"]
---

The shift leader sends two lists: names and sign-in counts. Their order matters: the first name belongs to the first count.

Use the function parameters to build the Series. The counts supply its values, and `index=` supplies its labels. The test inputs have matching lengths; you do not need to write error handling. Pandas itself rejects lists of different lengths rather than silently dropping an entry.

## Your Task

1. Make `shift_card(names, counts)` return a Series whose index is `names` and whose values are `counts`, preserving their order.

Replace `return None` in `main.py`, then **Run**. The example should pair `north` with `3` and `south` with `8`. **Submit** checks different names and counts.
