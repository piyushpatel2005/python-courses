---
title: "Exercise: Save and Read a Message"
slug: exercise-save-a-message
order: 4
language: python
lesson_type: coding
runtime: pyodide
summary: Implement separate functions to write and read a temporary text file.
seo_title: "Exercise: Save and Read a Message | Python Basics"
seo_description: Implement separate functions to write and read a temporary text file.
seo_keywords: [python write read file exercise, with open]
---

For a different shift, save a supply reminder. The preceding demo showed `with open` writing and reading a file. Here the path is `supply-reminder.txt`. You do not need terminal input or a real device file; the browser filesystem is temporary. Reading a missing file raises `FileNotFoundError`, so the supplied sample writes before it reads. Mode `"w"` replaces earlier content, while mode `"r"` only reads.

Edit `main.py`, Run to view the saved reminder, then Submit. The tests write their own reminders before reading, so each task can be checked on its own.

## Your Tasks

1. Complete `save_reminder(text)` with `with open("supply-reminder.txt", "w", encoding="utf-8")` and write `text` into the file.
2. Complete `load_reminder()` with read mode and return the entire text from `supply-reminder.txt`.
