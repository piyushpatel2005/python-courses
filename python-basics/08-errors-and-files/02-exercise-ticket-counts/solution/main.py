def charge_value(text):
    try:
        return int(text)
    except ValueError:
        return 0

def charge_label(text):
    return f"Charge: {charge_value(text)}"

print(charge_label("3"))
print(charge_label("faded"))
