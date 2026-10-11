import numpy as np
record = np.array([6, 7, 8, 9])
window = record[1:3]
window[0] = 99  # Change 99 to 70.
print(np.shares_memory(record, window), record)
backup = record[1:3].copy()
backup[0] = -1
print(np.shares_memory(record, backup), record)
