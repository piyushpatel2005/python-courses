route = "ECHO"
beacons = 3
energy_cost = 4.25
heading = f"{route}: {beacons} beacons"
energy_line = f"Energy: {beacons * energy_cost:.2f}"
print(heading, energy_line)
