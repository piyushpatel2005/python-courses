from solution import *


def test_tools_use_the_class_default():
    assert getattr(Tool, "loan_days", None) == 7, "Set loan_days in the class body."
    first, second = Tool(), Tool()
    assert "loan_days" not in vars(first) and "loan_days" not in vars(second)
    original = Tool.loan_days
    try:
        Tool.loan_days = 12
        assert first.loan_days == second.loan_days == Tool().loan_days == 12, "Instances should consult the shared class default."
    finally:
        Tool.loan_days = original
