---
title: "Skip a Hazard, Stop at a Gate"
slug: skip-and-stop
order: 9
language: python
runtime: pyodide
lesson_type: coding
summary: "Compare continue and break along a short route."
seo_title: "Skip a Hazard, Stop at a Gate | Python Basics"
seo_description: "Compare continue and break along a short route."
seo_keywords: [python basics, control flow, lantern atlas]
---

A route has an unstable tile and a gate beyond it. The starter visits tiles in order, skips tile 2, and stops when it reaches tile 5.

The two instructions do different jobs:

- `continue` skips the rest of the current turn. The loop moves on to the next tile.
- `break` leaves the loop completely. No later tiles are visited.

Both checks come before the line that adds a tile to `cleared`. That order keeps the unstable tile and the gate itself out of the output.

In **main.py**, change the unstable tile to 3 and leave the stop at 5. Press **Run** to see `Cleared 1 | Cleared 2 | Cleared 4 | `, then **Submit**.

If you use `continue` in a counter-driven `while` loop, make sure the counter still changes before you skip to the next turn. Otherwise you can get stuck checking the same value.

## Your Tasks

1. Skip tile 3 instead of tile 2.
