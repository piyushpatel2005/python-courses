---
title: "Divide Beacon rooms"
slug: calculate-with-numbers
order: 2
language: python
lesson_type: coding
summary: "Use floor division and remainder to fill light up rooms."
seo_title: "Divide Beacon rooms | Python Basics"
seo_description: "Use floor division and remainder to lighten up rooms."
seo_keywords: [python basics, values and input, lantern atlas]
---

At the **Gear Forge**, each room needs 4 lamps to light up the whole room. With 17 lamps, you can fill four rooms and still will have one extra lamp left. The starter calculates both amounts from the same values.

`lamps // lamp_per_room` uses **floor division**. For these positive whole numbers, it counts complete groups of four. `rooms % lamp_per_room` uses the **remainder** operator to find what is left after those groups.

## Your Tasks

In **main.py**, leave the other code as it is.

1. Set `rooms` to `23`.
