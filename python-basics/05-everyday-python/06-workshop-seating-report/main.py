def energy_total(shard_energy):
    # Add the energy with a loop; an empty list totals zero.
    pass


def energy_needed(target, gathered):
    # Return zero if the beacon target is reached or exceeded.
    pass


def beacon_report(name, target, shard_energy):
    # Return "<name>: <gathered> energy, <needed> needed".
    pass


print("Final beacon report")
print(beacon_report("North Beacon", 8, [2, 1]))
