---
title: Notes in Browser Files
slug: notes-in-browser-files
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: Write and read a workshop note with Python's with open syntax.
seo_title: Python File Handling in Pyodide | Python Basics
seo_description: Practice with open, writing and reading a text file in Pyodide's temporary in-memory browser filesystem.
seo_keywords: [python file handling, with open, pyodide filesystem, read write file]
hints:
  - Use with open("workshop-note.txt", "w") as file: and file.write(text).
  - For reading, use mode "r" and return file.read().
---

The workshop coordinator needs a quick note about where to place supplies. Python can write a text file and read it back. **Here `open()` uses Pyodide's in-memory browser filesystem, not your computer's local files.** The note may disappear when the browser runner resets; this lesson does not download, upload, or edit a file on your device.

`open(path, "w")` creates or overwrites a file; `open(path, "r")` reads an existing file. The `with` block closes the file automatically, even when the block ends because of an error. For example, a different note might be saved as:

```python
with open("supply-label.txt", "w") as file:
    file.write("Markers on table B")
with open("supply-label.txt", "r") as file:
    print(file.read())  # Markers on table B
```

The starter provides two function names and a sample message. Complete one function at a time. On Run, you should see the original note returned by the reader, rather than `None`.

## Your Tasks

1. Complete `write_note(text)` so it writes `text` to `workshop-note.txt` using `with open(..., "w")`.
2. Complete `read_note()` so it reads and returns all text from `workshop-note.txt` using `with open(..., "r")`.
