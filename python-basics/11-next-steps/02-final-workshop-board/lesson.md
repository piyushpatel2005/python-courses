---
title: "Final Game Mission: Open the Exit Gate"
slug: final-workshop-board
order: 2
language: python
lesson_type: coding
runtime: pyodide
summary: Build a text game that restores every beacon and opens Ari’s exit gate.
seo_title: "Final Game Mission: Open the Exit Gate | Python Basics"
seo_description: Build a text game that restores every beacon and opens Ari’s exit gate.
seo_keywords: [python final game mission, beacon signals, functions loops dictionaries]
---

Ari has reached the Exit Gate, but it stays locked until **every** beacon holds at least its required signal strength. Build the last text-based mission of *The Lantern Atlas*: decode commands, charge known beacons, check the gate, then print the ending. The list of commands is a scripted player turn sequence so browser Run never waits for `input()`.

Each command has the form `"north:2"`; spaces and lowercase names are allowed. A bad command, an unknown beacon, or a non-positive strength must not crash the game or charge a beacon. Repeated valid commands add strength. The supplied dictionary maps beacon names to their required strengths. The gate opens only if there is at least one beacon **and all** requirements are met. No class, enum, recursion, or lambda is required.

Edit `main.py`, Run after each task, and Submit. While `play_mission` is unfinished, Run prints supplied helper checkpoints; incomplete helpers show `None`. When finished, Run prints a line for each beacon followed by a clear win or locked ending. Try removing a scripted command to see the locked outcome, then restore it before submitting.

## Your Tasks

1. Complete `parse_command(command)` using string operations and `try`/`except ValueError`: return `(NAME, strength)` with the name stripped and uppercased for one valid positive `name:number` command; return `None` for malformed, empty-name, or non-positive commands.
2. Complete `charge_beacons(beacons, commands)` with a loop and dictionary: start each known beacon at zero, use `parse_command` for each command, ignore invalid or unknown names, and add valid signal strengths. Return the charge dictionary.
3. Complete `gate_open(beacons, charges)` with a condition and loop: return `True` only when the beacon dictionary is nonempty and every beacon's charge meets its requirement; otherwise return `False`.
4. Complete `play_mission(beacons, commands)` using your helpers: return one `"<NAME>: <charge>/<required>"` line per beacon in dictionary order, then `"Exit Gate: OPEN - Ari leaves the Lantern Atlas with every beacon bright."` on a win or `"Exit Gate: LOCKED - Restore every beacon to continue."` otherwise.

When all beacons are bright, Ari can leave the Atlas; if one remains dim, the gate waits without ending the game in an error.
