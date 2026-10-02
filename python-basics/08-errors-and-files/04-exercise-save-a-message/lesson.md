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

Ari needs a separate shrine save for a beacon signal. The previous demo wrote and read one note; here you implement both actions as functions. `"w"` replaces previous contents, and `"r"` reads existing contents. The browser file is temporary and does not download to your device.

Edit `main.py`, **Run** to see the restored signal, then **Submit**.

## Your Tasks

1. Complete `save_signal(text)` to write `text` to `shrine-save.txt` using `with open(..., "w", encoding="utf-8")`.
2. Complete `load_signal()` to return the entire file using read mode and `with open`.
