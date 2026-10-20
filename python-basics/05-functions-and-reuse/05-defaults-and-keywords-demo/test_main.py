from solution import message

def test_changed_default():
    """Omitting suffix uses the new default."""
    assert message("Pickup at noon") == "Pickup at noon?"
    assert message("Pickup at noon", suffix="!") == "Pickup at noon!"
