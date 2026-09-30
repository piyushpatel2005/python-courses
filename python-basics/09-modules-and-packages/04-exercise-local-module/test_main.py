from solution import order_boxes
import solution
import inspect

def test_module_import():
    """The named helper comes from the local module"""
    source = inspect.getsource(solution)
    assert "from supply_rules import box_count" in source
    assert callable(solution.box_count)

def test_order_boxes():
    """The wrapper delegates to the reusable helper"""
    original = solution.box_count
    calls = []
    def tracked(items):
        calls.append(items)
        return original(items)
    try:
        solution.box_count = tracked
        assert order_boxes(9) == 3
        assert order_boxes(4) == 1
        assert order_boxes(0) == 0
        assert calls == [9, 4, 0], "Call the imported box_count(items) helper."
    finally:
        solution.box_count = original
