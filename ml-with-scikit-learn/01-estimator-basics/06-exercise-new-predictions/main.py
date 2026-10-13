import numpy as np
from sklearn.linear_model import LinearRegression


def predict_rows(model, query):
    # Return the result described in the task.
    return None


# Supplied fixture and observation probe.
X_train = np.array([[10.], [20.], [30.], [40.]])
y_train = np.array([25., 45., 65., 85.])
model = LinearRegression(n_jobs=1).fit(X_train, y_train)
query = np.array([[15.], [25.], [45.]])

print("Query shape:", query.shape)
print("Predictions:", predict_rows(model, query))
