---
title: "Read a sign-in record"
slug: read-a-fixed-record
order: 7
language: python
lesson_type: coding
runtime: pyodide
summary: "Index and unpack a fixed event sign-in tuple."
seo_title: "Read a sign-in record | Python Basics"
seo_description: "Index and unpack a fixed event sign-in tuple."
seo_keywords: [python basics, python collections, beginner python]
---

A sign-in record pairs one attendee name with the time they arrived. A tuple keeps these fields in a fixed order: `("Maya", "09:00")`. Like a list, it supports indexing. Unlike a list, it does not let you replace an element; `sign_in[0] = "Luis"` raises `TypeError`.

You can unpack a tuple into names: `name, arrival_time = sign_in`. The number of names must match the number of values. For a one-item tuple, keep the comma: `("Maya",)`.

The starter already unpacks both fields. Change `attendee` in `main.py` to read the first field by index. **Run** should print `Maya` and then `Sign-in: Maya 09:00`. **Submit** when it does.

## Your Task

1. Set `attendee` to the first item of `sign_in` by indexing.
