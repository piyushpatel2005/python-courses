---
title: "Turn a scoreboard"
slug: exercise-transpose
order: 4
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: 'Return a scoreboard with rounds in rows and players in columns.'
seo_title: "Turn a scoreboard | Intro to NumPy"
seo_description: 'Return a scoreboard with rounds in rows and players in columns.'
seo_keywords: [numpy, arrays, matrices]
hints:
  - Transpose scores itself, not the sample array in the print call.
---

A scoreboard stores players in rows and rounds in columns. The announcer wants one row per round, with each player's score beside the others.

Use the transpose you just tried, but apply it to the `scores` parameter. The sample has two players and three rounds, so the returned board should have three rows and two columns. Its first row will be `[2 4]`.

Replace the unfinished return in `main.py`. Run to inspect the whole board, then Submit to check another board too.

## Your Task

1. Implement `rounds_first(scores)` by returning the transposed array.
