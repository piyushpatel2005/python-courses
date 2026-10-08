import numpy as np
sky = np.array([[1, 2, 3], [4, 5, 6]])
column_offset = np.array([10, 20, 30])
adjusted = sky - column_offset
print(adjusted)
