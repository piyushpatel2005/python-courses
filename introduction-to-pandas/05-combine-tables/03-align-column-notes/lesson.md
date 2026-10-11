---
title: Align column notes
slug: align-column-notes
order: 3
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Align visit and weather columns by their shared date labels."
seo_title: Align column notes | Introduction to Pandas
seo_description: "Align visit and weather columns by their shared date labels."
seo_keywords:
  - pandas
  - align column notes
  - community market data
hints:
  - 'Use axis=1 to combine columns while keeping the union of the index labels.'
---

# Align column notes

The desk has visit counts for Monday and Tuesday, but weather notes for Tuesday and Wednesday. These tables describe different facts about the same dates. They belong side by side.

`axis=0` stacks rows; `axis=1` adds columns and matches the row index labels. Tuesday must receive both 8 visits and dry weather, even though Tuesday is in a different position in each input. Monday has no weather note and Wednesday has no visit count, so those cells remain missing. Run the starter, change the axis, and find the complete Tuesday row.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Change `axis=0` to `axis=1` in `align_notes`.
