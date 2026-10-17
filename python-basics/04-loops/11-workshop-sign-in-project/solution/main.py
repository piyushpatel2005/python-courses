gate_limit = 2
path = ""
steps = 0
for tile in range(1, 7):
    if tile == 2:
        continue
    path += f"{tile} "
    steps += 1
    if steps == gate_limit:
        break
if steps == gate_limit:
    gate_status = "Unlocked"
else:
    gate_status = "Sealed"
print("Path:", path)
print("Steps:", steps)
print("Gate:", gate_status)
