---
title: Name grouped results
slug: named-aggregation
order: 7
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: A report needs readable headings for several measures.
seo_title: Name grouped results | Introduction to Pandas
seo_description: A report needs readable headings for several measures.
seo_keywords:
- pandas
- named aggregation
- community market data
---

# Name grouped results

A report needs readable headings for several measures. Named aggregation uses `output_name=(input_column, operation)`. The average should use `mean`; `size` counts rows even when amounts are missing.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your change.

## Your Tasks

1. Change `average=("total", "sum")` to use `mean`.
