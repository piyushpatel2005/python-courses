from solution import *
def test_01_complete_pairs_and_units():
    assert ax is fig.axes[0] and len(ax.collections) == 1
    assert ax.collections[0].get_offsets().tolist() == [[16, 42], [25, 61]]
    assert ax.get_xlabel() == "Temperature (°C)"
