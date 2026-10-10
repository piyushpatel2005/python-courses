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
seo_keywords: [python file handling, with open, temporary browser files]
---

Leave a short save note at the shrine, then read it back. `open(path, "w")` creates a file or replaces its contents. `open(path, "r")` opens an existing file for reading.

A `with` block closes the file when the block ends. These files are temporary browser files, not downloads to your device. The starter writes before it reads so each Run has the file it needs.

Change `note` in `main.py` to `"Light the east beacon"`. Run to see the text read back from the file, then Submit.

## Your Task

1. Change `note` to `"Light the east beacon"` while preserving the write/read flow.
