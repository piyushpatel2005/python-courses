---
title: 'Write and read a temporary note'
slug: browser-file-demo
order: 3
language: python
lesson_type: coding
runtime: pyodide
summary: 'Write a note with open() and read it back in the same run.'
seo_title: 'Write and read a temporary note | Python Basics'
seo_description: 'Write a note with open() and read it back in the same run.'
seo_keywords: [python file handling, with open, temporary file]
---

A short pickup note can be written to a file and read back. `open(path, "w")` creates a file or replaces its contents. `open(path, "r")` reads an existing file. Inside each `with` block, the name `file` refers to the open file; Python closes it when the block ends.

The starter writes before reading, so it has a file to read each time you run it. In this browser exercise, the file is held in the running Python environment. It is not a download or a lasting file on your computer. Keep the write and read steps so `saved_note` comes from the file, not a copy of the text variable.

## Your Task

1. Change `note` to `"Order ready for pickup"` while keeping the write/read flow.

Edit `main.py`, press **Run** to see the note read back, then **Submit**.
