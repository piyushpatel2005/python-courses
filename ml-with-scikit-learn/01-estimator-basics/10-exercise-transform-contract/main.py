import numpy as np
from sklearn.preprocessing import StandardScaler


def apply_scaler(scaler, query):
    # Return the result described in the task.
    return None


# Supplied fixture and observation probe.
X_train = np.array([[10., 2.], [20., 4.], [30., 6.], [40., 8.]])
scaler = StandardScaler()
train_scaled = scaler.fit_transform(X_train)
query = np.array([[25., 5.], [50., 10.], [15., 3.]])

print("Training mean before:", scaler.mean_)
print("Transformed queries:", apply_scaler(scaler, query))
print("Training mean after:", scaler.mean_)
