import numpy as np

values = np.array([9, 4, 6])
column = values[:, np.newaxis]
print("shape:", column.shape)
print(column)
