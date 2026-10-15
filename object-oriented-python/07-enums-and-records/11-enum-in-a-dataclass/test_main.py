from solution import *


def test_enum_in_a_dataclass():
    from dataclasses import fields, is_dataclass
    assert is_dataclass(SupportCase)
    assert next(f for f in fields(SupportCase) if f.name == "state").type is CaseState
    first = SupportCase("One")
    second = SupportCase("Two")
    assert first.state is CaseState.OPEN and second.state is CaseState.OPEN
    first.state = CaseState.CLOSED
    assert second.state is CaseState.OPEN
    assert SupportCase("Three", CaseState.CLOSED).state is CaseState.CLOSED
