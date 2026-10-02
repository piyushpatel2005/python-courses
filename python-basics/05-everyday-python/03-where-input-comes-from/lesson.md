---
title: Where Input Comes From
slug: where-input-comes-from
order: 3
language: python
lesson_type: informational
runtime: pyodide
summary: Understand terminal input and why Ari’s browser missions use supplied values.
seo_title: Python input() and Browser Exercises | Python Basics
seo_description: Learn why Python input returns text and why Pyodide missions use provided values.
seo_keywords: [python input, input returns string, pyodide browser, command line]
---

# Where input comes from

In a terminal version of The Lantern Atlas, a player could type Ari’s next move. Python's `input()` displays a prompt, pauses for a line, and returns **text** (`str`), even when the player types digits.

This is an **illustration for a terminal program, not a runnable browser exercise**:

```python
hero = input("Hero name: ")
energy_text = input("Beacon energy: ")
energy = int(energy_text)  # Invalid text raises ValueError.
print(f"{hero} carries {energy} energy")
```

Do **not** copy this into the browser editor: `input()` may wait for a prompt the Pyodide runner cannot supply. Browser missions start with a value such as `energy_text = "2"`; pass it to a function, then Run or Submit. The `try` / `except ValueError` from the save-shrine lesson can handle invalid text in a real terminal game.
