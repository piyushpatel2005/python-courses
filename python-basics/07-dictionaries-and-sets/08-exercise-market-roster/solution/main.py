signups = [{"name": "Lia", "activity": "seeds"}, {"name": "Ren", "activity": "tools"}, {"name": "Lia", "activity": "tools"}]
location = ("Market Hall", "10:00")
names = []
for signup in signups:
    names.append(signup["name"])
unique_names = set(names)
activity_counts = {}
for signup in signups:
    activity = signup["activity"]
    activity_counts[activity] = activity_counts.get(activity, 0) + 1
report = f"{location[0]} at {location[1]}: {len(unique_names)} people, {len(signups)} bookings"
print(names, sorted(unique_names), activity_counts, report)
