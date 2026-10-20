from solution import receipt_total, receipt_line

def test_receipt_total():
    """Quantity and unit price give a reusable dollar total."""
    assert receipt_total(3, 4) == 12
    assert receipt_total(2, 9) == 18

def test_receipt_line():
    """The receipt line labels any item and dollar amount."""
    assert receipt_line("Notebooks", 12) == "Notebooks: $12"
    assert receipt_line("Folders", 5) == "Folders: $5"
