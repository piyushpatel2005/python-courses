---
title: Shadow a class default
slug: shadow-a-class-default
order: 6
language: python
lesson_type: coding
summary: Complete `extend_loan(tool, days)` to set that tool's own `loan_days` to `days`, leaving `Tool.loan_days` and other
  tools unchanged.
seo_title: Shadow a class default | Python OOP practice
seo_description: Complete `extend_loan(tool, days)` to set that tool's own `loan_days` to `days`, leaving `Tool.loan_days`
  and other tools unchanged.
seo_keywords:
- Python OOP
- shadow a class default
- coding practice
---

# Shadow a class default

One tool is needed for a longer job. Give that tool its own loan period while leaving the workshop's default alone. This is an instance override, often called **shadowing** a class attribute.

## The nearest value wins

```python
class Pass:
    valid_days = 2

visitor = Pass()
member = Pass()
member.valid_days = 10
print(visitor.valid_days)  # 2
print(member.valid_days)   # 10
print(Pass.valid_days)     # 2
```

The assignment through `member` stores an instance attribute. Reads from that object now find its own value before consulting the class. Nothing was removed from `Pass`; the original default is still there for objects without an override.

Writing `Pass.valid_days = 10` would be a different operation. It changes the shared class attribute, affecting objects that still rely on it. The object before the dot determines where the assignment goes, so keep your attention on that part of the expression.

A later change to `Pass.valid_days` does not replace `member.valid_days`. The member already has its own value. You can think of the class setting as a fallback, not as a broadcast that overwrites every instance.

The supplied `extend_loan(tool, days)` function receives a tool and the desired new period. Despite its name, this function sets a replacement period; it does not add days to the existing period. That contract is useful when the caller has already chosen a final duration.

Only the received tool should change. The probe creates two tools and customizes one, then prints both values and the class default. Reading all three is more revealing than reading only the customized tool: a mistaken class assignment can make that one reading look correct while changing every other tool as well.

## Your Tasks

1. Complete `extend_loan(tool, days)` to set that tool's own `loan_days` to `days`, leaving `Tool.loan_days` and other tools unchanged.

## Run and check

Edit `main.py`. Press **Run** to inspect the supplied console probe, then **Submit** to check your implementation. The completed probe prints `Loan periods: 14 7 7`.
