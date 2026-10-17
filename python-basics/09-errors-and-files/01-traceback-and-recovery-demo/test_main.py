from solution import safe_charge

def test_invalid_count_fallback():
    assert safe_charge("faded") == -1
    assert safe_charge("4") == 4
