caches = {"ridge": 3, "cove": 5}
lines = []
for landmark, marks in caches.items():
    lines.append(f"{landmark}: {marks} marks")
total_marks = 0
for marks in caches.values():
    total_marks += marks
print(lines, total_marks)
