from solution import *


def test_validate_reporting_bounds():
    d = DispatchWorkbench({"s": []}, days=4)
    assert d.check_load_bounds(0, 4) is None and d.check_load_bounds(4, 4) is None
    for a, b in [(-1, 2), (3, 2), (0, 5), (True, 2), (0, 2.5)]:
        try:
            d.check_load_bounds(a, b)
        except ValueError:
            pass
        else:
            assert False


def test_delegate_half_open_range():
    d = DispatchWorkbench({"s": []}, days=4)
    calls = []

    class Index:
        def range_sum(self, a, b):
            calls.append((a, b))
            return 27

    d.loads = Index()
    assert d.read_load_range(1, 3) == 27 and calls == [(1, 3)]
