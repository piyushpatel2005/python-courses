---
title: Save a Note at the Shrine
slug: notes-in-browser-files
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: Write and read Adi’s shrine note in a temporary browser file.
seo_title: Python File Handling in Pyodide | Python Basics
seo_description: Practice with open for Adi’s save-shrine note in Pyodide’s in-memory filesystem.
seo_keywords: [python file handling, with open, pyodide filesystem, read write file]
hints:
  - Use with open("atlas-save.txt", "w") as file: and file.write(text).
  - For reading, use mode "r" and return file.read().
---

# Save a note at the shrine

Adi needs to leave a clue at the save shrine. You'll write the clue to a text file, then read it back.

Files in this exercise are temporary and stay inside the browser workspace. They may disappear when the workspace resets. Writing a note here does not download a file or change files on your device.

Use `open(path, "w")` to create a file or replace its contents. Use `open(path, "r")` to read an existing file. The `with` statement closes the file when you leave its indented block.

Here is a separate clue saved in `cave-clue.txt`:

```python
with open("cave-clue.txt", "w") as file:
    file.write("Follow the blue glow")
with open("cave-clue.txt", "r") as file:
    print(file.read())  # Follow the blue glow
```

`file.write(text)` stores the text you give it. `file.read()` returns the file's contents as a string, including any line breaks.

In `main.py`, the call to `write_note()` and the print call are already supplied. Complete the two functions in order. After the first, Run will still show `Saved clue: None`: the note is written, but `read_note()` does not return it yet. After both, Run should show `Saved clue: Follow the silver path`. Submit checks each function separately.

## Your Tasks

1. Complete `write_note(text)` to write `text` to `atlas-save.txt` using `with open(..., "w")`.
2. Complete `read_note()` to return all the text in `atlas-save.txt` using `with open(..., "r")`.
