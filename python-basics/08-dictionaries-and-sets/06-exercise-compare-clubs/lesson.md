---
title: "Exercise: Compare sign-in lists"
slug: exercise-compare-clubs
order: 6
language: python
lesson_type: coding
runtime: pyodide
summary: "Find attendees shared by two sessions and those in only one."
seo_title: "Exercise: Compare sign-in lists | Python Basics"
seo_description: "Find attendees shared by two sessions and those in only one."
seo_keywords: [python basics, python collections, beginner python]
---

Two sessions have separate sign-in lists. One person may sign in twice, but you want to compare people, not entries. Convert the morning list to a set. The intersection operator `&` keeps names in both sets. The difference operator `-` keeps names on the left but not the right, so its direction matters.

The starter sorts the sets only for printing, since sets themselves have no fixed display order. Edit `main.py`; **Run** to inspect the three groups, then **Submit**.

## Your Tasks

1. Set `morning_attendees` to a set built from `morning_sign_ins`.
2. Set `both_sessions` to the intersection of `morning_attendees` and a set of `afternoon_sign_ins`.
3. Set `morning_only` to the difference between `morning_attendees` and a set of `afternoon_sign_ins`.
