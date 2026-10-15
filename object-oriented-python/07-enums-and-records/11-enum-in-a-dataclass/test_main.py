from solution import *


def test_enum_in_a_dataclass():
    from dataclasses import fields, is_dataclass
    assert is_dataclass(QuestEntry)
    assert next(f for f in fields(QuestEntry) if f.name == "state").type is QuestState
    first = QuestEntry("Bridge watch")
    second = QuestEntry("Cave survey")
    assert first.state is QuestState.NEW and second.state is QuestState.NEW
    first.state = QuestState.DONE
    assert second.state is QuestState.NEW
    assert QuestEntry("Beacon repair", QuestState.DONE).state is QuestState.DONE
