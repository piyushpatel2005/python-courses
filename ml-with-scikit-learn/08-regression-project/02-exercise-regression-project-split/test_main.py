from solution import *

def test_01_behavior():
    """Exercise: freeze the regression evaluation split"""
    table = make_data()
    for frame in (table, table.iloc[::-1].reset_index(drop=True)):
        got = make_splits(frame)
        assert isinstance(got, dict), "Return the three named partitions."
        dev, test = train_test_split(frame, test_size=0.2, random_state=41)
        train, val = train_test_split(dev, test_size=0.25, random_state=41)
        for name, ref in (("train", train), ("validation", val), ("test", test)):
            pd.testing.assert_frame_equal(got[name], ref)
        ids = [set(got[name].product_id) for name in ("train", "validation", "test")]
        assert not(ids[0]&ids[1] or ids[0]&ids[2] or ids[1]&ids[2])
        assert set.union(*ids) == set(frame.product_id)

