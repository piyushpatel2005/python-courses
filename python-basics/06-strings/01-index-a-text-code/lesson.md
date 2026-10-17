---
title: "Read a Rune Code: Demo"
slug: index-a-text-code
order: 1
language: python
lesson_type: coding
runtime: pyodide
summary: Index the first and last symbols of a cavern rune code.
seo_title: "Read a Rune Code: Demo | Python Basics"
seo_description: Index the first and last symbols of a cavern rune code.
seo_keywords: [python basics, strings, lantern atlas]
---

# Read a Rune Code: Demo

The route signs in Cipher Caverns contain short text codes. You can read one character from a string by putting its position, called an **index**, in square brackets.

Python counts positions from zero. In `code = "NOVA-R"`, `code[0]` gives `N`. A negative index counts from the end: `code[-1]` gives the last character, `R`.

The starter reads the first character twice. Run it to see `N N`.

## Your Task

1. Set `last` to the last character of `code` using a negative index.

Run `main.py` again to see `N R`, then Submit.

A useful boundary to remember: `len(code)` counts the characters, but the last non-negative index is one less than that count. An index outside the string raises `IndexError`. Indexing reads a character; it can't replace a character in the original string.
