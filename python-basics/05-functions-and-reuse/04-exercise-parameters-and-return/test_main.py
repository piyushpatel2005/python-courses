from solution import total_pages

def test_total_pages():
    """The result uses both page counts."""
    assert total_pages(8, 3) == 11
    assert total_pages(1, 9) == 10
