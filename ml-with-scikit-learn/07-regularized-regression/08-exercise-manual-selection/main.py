import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error


def select_settings(training, target, validation, actual, candidates):
    return None

training = np.linspace(-3., 3., 21).reshape(-1, 1)
target = 18. + 2.*training[:, 0] + 1.5*training[:, 0]**2
validation = np.array([[-2.5], [-0.6], [0.8], [2.7]])
actual = 18. + 2.*validation[:, 0] + 1.5*validation[:, 0]**2
candidates = [(1, 0.1), (2, 0.5), (2, 8.)]

print("Selected pair and validation MAEs:", select_settings(training, target, validation, actual, candidates))
