---
title: "Join Messages with +"
slug: join-strings-with-plus
order: 4
language: python
lesson_type: coding
summary: "Join string values with + to make a route message."
seo_title: "Concatenate Strings with + | Python Basics"
seo_description: "Learn how Python joins text with the + operator and how to include spaces in a printed message."
seo_keywords: [python basics, string concatenation, print strings]
---

At the Gear Forge, a route message needs a pathfinder's name and a destination. You have used `print()` to show values. Now you can build one string from several pieces before printing it.

## Join text with `+`

When both sides are strings, `+` **concatenates** them. Simply put, it joins the text in order. Unlike `print("North", "Gate")`, which inserts a space between its arguments, `"North" + "Gate"` produces `NorthGate`. Put the spaces you need inside the quoted pieces.

```python run
keeper = "Mira"
place = "Moon Dock"
print("Super guide " + keeper + " waits at " + place + ".")
```

The result is `Super guide Mira waits at Moon Dock.`. Notice the space after `Super guide` and around `waits at`. Python does not add them for `+`. Concatenation needs strings on both sides. To join a number with a string this way, convert the number into string format first, as in `"Lamps: " + str(3)`. You'll use numeric text conversions again later in this level.

## Your Tasks

1. Set `route_line` so it prints `Pathfinder Adam enters Beacon Ridge.`

Press **Run** to read the line, then **Submit** to check it.
