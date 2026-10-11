from solution import *

def test_01_channel_and_threshold():
    """Select rows by both variable criteria, including the boundary"""
    frame = pd.DataFrame({"sale_id": [8, 9, 10, 11], "channel": ["Walk-in", "Preorder", "Walk-in", "Preorder"], "revenue": [4.0, 12.0, 3.99, 4.0]})
    original = frame.copy(deep=True)
    for channel, minimum, expected in [("Walk-in", 4, [8]), ("Preorder", 4, [9, 11]), ("Walk-in", 9, [])]:
        result = select_sales(frame, channel, minimum)
        assert result.sale_id.tolist() == expected
        assert result.index.tolist() == list(range(len(result)))
    pd.testing.assert_frame_equal(frame, original)
