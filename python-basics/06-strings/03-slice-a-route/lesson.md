---
title: "Slice a Store Status: Demo"
slug: slice-a-route
order: 3
language: python
runtime: pyodide
lesson_type: coding
summary: Use a stop-exclusive slice to read a status word.
seo_title: "Slice a Store Status: Demo | Python Basics"
seo_description: Use a stop-exclusive slice to read a status word.
seo_keywords: [python basics, strings, python strings, slicing, stop index]
---

# Slice a store status

A store-hours entry reads `OPEN:0900`. You want the status word without the colon or the opening time. A **slice** reads a stretch of characters.

The pattern is `text[start:stop]`. Python includes `start` and stops *before* `stop`. Omitting `start` begins at zero.

![The slice includes OPEN at indexes zero through three and excludes the colon at four](string-slicing.svg "Stop-exclusive slice of a store-hours entry")

The starter uses `entry[:2]`, so Run prints `OP`. The colon is at index `4` and is not part of the status.

## Your Task

1. Change the slice assigned to `status` so it reads `OPEN` from `entry`.

Run `main.py` to check that the colon stays out, then Submit. Unlike a single index, a slice may extend past the string's end without raising `IndexError`.
