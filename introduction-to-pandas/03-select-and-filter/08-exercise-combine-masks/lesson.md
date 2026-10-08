---
title: "Exercise: build two volunteer queues"
slug: exercise-combine-masks
order: 8
language: python
lesson_type: coding
pyodide_packages: [pandas]
summary: "Use & and | for separate row-by-row rules."
seo_title: "Exercise: build two volunteer queues | Introduction to Pandas"
seo_description: "Use & and | for separate row-by-row rules."
seo_keywords: [pandas, python, data selection]
---

Volunteers ask for two views of pending market requests: a strict queue and a broad queue. Use `hours` and `urgent` from the supplied table. A row matching both rules appears in both results; keep its label.

## Your Tasks

1. In `priority_queue(frame, minimum)`, return requests with `hours >= minimum` **and** `urgent == True`.
2. In `review_queue(frame, minimum)`, return requests with `hours >= minimum` **or** `urgent == True`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
