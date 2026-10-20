---
title: "Count Down with while"
slug: repeat-with-while
order: 1
language: python
runtime: pyodide
lesson_type: coding
summary: "See a while loop count down the minutes on a timer."
seo_title: "Python while Loop Countdown | Python Basics"
seo_description: "Use a changing condition and a countdown to understand when a while loop stops."
seo_keywords: [python while loop, countdown, loop condition]
---

In the previous section, a condition helped your program choose what to do once. Now a kitchen timer needs to print its remaining minutes repeatedly. Instead of writing one print call per minute, `while` repeats an indented block while its condition is true.

Before each turn, Python checks `minutes_left > 0`. The body prints the count and subtracts one. `minutes_left -= 1` means `minutes_left = minutes_left - 1`. At zero, Python skips the body and runs the unindented `print("Timer done")`.

![Flowchart: check remaining minutes, print and subtract one while positive, otherwise finish](while-loop-flow.svg "A countdown checks before each turn")

The starter prints `Minutes left 3`, `Minutes left 2`, `Minutes left 1`, then `Timer done`, each on a new line.

## Your Tasks

1. Start `minutes_left` at `4`, so the countdown begins with `Minutes left 4`.

Edit `main.py`, press **Run**, then **Submit**. Keep the subtraction inside the loop or the timer will never reach zero.
