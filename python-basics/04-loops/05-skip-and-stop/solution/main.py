packed = ""
for order_number in range(1, 7):
    if order_number == 3:  # Canceled order
        continue
    if order_number == 5:  # Stop before this order
        break
    packed += f"Packed {order_number} | "
print(packed)
