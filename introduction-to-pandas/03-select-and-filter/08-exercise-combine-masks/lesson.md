---
title: 'Exercise: build two volunteer queues'
slug: exercise-combine-masks
order: 8
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Use & and | for separate row-by-row rules.
seo_title: 'Exercise: build two volunteer queues | Introduction to Pandas'
seo_description: Use & and | for separate row-by-row rules.
seo_keywords:
  - pandas
  - python
  - data selection
hints:
  - Use & for the priority mask and | for the review mask, with comparisons in parentheses.
---

Volunteers need a strict priority queue and a broader review queue from the same requests. The `urgent` column already contains Boolean values. The other rule compares hours with the supplied minimum.

The priority queue requires both rules; the review queue accepts either. A row satisfying both still appears only once in each result. Keep full rows and their labels, without changing the incoming table.

Work on one function at a time. With the supplied minimum of 4, Run should show Signs in the first table. Once the second function is ready, its table should show Signs, Chairs, and Bins.

## Your Tasks

1. In `priority_queue(frame, minimum)`, return requests with `hours >= minimum` **and** `urgent == True`.
2. In `review_queue(frame, minimum)`, return requests with `hours >= minimum` **or** `urgent == True`.

Edit `main.py`, press **Run** to inspect the table, then **Submit** to check your work.
