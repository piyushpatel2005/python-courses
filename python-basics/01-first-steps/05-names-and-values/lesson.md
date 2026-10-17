---
title: "Name a Map Location"
slug: names-and-values
order: 5
language: python
lesson_type: coding
summary: "Assign a new string value to a location variable."
seo_title: "Name a Map Location | Python Basics"
seo_description: "Assign a new string value to a location variable."
seo_keywords: [python basics, first steps, lantern atlas]
---

Programs need to remember information for later processing. A calculator needs its input numbers and result. A map application needs the name of the current location. You can store information in programming in general using variables. You assign a value to a variable name.

The assignment `room = "Spawn Camp"` makes the name `room` refer to the string `"Spawn Camp"`. In the diagram below, the name and value are separate. The arrow shows that the variable `name` refers to value stored in the variable, which in this case is `"Spawn Camp"`.

![Variable and the value](python-variable-reference.svg "A name refers to a value")

To print the value of a variable, pass the variable name to `print()` without quotes:

```python run
room = "Spawn Camp"
print(room)
```

It prints `Spawn Camp`, not `room`. Writing `print("room")` would print the word itself.

## Choose a useful name

There are some rules we have to abide by for naming our variables.

- Variable names are case-sensitive: `room`, `Room`, and `ROOM` are different names. 
- A name cannot start with a digit or contain spaces. 
- For names with several words, Python programmers usually use **snake_case**, such as `current_room`.

Short names like these provide no idea what `a` or `n` stores. So, always use descriptive and meaningful names for your variables.

```python
a = "Good morning"
n = "Eddie"
```

The following names explain what it stores. Run this example to see that `print()` can display two values, separated by a space. You can see that you can print multiple items using the same `print()` function.

```python run
greeting = "Good morning"
name = "Eddie"
print(greeting, name)
```

In some literature, you may hear the terms *defining* and *initializing* a variable. In some programming languages, variables are created in two steps. First, you provide what kind of data the variable is going to store, also called defining a variable. Next, you assign a value to this variable for the first time in your code, also known as initializing a variable. In Python, these two steps are grouped together into single step. You also don't need to specify what type of data the variable is going to store.

You can re-assign the variable to something else later in your code.

```python run
name = "Eddie"
print(name)
name = "Aisha"
print(name)
```

In **main.py**, the print call is already supplied. Leave it in place and change the location assignment. Press **Run** to see `Beacon Ridge`, then **Submit**.

## Your Tasks

1. Set `room` to `"Beacon Ridge"`.
