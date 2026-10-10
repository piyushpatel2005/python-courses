---
title: 'Exercise: Save a Beacon Signal'
slug: exercise-save-a-message
order: 4
language: python
lesson_type: coding
runtime: pyodide
summary: 'Write and read shrine signals in a temporary browser file.'
seo_title: 'Exercise: Save a Beacon Signal | Python Basics'
seo_description: 'Write and read shrine signals in a temporary browser file.'
seo_keywords: [python write read file exercise, with open]
---

Turn the previous write-and-read example into two reusable helpers. One saves a signal; the other returns the saved text.

Use `"w"` to replace the previous contents and `"r"` to read them. Keep each file operation inside a `with open` block. As before, the file is temporary and does not download to your device.

Edit `main.py`. The supplied calls save a signal before loading it. Run to see the restored text, then Submit.

## Your Tasks

1. Complete `save_signal(text)` to write `text` to `shrine-save.txt` using `with open(..., "w", encoding="utf-8")`.
2. Complete `load_signal()` to return the entire file using read mode and `with open`.
