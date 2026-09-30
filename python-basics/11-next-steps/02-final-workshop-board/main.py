def reserved_total(numbers):
    # Add every reservation count with a loop.
    pass

def available_places(capacity, reserved):
    # Never return a negative number.
    pass

def build_board(sessions):
    # Return one report line for each session.
    pass

sessions = [
    {"name": "Pottery", "capacity": 8, "reservations": [2, 3]},
    {"name": "Drawing", "capacity": 3, "reservations": [2, 2]},
]
for line in build_board(sessions) or []:
    print(line)
