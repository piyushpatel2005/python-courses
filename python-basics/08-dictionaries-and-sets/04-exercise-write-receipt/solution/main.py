stock_counts = {"notebooks": 3, "pens": 5}
lines = []
for product, count in stock_counts.items():
    lines.append(f"{product}: {count} in stock")
total_units = 0
for count in stock_counts.values():
    total_units += count
print(lines, total_units)
