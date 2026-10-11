from solution import ability_mark

def test_changed_default():
    """Omitting suffix uses the new default"""
    assert ability_mark("Glow") == "Glow?"
    assert ability_mark("Glow", suffix="!") == "Glow!"
