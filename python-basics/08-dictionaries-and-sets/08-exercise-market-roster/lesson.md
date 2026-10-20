---
title: "Exercise: Build an event registration summary"
slug: exercise-market-roster
order: 8
language: python
lesson_type: coding
runtime: pyodide
summary: "Report distinct attendees and registration counts by session."
seo_title: "Exercise: Build an event registration summary | Python Basics"
seo_description: "Report distinct attendees and registration counts by session."
seo_keywords: [python basics, python collections, beginner python]
---

A workshop can have several registrations for the same person: Maya signed up for both sessions. Keep all registrations in their original order, but count Maya only once when reporting attendees. The event's name and day are stored together as a tuple. Each registration is a dictionary with `"name"` and `"session"` fields.

Keep the supplied data. In `main.py`, collect names in a list, make a set for distinct people, and tally registrations per session in a dictionary. Build the final sentence from the values you calculated rather than typing a fixed result; it should also work if registrations change. **Run** to inspect the output, then **Submit**.

## Your Tasks

1. Loop over `registrations` and append each name, in registration order, to `names`.
2. Set `unique_names` to a set built from `names`.
3. Count each session in `session_counts` using its current count (or zero) plus one.
4. Build `report` with an f-string using both fields of `event`, the count of `unique_names`, and the count of `registrations`. The supplied data should produce `Community Workshop on Saturday: 2 attendees, 3 registrations`.
