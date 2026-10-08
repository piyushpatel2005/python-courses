from solution import *

def test_01_registry_names():
    """Read names from each JSON registry"""
    for text, expected in [
        ('[{"stall_id":"S1","name":"Honey Table"},{"stall_id":"S2","name":"Clay Corner"}]', ["Honey Table", "Clay Corner"]),
        ('[{"stall_id":"X9","name":"Seed Library"}]', ["Seed Library"]),
    ]:
        assert lookup_names(text).tolist() == expected
