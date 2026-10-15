from solution import *


def test_non_data_descriptor_priority():
    a, b = Profile("Ivo"), Profile("Nia")
    assert a.greeting == "Hello, Ivo" and b.greeting == "Hello, Nia"
    a.greeting = "Custom"
    assert a.greeting == "Custom" and b.greeting == "Hello, Nia"
    a.name = "Lee"
    del a.greeting
    assert a.greeting == "Hello, Lee"
    descriptor_type = type(Profile.__dict__["greeting"])
    assert not hasattr(descriptor_type, "__set__") and not hasattr(descriptor_type, "__delete__")
