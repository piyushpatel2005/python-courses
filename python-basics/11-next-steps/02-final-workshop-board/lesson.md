---
title: "Final Game Mission: Open the Exit Gate"
slug: final-workshop-board
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: Build a text game that restores every beacon and opens Adam’s exit gate.
seo_title: "Final Game Mission: Open the Exit Gate | Python Basics"
seo_description: Build a text game that restores every beacon and opens Adam’s exit gate.
seo_keywords: [python final game mission, beacon signals, functions loops dictionaries]
---

The Exit Gate stays locked until every beacon has enough signal strength. Your final program will read commands, charge the known beacons, and report whether Adam can leave the Atlas. The starter supplies a list of player commands, so Run does not wait for keyboard input.

A command looks like `"north:2"`. Accept spaces and lowercase names, but ignore a malformed command, an unknown beacon, or a strength of zero or less. Repeated valid commands add strength. The supplied `beacons` dictionary gives each beacon's required charge.

Work on one helper at a time in `main.py`. Run prints helper checkpoints while `play_mission` is unfinished; an unfinished helper may show `None`. Submit after each task. You do not need classes, enums, recursion, or lambdas.

## Split a command into two parts

`text.split(":", 1)` returns a list, splitting at only the first colon. Check that it has two parts before unpacking. An extra colon stays in the second part, so converting that part with `int()` raises `ValueError`.

Run this small delivery example. Notice the two-item list, the missing separator, and the invalid numbers:

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

For your game, also reject an empty name and strengths of zero or less. Build and Run each helper before moving to the next task.

## Helper checkpoints

`parse_command` returns a `(NAME, strength)` tuple. Strip spaces from the name and uppercase it; convert the strength inside `try`/`except ValueError`. Return `None` for a malformed command, an empty name, or a strength of zero or less. For example, `" north:2 "` becomes `("NORTH", 2)`.

`charge_beacons` starts each known beacon at zero. Loop through the commands, call `parse_command`, and add valid strengths to known names. Ignore invalid commands and unknown names. Return the charge dictionary.

`gate_open` uses a condition and a loop to check every required charge. An empty beacon dictionary returns `False`. A missing or insufficient charge also returns `False`; return `True` only when all requirements are met.

`play_mission` uses your helpers and returns a list of lines. Keep dictionary order and format each beacon as `"<NAME>: <charge>/<required>"`. Add one final line:

- On a win: `"Exit Gate: OPEN - Adam leaves the Lantern Atlas with every beacon bright."`
- Otherwise: `"Exit Gate: LOCKED - Restore every beacon to continue."`

## Your Tasks

1. Complete `parse_command(command)` to return a valid command tuple or `None`.
2. Complete `charge_beacons(beacons, commands)` to return accumulated charges using `parse_command`.
3. Complete `gate_open(beacons, charges)` to check the gate condition.
4. Complete `play_mission(beacons, commands)` to return the report and ending using your helpers.

Once the full mission runs, remove one valid command to try the locked ending. Restore the command and Submit again to finish.
