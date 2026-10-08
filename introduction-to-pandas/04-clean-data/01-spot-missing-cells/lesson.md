---
title: "Spot missing records before filing"
slug: spot-missing-cells
order: 1
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Use isna to see missing cells and dropna subset to require one field."
seo_title: "Spot missing records before filing | Introduction to Pandas"
seo_description: "Use isna to see missing cells and dropna subset to require one field."
seo_keywords: [pandas, python, data cleaning]
---

A sign-up table has some missing emails and some missing notes. `frame.isna()` marks every missing cell. `frame.dropna(subset=["email"])` only removes rows without an email; a missing note can remain. Do not replace absent text with an empty string when you need to detect missing values.

The starter checks only `note`. Change the one column name in `subset` to `email` so the contact list can actually be used.

![A three-row table marks missing cells; only rows missing the required email are removed.](missing-data-flow.svg)

## Your Tasks

1. Require a non-missing `email` when creating `result`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
