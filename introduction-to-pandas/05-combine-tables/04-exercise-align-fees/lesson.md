---
title: 'Exercise: Align fees'
slug: exercise-align-fees
order: 4
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Attach fees by stall index while keeping unmatched labels visible."
seo_title: 'Exercise: Align fees | Introduction to Pandas'
seo_description: "Attach fees by stall index while keeping unmatched labels visible."
seo_keywords:
  - pandas
  - exercise align fees
  - community market data
hints:
  - 'Concatenate [a, b] along axis 1; the default outer alignment retains unmatched labels.'
---

# Exercise: Align fees

Stock counts use stall IDs as row labels, and the fee sheet does too. Combine the columns by those labels, not by their positions.

B2 should have 6 jars and a fee of 12. Keep A1 and C3 as well: a missing fee or stock count is something the desk still needs to investigate. Do not fill those gaps with zero.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Complete `align_fees(a, b)` by concatenating columns along axis 1.
