import pandas as pd

def labeled_cell(table, row_label, column_name):
    return None

def positioned_cell(table, row_number, column_number):
    return None

sample = pd.DataFrame({"sold": [5, 8], "cost": [2, 3]}, index=["am", "pm"])
print(labeled_cell(sample, "pm", "sold"), positioned_cell(sample, 0, 1))
