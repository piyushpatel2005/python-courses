from solution import safe_count

def test_invalid_count_fallback():
    assert safe_count("unknown") == -1
    assert safe_count("4") == 4
