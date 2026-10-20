---
title: "Local Chair Counts: Demo"
slug: scope-demo
order: 7
language: python
runtime: pyodide
lesson_type: coding
summary: Change a local preview count without changing the stored chair count.
seo_title: "Local Chair Counts: Demo | Python Basics"
seo_description: Change a local preview count without changing the stored chair count.
seo_keywords: [python basics, functions and reuse, python scope, local variables, functions]
hints:
  - Edit only the indented chairs assignment.
---

# Local chair counts

A room has `20` chairs listed on its inventory. You can preview a smaller setup inside a function without changing that outer count.

`main.py` assigns `chairs` twice. The indented assignment in `preview_chairs()` is a **local variable**. It is separate from the `chairs` assignment outside the function, despite the shared name.

Run the starter. Both counts are `20`, so the difference is not yet visible.

## Your Tasks

1. Change the `chairs` assignment inside `preview_chairs()` to `15`.

Leave the outer assignment at `20`. Run again to see `15` followed by `20`, then Submit.
