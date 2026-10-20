registrations = [{"name": "Maya", "session": "Python"}, {"name": "Luis", "session": "Drawing"}, {"name": "Maya", "session": "Drawing"}]
event = ("Community Workshop", "Saturday")
names = []
for registration in registrations:
    names.append(registration["name"])
unique_names = set(names)
session_counts = {}
for registration in registrations:
    session = registration["session"]
    session_counts[session] = session_counts.get(session, 0) + 1
report = f"{event[0]} on {event[1]}: {len(unique_names)} attendees, {len(registrations)} registrations"
print(names, sorted(unique_names), session_counts, report)
