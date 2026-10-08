from solution import *

def test_01_import_both_sheets():
    """Read both supplied sheets, not just the display sample"""
    for sales_text, stalls_text in [
        (SALES_CSV, STALLS_CSV),
        ("sale_id,sold_at,stall_id,item,units,unit_price,channel\n9,2025-01-04,XX,Jam,7,1.25,Walk-in\n10,2025-01-05,YY,Tea,2,3.00,Preorder\n11,2025-01-06,XX,Bread,4,2.50,Walk-in\n", "stall_id,stall_name,neighborhood\nXX,Jam Club,East\nYY,Tea Cart,West\nZZ,Oven,North\n"),
    ]:
        sales, stalls = read_tables(sales_text, stalls_text)
        assert list(sales.columns) == ["sale_id", "sold_at", "stall_id", "item", "units", "unit_price", "channel"]
        assert list(stalls.columns) == ["stall_id", "stall_name", "neighborhood"]
        pd.testing.assert_frame_equal(sales, pd.read_csv(StringIO(sales_text)))
        pd.testing.assert_frame_equal(stalls, pd.read_csv(StringIO(stalls_text)))
