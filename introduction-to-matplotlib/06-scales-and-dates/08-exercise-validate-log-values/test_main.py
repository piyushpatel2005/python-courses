from solution import *
def test_01_changed_positive_bars_and_scale():
    figure, axis = plot_event_range(["A", "B", "C"], [2, 75, 900])
    assert axis in figure.axes and axis.get_yscale() == "log"
    assert [tick.get_text() for tick in axis.get_xticklabels()] == ["A", "B", "C"]
    assert [bar.get_height() for bar in axis.patches] == [2, 75, 900]
    _, changed = plot_event_range(["D"], [15])
    assert [bar.get_height() for bar in changed.patches] == [15]

def test_02_nonpositive_values_rejected():
    for values in ([1, 0], [2, -4]):
        try:
            plot_event_range(["A", "B"], values)
        except ValueError:
            pass
        else:
            assert False, "A logarithmic axis must reject zero and negative counts"
