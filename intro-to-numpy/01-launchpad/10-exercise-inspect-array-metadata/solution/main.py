import numpy as np

def describe_observation(observation):
    return (observation.ndim, observation.shape, observation.size, len(observation))

print(describe_observation(np.array([[3, 4, 5], [6, 7, 8]])))
