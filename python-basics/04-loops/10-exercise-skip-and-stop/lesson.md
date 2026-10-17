---
title: "Exercise: Cross Safe Tiles"
slug: exercise-skip-and-stop
order: 10
language: python
runtime: pyodide
lesson_type: coding
summary: "Skip an unstable tile and stop at a safe-route limit."
seo_title: "Exercise: Cross Safe Tiles | Python Basics"
seo_description: "Skip an unstable tile and stop at a safe-route limit."
seo_keywords: [python basics, control flow, lantern atlas]
---

Cross three safe tiles, then stop. Tile 3 is unstable, so it must not count toward the route limit.

The starter supplies an empty `safe_tiles` string, a `cleared_count` of zero, and a `route_limit` of three. Add your loop above the print calls in **main.py**.

First build the route with tile 3 skipped. Before you add the stopping rule, **Run** should list `1 2 4 5 6 7 8 ` and show a count of `7`. After the stopping rule, it should list only `1 2 4 ` and show `3`. **Submit** checks these two stages separately.

## Your Tasks

1. Build the safe-tile list with a loop over `range(1, 9)`: use `continue` to skip tile 3, and for each remaining tile add `f"{tile} "` to `safe_tiles` and add 1 to `cleared_count`.
2. After counting a safe tile, use `break` when `cleared_count == route_limit`.

Put the stopping check after the count increases so the third safe tile is included before the loop ends.
