---
title: "Exercise: Label Even Patrols"
slug: exercise-for-and-range
order: 8
language: python
runtime: pyodide
lesson_type: coding
summary: "Use a stepped range to mark patrol positions."
seo_title: "Exercise: Label Even Patrols | Python Basics"
seo_description: "Use a stepped range to mark patrol positions."
seo_keywords: [python basics, control flow, lantern atlas]
---

Record patrols at positions 2, 4, and 6. This needs a step size of two rather than the one-at-a-time sequence in the demo.

The starter's `labels` is an empty string. Build it with a `for` loop above the supplied print call. Use `patrol` as the loop variable and `+=` to add one formatted label on each turn.

`range(2, 8, 2)` starts at 2, advances by 2, and stops before 8. Press **Run** after editing **main.py**. You should see `Patrol 2 | Patrol 4 | Patrol 6 | ` on one line. Then **Submit**.

## Your Tasks

1. Use `for` and `range(2, 8, 2)` to append `f"Patrol {patrol} | "` to `labels`.
