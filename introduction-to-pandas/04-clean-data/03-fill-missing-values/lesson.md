---
title: "Fill an absent attendance count"
slug: fill-missing-values
order: 3
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Use fillna for an explicitly chosen fallback without changing the input."
seo_title: "Fill an absent attendance count | Introduction to Pandas"
seo_description: "Use fillna for an explicitly chosen fallback without changing the input."
seo_keywords: [pandas, python, data cleaning]
---

An empty attendee count means the desk has not recorded anyone yet. For this report the team has decided to display `0`. `fillna({"attendees": 0})` fills only that column; the absent comment stays missing. This choice is a reporting rule, not a claim that every missing number means zero.

The starter fills counts with `-1`. Change that single fallback value to `0`.

## Your Tasks

1. Fill missing `attendees` with 0 in `result`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
