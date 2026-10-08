from solution import *
import pandas as pd

def test_01_exercise_find_table_cells():
    """Make `labeled_cell(table, row_label, column_name)` return the cell selected with `loc`."""
    assert labeled_cell(pd.DataFrame({"sold": [5, 8], "cost": [2, 3]}, index=["am", "pm"]), "pm", "sold") == 8 and labeled_cell(pd.DataFrame({"cost": [4, 9]}, index=[20, 10]), 20, "cost") == 4

def test_02_exercise_find_table_cells():
    """Make `positioned_cell(table, row_number, column_number)` return the cell selected with `iloc`."""
    assert positioned_cell(pd.DataFrame({"sold": [5, 8], "cost": [2, 3]}, index=["am", "pm"]), 0, 1) == 2 and positioned_cell(pd.DataFrame({"cost": [4, 9]}, index=[20, 10]), 1, 0) == 9

