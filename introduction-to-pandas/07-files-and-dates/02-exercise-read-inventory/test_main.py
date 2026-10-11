from solution import *

def test_01_inventory_changes():
    """Load inventory from either supplied sheet"""
    for text, items, stock in [
        ("item,stock\nPaper bags,20\nLabels,7\n", ["Paper bags", "Labels"], [20, 7]),
        ("item,stock\nBoxes,13\n", ["Boxes"], [13]),
    ]:
        result = load_inventory(text)
        assert list(result.columns) == ["item", "stock"]
        assert result.item.tolist() == items
        assert result.stock.tolist() == stock
        assert pd.api.types.is_numeric_dtype(result.stock)
