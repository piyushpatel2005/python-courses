from solution import ability_label
import inspect

def test_default_label():
    """An omitted mark uses a period"""
    assert ability_label("Flare") == "Flare."
    assert ability_label("Pulse", "?") == "Pulse?"

def test_keyword_call():
    """The second call uses a named override"""
    source = inspect.getsource(__import__("solution"))
    assert 'ability_label("Pulse", mark="!")' in source
