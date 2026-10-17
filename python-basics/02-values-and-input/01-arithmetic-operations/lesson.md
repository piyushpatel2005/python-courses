---
title: "Performing Calculations with Python"
slug: arithmetic-operations
order: 1
language: python
lesson_type: interactive
summary: "Perform arithmetic operations using Python operators. These can be used to perform calculations on numeric data."
seo_title: "Arithmetic operators | Python Basics"
seo_description: "Learn how to perform arithmetic calculations in Python programming"
seo_keywords: [python basics, arithmetic operators, arithmetic operations using python, mathematic calculations]
---

In Python, you could perform mathematical calculations using arithmetic operators. These are simple operations you use in everyday calculator application. Let's learn about these.

| Operator | Description |
| --- | --- |
| `+` | Used to perform addition of two numbers |
| `-` | Subtract two numbers |
| `*` | Multiply two numbers |
| `/` | Divide two numbers. This produces result as a float number. |
| `**` | Raise to a power of second number |

```python run
print(2 + 3) # 5
print(5 - 2) # 3
print(2 * 3) # 6
print(4 / 2) # 2.0
print(2 ** 3) # 6
```

Python also provides modulo operator and floor division. Let's understand what they do.

| Operator | Description |
| --- | --- |
| `%` | Modulo operator which returns the remainder of a division operation |
| `//` | Floor division which provides the quotient of a division operation. This returns a whole number (integer) |

```python run
print(8 % 3) # 2
print(8 // 3) # 2
```

```python run 
print(7 % 2)
print(7 // 2)
```