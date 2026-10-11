def energy_total(shard_energy):
    total = 0
    for amount in shard_energy:
        total += amount
    return total


def energy_needed(target, gathered):
    needed = target - gathered
    if needed > 0:
        return needed
    return 0


def beacon_report(name, target, shard_energy):
    gathered = energy_total(shard_energy)
    needed = energy_needed(target, gathered)
    return f"{name}: {gathered} energy, {needed} needed"


print("Final beacon report")
print(beacon_report("North Beacon", 8, [2, 1]))
