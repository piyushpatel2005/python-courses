from solution import parcel_label
import inspect

def test_default_label():
    """An omitted mark uses a period"""
    assert parcel_label("Bag") == "Bag."
    assert parcel_label("Box", "?") == "Box?"

def test_keyword_call():
    """The second call uses a named override"""
    source = inspect.getsource(__import__("solution"))
    assert 'parcel_label("Box", mark="!")' in source
