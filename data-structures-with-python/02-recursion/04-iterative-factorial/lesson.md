---
title: "Iterative factorial and its invariant"
slug: iterative-factorial
order: 4
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `factorial_loop(n)` with an explicit loop over factors 1 through n, returning `(product, multiplications)` after validation."
seo_title: "Iterative factorial and its invariant | Python data structures"
seo_description: "Practice iterative factorial through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - iterative factorial
  - data structures practice
---

# Iterative factorial and its invariant

Factorial multiplies the positive integers up to n. For a small set of distinct cards, it counts the possible orders. Start with an iterative version so its state is clear before expressing the same recurrence with function calls.

## An accumulator represents completed work

The factorial of zero is one: the product with no factors uses one as its identity. Initialize a running product to one, then multiply by each factor from one through n. Python's `range` excludes its stop value, so the upper boundary needs to include n deliberately.

After multiplying by factor k, the invariant is that the accumulator equals the product from one through k. The next multiplication extends that completed prefix by one factor. Starting at zero would destroy the product because every later multiplication would still be zero.

```python
product = 1
for factor in [2, 5]:
    product *= factor
print(product)  # 10
```

That example multiplies two selected factors, not all factors through n. In the exercise, return both the product and the number of multiplications performed. Our chosen loop includes factor one, so the count is n. For zero it performs no multiplications and returns a product of one. Counting the harmless multiplication by one makes the loop boundary observable.

## Numeric cost and safe inputs

`factorial_loop(n)` is a fresh standalone implementation. Use the supplied `_check_n` helper to accept integer n from zero through 100. It rejects invalid types and values rather than allowing a negative range to silently produce one. Do not use a factorial library function or a direct lookup table.

Under a model that treats each multiplication as one operation, the loop performs O(n) work and keeps O(1) numeric variables. Python's integers are not fixed-width: factorial results grow, and large-integer multiplication costs more than a constant amount. Therefore the operation count is a useful model, not a claim that an enormous factorial takes linear bit-operation time or constant bytes. The next lesson keeps the mathematical product but replaces the loop's control flow with recursion.

## Build in small steps

The accumulator starts at one, and the loop already covers factors one through n. Validation, product updates, and work counting have separate checks. The tuple return is supplied.

## Your Tasks

1. Validate n with `_check_n(n)` before doing any work.
2. Multiply `product` by each supplied loop factor.
3. Increment `multiplications` once per factor.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
