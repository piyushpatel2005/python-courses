def quantity_value(text):
    try:
        return int(text)
    except ValueError:
        return 0

def quantity_label(text):
    return f"Quantity: {quantity_value(text)}"

print(quantity_label("3"))
print(quantity_label("unknown"))
