---
title: Read a Fixed Tuple Record
slug: read-a-fixed-record
order: 7
language: python
lesson_type: coding
runtime: pyodide
summary: Create and unpack a Python tuple.
seo_title: Read a Fixed Tuple Record | Python Basics
seo_description: Create and unpack a Python tuple with an editable Python example
  and checked task.
seo_keywords:
- python tuples
- beginner tuples exercise
---

A tuple is an ordered, fixed sequence written with parentheses. Its indexed elements can be read, but assigning `record[0] = ...` raises `TypeError`. `room, time = record` unpacks two values into two names. A one-item tuple needs a comma: `(42,)`.

This is an editable worked demo. Edit `main.py`, press **Run** to compare the result, then **Submit** to check your small change. The next lesson transfers the idea to a different setting.

Change `room` to read the first part of this fixed reservation; Run should show `Blue`; then Submit.

## Your Task

1. Set `room` to the first element of `reservation`.
