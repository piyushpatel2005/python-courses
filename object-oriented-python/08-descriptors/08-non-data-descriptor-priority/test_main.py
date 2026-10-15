from solution import *


def test_non_data_descriptor_priority():
    a, b = PlayerProfile("Ivo"), PlayerProfile("Nia")
    assert a.greeting == "Hello, Ivo" and b.greeting == "Hello, Nia"
    a.greeting = "Custom"
    assert a.greeting == "Custom" and b.greeting == "Hello, Nia"
    a.name = "Lee"
    del a.greeting
    assert a.greeting == "Hello, Lee"
    descriptor_type = type(PlayerProfile.__dict__["greeting"])
    assert not hasattr(descriptor_type, "__set__") and not hasattr(descriptor_type, "__delete__")
