from solution import *

def test_01_clean_changing_sales():
    """Keep valid unique sales and preserve the original sheet"""
    for text, expected_ids, first_date, first_units, first_price in [
        (SALES_CSV, [1, 2, 4, 5], "2026-09-05", 3, 2.5),
        ("sale_id,sold_at,stall_id,item,units,unit_price,channel\n10,2025-02-01,X,Jam,2,1.50,Walk-in\n10,2025-02-02,X,Jam,8,1.50,Walk-in\n11,bad,X,Jam,2,1.50,Walk-in\n12,2025-02-03,X,Jam,0,1.50,Walk-in\n13,2025-02-04,X,Jam,3,0,Walk-in\n14,2025-02-05,X,Jam,4,nope,Walk-in\n", [10, 13], "2025-02-01", 2, 1.5),
    ]:
        sales = pd.read_csv(StringIO(text))
        original = sales.copy(deep=True)
        result = clean_sales(sales)
        assert result.sale_id.tolist() == expected_ids
        assert result.sold_at.iloc[0] == pd.Timestamp(first_date)
        assert result.units.iloc[0] == first_units
        assert result.unit_price.iloc[0] == first_price
        assert pd.api.types.is_datetime64_any_dtype(result.sold_at)
        assert pd.api.types.is_numeric_dtype(result.units)
        assert pd.api.types.is_numeric_dtype(result.unit_price)
        assert result.index.tolist() == list(range(len(result)))
        pd.testing.assert_frame_equal(sales, original)
