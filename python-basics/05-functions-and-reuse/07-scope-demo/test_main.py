from solution import preview_chairs, chairs

def test_local_chairs():
    """Only the local chair count changes."""
    assert preview_chairs() == 15
    assert chairs == 20
