def parse_command(command):
    # Split once at the colon; handle bad quantities without crashing.
    pass


def book_seats(workshops, commands):
    # Start each workshop at zero bookings; refuse requests over capacity.
    pass


def all_full(workshops, bookings):
    # There must be at least one workshop, and every one must be full.
    pass


def registration_report(workshops, commands):
    # List each workshop, add combined totals, then choose a status.
    pass


workshops = {"POTTERY": 3, "DRAWING": 2}
commands = ["pottery:2", "bad command", "POTTERY:1", "drawing:2", "DANCE:9"]
report = registration_report(workshops, commands)
if report is None:  # Checkpoints work before the full report is built.
    print("Parsed sample:", parse_command(" pottery:2 "))
    print("Bookings sample:", book_seats({"POTTERY": 3}, ["pottery:2"]))
    print("Full sample:", all_full({"POTTERY": 3}, {"POTTERY": 3}))
else:
    for line in report:
        print(line)
