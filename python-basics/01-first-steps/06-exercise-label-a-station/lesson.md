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

Give a beacon both a name and a number. The name is text, so it needs quotation marks. The number is a whole-number value, so it does not need quotes.

Python calls text data a **string**. You can create string type data using single or double qoutes around your data. I would recommend you to be consistent with your choice of single or double quotes. Consistely use the same pattern in your coding style. 

Run below example and you will see that both assignments produce the same results.

```python run
name = 'Charles'
print(name)

name = "Charles"
print(name)
```

A whole number has type **int**, short for integer. I know it sounds kind of different but don't worry too much. You will automatically remember these terminologies when you're done with the course.
Take a look at below example and compare the quoted name with the unquoted age. The integer data type does not need quotes around it.

```python run
name = "Charles"
age = 25
print(name)
print(age)
```

Now it's your turn. Edit the two variable assignments in **main.py**. The print calls are already there. Press **Run** to see the beacon name and number on separate lines, then **Submit**.

## Your Tasks

1. Set `beacon` to `"North beacon"`.
2. Set `beacon_number` to the integer `4`, without quotes.
