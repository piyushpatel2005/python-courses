from solution import *

def test_01_behavior():
    """Exercise: encode ordered categories"""
    for levels in (["low", "middle", "high"], ["basic", "plus", "premium"]):
        train = np.array([[levels[2]], [levels[0]], [levels[1]]])
        query = np.array([[levels[1]], ["unseen"], [levels[0]], [levels[2]]])
        got = encode_sizes(train, query, levels)
        assert got is not None, "Return encoded incoming rows."
        assert np.asarray(got).shape == (4, 1)
        assert np.array_equal(got, [[1], [-1], [0], [2]]), "Honor the supplied rank and keep unknown separate."

