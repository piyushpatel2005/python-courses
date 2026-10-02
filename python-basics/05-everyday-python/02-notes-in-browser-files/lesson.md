---
title: Save a Note at the Shrine
slug: notes-in-browser-files
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: Write and read Ari’s shrine note in a temporary browser file.
seo_title: Python File Handling in Pyodide | Python Basics
seo_description: Practice with open for Ari’s save-shrine note in Pyodide’s in-memory filesystem.
seo_keywords: [python file handling, with open, pyodide filesystem, read write file]
hints:
  - Use with open("atlas-save.txt", "w") as file: and file.write(text).
  - For reading, use mode "r" and return file.read().
---

# Save a note at the shrine

Ari records a clue at the save shrine before the final beacon mission. Python can write and read a text file. **Here `open()` uses Pyodide's in-memory browser filesystem, not your computer's local files.** The note can disappear when the runner resets; this lesson does not download or edit a file on your device.

`open(path, "w")` creates or overwrites a file; `open(path, "r")` reads an existing file. `with` closes the file when its block ends. A different clue might be saved like this:

```python
with open("cave-clue.txt", "w") as file:
    file.write("Follow the blue glow")
with open("cave-clue.txt", "r") as file:
    print(file.read())  # Follow the blue glow
```

Complete one function at a time in `main.py`. Run should show the saved clue instead of `None`.

## Your Tasks

1. Complete `write_note(text)` so it writes `text` to `atlas-save.txt` using `with open(..., "w")`.
2. Complete `read_note()` so it reads and returns all text from `atlas-save.txt` using `with open(..., "r")`. Run and Submit.
