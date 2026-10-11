def parse_command(command):
    # Split once at the colon; handle bad numbers without crashing.
    pass


def charge_beacons(beacons, commands):
    # Begin with zero charge for each known beacon; process commands in order.
    pass


def gate_open(beacons, charges):
    # An empty beacon dictionary cannot open the gate.
    pass


def play_mission(beacons, commands):
    # Build the beacon lines, then add the win or locked ending.
    pass


beacons = {"NORTH": 3, "SOUTH": 2}
commands = ["north:2", "bad command", "NORTH:1", "south:2", "WEST:9"]
report = play_mission(beacons, commands)
if report is None:  # Supplied checkpoints work before the full game is built.
    print("Parsed sample:", parse_command(" north:2 "))
    print("Charged sample:", charge_beacons({"NORTH": 3}, ["north:2"]))
    print("Gate sample:", gate_open({"NORTH": 3}, {"NORTH": 3}))
else:
    for line in report:
        print(line)
