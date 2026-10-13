import numpy as np
from sklearn.linear_model import LinearRegression


def predict_rows(model, query):
    return model.predict(query[:1])


# Supplied fixture and observation probe.
X_train = np.array([[1.], [2.], [3.], [4.]])
y_train = np.array([5., 7., 9., 11.])
model = LinearRegression(n_jobs=1).fit(X_train, y_train)
query = np.array([[5.], [7.]])

print("Query shape:", query.shape)
print("Predictions:", predict_rows(model, query))
