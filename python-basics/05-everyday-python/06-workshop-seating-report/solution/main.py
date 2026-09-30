def seat_total(seat_counts):
    total = 0
    for count in seat_counts:
        total += count
    return total


def remaining_seats(capacity, reserved):
    seats = capacity - reserved
    if seats > 0:
        return seats
    return 0


def workshop_report(name, capacity, seat_counts):
    reserved = seat_total(seat_counts)
    available = remaining_seats(capacity, reserved)
    return f"{name}: {reserved} reserved, {available} available"


print("Workshop seating report")
print(workshop_report("Ceramics", 8, [2, 1]))
