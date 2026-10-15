---
title: "Recursive factorial and waiting frames"
slug: recursive-factorial
order: 5
language: python
runtime: pyodide
lesson_type: coding
summary: "Implement `factorial_recursive(n)` using recursion and the supplied validation, returning the factorial and total calls including the base case."
seo_title: "Recursive factorial and waiting frames | Python data structures"
seo_description: "Practice recursive factorial through a focused Python implementation, concrete traces, and boundary checks."
seo_keywords:
  - Python
  - recursive factorial
  - data structures practice
---

# Recursive factorial and waiting frames

The product through n can be described as n times the product through n - 1. This relationship gives factorial a recursive case. The base case is still zero factorial equals one, exactly as in the iterative version.

## Multiplication waits for a return

For factorial of three, the first call waits to multiply three by the answer for two. That call waits to multiply two by the answer for one. The call for one waits for zero, which returns one without another call. The pending multiplications then finish on the way back up.

```python
smaller_product = 6
next_factor = 4
print(next_factor * smaller_product)  # 24
```

The example shows one combination step. Your recursive function must obtain the smaller product by calling itself. Returning n times n - 1 would combine only two factors and stop too early. Forgetting to return the recursive expression would make callers receive `None` instead of the completed product.

## Make call count observable

This fresh variation is named `factorial_recursive(n)` and returns `(product, calls)`. Count the current call as one, including the base case. For a positive n, obtain both values from the smaller call, multiply its product by n, and add one to its call count. Counting calls differs from the preceding lesson's count of multiplications: the base call returns directly but still exists.

Use the supplied `_check_n` helper for integer inputs from zero through 100. The result for zero is a product of one with one call. There are n + 1 calls and n multiplications. Under the bounded-arithmetic model the time is O(n), but stack space is also O(n), unlike the loop's constant number of variables. Each waiting frame must remember its n until the smaller result returns.

The result's integer size still grows, so exact arithmetic costs are not constant for unbounded n. Keep this implementation small and compare its reasoning with the loop rather than assuming recursion is faster. Both compute the same mathematical product; they store unfinished work differently.

![Recursive factorial: fact(3): wait for 3 × fact(2); fact(2): wait for 2 × fact(1); fact(1): wait for 1 × fact(0); fact(0): return 1 (base). Unwind: return 1, 1 × 1 = 1, 2 × 1 = 2, 3 × 2 = 6. Product lane shown; factorial_recursive(3) returns (6, 4): product 6 and four calls.](recursion-recursive-factorial-trace.svg)

The return lane shows only the product; your result also counts all four calls, including the base call.

## Build in small steps

The final task is one recursive combination: unpack the smaller result, multiply its product, and add the current call to its count. It does not need any new validation or setup.

## Your Tasks

1. Validate n with `_check_n(n)` before doing any work.
2. Return product one and call count one at n = 0.
3. Combine the smaller factorial with n and count the current call.

## Run and check

Edit `main.py`, then press **Run** to inspect the supplied probe. Press **Submit** to check the operation on additional inputs. You do not need to copy code from another lesson.
