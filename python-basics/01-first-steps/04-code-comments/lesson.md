---
title: "Code Comments"
slug: code-comments
order: 4
language: python
lesson_type: interactive
summary: "Learn about Code comments in Python"
seo_title: "Code comments in Python | Python Basics"
seo_description: "Learn about Code comments in Python"
seo_keywords: [python basics, code comments]
---

A comment is a note inside your code. It can explain a choice that might not be obvious when you or someone else reads the program later.

Outside a quoted string, `#` starts a comment. Python ignores the rest of that line. Run this example: only `Hi there` appears in the console.

```python run
# Print function prints on the console
print("Hi there")
```

Comments can be useful study notes too. In the next example, the note reminds you that each of these print calls puts its message on a separate line.

```python run
# Each of these print calls ends its output with a new line
print("Hi there")
print("I am going to be a Python Programmer!")
```

Run it and look for two output lines, not three. The comment does not appear.

As your programs grow, aim to explain *why* a piece of code is there rather than repeating what every line does. A note about a tricky rule is more useful than a comment on every print call. Later, you will also learn how to change the default line ending of `print()`.
