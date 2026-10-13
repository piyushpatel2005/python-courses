import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd


def scale_holdout(train, validation):
    # Return the result described in the task.
    return None


# Supplied fixture and observation probe.
training = pd.read_csv("training.csv", float_precision="round_trip")
queries = pd.read_csv("queries.csv", float_precision="round_trip")
train = training[['width_cm', 'volume_l']].to_numpy()
validation = queries[['width_cm', 'volume_l']].to_numpy()

result = scale_holdout(train, validation)
if result is not None:
    scaler, values = result
    print("Fitted mean:", scaler.mean_)
    print("Validation values:", values)
else:
    print("Learn preprocessing only from training rows.")
