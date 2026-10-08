---
title: "Exercise: Combine two shifts"
slug: exercise-align-shifts
order: 11
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Add aligned Series for a community market data desk."
seo_title: "Exercise: Combine two shifts | Pandas for beginners"
seo_description: "Add aligned Series for a community market data desk."
seo_keywords: ["pandas", "Python data analysis", "add aligned series"]
---
Two volunteers report stall counts with labels in different orders. Adding their Series directly lines up matching stalls. For a label in only one shift, ordinary addition gives a missing value; do not quietly treat it as zero yet.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check your work.

## Your Task

1. Make `combine_shifts(first, second)` return their label-aligned sum as a Series.
