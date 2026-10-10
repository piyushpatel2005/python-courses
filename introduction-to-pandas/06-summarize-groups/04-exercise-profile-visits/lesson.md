---
title: 'Exercise: Profile stall visits'
slug: exercise-profile-visits
order: 4
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Describe visitor counts and tally stall types, including missing labels."
seo_title: 'Exercise: Profile stall visits | Introduction to Pandas'
seo_description: "Describe visitor counts and tally stall types, including missing labels."
seo_keywords:
  - pandas
  - exercise profile visits
  - community market data
hints:
  - 'Use describe() on visitors and value_counts(dropna=False) on type.'
---

# Exercise: Profile stall visits

The visit log has two gaps: an unknown visitor count for Art and an unknown type label on another row. A numeric description should ignore the missing visitor count, while the type tally should show the missing label as its own entry.

The function returns two Series in a tuple. Fill the first slot with the description, then the second with the label counts. For the supplied data, the description has 2 known visitor counts and a mean of 14. The type tally includes all three rows.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Return the numeric visitors description in the first tuple slot.
2. Return type frequencies, including missing labels, in the second tuple slot.
