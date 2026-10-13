import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, precision_recall_fscore_support, roc_auc_score, average_precision_score
from sklearn.datasets import make_classification, make_regression, load_iris, load_wine

dataset = load_iris()
truth = dataset.target.copy()
predicted = truth.copy()
predicted[::7] = (predicted[::7] + 1) % 3
labels = np.arange(len(dataset.target_names))

def class_report(truth, predicted, labels):
    average = 'weighted'
    per_class = f1_score(truth, predicted, labels=labels, average=average, zero_division=0)
    support = np.array([np.sum(np.asarray(truth) == label) for label in labels])
    return per_class, float(np.mean(per_class)), support

if __name__ == "__main__":
    print("Checkpoint:", class_report(truth, predicted, labels))
