from solution import badge

def test_changed_default():
    """Omitting suffix uses the new default"""
    assert badge("Jo") == "Jo?"
    assert badge("Jo", suffix="!") == "Jo!"
