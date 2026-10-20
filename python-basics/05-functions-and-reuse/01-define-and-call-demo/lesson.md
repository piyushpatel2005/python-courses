---
title: "Define and Call a Welcome Function: Demo"
slug: define-and-call-demo
order: 1
language: python
runtime: pyodide
lesson_type: coding
summary: Change a welcome function and see when its body runs.
seo_title: "Define and Call a Welcome Function: Demo | Python Basics"
seo_description: Change a welcome function and see when its body runs.
seo_keywords: [python basics, functions and reuse, functions, defining functions, function calls]
hints:
  - Change the text inside print, not the function name.
---

# Define and call a welcome function

A workshop has a welcome message you'll need whenever someone arrives. A **function** gives those instructions a name so you can call them more than once.

Look at `main.py`:

- `def welcome():` defines the function. The colon starts its body.
- The indented `print(...)` belongs to the function.
- `welcome()` calls it. Without that call, the message would not appear.

Run the starter. It prints `Welcome to the morning workshop` because the function is called below its definition.

## Your Tasks

1. Change the message inside `welcome()` from `morning workshop` to `afternoon workshop`.

Leave the supplied call in place. Run `main.py` to see `Welcome to the afternoon workshop`, then Submit. Next you'll write the body of a different announcement function.
