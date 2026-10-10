---
title: Sketch data with text bars
slug: text-bars
order: 11
language: python
lesson_type: coding
pyodide_packages:
  - pandas
summary: Represent numeric values as a simple text bar chart without plotting tools.
seo_title: Sketch data with text bars | Introduction to Pandas
seo_description: Represent numeric values as a simple text bar chart without plotting
  tools.
seo_keywords:
  - pandas
  - text bar chart
  - Series visualization
hints:
  - "Change the default scale in the function definition; leave the supplied print call alone."
---

# Sketch data with text bars

For a few small counts, a text bar can make a comparison easier to scan. Use the same scale for every label: one `#` represents one visitor.

The supplied function loops over `counts.items()`, which yields each Series label and value together. `"#" * 3` makes `"###"`; the f-string adds the label, and `"\n".join(...)` places the bars on separate lines. The counts here are nonnegative whole numbers with no missing values. Zero gets an empty bar.

In `main.py`, change only the default argument `scale=2` to `scale=1`. The supplied one-argument call uses that default. Run should show three marks for Garden and one for Kitchen, then Submit.

## Your Tasks

1. Make `visit_bars(counts)` return one `name: ###` line per Series entry, with exactly one `#` per count.
