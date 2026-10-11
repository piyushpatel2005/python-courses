---
title: "Define a Beacon Ability: Demo"
slug: define-and-call-demo
order: 1
language: python
runtime: pyodide
lesson_type: coding
summary: Define and call a reusable ability to announce a beacon.
seo_title: "Define a Beacon Ability: Demo | Python Basics"
seo_description: Define and call a reusable ability to announce a beacon.
seo_keywords: [python basics, functions and reuse, lantern atlas]
hints:
  - Edit the text inside print, not the function name.
---

# Define a Beacon Ability: Demo

The workshop's welcome message is an action you'll want to use again. A **function** gives that action a name, so you can run it without copying its code.

Look at `main.py`:

- `def welcome():` defines the function. The colon starts its body.
- The indented `print(...)` belongs to that function.
- `welcome()` calls the function. This is the line that makes the message appear.

Defining a function doesn't run its body. Think of saving a game ability to a shortcut: you still need to activate it.

## Your Tasks

1. Change the destination inside `welcome()` from `North Beacon` to `East Beacon`.

Leave the supplied `welcome()` call in place. Run `main.py` to see `Welcome to the East Beacon`, then Submit to check your change. Next, you'll write the announcement inside a different function.
