---
title: 'Exercise: Save a message'
slug: exercise-save-a-message
order: 4
language: python
lesson_type: coding
runtime: pyodide
summary: 'Write and read a short message in a temporary file.'
seo_title: 'Exercise: Save a message | Python Basics'
seo_description: 'Write and read a short message in a temporary file.'
seo_keywords: [python write read file exercise, with open]
---

Turn the previous note example into two functions. `save_message(text)` writes a message, and `load_message()` reads it back. Use `"w"` to replace old contents and `"r"` to read them. Each function should use a `with open` block.

The starter calls the save function before the load function. The file exists only in the running environment for this exercise; writing it does not download a file to your device. The tests also try a different message, so write the text passed to the function rather than the visible example alone.

## Your Tasks

1. Complete `save_message(text)` to write `text` to `message.txt` using `with open(..., "w", encoding="utf-8")`.
2. Complete `load_message()` to return the entire contents of `message.txt` using read mode and `with open`.

Edit `main.py`. Press **Run** to see `Message: Please call before delivery`, then **Submit**.
