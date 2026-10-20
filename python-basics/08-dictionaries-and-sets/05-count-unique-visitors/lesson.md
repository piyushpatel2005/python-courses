---
title: "Count unique attendees"
slug: count-unique-visitors
order: 5
language: python
lesson_type: coding
runtime: pyodide
summary: "Use a set to remove duplicate attendee names."
seo_title: "Count unique attendees | Python Basics"
seo_description: "Use a set to remove duplicate attendee names."
seo_keywords: [python basics, python collections, beginner python]
---

The event sign-in sheet can include a name more than once if someone returns. A set keeps each distinct name only once. `set(sign_ins)` converts the list to a set, and `len()` then counts people rather than sign-in entries.

Sets do not preserve a reliable display order. Use `sorted()` if you need names in order; here you only print the count. An empty set is `set()`; `{}` makes an empty dictionary.

The starter counts every sign-in. Edit `main.py` so `unique_attendees` is a set. **Run** should print `2` rather than `3`; then **Submit**.

## Your Task

1. Set `unique_attendees` to a set built from `sign_ins`.
