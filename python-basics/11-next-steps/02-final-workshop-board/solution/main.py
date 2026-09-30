def reserved_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def available_places(capacity, reserved):
    if reserved >= capacity:
        return 0
    return capacity - reserved

def build_board(sessions):
    lines = []
    for session in sessions:
        reserved = reserved_total(session["reservations"])
        available = available_places(session["capacity"], reserved)
        lines.append(f'{session["name"]}: {reserved} reserved, {available} available')
    return lines

sessions = [
    {"name": "Pottery", "capacity": 8, "reservations": [2, 3]},
    {"name": "Drawing", "capacity": 3, "reservations": [2, 2]},
]
for line in build_board(sessions):
    print(line)
