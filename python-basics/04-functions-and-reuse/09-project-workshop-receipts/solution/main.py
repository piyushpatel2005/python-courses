def bag_total(count, price):
    return count * price

def receipt(name, amount):
    return f"{name}: ${amount}"

print(receipt("Tool bag", bag_total(3, 4)))
