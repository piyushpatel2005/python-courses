def total_arrivals(entries):
    total = 0
    for text in entries:
        try:
            total += int(text)
        except ValueError:
            pass
    return total

def save_log(entries):
    with open("attendance-log.txt", "w", encoding="utf-8") as file:
        file.write(f"Arrivals: {total_arrivals(entries)}")

def read_log():
    with open("attendance-log.txt", "r", encoding="utf-8") as file:
        return file.read()

save_log(["2", "unknown", "3"])
print(read_log())
