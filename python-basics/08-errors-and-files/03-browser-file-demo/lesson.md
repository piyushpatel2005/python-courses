---
title: Write and Read a Browser File Demo
slug: browser-file-demo
order: 3
language: python
lesson_type: coding
runtime: pyodide
summary: Edit a file note and read it back in Pyodide’s temporary filesystem.
seo_title: "Write and Read a Browser File Demo | Python Basics"
seo_description: Edit a file note and read it back in Pyodide’s temporary filesystem.
seo_keywords: [python file handling, with open, pyodide memory]
---

A helper leaves a note for the next workshop shift. `open(path, "w")` creates or **overwrites** a file; `open(path, "r")` reads an existing one. A `with` block closes it even when the block exits early. The sample file lives in the Pyodide browser runner's **temporary in-memory filesystem**, not on your computer. It may be reset between runs; write before you read within each run. This lesson does not upload, download, or preserve files on your device.

Edit `main.py`: replace the note text with `"Check the north door"`. Run to see the note read back; Submit to check the edit. Next, you'll write the two operations yourself with a different file.

## Your Task

1. Change `note` to `"Check the north door"`; keep the write/read flow intact.
