---
title: Profile values and labels
slug: profile-values
order: 3
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: "Read a numeric description and include missing labels in a frequency tally."
seo_title: Profile values and labels | Introduction to Pandas
seo_description: "Read a numeric description and include missing labels in a frequency tally."
seo_keywords:
  - pandas
  - profile values
  - community market data
hints:
  - 'Change the missing-label option on value_counts, not on describe.'
---

# Profile values and labels

Before publishing, the desk checks both the range of amounts and the frequency of category labels. `describe()` on a numeric Series returns the known count, mean, sample standard deviation (`std`), minimum, maximum, and three percentiles. The 50% value is the median; 25% and 75% mark the lower and upper quarters of the data. You do not need to calculate these by hand here.

`value_counts()` answers a different question: how often does each label occur? It leaves missing labels out unless you pass `dropna=False`. In the supplied data, Food occurs twice, Craft once, and one row has no category. After your edit, all four rows should be represented in the category tally. The numeric description should stay unchanged.

Edit `main.py`, press **Run** to inspect the result, then **Submit** to check each task.

## Your Tasks

1. Change `dropna=True` to `dropna=False` in `profile_sales`.
