---
title: "Exercise: Recursive Ticket Sum"
slug: exercise-recursive-ticket-sum
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: Write a small recursive sum with a reachable base case.
seo_title: "Exercise: Recursive Ticket Sum | Python Basics"
seo_description: Write a small recursive sum with a reachable base case.
seo_keywords: [python recursive sum, base case exercise]
---

The demo counted down by one; this time a box holds a short list of ticket bundles. Sum the first bundle and ask the same function to sum the remainder. The empty list is the base case, and `bundles[1:]` shrinks the problem each time. Only use small lists here; a normal loop is clearer for large inputs.

Edit `main.py`, Run for the sample total, then Submit. The function name and print are supplied.

## Your Task

1. Complete `bundle_total(bundles)` recursively: return `0` for an empty list; otherwise return the first number plus `bundle_total(bundles[1:])`.
