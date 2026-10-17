map_entry = {"landmark": "Moss Gate", "marks": 2}
landmark = map_entry["landmark"]
map_entry["marks"] = 3
clue = map_entry.get("clue", "unmarked")
print(landmark, map_entry, clue)
