---
title: "Final Project: Workshop Board"
slug: final-workshop-board
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: Build a practical report with ordinary functions, loops, lists, and strings.
seo_title: "Final Project: Workshop Board | Python Basics"
seo_description: Build a practical report with ordinary functions, loops, lists, and strings.
seo_keywords: [python final project, workshop board, loops functions]
---

The coordinator needs a board for several workshop sessions. Each session is a dictionary with `name`, `capacity`, and a list of numeric `reservations`. Use familiar functions and loops; **no classes, inheritance, enums, recursion, or lambda are needed**. The supplied fixture replaces keyboard input, so Run never pauses for `input()`.

Edit `main.py` and Run to see one line per workshop. Submit tasks in order: first count, then calculate space, then assemble the board. One workshop can be overbooked, so available places must not go below zero.

## Your Tasks

1. Complete `reserved_total(numbers)` with a loop that sums the numbers, returning `0` for an empty list.
2. Complete `available_places(capacity, reserved)` to return the larger of `capacity - reserved` and `0` using a condition.
3. Complete `build_board(sessions)` to return a list of lines in input order, each exactly `"<name>: <reserved> reserved, <available> available"`, using your two helpers and an f-string.

The board now gives the coordinator a quick, readable seating update.
