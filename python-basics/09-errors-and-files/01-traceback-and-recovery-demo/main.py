def safe_quantity(text):
    try:
        return int(text)
    except ValueError:
        return 0  # Change this fallback to -1.

print("Quantity:", safe_quantity("4"))
print("Needs review:", safe_quantity("unknown"))
