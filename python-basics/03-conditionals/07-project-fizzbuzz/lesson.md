---
title: "Project: Build FizzBuzz"
slug: project-fizzbuzz
order: 7
language: python
lesson_type: coding
summary: "Use ordered if/elif branches and divisibility checks to print FizzBuzz."
seo_title: "Build a FizzBuzz Program | Python Basics"
seo_description: "Practice modulo, logical and, and ordered Python conditions by printing FizzBuzz for numbers 1 through 15."
seo_keywords: [python fizzbuzz, conditional project, modulo, if elif]
---

The Golden Gate has one last challenge before the section quiz: turn a sequence of numbers into a short signal. Your program will print one line for each number from 1 through 15.

- A number divisible by **both** 3 and 5 prints `FizzBuzz`.
- A number divisible by **only** 3 prints `Fizz`.
- A number divisible by **only** 5 prints `Buzz`.
- Every other number prints the number itself.

You used `%` earlier to find a remainder. `number % 3 == 0` means 3 divides the number with nothing left over. To check both divisors, join two such comparisons with `and`.

## Check the combined case first

For 15, both `15 % 3 == 0` and `15 % 5 == 0` are true. If you check 3 alone first, Python takes that branch and prints only `Fizz`. Put the combined case first, then use `elif` for the separate cases. The supplied `label = str(number)` is the fallback when none matches.

`main.py` already contains a `for` line that supplies the numbers and a `print(label)` line. You do not need to edit either line. The loop repeats your decision for each number; the next section teaches you how to write loops yourself. For now, focus on the conditional chain inside it. Indent your `if` under the loop, and indent each assignment under its branch.

## Your Tasks

1. Add an `if` branch for numbers divisible by both 3 and 5 using `and`; set `label` to `"FizzBuzz"`.
2. Add an `elif` branch for numbers divisible by 3; set `label` to `"Fizz"`.
3. Add an `elif` branch for numbers divisible by 5; set `label` to `"Buzz"`.

Edit `main.py`, press **Run** after each branch, then **Submit**. With only the first branch finished, 15 should print `FizzBuzz` while 3 still prints `3`. After all three, the last three lines for 13, 14, and 15 should be `13`, `14`, and `FizzBuzz`.
