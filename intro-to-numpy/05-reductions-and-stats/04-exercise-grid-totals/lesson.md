---
title: "Summarize both directions"
slug: exercise-grid-totals
order: 4
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Calculate separate totals per round and per player."
seo_title: "Summarize both directions | Intro to NumPy"
seo_description: "Calculate separate totals per round and per player."
seo_keywords: [numpy, arrays, statistics]
hints:
  - 'Round totals collapse axis 0; player totals collapse axis 1.'
---

An arcade records scores with one player per row and one round per column. Use the same axis rule on this new grid: collapse players for round totals, or collapse rounds for player totals.

The starter returns two placeholders in the required order. Each task fills one of them.

## Your Tasks

1. Set `round_totals` to `np.sum(scores, axis=0)`.
2. Set `player_totals` to `np.sum(scores, axis=1)`.

Run `main.py` to check round totals `[10 11 9]` and player totals `[14 16]`. Submit to check them separately.
