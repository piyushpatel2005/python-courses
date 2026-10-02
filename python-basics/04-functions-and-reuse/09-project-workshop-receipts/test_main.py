from solution import loadout_energy, loadout_note

def test_loadout_energy():
    """Count and cost make a reusable total"""
    assert loadout_energy(3, 4) == 12
    assert loadout_energy(2, 9) == 18

def test_loadout_note():
    """A loadout_note labels any amount"""
    assert loadout_note("Lantern pulse", 12) == "Lantern pulse: 12 energy"
    assert loadout_note("Spark", 5) == "Spark: 5 energy"
