---
title: "Project: Build an Ability Loadout"
slug: project-workshop-receipts
order: 9
language: python
runtime: pyodide
lesson_type: coding
summary: Combine reusable energy calculation and a named loadout readout.
seo_title: "Project: Build an Ability Loadout | Python Basics"
seo_description: Combine reusable energy calculation and a named loadout readout.
seo_keywords: [python basics, functions and reuse, lantern atlas]
hints:
  - Return values from each function; the supplied print combines them.
---

# Project: Build an Ability Loadout

Before leaving the workshop, prepare a loadout for Cipher Caverns. You'll use one function to calculate its energy and another to write the label.

Both functions should work with the values they receive. For example, changing the number of charges should change the total without requiring you to rewrite the function.

## Your Tasks

1. Complete `loadout_energy(charges, cost)` so it returns `charges * cost`.
2. Complete `loadout_note(name, amount)` so it returns text in the form `name: amount energy`, using its parameters.

Work in `main.py`; the print calls are already supplied. After the first task, Run should show `Loadout energy: 12`, even while the note is unfinished. After the second, it should also show `Lantern pulse: 12 energy`.

Submit to check both functions. You've now built a calculation and a label that can be reused with a different loadout. In the caverns, you'll work with the text on route signs.
