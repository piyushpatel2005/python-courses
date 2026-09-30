---
title: Where Input Comes From
slug: where-input-comes-from
order: 3
language: python
lesson_type: informational
runtime: pyodide
summary: Understand console input and why browser exercises use provided values.
seo_title: Python input() and Browser Exercises | Python Basics
seo_description: See how input() accepts text in terminal programs and why Pyodide browser lessons use ready-made values instead of blocking prompts.
seo_keywords: [python input, input returns string, pyodide browser, command line]
---

At a command-line workshop sign-up desk, a program might ask the coordinator for a participant's name. Python's `input()` displays a prompt, pauses until someone types a line, and returns **text** (`str`), even if the person typed digits.

This is an **illustration for a terminal program, not a runnable browser exercise**:

```python
name = input("Participant name: ")
seats_text = input("Seats requested: ")
seats = int(seats_text)  # Converts digit text; invalid text raises ValueError.
print(f"{name} reserved {seats} seats")
```

Do **not** copy that snippet into the browser editor: `input()` may wait for a prompt the Pyodide lesson runner cannot supply. In these browser lessons, start with a supplied value such as `seats_text = "2"`; pass it to a function, then Run or Submit without waiting for anyone to type. The `try`/`except ValueError` from the first lesson can handle invalid numeric text if a real terminal user enters it.
