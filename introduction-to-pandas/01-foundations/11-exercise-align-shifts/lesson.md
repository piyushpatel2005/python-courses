---
title: "Exercise: Combine two shifts"
slug: exercise-align-shifts
order: 11
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Combine differently ordered shift counts while preserving missing matches."
seo_title: "Exercise: Combine two shifts | Pandas for beginners"
seo_description: "Combine differently ordered shift counts while preserving missing matches."
seo_keywords: ["pandas", "Python data analysis", "add aligned series"]
---

Two volunteers have sent stall counts in different orders. Your function should add the Series directly so pandas matches stall labels.

For the supplied example, tea has `3 + 2` visitors and jam has `5 + 4`. Do not combine values by their displayed positions. If only one shift includes a stall, leave the resulting total missing; an absent report does not necessarily mean zero visitors.

## Your Task

1. Make `combine_shifts(first, second)` return their label-aligned sum as a Series.

Edit `main.py`, **Run**, and look for `tea: 5` and `jam: 9`. The output may list the labels in a different order from either input. **Submit** also checks unmatched labels.

You can now build, label, select, and add a Series. After the quiz, you will put several named columns together in a DataFrame.
