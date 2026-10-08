---
title: "Turn text counts into numbers"
slug: convert-text-to-numbers
order: 7
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Coerce invalid numeric text and choose an explicit integer fallback."
seo_title: "Turn text counts into numbers | Introduction to Pandas"
seo_description: "Coerce invalid numeric text and choose an explicit integer fallback."
seo_keywords: [pandas, python, data cleaning]
---

The tally sheet imported counts as text. `pd.to_numeric(..., errors="coerce")` converts valid text and turns invalid entries into missing numbers instead of raising a `ValueError`. Only after choosing what missing means here can `.fillna(0).astype(int)` produce whole-number counts. Without the fallback, an ordinary integer type cannot store missing values; the nullable `Int64` type can.

The starter's report uses `-1` for bad text. Change just that fallback to `0`.

## Your Tasks

1. Use 0 as the fallback for invalid counts before converting to integers.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
