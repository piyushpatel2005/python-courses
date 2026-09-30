visits = [{"name": "Tess", "room": "Art"}, {"name": "Tess", "room": "Math"}, {"name": "Omar", "room": "Art"}]
names = []
counts = {}
for visit in visits:
    names.append(visit["name"])
    room = visit["room"]
    counts[room] = counts.get(room, 0) + 1
people = len(names)
print(f"{people} visitors; {counts}")
