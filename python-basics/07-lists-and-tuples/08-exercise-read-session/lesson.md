---
title: "Exercise: Read a session record"
slug: exercise-read-session
order: 8
language: python
lesson_type: coding
runtime: pyodide
summary: "Index and unpack an event session tuple."
seo_title: "Exercise: Read a session record | Python Basics"
seo_description: "Index and unpack an event session tuple."
seo_keywords: [python basics, python collections, beginner python]
---

An event schedule stores a room name and its session start time as one fixed record. The tuple `session_record` has exactly two fields in that order. Read the room by index first; then unpack the pair so each field has its own variable.

Edit `main.py`. Press **Run** to see the room and time, then **Submit** to check both tasks. Next, you'll use named dictionary keys when a record has several fields.

## Your Tasks

1. Set `room_name` to the first item of `session_record` by indexing.
2. Unpack `session_record` into `room` and `start_time`.
