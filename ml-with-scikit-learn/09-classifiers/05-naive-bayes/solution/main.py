import numpy as np
from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def fit_bayes(training, labels, priors):
    return GaussianNB(priors=priors).fit(training, labels)

data = load_iris()
training, queries, labels, actual = train_test_split(data.data, data.target, test_size=0.3, random_state=17, stratify=data.target)
priors = np.array([0.2, 0.3, 0.5])

model = fit_bayes(training, labels, priors)
if model is not None:
    print("Class order:", model.classes_)
    print("Class priors:", model.class_prior_)
    print("Probabilities:", model.predict_proba(queries[:3]))
else:
    print("Fit Gaussian naive Bayes.")
