def parse_command(command):
    parts = command.split(":", 1)
    if len(parts) != 2:
        return None
    name = parts[0].strip().upper()
    if not name:
        return None
    try:
        quantity = int(parts[1].strip())
    except ValueError:
        return None
    if quantity <= 0:
        return None
    return name, quantity


def book_seats(workshops, commands):
    bookings = {}
    for name in workshops:
        bookings[name] = 0
    for command in commands:
        parsed = parse_command(command)
        if parsed is None:
            continue
        name, quantity = parsed
        if name in bookings and bookings[name] + quantity <= workshops[name]:
            bookings[name] += quantity
    return bookings


def all_full(workshops, bookings):
    if not workshops:
        return False
    for name, capacity in workshops.items():
        if bookings.get(name, 0) < capacity:
            return False
    return True


def registration_report(workshops, commands):
    bookings = book_seats(workshops, commands)
    lines = []
    total_booked = 0
    total_capacity = 0
    for name, capacity in workshops.items():
        lines.append(f"{name}: {bookings[name]}/{capacity} seats booked")
        total_booked += bookings[name]
        total_capacity += capacity
    lines.append(f"Total seats: {total_booked}/{total_capacity} booked")
    if not workshops:
        lines.append("Registration: NO WORKSHOPS - Add a workshop first.")
    elif all_full(workshops, bookings):
        lines.append("Registration: FULL - All workshop seats are booked.")
    else:
        lines.append("Registration: OPEN - Seats are still available.")
    return lines


workshops = {"POTTERY": 3, "DRAWING": 2}
commands = ["pottery:2", "bad command", "POTTERY:1", "drawing:2", "DANCE:9"]
report = registration_report(workshops, commands)
if report is None:
    print("Parsed sample:", parse_command(" pottery:2 "))
    print("Bookings sample:", book_seats({"POTTERY": 3}, ["pottery:2"]))
    print("Full sample:", all_full({"POTTERY": 3}, {"POTTERY": 3}))
else:
    for line in report:
        print(line)
