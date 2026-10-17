---
title: "Project: Build Adam’s Gear HUD"
slug: exercise-build-a-ticket
order: 12
language: python
lesson_type: coding
summary: "Combine response text, conversion, multiplication, and formatting."
seo_title: "Project: Build Adam’s Gear HUD | Python Basics"
seo_description: "Combine response text, conversion, multiplication, and formatting."
seo_keywords: [python basics, values and input, lantern atlas]
---

Put the Gear Forge skills together in a small heads-up display, or **Display**: a text line that tells the player what gear is ready and what it costs.

The supplied responses choose Adam and three flares. Each flare costs six energy. `player_text` and `flares_text` are prefilled strings.

## Your Tasks

1. Convert `flares_text` with `int()` into `flare_count`.
2. Set `energy_cost` to `flare_count` multiplied by `flare_cost`.
3. Set `display_line` to an f-string using `player_text`, `flare_count`, and `energy_cost`, with energy shown to two decimals: `Gear for Adam: 3 flares, 18.00 energy`.

The finished last line should read `Gear for Adam: 3 flares, 18.00 energy`.