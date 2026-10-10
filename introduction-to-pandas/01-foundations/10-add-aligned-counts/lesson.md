---
title: "Add counts by label"
slug: add-aligned-counts
order: 10
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "See how Series addition matches labels rather than row positions."
seo_title: "Add counts by label | Pandas for beginners"
seo_description: "See how Series addition matches labels rather than row positions."
seo_keywords: ["pandas", "Python data analysis", "series arithmetic alignment"]
---

The morning volunteer listed `north` first; the afternoon volunteer listed `south` first. Adding their Series still combines the right places because pandas matches index labels before adding.

In the starter, north's total is `4 + 2 = 6`, and south's is `7 + 3 = 10`. Adding the first displayed values, `4 + 3`, would mix two different places.

![Series addition matches north with north and south with south despite reversed input order](label-alignment.svg)

A label found in only one Series has no partner. Ordinary addition leaves its total missing, often displayed as `NaN`, rather than guessing that the absent count is zero.

## Your Task

1. Change north's value in `afternoon` from `2` to `5`, leaving the other values and the addition in place.

Edit `main.py` and **Run**. North should now total `9`; south should still total `10`. Then **Submit**.
