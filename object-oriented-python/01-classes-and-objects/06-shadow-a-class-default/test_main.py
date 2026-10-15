from solution import *


def test_one_tool_overrides_the_default():
    original = Tool.loan_days
    try:
        first, second = Tool(), Tool()
        extend_loan(first, 11)
        assert first.loan_days == 11, "Assign the override on the supplied tool."
        assert second.loan_days == Tool.loan_days == original, "Do not change the class default."
        extend_loan(first, 3)
        assert first.loan_days == 3, "days is the replacement period, not an increment."
        Tool.loan_days = 9
        assert first.loan_days == 3 and second.loan_days == 9
    finally:
        Tool.loan_days = original
