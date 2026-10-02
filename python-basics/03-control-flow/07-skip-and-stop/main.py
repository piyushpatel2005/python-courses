cleared = ""
for tile in range(1, 7):
    if tile == 2:
        continue
    if tile == 5:
        break
    cleared += f"Cleared {tile} | "
print(cleared)
