---
title: Find rows by label and position
slug: labels-and-positions
order: 3
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Compare inclusive loc label slices with exclusive iloc position slices.
seo_title: Find rows by label and position | Introduction to Pandas
seo_description: Compare inclusive loc label slices with exclusive iloc position slices.
seo_keywords:
  - pandas
  - python
  - data selection
hints:
  - In a loc label slice, the label after the colon is included.
---

The ledger labels its rows `early`, `mid`, and `late`. Those names identify rows; positions describe where rows currently sit, starting at zero. An integer label would still be a label, not automatically a position.

Read `.loc[rows, columns]` as two selectors separated by a comma. `ledger.loc["early":"mid", ["stall", "sales"]]` takes the rows from early through mid, including both endpoints, and the two named columns. It follows the existing index order, not alphabetical order. These examples use unique, existing endpoint labels.

`.iloc[0:2, 0:2]` uses positions for both axes. Like a Python list slice, it includes 0 and 1 but stops before 2. The starter prints that window first. Extend the second window to mid; both outputs should then show Fern and Bee.

![Two highlighted ledger rows: loc includes the ending label, iloc excludes the ending position.](index-windows.svg)

## Your Tasks

1. Change the `.loc` window to include the row labeled `mid`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
