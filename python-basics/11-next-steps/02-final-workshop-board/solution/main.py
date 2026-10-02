def parse_command(command):
    parts = command.split(":", 1)
    if len(parts) != 2:
        return None
    name = parts[0].strip().upper()
    if not name:
        return None
    try:
        strength = int(parts[1].strip())
    except ValueError:
        return None
    if strength <= 0:
        return None
    return name, strength


def charge_beacons(beacons, commands):
    charges = {}
    for name in beacons:
        charges[name] = 0
    for command in commands:
        parsed = parse_command(command)
        if parsed is None:
            continue
        name, strength = parsed
        if name in charges:
            charges[name] += strength
    return charges


def gate_open(beacons, charges):
    if not beacons:
        return False
    for name, required in beacons.items():
        if charges.get(name, 0) < required:
            return False
    return True


def play_mission(beacons, commands):
    charges = charge_beacons(beacons, commands)
    lines = []
    for name, required in beacons.items():
        lines.append(f"{name}: {charges[name]}/{required}")
    if gate_open(beacons, charges):
        lines.append("Exit Gate: OPEN - Ari leaves the Lantern Atlas with every beacon bright.")
    else:
        lines.append("Exit Gate: LOCKED - Restore every beacon to continue.")
    return lines


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
