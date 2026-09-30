from solution import shelves_needed
import inspect

def test_shelf_call():
    """The revised call uses eleven items"""
    assert shelves_needed(11) == 3
    assert "shelves_needed(11)" in inspect.getsource(__import__("solution"))
