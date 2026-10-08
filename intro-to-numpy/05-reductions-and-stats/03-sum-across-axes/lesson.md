---
title: "Choose an axis"
slug: sum-across-axes
order: 3
language: python
lesson_type: coding
pyodide_packages: [numpy]
summary: "Choose an axis with NumPy arrays."
seo_title: "Choose an axis | Intro to NumPy"
seo_description: "Practice choose an axis in a runnable NumPy lesson."
seo_keywords: [numpy, arrays, statistics]
hints:
  - Read the shape of the input and the requested result before choosing an axis.
---

A grid has rows for nights and columns for sensors. `axis=0` collapses rows to give one total per sensor; `axis=1` collapses columns to give one total per night. Think **which axis disappears**: `axis=0` reduces the row dimension and retains columns; `axis=1` reduces columns and retains rows.

![Two nights as rows, three sensors as columns; axis 0 collapses nights into three sensor totals while axis 1 collapses sensors into two night totals](axes-rows-columns.svg)


Run `main.py` first, make the small edit, then Submit.

## Your Task

1. Change the axis to `1` to print `[10 11]`, one total per night.
