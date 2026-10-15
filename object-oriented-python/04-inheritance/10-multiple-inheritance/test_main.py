from solution import *


def test_01_multiple_inheritance():
    assert QuestCard.__bases__ == (LabelMixin, JournalMixin), "Use the two bases in the requested order."
    assert "print_label" not in QuestCard.__dict__
    assert "journal_path" not in QuestCard.__dict__
    for code in ("K9", "A-12", "sample"):
        item = QuestCard(code)
        assert item.code == code
        assert item.print_label() == f"Item {code}"
        assert item.journal_path() == f"/journal/{code}"
        assert isinstance(item, LabelMixin) and isinstance(item, JournalMixin)
