def total_charge(entries):
    total = 0
    for text in entries:
        try:
            total += int(text)
        except ValueError:
            pass
    return total

def save_beacons(entries):
    with open("beacon-save.txt", "w", encoding="utf-8") as file:
        file.write(f"Charge: {total_charge(entries)}")

def read_beacons():
    with open("beacon-save.txt", "r", encoding="utf-8") as file:
        return file.read()

save_beacons(["2", "unknown", "3"])
print(read_beacons())
