plants = {"mint": 3, "sage": 5}
lines = []
for name, price in plants.items():
    lines.append(f"{name}: ${price}")
total = 0
for price in plants.values():
    total += price
print(lines, total)
