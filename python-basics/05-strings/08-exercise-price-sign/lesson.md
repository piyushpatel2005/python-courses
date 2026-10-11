---
title: "Exercise: Write a Decoded Route Sign"
slug: exercise-price-sign
order: 8
language: python
lesson_type: coding
runtime: pyodide
summary: Build a cavern heading and formatted energy line with f-strings.
seo_title: "Exercise: Write a Decoded Route Sign | Python Basics"
seo_description: Build a cavern heading and formatted energy line with f-strings.
seo_keywords: [python basics, strings, lantern atlas]
---

# Exercise: Write a Decoded Route Sign

Write a two-line sign for the exit route: its name and beacon count on the first line, then the total energy on the second.

The supplied `energy_cost` is the cost of one beacon. Multiply it by `beacons` to calculate the total. An f-string can contain that calculation inside its braces, just as it can contain a variable name.

## Your Tasks

1. Set `heading` with an f-string using `route` and `beacons`, giving `ECHO: 3 beacons`.
2. Set `energy_line` with an f-string showing the total energy to two decimal places, giving `Energy: 12.75`.

The two print calls are ready for you. Run `main.py` to inspect each line, then Submit. You can now read, clean, and format a route sign. After the section quiz, you'll use collections to organise supplies for Inventory Ridge.
