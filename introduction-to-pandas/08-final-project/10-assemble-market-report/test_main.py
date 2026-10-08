from solution import *

def test_01_end_to_end_report():
    """Fresh sheets, channel and threshold all affect the exported report"""
    cases = [
        (SALES_CSV, STALLS_CSV, "Walk-in", 4, [("North", 3, 7.5), ("South", 4, 16.0)]),
        ("sale_id,sold_at,stall_id,item,units,unit_price,channel\n8,2025-01-01,X,Jam,2,3.00,Preorder\n9,2025-01-02,Y,Bread,3,4.00,Preorder\n10,2025-01-03,X,Jam,1,3.00,Walk-in\n", "stall_id,stall_name,neighborhood\nY,Oven,West\nX,Pantry,East\n", "Preorder", 6, [("East", 2, 6.0), ("West", 3, 12.0)]),
        (SALES_CSV, STALLS_CSV, "Preorder", 4, [("South", 2, 8.0)]),
        (SALES_CSV, STALLS_CSV, "Walk-in", 8, [("South", 4, 16.0)]),
        ("sale_id,sold_at,stall_id,item,units,unit_price,channel\n8,2025-01-01,X,Jam,2,3.00,Preorder\n9,2025-01-02,Y,Bread,3,4.00,Preorder\n10,2025-01-03,X,Jam,1,3.00,Walk-in\n", "stall_id,stall_name,neighborhood\nY,Oven,West\nX,Pantry,East\n", "Walk-in", 3, [("East", 1, 3.0)]),
    ]
    for sales_text, stalls_text, channel, minimum, expected in cases:
        text = build_report(sales_text, stalls_text, channel, minimum)
        assert text.splitlines()[0] == "neighborhood,units,revenue"
        result = pd.read_csv(StringIO(text))
        assert list(result.itertuples(index=False, name=None)) == expected

    # A direct aggregation of raw/cleaned sales is not the requested pipeline.
    # Wrap the real helpers so their inputs and order remain observable.
    namespace = build_report.__globals__
    steps = ("read_tables", "clean_sales", "enrich_sales", "select_sales",
             "attach_stalls", "total_by_neighborhood", "export_report")
    original = {name: namespace[name] for name in steps}
    calls = []
    def trace(name):
        def wrapped(*args):
            result = original[name](*args)
            calls.append((name, args, result))
            return result
        return wrapped
    try:
        for name in steps:
            namespace[name] = trace(name)
        sales_text = "sale_id,sold_at,stall_id,item,units,unit_price,channel\n21,2025-03-01,A,Tea,2,4.00,Walk-in\n22,2025-03-02,B,Jam,1,9.00,Preorder\n"
        stalls_text = "stall_id,stall_name,neighborhood\nA,Tea Stand,North\nB,Jam Stand,South\n"
        output = build_report(sales_text, stalls_text, "Walk-in", 5)
        assert [name for name, _, _ in calls] == list(steps)
        assert calls[0][1] == (sales_text, stalls_text)
        assert calls[1][1][0] is calls[0][2][0]
        assert calls[2][1][0] is calls[1][2]
        assert calls[3][1] == (calls[2][2], "Walk-in", 5)
        assert calls[4][1][0] is calls[3][2] and calls[4][1][1] is calls[0][2][1]
        assert calls[5][1][0] is calls[4][2]
        assert calls[6][1][0] is calls[5][2]
        assert output == calls[6][2]
        assert list(pd.read_csv(StringIO(output)).itertuples(index=False, name=None)) == [("North", 2, 8.0)]
    finally:
        for name in steps:
            namespace[name] = original[name]
