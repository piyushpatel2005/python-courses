---
title: "Exercise: Label a Beacon"
slug: exercise-label-a-station
order: 6
language: python
lesson_type: coding
summary: "Assign a beacon name and number for Adam’s map."
seo_title: "Exercise: Label a Beacon | Python Basics"
seo_description: "Assign a beacon name and number for Adam’s map."
seo_keywords: [python basics, first steps, lantern atlas]
---

Give a beacon both a name and a number. The name is text, so it needs quotation marks. The number is a whole-number value, so it does not.

Python calls text a **string**. Single and double quotes both work, as long as you use the same kind at each end. Run this example; both assignments produce the same name.

```python run
name = 'Charles'
print(name)

name = "Charles"
print(name)
```

A whole number has type **int**, short for integer. Compare the quoted name with the unquoted age:

```python run
name = "Charles"
age = 25
print(name)
print(age)
```

Now edit the two assignments in **main.py**. The print calls are already there. Press **Run** to see the beacon name and number on separate lines, then **Submit**.

## Your Tasks

1. Set `beacon` to `"North beacon"`.
2. Set `beacon_number` to the integer `4`, without quotes.
