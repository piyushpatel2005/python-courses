---
title: "Project: Build Adam’s Gear HUD"
slug: exercise-build-a-ticket
order: 8
language: python
lesson_type: coding
summary: "Combine response text, conversion, multiplication, and formatting."
seo_title: "Project: Build Adam’s Gear HUD | Python Basics"
seo_description: "Combine response text, conversion, multiplication, and formatting."
seo_keywords: [python basics, values and input, lantern atlas]
---

Put the Gear Forge skills together in a small heads-up display, or **HUD**: a text line that tells the player what gear is ready and what it costs.

The supplied responses choose Adam and three flares. Each flare costs six energy. `player_text` and `flares_text` are prefilled strings, so you do not need `input()`.

In **main.py**, complete the assignments in order. The first print call shows the converted flare count, the second shows the calculated energy, and the last shows your formatted message. Keep these calls in place.

Press **Run** after each change, then **Submit** to check your work. The finished last line should read `Gear for Adam: 3 flares, 18.00 energy`.

## Your Tasks

1. Convert `flares_text` with `int()` into `flare_count`.
2. Set `energy_cost` to `flare_count` multiplied by `flare_cost`.
3. Set `hud_line` to an f-string using `player_text`, `flare_count`, and `energy_cost`, with energy shown to two decimals: `Gear for Adam: 3 flares, 18.00 energy`.

You can now turn response text into numbers, calculate a cost, and display it. At the Gate Trials, your programs will start choosing what to do next.
