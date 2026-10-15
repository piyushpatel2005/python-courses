---
title: "Match brackets in nested order"
slug: "balanced-brackets"
order: 5
language: "python"
runtime: pyodide
lesson_type: "coding"
summary: "Implement `balanced(text)` using the supplied Stack to return whether `()`, `[]`, and `{}` are correctly nested; ignore every non-bracket character."
seo_title: "Match brackets in nested order | Python data structures"
seo_description: "Implement `balanced(text)` using the supplied Stack to return whether `()`, `[]`, and `{}` are correctly nested; ignore every non-bracket character."
seo_keywords:
  - "Python"
  - "balanced brackets"
  - "data structures"
---

# Match brackets in nested order

Matching bracket counts is not enough to validate nesting. A closing bracket must match the most recently opened bracket that has not yet closed. That is exactly the ordering a stack provides.

Keep one stack of unfinished opening characters. Push an opening bracket when encountered. For a closing bracket, first check that an opening exists, then consume the top and verify its type. A closer with an empty stack or the wrong opening type makes the whole string invalid immediately. After reading every character, the stack must also be empty; otherwise some opening brackets never closed.

The invariant is that the stack contains precisely the unmatched openings in their encounter order, with the innermost opening on top. Removing the top on a matching close restores the surrounding context. This handles nesting of any depth that fits available storage without writing a separate branch for each depth.

The starter preserves the completed Stack and adds one unfinished function. Use that Stack rather than a counter or a sorted collection of symbols. Non-bracket characters are ignored, including letters, spaces, digits, and punctuation. This is a bracket checker, not a programming-language parser: it does not treat quoted text or comments specially.

An empty string is balanced. A string with no brackets is balanced too. A singleton opening or closing bracket is not. Each call uses a fresh local stack so a failed check cannot leak unfinished state into the next call.

## Trace it first

For `{a[b(c)]}`, the stack grows through `{`, `[`, `(` and then shrinks in the reverse order. For `([)]`, the first closer is `)` while the top opening is `[`, so reject immediately even though the total counts match.

## Cost

For n characters, time is O(n) amortized and worst-case stack space is O(n). Each bracket is pushed and popped at most once; no rescanning of earlier characters is needed.

## Operation contract

Implement `balanced(text)` using the supplied Stack to return whether `()`, `[]`, and `{}` are correctly nested; ignore every non-bracket character.

![For valid input ([]), the diagram pushes expected closers ) then ]; ] and ) consume those expectations in reverse order. For ([), the closer ) conflicts with the expected ], so the scan rejects it.](bracket-stack-trace.svg)

The diagram stores expected closers. In this exercise, store the openings instead and compare each popped opening with the closing character; both approaches track the same nesting. Only bracket characters are shown.

## Your Tasks

1. Implement `balanced(text)` to check bracket nesting with Stack.

## Run and check

Edit `balanced` in `main.py`. The earlier definitions and Run probe are supplied. Run the completed operation to see:

```text
True
False
```

Press **Submit** to check the tasks on additional inputs and boundary cases.
