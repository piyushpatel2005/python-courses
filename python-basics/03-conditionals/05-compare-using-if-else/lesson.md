---
title: "Win or Lose using if else"
slug: compare-and-branch
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: "Use if and else to choose a message for remaining bread stock."
seo_title: "Python if, elif, else Branches | Python Basics"
seo_description: "You've won the battle so you win the game. Can you code it using a Python conditional?."
seo_keywords: [python if else, python conditionals, decision making in Python]
---

You're at the final stage of fictitious game, The Glorious Gang and you're in the final battle of beating the giant army. If you win the battle, you win the game and you want to print the message on the screen. How do you do that?

This is where `if...else` comes to help. You can run one of the two Python blocks using this conditional flow.

The basic structure of `if..else` looks like this.

```python
if condition:
    ... ...
else:
    ... ...
```

After the `if` keyword, you specify some kind of condition which returns a boolean value `True` or `False`. At the end you add colon ()`:` to open a new code block. Anything indented in this new block is part of the `if` block. Similarly, you write code block for `else` statement. You can write one or more lines in this blocks. For example, in below code, you see multiple lines for the `else` blocks, both indented by 4 spaces. You can indent by any number of spaces, but you have to be consistent in your code file. If you do not indent by the same number of spaces, you will get `IndentationError`.

```python run
army_defeated = True
if army_defeated:
    print("Congraulations! You win)
else:
    print("Sorry, you lost!")
    print("Try again!")
```

You could also combine the knowledge of logical operators to make conditions more complex. For example, if you're health is greater than 10 and `enemy_power < 10`, you win.

Read the branches in `main.py` from top to bottom. It has the same condition structure with two separate checks.

- If `player_health > 10` and `enemy_health < 10`, you win the game
- else you lose


## Your Tasks

1. Set `loaves_left` to `4` while keeping the branches. **Run** should now print `Bake more bread`.

Edit `main.py`, press **Run**, then **Submit**. Next you'll write the branches yourself.
