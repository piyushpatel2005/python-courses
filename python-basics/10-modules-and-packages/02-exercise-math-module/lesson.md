---
title: 'Exercise: Calculate Lantern Capacity'
slug: exercise-math-module
order: 2
language: python
runtime: pyodide
lesson_type: coding
summary: 'Use math.ceil to size six-spark lanterns.'
seo_title: 'Exercise: Calculate Lantern Capacity | Python Basics'
seo_description: 'Use math.ceil to size six-spark lanterns.'
seo_keywords: [python basics, exercise math module, python practice]
hints:
  - Divide sparks by six, then round up with math.ceil.
---

These lanterns each hold six sparks, rather than the four in the beacon demo. A partly filled lantern still counts, so round the division result up with `math.ceil`.

Complete the helper in `main.py`. Run should show `3` lanterns for thirteen sparks. Submit also checks other counts, including zero.

## Your Task

1. Implement `lanterns_needed(sparks)` with `math.ceil` for six-spark lanterns.
