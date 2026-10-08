import numpy as np

def blank_panel(rows, columns):
    return np.zeros((rows, columns))

def active_panel(rows, columns):
    return np.ones((rows, columns))

print(blank_panel(2, 3))
print(active_panel(2, 3))
