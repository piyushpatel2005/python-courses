---
title: "Level 1: Spawn Camp"
slug: welcome-to-python
order: 1
language: python
lesson_type: interactive
summary: "Learn to run Python and print the first lines of Adi’s route."
seo_title: "Level 1: Spawn Camp | Python Basics"
seo_description: "Learn to run Python and print the first lines of Adi’s route."
seo_keywords: [python basics, first steps, lantern atlas]
---

Adi is a pathfinder in **The Lantern Atlas**, a text-based game whose beacons have gone dark. You will write the messages and small programs that help Adi find the way. At Spawn Camp, start with output, variables, and a few supplies.

## A little background

Guido van Rossum created Python in the early 1990s. This course uses Python 3. Older tutorials may use Python 2, which is no longer supported; use Python 3 examples as you learn.

Python is a general-purpose language. People use it for websites, data analysis and machine learning, image processing, desktop applications, networking, automation, and games. Here, a small text-based game gives us a reason to practice without needing graphics or a game engine.

## What working in Python feels like

Python code often reads closely to the steps you want a program to take. You can run a short program, inspect its output, and change one line to see what happens.

A few features are worth knowing now. The later lessons will give you practice with them:

- You can assign a value to a variable without declaring its type first. This is called **dynamic typing**; it does not mean dynamic programming, which is a different idea.
- Python is open source and free to use. Programs can run on Windows, macOS, and Linux, though operating-system-specific code may need changes.
- A Python interpreter runs your code. You do not normally perform a separate compilation step yourself. The usual Python implementation does compile code to an intermediate form internally, so it is more than a line-by-line translation into machine code.
- Python manages memory automatically, including reclaiming objects that are no longer needed.
- Its standard library and additional packages provide tools for common jobs, so you do not have to write everything yourself.

You do not need to memorize that list before writing your first line.

## Print a message

`print()` displays a value in the console, the area where program output appears. Put text inside quotation marks and place it between the parentheses.

Press **Run** below. You should see `Hello there`, without quotation marks.

```python run
print("Hello there")
```

The quotation marks tell Python where the text begins and ends. They are part of the code, not part of the message it prints.

Run this example too:

```python run
print("Hey Adi, Welcome to Spawn Camp")
```

The next lesson gives you an editor so you can change the camp message yourself.
