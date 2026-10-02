---
title: "Slice a Cavern Route: Demo"
slug: slice-a-route
order: 3
language: python
lesson_type: coding
runtime: pyodide
summary: Use a stop-exclusive slice to read a route prefix.
seo_title: "Slice a Cavern Route: Demo | Python Basics"
seo_description: Use a stop-exclusive slice to read a route prefix.
seo_keywords: [python basics, strings, lantern atlas]
---

# Slice a Cavern Route: Demo

Ari finds `GLOW:TRAM` carved on a route sign. `text[start:stop]` includes the start but not the stop; omitting the start begins at zero. A slice past the end is safe, unlike an invalid single index.

![Stop-exclusive slice across a cavern route sign](string-slicing.svg "String slicing: start included, stop excluded")

Change `district` in `main.py` to slice out `GLOW`. Run should print `GLOW`; then Submit. The next task separates another sign's fields.

## Your Task

1. Slice `route` to set `district` to `"GLOW"`.
