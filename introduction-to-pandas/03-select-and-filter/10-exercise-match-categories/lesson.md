---
title: 'Exercise: list invited workshop types'
slug: exercise-match-categories
order: 10
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Filter membership against any supplied category collection.
seo_title: 'Exercise: list invited workshop types | Introduction to Pandas'
seo_description: Filter membership against any supplied category collection.
seo_keywords:
  - pandas
  - python
  - data selection
hints:
  - Select rows with frame.loc and a membership mask from frame["type"].isin(types).
---

The workshop coordinator changes the invited types each week. Use the `types` input as the collection passed to `isin`; do not put garden or food permanently inside the function.

The mask checks the `type` column, but the result should contain every column of each matching row. Keep original labels and order. An empty invite list, or a list with no matching types, should produce an empty table.

The supplied Run call should show Seeds and Baking with labels s5 and s6. Try an empty list to check the no-invitations case, then restore the original call.

## Your Tasks

1. Return rows whose `type` appears in `types`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
