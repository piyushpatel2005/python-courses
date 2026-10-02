route_limit = 3
safe_tiles = ""
cleared_count = 0
for tile in range(1, 9):
    if tile == 3:
        continue
    safe_tiles += f"{tile} "
    cleared_count += 1
    if cleared_count == route_limit:
        break
print(safe_tiles)
print(cleared_count)
