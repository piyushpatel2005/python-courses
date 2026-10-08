import numpy as np

def column_scan(grid):
    return grid.ravel()  # Choose the other traversal order.

def audit_scans(grid):
    row_scan = grid.ravel()
    col_scan = grid.T.ravel()
    return (False, False)  # Check each scan against grid.

camera = np.array([[2, 5, 8], [1, 4, 7]])
print("column scan:", column_scan(camera))
print("shared flags:", audit_scans(camera))
