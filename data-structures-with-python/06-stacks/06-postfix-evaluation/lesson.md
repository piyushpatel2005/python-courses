---
title: "Evaluate postfix arithmetic with an operand stack"
slug: "postfix-evaluation"
order: 6
language: "python"
runtime: pyodide
lesson_type: "coding"
summary: "Implement `postfix(tokens)` using Stack for a list of integer strings and `+`, `-`, `*` tokens; return the integer result and raise `ValueError` for invalid tokens, insufficient operands, or a final stack size other than one. Do not use `eval`."
seo_title: "Evaluate postfix arithmetic with an operand stack | Python data structures"
seo_description: "Implement `postfix(tokens)` using Stack for a list of integer strings and `+`, `-`, `*` tokens; return the integer result and raise `ValueError` for invalid tokens, insufficient operands, or a final stack size other than one. Do not use `eval`."
seo_keywords:
  - "Python"
  - "postfix evaluation"
  - "data structures"
---

# Evaluate postfix arithmetic with an operand stack

Postfix notation places an operator after its operands. That makes evaluation possible in one left-to-right pass without parentheses or precedence rules. Every number is an available operand; every operator combines the two most recently available operands.

Use a fresh local Stack. Integer-string tokens, including negative numbers such as "-6", become integers pushed onto it. The exact tokens "+", "-", and "*" are binary operators. The domain is a list of strings; division and other operators are not supported in this exercise. Python's int conversion supplies integer parsing, and invalid strings must lead to ValueError.

For an operator, require at least two values before popping. The first pop is the right operand and the second is the left operand. This order is easy to overlook because addition and multiplication give the same result when swapped. Subtraction exposes the mistake immediately.

Push the computed result back so it can become an operand for a later operator. After all tokens, exactly one value must remain. Zero values means no result; more than one means the expression left unused operands. Both are invalid. Do not return a plausible top value while ignoring leftovers.

The earlier bracket checker and stack methods remain complete. Only postfix is new. Evaluate through stack operations rather than building an expression string for eval. Each call is independent, so a malformed expression cannot corrupt the next evaluation.

## Trace it first

For tokens `9 4 - 2 *`, push 9 and 4, then subtract right 4 from left 9 to leave 5. Push 2 and multiply to leave 10. For `9 -`, the operator has only one operand and must raise rather than borrowing a default zero.

## Cost

For t tokens and bounded-size integers, evaluation is O(t) amortized time and O(t) stack space. Parsing and arithmetic on arbitrarily large integers add costs based on digit length; multiplication is not universally O(1).

## Operation contract

Implement `postfix(tokens)` using Stack for a list of integer strings and `+`, `-`, `*` tokens; return the integer result and raise `ValueError` for invalid tokens, insufficient operands, or a final stack size other than one. Do not use `eval`.

![Read token 12: (12). Bottom → top; last slot is top. Read token 5: (12, 5). Bottom → top; last slot is top. Read token -: (7). Pop right 5, then left 12; push 7. Read token 3: (7, 3). Bottom → top; last slot is top. Read token *: (21). Pop right 3, then left 7; push 21.](stacks-postfix-evaluation-trace.svg)

Final one-item stack gives result 21. Original illustrative example; not exercise input.

## Your Tasks

1. Parse and push integer tokens, including negative numbers; reject invalid strings with `ValueError`.
2. For `+`, `-`, or `*`, require two operands, pop right then left, compute, and push the result.
3. Reject a final stack whose size is not one; otherwise pop and return its result.

## Run and check

Edit `postfix` in `main.py`. The Stack and token loop are supplied. The `return 0` is a temporary placeholder, not a correct result; Run prints `0` until you complete task 3. Submit after each step to see its own check. Run the completed operation to see:

```text
15
```

Press **Submit** to check the tasks on additional inputs and boundary cases.
