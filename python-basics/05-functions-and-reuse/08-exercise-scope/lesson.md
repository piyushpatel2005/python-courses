---
title: "Exercise: Preview a Paper Stack"
slug: exercise-scope
order: 8
language: python
runtime: pyodide
lesson_type: coding
summary: Return a local paper count without changing the stored count.
seo_title: "Exercise: Preview a Paper Stack | Python Basics"
seo_description: Return a local paper count without changing the stored count.
seo_keywords: [python basics, functions and reuse, python scope, local assignment, return]
hints:
  - Indent the new assignment within the function.
---

# Exercise: preview a paper stack

The supply shelf has `40` sheets of paper, but a small print job will use a stack of `30`. Preview that stack without changing the shelf count.

Write the body of `preview_sheets()`. An assignment inside the function creates a local `sheets`; return it for the supplied print call.

## Your Tasks

1. Complete `preview_sheets()` so it creates a local `sheets` value of `30` and returns it.

Keep the outer `sheets = 40`. Run `main.py` to see `30` and then `40`, then Submit.
