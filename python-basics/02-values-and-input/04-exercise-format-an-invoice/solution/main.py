event = "the art fair"
quantity = 4
unit_price = 2.5
total = quantity * unit_price
heading = f"{quantity} posters for {event}"
payment_line = f"Due: ${total:.2f}"
print(heading)
print(payment_line)
