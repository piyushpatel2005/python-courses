from solution import *


def test_01_behavior():
    """Use stratify with enough samples per class and explain when random row splitting is inappropriate."""
    for zeros, ones in ((64, 16), (60, 40)):
        labels = np.array([0]*zeros + [1]*ones)
        ids = np.arange(len(labels))
        got = stratified_ids(ids, labels)
        assert got is not None, "Return two stratified ID partitions."
        train, test = got
        assert set(train).isdisjoint(test) and set(train) | set(test) == set(ids)
        np.testing.assert_array_equal(np.bincount(labels[test]), [zeros//4, ones//4])
        np.testing.assert_array_equal(np.bincount(labels[train]), [zeros*3//4, ones*3//4])
        expected = train_test_split(ids, test_size=.25, random_state=17, stratify=labels)
        for a, b in zip(got, expected):
            np.testing.assert_array_equal(a, b)
    try:
        stratified_ids(np.arange(8), np.array([0]*7+[1]))
    except ValueError:
        pass
    else:
        assert False, "Let sklearn reject a class represented by only one row."
