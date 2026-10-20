---
title: "Final project: Workshop registration report"
slug: final-workshop-board
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: Process workshop seat requests and print a registration report with totals and status.
seo_title: "Python Final Project: Workshop Registration Report"
seo_description: Build a small in-memory workshop registration report with command parsing, seat limits, totals, and status.
seo_keywords: [python final project, workshop registration, dictionaries, functions, loops]
---

A community center offers a pottery workshop with 3 seats and a drawing workshop with 2. The coordinator has a list of seat requests and needs a report before registration closes. This program works on the supplied commands in memory; it does not take keyboard input or save bookings.

The `workshops` dictionary maps uppercase names to seat capacities. A command such as `"pottery:2"` requests two seats. Accept extra spaces and lowercase names. Ignore malformed commands, unknown workshops, nonpositive quantities, and a request that would exceed the remaining seats. A request is accepted in full or ignored; never count more bookings than the capacity. Repeated valid requests for the same workshop add together.

Build one helper at a time in `main.py`. **Run** shows a sample from each helper until `registration_report` is complete; an unfinished helper may print `None`. **Submit** checks each numbered task. You need functions, strings, conditions, loops, and dictionaries, but not classes, recursion, or lambdas.

## Reading a request

`text.split(":", 1)` splits at the first colon. Check for two parts before unpacking. A second colon stays in the quantity, where `int()` raises `ValueError`. This separate delivery example shows the pieces:

```python run
for text in [" dock :3", "dock", "dock:3:4", "dock:many"]:
    parts = text.split(":", 1)
    print(parts)
    if len(parts) != 2:
        print("Missing separator")
        continue
    place, amount_text = parts
    try:
        amount = int(amount_text)
        print(place.strip().upper(), amount)
    except ValueError:
        print("Invalid amount")
```

For a workshop request, also reject an empty name and a quantity of zero or less.

## Helper checkpoints

`parse_command` returns a `(NAME, quantity)` tuple. Strip spaces from the name, uppercase it, and convert the quantity inside `try`/`except ValueError`. Return `None` if the command is malformed. For example, `" pottery:2 "` becomes `("POTTERY", 2)`.

`book_seats` starts every known workshop at zero bookings. For each command, call `parse_command`; ignore invalid requests and unknown names. Add a request only if the new count would not exceed that workshop's capacity. Return the bookings dictionary without changing `workshops`.

`all_full` checks every workshop with a loop. It returns `True` only if there is at least one workshop and each has reached its capacity. A missing booking count is treated as zero. The supplied capacities are positive integers.

`registration_report` calls your helpers and returns a list of lines in dictionary order. Format each workshop as `"<NAME>: <booked>/<capacity> seats booked"`. Follow those lines with `"Total seats: <booked>/<capacity> booked"`, then one of these statuses:

- All workshops full: `"Registration: FULL - All workshop seats are booked."`
- Seats remain: `"Registration: OPEN - Seats are still available."`
- No workshops listed: `"Registration: NO WORKSHOPS - Add a workshop first."`

For the supplied commands, the pottery requests `2` and `1` fill its 3 seats; the drawing request fills its 2 seats. The invalid command and request for an unknown workshop do not change the totals.

## Your Tasks

1. Complete `parse_command(command)` to return a valid request tuple or `None`.
2. Complete `book_seats(workshops, commands)` to accumulate valid requests without exceeding any capacity; use `parse_command`.
3. Complete `all_full(workshops, bookings)` to check whether every listed workshop is full, returning `False` for an empty dictionary.
4. Complete `registration_report(workshops, commands)` to return the workshop lines, combined total, and appropriate status using your helpers.

Edit `main.py` and **Run** after each helper. When the report is finished, you should see `POTTERY: 3/3 seats booked`, `DRAWING: 2/2 seats booked`, `Total seats: 5/5 booked`, and the `FULL` status. Remove `"DRAWING:2"` temporarily to see the `OPEN` status; restore it before **Submit**.
