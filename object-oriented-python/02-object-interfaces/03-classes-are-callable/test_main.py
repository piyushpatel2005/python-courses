from solution import *


def test_record_creation_calls_the_supplied_factory_once():
    for factory, name in ((Tool, "drill"), (Member, "Imani"), (Tool, "plane")):
        record = create_record(factory, name)
        assert isinstance(record, factory), "Construct using the factory parameter."
        assert record.name == name
    calls = []
    marker = object()
    def factory(name):
        calls.append(name)
        return marker
    assert create_record(factory, "custom") is marker, "Return the factory's actual result."
    assert calls == ["custom"], "Call the factory once with the supplied name."
