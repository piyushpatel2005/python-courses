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
  - Edit the indented room assignment only.
---

# Local Energy Scope: Demo

Names assigned inside a function are local to that call. Ari's stored `energy` and the temporary `energy` inside `preview_pulse()` can differ without overwriting one another. Run the starter: both lines show `20`. Change only the inner assignment to `15`; Run should show `15` then `20`. Submit to check.

## Your Tasks

1. Change the assignment inside `preview_pulse()` to `15`, leaving the outer `energy` at `20`.
