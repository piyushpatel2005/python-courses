import numpy as np

def station_identity(count):
    return np.eye(count)

def station_weights(weights):
    return np.diag(weights)

def hold_signal(value, times):
    return np.repeat(value, times)

print(station_identity(2))
print(station_weights([3, 5]))
print(hold_signal(7, 3))
