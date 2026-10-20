from solution import safe_quantity

def test_invalid_quantity_fallback():
    """Invalid quantity returns -1; numeric text still converts."""
    assert safe_quantity("unknown") == -1
    assert safe_quantity("4") == 4
    assert safe_quantity("12") == 12
