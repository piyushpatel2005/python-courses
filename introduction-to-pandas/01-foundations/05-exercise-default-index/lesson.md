---
title: "Exercise: Number the arrivals"
slug: exercise-default-index
order: 5
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Return the automatically generated Index for a fresh list of arrivals."
seo_title: "Exercise: Number the arrivals | Pandas for beginners"
seo_description: "Return the automatically generated Index for a fresh list of arrivals."
seo_keywords: ["pandas", "Python data analysis", "default index for new series"]
---

A volunteer brings a fresh list of arrival counts. This time the desk needs the labels for that list, not the counts themselves.

Build a Series from the function's `counts` parameter, then read its `.index` attribute. Attributes such as `.index` do not need parentheses. Return the Index object itself, rather than a Python list of labels or the entire Series.

## Your Task

1. Make `arrival_labels(counts)` return the default index of a Series built from the supplied counts.

Edit `main.py` and **Run**. For three counts, the output describes a `RangeIndex` starting at `0`, stopping before `3`, with a step of `1`. **Submit** also checks shorter and longer lists, including an empty one.
