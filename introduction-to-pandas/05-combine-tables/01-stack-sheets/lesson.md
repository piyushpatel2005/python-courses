---
title: Stack delivery sheets
slug: stack-sheets
order: 1
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Two shifts send the desk matching delivery columns.
seo_title: Stack delivery sheets | Introduction to Pandas
seo_description: Two shifts send the desk matching delivery columns.
seo_keywords:
- pandas
- stack sheets
- community market data
---

# Stack delivery sheets

Two shifts send the desk matching delivery columns. `pd.concat` stacks rows; `ignore_index=True` replaces old row labels with a clean sequence.

![Two sheets stacked with fresh row labels](row-concat.svg)

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.

## Your Tasks

1. Change `ignore_index` to `True` in `stack_sheets`.
