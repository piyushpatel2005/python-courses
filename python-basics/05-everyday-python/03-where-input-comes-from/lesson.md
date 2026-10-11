---
title: Where Input Comes From
slug: where-input-comes-from
order: 3
language: python
lesson_type: informational
runtime: pyodide
summary: Understand terminal input and why Adi’s browser missions use supplied values.
seo_title: Python input() and Browser Exercises | Python Basics
seo_description: Learn why Python input returns text and why Pyodide missions use provided values.
seo_keywords: [python input, input returns string, pyodide browser, command line]
---

# Where input comes from

In a terminal version of The Lantern Atlas, the player could type a hero name and an energy reading. Python's `input()` displays a prompt and waits for a line of text. It returns a string even when the player types digits.

This example is for a terminal program, not the browser editor:

```python
hero = input("Hero name: ")
energy_text = input("Beacon energy: ")
energy = int(energy_text)  # Invalid text raises ValueError.
print(f"{hero} carries {energy} energy")
```

Notice the separate conversion step. `input()` collects the energy as text; `int()` turns that text into a number. If the player types `unknown`, the conversion raises `ValueError`. The `try` / `except ValueError` pattern from the beacon-reading lesson could handle that case.

Keep this example out of the browser editor, where a terminal prompt may not be available. The browser missions supply values such as `energy_text = "2"` instead. You can pass those values to a function and use Run or Submit without waiting for someone to type a response.
