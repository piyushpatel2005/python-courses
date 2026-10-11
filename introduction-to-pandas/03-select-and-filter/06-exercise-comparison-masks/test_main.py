from solution import *
import pandas as pd

def test_ready_orders():
    """Use the supplied minimum on different order lists"""
    for amounts, minimum in [([3, 7, 5], 5), ([11, 2, 9, 11], 11), ([0, 1, 2], 8)]:
        frame = pd.DataFrame({"order": list("ABCD")[:len(amounts)], "quantity": amounts}, index=[f"ticket-{i}" for i in range(len(amounts))])
        pd.testing.assert_frame_equal(ready_orders(frame, minimum), frame.loc[frame["quantity"] >= minimum])
