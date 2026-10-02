---
title: "Exercise: Cross Safe Tiles"
slug: exercise-skip-and-stop
order: 8
language: python
runtime: pyodide
lesson_type: coding
summary: "Skip an unstable tile and stop at a safe-route limit."
seo_title: "Exercise: Cross Safe Tiles | Python Basics"
seo_description: "Skip an unstable tile and stop at a safe-route limit."
seo_keywords: [python basics, control flow, lantern atlas]
---

Unlike the fixed stop tile in the demo, this route ends after **three safe tiles**. Tile 3 is unstable. The starter supplies `safe_tiles`, `cleared_count`, and `route_limit`. Press **Run** after each edit in **main.py**, then **Submit**. Final lines are `1 2 4 ` and `3`.

## Your Tasks

1. Loop over `range(1, 9)`; use `continue` to skip tile 3, append each other tile to `safe_tiles` as `f"{tile} "`, and increment `cleared_count`.
2. After counting a safe tile, use `break` when `cleared_count == route_limit`.
