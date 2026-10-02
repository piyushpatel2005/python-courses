---
title: "Clean a Rune Message: Demo"
slug: clean-a-message
order: 5
language: python
lesson_type: coding
runtime: pyodide
summary: Normalize a rune message with strip and lower.
seo_title: "Clean a Rune Message: Demo | Python Basics"
seo_description: Normalize a rune message with strip and lower.
seo_keywords: [python basics, strings, lantern atlas]
---

# Clean a Rune Message: Demo

Rune messages can have stray spaces and mixed case. `strip()` removes surrounding whitespace; `lower()` changes case. `replace(old, new)` creates a changed string, and `startswith()` checks a prefix. These methods return new results without changing the original.

In `main.py`, add `.lower()` after `.strip()`. Run should print `beacon dim`, then Submit. The next sign needs a fuller cleanup.

## Your Task

1. Set `cleaned` to the stripped, lowercased message.
