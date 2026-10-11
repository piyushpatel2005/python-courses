map_card = {"landmark": "lens", "marks": 4}
landmark = map_card["landmark"]
print(landmark)
map_card["marks"] = 9
print("Marks:", map_card["marks"])
print("Route:", map_card.get("route", "unknown"))
