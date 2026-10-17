def safe_charge(text):
    try:
        return int(text)
    except ValueError:
        return 0  # Change this fallback to -1.

print("Beacon charge:", safe_charge("4"))
print("Unknown beacon charge:", safe_charge("faded"))
