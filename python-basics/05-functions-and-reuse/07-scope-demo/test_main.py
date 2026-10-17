from solution import preview_pulse, energy

def test_local_energy():
    """Only the local energy changes"""
    assert preview_pulse() == 15
    assert energy == 20
