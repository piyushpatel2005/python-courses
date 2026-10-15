---
title: Function attributes
slug: function-attributes
order: 2
language: python
lesson_type: coding
summary: Implement `set_description(command, text)` so it sets the supplied Python function's `description` attribute to `text`
  without invoking the function.
seo_title: Function attributes | Python OOP practice
seo_description: Implement `set_description(command, text)` so it sets the supplied Python function's `description` attribute
  to `text` without invoking the function.
seo_keywords:
- Python OOP
- function attributes
- coding practice
---

# Function attributes

A game command menu needs descriptions for its functions. Attach the description to the function object without running the command. This keeps the menu text available even when selecting the command would change game state.

## The function is a value

```python
def open_map():
    return "clearing"

open_map.category = "navigation"
print(open_map.category)  # navigation
print(open_map())         # clearing
```

`open_map` refers to the function object. `open_map()` invokes that object and evaluates to its result. The `category` attribute belongs to the function, not to the returned string. Setting it does not change the function's instructions.

The same rule works when another variable refers to that function. If `chosen = open_map`, then `chosen.category` and `open_map.category` read the same attribute because both names refer to one object. You practiced this identity idea with item instances; it applies to function objects as well.

A function can accept another function as a parameter. Inside the receiving function, that parameter is a local name for the passed object. You can attach an attribute through that name just as you attached `name` to an item in the first module.

The supplied `set_description(command, text)` helper should add a `description` attribute to an ordinary Python function. Do not run the command to discover its result; commands may have side effects, and this helper only records metadata. The task does not require wrapping or replacing the function.

The probe attaches text to `list_items`, prints the metadata, and then calls `list_items` separately. Keeping those actions separate shows that the function's normal return value still works. Tests use more than one function and update existing metadata, so avoid referring to the sample function by its global name inside your helper.

## Your Tasks

1. Implement `set_description(command, text)` so it sets the supplied Python function's `description` attribute to `text` without invoking the function.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe shows the attached description followed by the unchanged command result.
