import numpy as np
from sklearn.preprocessing import StandardScaler


def apply_scaler(scaler, query):
    return scaler.fit_transform(query)


# Supplied fixture and observation probe.
X_train = np.array([[2.], [4.], [6.]])
scaler = StandardScaler()
train_scaled = scaler.fit_transform(X_train)
query = np.array([[4.], [8.]])

print("Training mean before:", scaler.mean_)
print("Transformed queries:", apply_scaler(scaler, query))
print("Training mean after:", scaler.mean_)
