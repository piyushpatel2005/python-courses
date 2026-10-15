---
title: Route shop commands
slug: command-router
order: 12
language: python
lesson_type: coding
summary: Connect product listing, cart operations, checkout, and order queries through
  one command method.
seo_title: Route shop commands | Python OOP practice
seo_description: Connect product listing, cart operations, checkout, and order queries
  through one command method.
seo_keywords:
  - Python
  - command router
  - object oriented programming
hints:
  - Validate the token count in each branch before reading arguments.
---

# Route shop commands

Connect product listing, cart operations, checkout, and order queries through one command method.

The supplied Shop methods already perform individual actions. Your router chooses one based on a whitespace-separated command. `split()` accepts extra spaces; commands remain case-sensitive. Check both the command name and argument count before calling a handler. In the next lesson, you will add a session layer that turns expected errors into messages. For now, malformed commands raise `ValueError` and unknown identifiers retain `KeyError`. All handlers return strings rather than printing, so they can be tested without reading the Console.

The grammar is `products`, `add SKU Q`, `remove SKU`, `cart`, `checkout`, `orders`, `track ID`, `show ID`, and `status ID STATE`. `show` renders an invoice; `orders` lists IDs in creation order or returns `No orders`. Checkout chooses the next `O1`, `O2`, ... ID and registers its result.

Most command names match methods directly; cart is the exception and calls cart_text(). Check len(parts) before indexing arguments so a short command produces the documented ValueError rather than an accidental IndexError. The supplied methods manage state, so execute should not duplicate their calculations.

## A smaller example

The help router returns a result only for the exact supported token list.

```python
def choose(command):
    parts = command.split()
    if parts == ["help"]:
        return "Available: help"
    raise ValueError("unknown command")
```

## Your Tasks

1. Implement `Shop.execute(command)` to dispatch the documented grammar to the supplied same-purpose handlers (use `int` for Q). Return their strings. Reject unknown commands, empty input, and wrong argument counts with `ValueError("invalid command")`; allow conversion, lookup, and domain errors to propagate.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished probe lists the Mug with `$12.50`. Press **Submit** to check the behavior with other inputs.
