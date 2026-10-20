---
title: "Index a Room Label: Demo"
slug: index-a-text-code
order: 1
language: python
runtime: pyodide
lesson_type: coding
summary: Read the first and last characters of a room label.
seo_title: "Index a Room Label: Demo | Python Basics"
seo_description: Read the first and last characters of a room label.
seo_keywords: [python basics, strings, python strings, indexing, negative index]
---

# Index a room label

A room label such as `ROOM-B` contains a name and a final letter identifying the room. To read one character of a string, put its position, called an **index**, in square brackets.

Python counts from zero. For `code = "ROOM-B"`, `code[0]` is `R`. A negative index counts from the end, so `code[-1]` is `B`.

The starter reads the first character twice. Run it to see `R R`.

## Your Task

1. Set `last` to the last character of `code` using a negative index.

Run `main.py` again to see `R B`, then Submit. `len(code)` counts characters, but the final non-negative index is one less than that count. An index outside the string raises `IndexError`. Indexing reads a character; it cannot change the string in place.
