---
title: Launch the console shop
slug: shop-main
order: 14
language: python
lesson_type: coding
summary: Wire a fresh shop into a callable main entrypoint and print its session transcript.
seo_title: Launch the console shop | Python OOP practice
seo_description: Wire a fresh shop into a callable main entrypoint and print its session
  transcript.
seo_keywords:
  - Python
  - shop main
  - object oriented programming
hints:
  - Choose defaults with commands is None, not with a truthiness check.
---

# Launch the console shop

Wire a fresh shop into a callable main entrypoint and print its session transcript.

The earlier stages built the behavior; this last function chooses the starting catalog and starts a session. The supplied `DEFAULT_COMMANDS` walks through listing products, editing a cart, buying items, and viewing an order. `main(commands=None)` uses that script only when no commands were supplied. An explicitly empty list must stay empty. Construct a fresh Shop each call so repeat runs start at order O1.

The guard at the bottom already calls `main()`. It runs when you press Run or execute the file as a script, but importing the file for tests does not launch the session. Keep business logic in the classes and helpers; main should only assemble, run, print, and return the transcript.

Run the completed main twice and compare the order identifiers. Each call creates new in-memory state, so both sessions begin with O1. Returning the same list that you print also makes the function useful to another Python caller without requiring that caller to capture Console output.

## A smaller example

The launch function prints its results only when it is called.

```python
def launch(messages):
    for message in messages:
        print(message)
    return messages

if __name__ == "__main__":
    launch(["Ready"])
```

## Your Tasks

1. Implement `main(commands=None)` to create a fresh Shop from the supplied `PRODUCTS`, run `DEFAULT_COMMANDS` only for `None` (otherwise use commands), print every returned response in order, and return the response list. Use the supplied guarded call unchanged.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The completed default transcript ends with the Mug invoice and `Total: $25.00`. You now have a complete in-memory console shop. Press **Submit** to check the behavior with other inputs.
