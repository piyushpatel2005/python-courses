from solution import *


def test_01_incoming() -> None:
    adj = {"a": ["b", "b"], "b": ["b"], "c": ["b"], "idle": []}
    assert {v: d[0] for v, d in degrees(adj).items()} == {"a": 0, "b": 3, "c": 0, "idle": 0}


def test_02_outgoing() -> None:
    adj = {"a": ["b", "b"], "b": ["b"], "idle": []}
    assert {v: d[1] for v, d in degrees(adj).items()} == {"a": 1, "b": 1, "idle": 0}
    assert adj == {"a": ["b", "b"], "b": ["b"], "idle": []}
    assert degrees({}) == {}

