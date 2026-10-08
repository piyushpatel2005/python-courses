---
title: Sketch data with text bars
slug: text-bars
order: 11
language: python
lesson_type: coding
pyodide_packages:
- pandas
summary: Represent numeric values as a simple text bar chart without plotting tools.
seo_title: Sketch data with text bars | Introduction to Pandas
seo_description: Represent numeric values as a simple text bar chart without plotting
  tools.
seo_keywords:
- pandas
- text bar chart
- Series visualization
hints:
- Use the example above the task and check the printed result before submitting.
---

# Sketch data with text bars

A quick text chart is enough to compare small counts. One `#` per visitor makes length meaningful; use the same unit for each row. A function that accepts a Series can handle any names and counts.

`visit_bars` currently draws two marks per visitor. Change only `scale=2` to `scale=1`. Run: the first bar should have three marks, not six. Submit to check a different Series too.

## Your Tasks

1. Make `visit_bars(counts)` return one `name: ###` line per Series entry, with exactly one `#` per count.
