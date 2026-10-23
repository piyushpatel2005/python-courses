daily_limit = 3
processed_orders = ""
processed_count = 0
for order_number in range(1, 9):
    if order_number == 3:
        continue
    processed_orders += f"{order_number} "
    processed_count += 1
    if processed_count == daily_limit:
        break
print(processed_orders)
print(processed_count)
