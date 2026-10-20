from solution import preview_sheets, sheets

def test_local_sheets():
    """The preview stack is local."""
    assert preview_sheets() == 30
    assert sheets == 40
