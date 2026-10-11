import numpy as np
pulses = np.array([10, 11, 12, 13, 14, 15])
window = pulses[1:6:2]
print(window)  # Before the assignment, the selected samples are 11, 13, 15.
pulses[1:6:2] = -1
print(pulses)
