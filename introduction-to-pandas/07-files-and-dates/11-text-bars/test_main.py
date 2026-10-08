from solution import *

def test_01_one_mark_per_visit():
    """Every Series entry gets a correctly sized text bar"""
    for counts, expected in [
        (pd.Series([3, 1], index=["Garden", "Kitchen"]), "Garden: ###\nKitchen: #"),
        (pd.Series([0, 4], index=["Tea", "Bread"]), "Tea: \nBread: ####"),
    ]:
        assert visit_bars(counts) == expected
