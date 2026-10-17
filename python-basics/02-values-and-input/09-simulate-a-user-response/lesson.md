---
title: "Read a Pathfinder Name"
slug: simulate-a-user-response
order: 9
language: python
lesson_type: coding
summary: "Use a browser-safe prefilled response as a name."
seo_title: "Read a Pathfinder Name | Python Basics"
seo_description: "Use a browser-safe prefilled response as a name."
seo_keywords: [python basics, values and input, lantern atlas]
---

A program running in a terminal can ask for a name with `input("Name: ")`. It pauses while the person types, then returns their response as a string.

Create a file named `user_response.py` in your local system and add below code.

```python
pathfinder = input("What's your name? ")
print(f"Welcome to next level, {pathfinder}!")
```

Now, you can execute this code in your terminal using `python user_response.py`. When it prompts for your name, type your name and hit Enter.

This distinction matters for numbers too. A terminal user who types digits still gives `input()` a string. You would convert that text with `int()` or `float()` before doing arithmetic, just as you did in the previous exercise.

Keep the supplied f-string and change the name. Press **Run** to see `Gear ready for Adam`, then **Submit**.

## Your Tasks

1. Set `pathfinder` to `"Adam"`.
