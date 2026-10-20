def receipt_total(quantity, price):
    return quantity * price

def receipt_line(item, amount):
    return item + ": $" + str(amount)

print("Total: $" + str(receipt_total(3, 4)))
print(receipt_line("Notebooks", receipt_total(3, 4)))
