---
title: Checkout without losing the cart
slug: checkout-service
order: 8
language: python
lesson_type: coding
summary: Create a snapshot before clearing a successfully checked-out cart.
seo_title: Checkout without losing the cart | Python OOP practice
seo_description: Create a snapshot before clearing a successfully checked-out cart.
seo_keywords:
  - Python
  - checkout service
  - object oriented programming
hints:
  - Create the Order before calling cart.lines.clear().
---

# Checkout without losing the cart

Create a snapshot before clearing a successfully checked-out cart.

Checkout coordinates two existing operations: capture the purchase, then clear the working cart. Check emptiness first. If snapshot creation fails, clearing must not happen. This service returns the order to its caller; it does not register or track it yet. Keeping that boundary explicit avoids requiring the registry before you have built it. Checkout is an in-memory exercise, not a payment operation.

The empty-cart check belongs here rather than in snapshot_order: a snapshot can describe an empty state, but a purchase needs at least one line. Returning the created Order gives the next layer a value it can register and display, without making checkout depend on that layer.

## A smaller example

The archive example copies the pending values before clearing them.

```python
pending = ["draft"]
archived = tuple(pending)
pending.clear()
print(archived, pending)
```

## Your Tasks

1. Implement `CheckoutService.checkout(cart, order_id)` to raise `ValueError("cart is empty")` for an empty cart; otherwise create a snapshot, clear cart lines only after creation succeeds, and return the order.

## Run and check

Edit `main.py`, then press **Run**. The supplied probe catches unfinished-code errors so you can inspect the Console before submitting. The finished probe prints an order followed by an empty cart. Press **Submit** to check the behavior with other inputs.
