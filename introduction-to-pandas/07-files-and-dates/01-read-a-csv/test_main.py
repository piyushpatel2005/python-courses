from solution import *

def test_01_comma_columns():
    """A comma separates the header and numeric values"""
    for text, names, counts in [
        ("stall,visits\nFlower Cart,8\nSoup Stand,5\n", ["Flower Cart", "Soup Stand"], [8, 5]),
        ("stall,visits\nBook Tent,12\n", ["Book Tent"], [12]),
    ]:
        result = load_visits(text)
        assert list(result.columns) == ["stall", "visits"]
        assert result.stall.tolist() == names
        assert result.visits.tolist() == counts
