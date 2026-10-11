import numpy as np

def column_scan(grid):
    return grid.T.ravel()

def audit_scans(grid):
    row_scan = grid.ravel()
    col_scan = grid.T.ravel()
    return (np.shares_memory(grid, row_scan), np.shares_memory(grid, col_scan))

camera = np.array([[2, 5, 8], [1, 4, 7]])
print("column scan:", column_scan(camera))
print("shared flags:", audit_scans(camera))
