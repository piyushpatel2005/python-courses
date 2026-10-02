discoveries = [{"location": "Ridge", "treasure": "chest"}, {"location": "Cove", "treasure": "compass"}, {"location": "Ridge", "treasure": "compass"}]
location = ("Map Archive", "dawn")
locations = []
for discovery in discoveries:
    locations.append(discovery["location"])
unique_locations = set(locations)
treasure_counts = {}
for discovery in discoveries:
    treasure = discovery["treasure"]
    treasure_counts[treasure] = treasure_counts.get(treasure, 0) + 1
report = f"{location[0]} at {location[1]}: {len(unique_locations)} places, {len(discoveries)} finds"
print(locations, sorted(unique_locations), treasure_counts, report)
