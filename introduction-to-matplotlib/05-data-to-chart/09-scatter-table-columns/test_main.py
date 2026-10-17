from solution import *
def test_01_scatter_pairs_and_size():
    assert ax is fig.axes[0] and len(ax.collections) == 1
    assert ax.collections[0].get_offsets().tolist() == [[2, 12], [5, 8], [3, 10]]
    assert list(ax.collections[0].get_sizes()) == [80]
