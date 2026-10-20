def total_attendance(entries):
    total = 0
    for text in entries:
        try:
            total += int(text)
        except ValueError:
            pass
    return total

def save_attendance(entries):
    with open("attendance-log.txt", "w", encoding="utf-8") as file:
        file.write(f"Attendees: {total_attendance(entries)}")

def read_attendance():
    with open("attendance-log.txt", "r", encoding="utf-8") as file:
        return file.read()

save_attendance(["2", "unknown", "3"])
print(read_attendance())
