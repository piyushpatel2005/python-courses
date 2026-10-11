---
title: "Local Energy Scope: Demo"
slug: scope-demo
order: 7
language: python
runtime: pyodide
lesson_type: coding
summary: Keep temporary ability energy separate from the outer energy value.
seo_title: "Local Energy Scope: Demo | Python Basics"
seo_description: Keep temporary ability energy separate from the outer energy value.
seo_keywords: [python basics, functions and reuse, lantern atlas]
hints:
  - Edit the indented energy assignment only.
---

# Local Energy Scope: Demo

The workshop has `20` energy stored. You can preview a different amount inside a function without changing that stored value.

There are two assignments named `energy` in `main.py`. The indented one belongs to `preview_pulse()`: it's a **local variable**. The assignment outside the function is separate, even though it uses the same name.

Run the starter. Both values happen to be `20`, so the difference isn't visible yet.

## Your Tasks

1. Change the `energy` assignment inside `preview_pulse()` to `15`.

Leave the outer assignment at `20`. Run again and compare the lines: the function returns `15`, but the stored value is still `20`. Submit to check that only the local value changed.
