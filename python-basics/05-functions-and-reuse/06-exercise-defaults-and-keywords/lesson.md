---
title: "Exercise: Label an Event"
slug: exercise-defaults-and-keywords
order: 6
language: python
runtime: pyodide
lesson_type: coding
summary: Give an event label a default ending and override it by name.
seo_title: "Exercise: Label an Event | Python Basics"
seo_description: Give an event label a default ending and override it by name.
seo_keywords: [python basics, functions and reuse, default parameters, keyword argument, label function]
hints:
  - Add the default in the definition, then name mark in the second call.
---

# Exercise: label an event

Use the same function pattern for a printed event label. The supplied function already joins `name` and `mark`. Make the mark optional, then override it in one call.

Both print calls currently pass a period as a positional argument. A default goes in the definition; a keyword argument goes in the call.

## Your Tasks

1. Give `mark` in `event_label` the default value `"."`.
2. Change the second call to pass `mark="!"` by name.

Run after each change. The finished lines are `Market day.` and `Market day!`. Submit also checks a call that omits `mark`.
