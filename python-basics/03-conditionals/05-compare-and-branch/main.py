signal = 12
foggy = False
if signal < 8:
    route_hint = "Repair beacon"
elif signal < 16 and not foggy:
    route_hint = "Follow lit path"
else:
    route_hint = "Scout ahead"
print(route_hint)
