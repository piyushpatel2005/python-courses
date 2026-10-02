def loadout_energy(charges, cost):
    return charges * cost

def loadout_note(name, amount):
    return f"{name}: {amount} energy"

print("Loadout energy:", loadout_energy(3, 4))
print(loadout_note("Lantern pulse", loadout_energy(3, 4)))
