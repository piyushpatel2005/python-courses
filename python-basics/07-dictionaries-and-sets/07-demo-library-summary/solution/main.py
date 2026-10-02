finds = [{"location": "Pine Pass", "beacon": "North"}, {"location": "Pine Pass", "beacon": "West"}, {"location": "Salt Cove", "beacon": "North"}]
locations = []
beacon_counts = {}
for find in finds:
    locations.append(find["location"])
    beacon = find["beacon"]
    beacon_counts[beacon] = beacon_counts.get(beacon, 0) + 1
places = len(set(locations))
print(f"{places} locations; {beacon_counts}")
