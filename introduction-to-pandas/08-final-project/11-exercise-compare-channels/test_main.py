from solution import *

def test_01_compare_changing_channels():
    """Compare both channels using the completed pipeline"""
    cases = [
        (SALES_CSV, STALLS_CSV, 4, {"Walk-in": 23.5, "Preorder": 8.0}),
        ("sale_id,sold_at,stall_id,item,units,unit_price,channel\n1,2025-01-01,X,Jam,2,3.00,Preorder\n2,2025-01-02,X,Jam,1,2.00,Walk-in\n3,2025-01-03,X,Jam,4,1.00,Walk-in\n", "stall_id,stall_name,neighborhood\nX,Jam Club,East\n", 4, {"Walk-in": 4.0, "Preorder": 6.0}),
        ("sale_id,sold_at,stall_id,item,units,unit_price,channel\n1,2025-01-01,X,Jam,1,1.00,Walk-in\n", "stall_id,stall_name,neighborhood\nX,Jam Club,East\n", 10, {"Walk-in": 0.0, "Preorder": 0.0}),
    ]
    for sales_text, stalls_text, minimum, expected in cases:
        assert compare_channels(sales_text, stalls_text, minimum) == expected

    # Both requested reports must be built from the supplied inputs, not
    # recomputed independently from the cleaned sales or the display fixture.
    namespace = compare_channels.__globals__
    original = namespace["build_report"]
    calls = []
    def observed(sales_text, stalls_text, channel, minimum):
        calls.append((sales_text, stalls_text, channel, minimum))
        return original(sales_text, stalls_text, channel, minimum)
    try:
        namespace["build_report"] = observed
        sales_text = "sale_id,sold_at,stall_id,item,units,unit_price,channel\n21,2025-03-01,A,Tea,2,4.00,Walk-in\n22,2025-03-02,B,Jam,1,9.00,Preorder\n"
        stalls_text = "stall_id,stall_name,neighborhood\nA,Tea Stand,North\nB,Jam Stand,South\n"
        assert compare_channels(sales_text, stalls_text, 5) == {"Walk-in": 8.0, "Preorder": 9.0}
        assert calls == [(sales_text, stalls_text, "Walk-in", 5),
                         (sales_text, stalls_text, "Preorder", 5)]
    finally:
        namespace["build_report"] = original
