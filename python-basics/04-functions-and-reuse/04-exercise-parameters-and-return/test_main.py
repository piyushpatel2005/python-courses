from solution import combine_energy

def test_combine_energy():
    """The result uses both inputs"""
    assert combine_energy(8, 3) == 11
    assert combine_energy(1, 9) == 10
