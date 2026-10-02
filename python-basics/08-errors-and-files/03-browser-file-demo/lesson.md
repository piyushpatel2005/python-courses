---
title: 'Demo: Write a Shrine Save'
slug: browser-file-demo
order: 3
language: python
lesson_type: coding
runtime: pyodide
summary: 'Write and read a temporary shrine note with open().'
seo_title: 'Demo: Write a Shrine Save | Python Basics'
seo_description: 'Write and read a temporary shrine note with open().'
seo_keywords: [python file handling, with open, pyodide memory]
---

Ari leaves a save note at the shrine. `open(path, "w")` creates or overwrites it, and `open(path, "r")` reads it back. A `with` block closes each file. In the browser this is Pyodide’s temporary filesystem, not a file saved to your device; always write before reading within the run.

Edit `main.py`: change the note to `"Light the east beacon"`. Press **Run** to read the saved note, then **Submit**. The next exercise builds the write/read functions with different text.

## Your Task

1. Change `note` to `"Light the east beacon"` while preserving the write/read flow.
