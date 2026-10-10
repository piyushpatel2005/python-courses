---
title: "Exercise: Read an Exit Checkpoint"
slug: exercise-read-session
order: 8
language: python
lesson_type: coding
runtime: pyodide
summary: Index and unpack a fixed exit checkpoint record.
seo_title: "Exercise: Read an Exit Checkpoint | Python Basics"
seo_description: Index and unpack a fixed exit checkpoint record.
seo_keywords: [python basics, lists and tuples, lantern atlas]
---

Read the record at the ridge exit. Its marker and signal time are stored together in `exit_record`. First read just the marker by index; then unpack both values into separate names.

Edit `main.py` and use the supplied printout to check each result with Run. Submit after each task. This is the ridge exit, not the final Exit Gate; the Map Archive comes next.

## Your Tasks

1. Set `marker_name` to the first element of `exit_record` by indexing.
2. Unpack `exit_record` into `marker` and `signal_time`.
