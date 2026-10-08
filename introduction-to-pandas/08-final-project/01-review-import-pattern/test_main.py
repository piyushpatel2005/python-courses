from solution import *

def test_01_ticket_csv():
    """Parse workshop names and ticket counts from supplied text"""
    for text, expected in [
        ("workshop,tickets\nPottery,7\nPrinting,4\n", [("Pottery", 7), ("Printing", 4)]),
        ("workshop,tickets\nWeaving,12\n", [("Weaving", 12)]),
    ]:
        result = read_tickets(text)
        assert list(result.columns) == ["workshop", "tickets"]
        assert list(result.itertuples(index=False, name=None)) == expected
