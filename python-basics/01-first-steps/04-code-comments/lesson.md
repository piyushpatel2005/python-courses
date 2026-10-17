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

In the last lesson you saw comments. Let's learn about those.

A comment is a note inside your code. It can explain a choice that might not be obvious when you or someone else reads the program later. 

As a software engineer, you will write several thousands of lines of code. You might need to revisit those code lines after a year or two and at that time you may not remember what you did for some complicated logic. This is where comments help you. You also work with several different engineers as a part of your team. Your notes may also help them understand the logic of code.

Outside a quoted string, `#` starts a comment. Python ignores the lines starting with pound sign (`#`). Run this example: only `Hi there` appears in the console.

```python run
# Print function prints on the console
print("Hi there")
```

Comments can be useful study notes too. In the next example, the note reminds you that each of these print calls puts its message on a separate line.

```python run
# Each of these print lines print the text inside parenthesis
print("Hi there")
print("I am going to be a Python Programmer!")
```

Run it and the comment does not appear.

As your programs grow, aim to explain *why* a piece of code is there rather than repeating what every line does. A note about a tricky rule is more useful than a comment on every print call.
