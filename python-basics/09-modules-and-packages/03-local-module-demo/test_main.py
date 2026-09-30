from solution import travel_minutes
import inspect

def test_route_call():
    """The local module function is called with three stops"""
    assert travel_minutes(3) == 15
    assert "travel_minutes(3)" in inspect.getsource(__import__("solution"))
