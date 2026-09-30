from solution import bag_total, receipt

def test_bag_total():
    """Count and price make a reusable total"""
    assert bag_total(3, 4) == 12
    assert bag_total(2, 9) == 18

def test_receipt():
    """A receipt labels any amount"""
    assert receipt("Tool bag", 12) == "Tool bag: $12"
    assert receipt("Glue", 5) == "Glue: $5"
