---
title: "Exercise: Name a Beacon Ability"
slug: exercise-defaults-and-keywords
order: 6
language: python
runtime: pyodide
lesson_type: coding
summary: Define a default mark and override it in a keyword call.
seo_title: "Exercise: Name a Beacon Ability | Python Basics"
seo_description: Define a default mark and override it in a keyword call.
seo_keywords: [python basics, functions and reuse, lantern atlas]
hints:
  - Add the default in the definition first; then name mark in the second call.
---

# Exercise: Name a Beacon Ability

Use the same pattern to label a different ability. The supplied function already joins `name` and `mark`; your job is to make the mark optional and pass one override by name.

Both print calls currently supply `"."` as a second positional argument. A default belongs in the function definition, while a keyword argument belongs in a call.

## Your Tasks

1. Give the `mark` parameter of `ability_label` the default value `"."`.
2. Change the second call to pass `mark="!"` as a keyword argument.

Run `main.py` after each change. When you're finished, the lines should be `Pulse.` and `Pulse!`. Submit also checks a call that leaves out `mark`, so it can check your default rather than just the visible output.
