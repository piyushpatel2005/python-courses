---
title: "Project: Build FizzBuzz"
slug: project-fizzbuzz
order: 8
language: python
lesson_type: coding
summary: "Use ordered if/elif branches and divisibility checks to print FizzBuzz."
seo_title: "Build a FizzBuzz Program | Python Basics"
seo_description: "Practice modulo, logical and, and ordered Python conditions for numbers 1 through 15."
seo_keywords: [python fizzbuzz, conditional project, modulo, if elif]
---

FizzBuzz is a number-labeling game. For each number from 1 through 15, print one of these line.

If the number is:
- Divisible by both 3 and 5, print `FizzBuzz`.
- Divisible by 3 but not 5, `Fizz`.
- Divisible by 5 but not 3, `Buzz`.
- Otherwise: the number itself.

You can use the modulo operator (`%`) to check if a number is divisible by another number. For example, if a `number` is divisible by 2, `number % 2 == 0` operation will result in `True`. 

The supplied loop in `main.py` provides numbers 1 through 15 and prints each label. You aren't asked to write or change the loop here; the next section teaches loops. Work only on the conditional chain inside it. `label = str(number)` is the supplied fallback.

## Your Tasks

1. Add an `if` branch that uses `and` to check divisibility by both 3 and 5; set `label` to `"FizzBuzz"`.
2. Add an `elif` branch for divisibility by 3; set `label` to `"Fizz"`.
3. Add an `elif` branch for divisibility by 5; set `label` to `"Buzz"`.

Press **Run** after each branch, then **Submit**. 
