import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, precision_recall_fscore_support, roc_auc_score, average_precision_score
from sklearn.datasets import make_classification, make_regression, load_iris, load_wine

dataset = load_wine()
truth = dataset.target.copy()
predicted = truth.copy()
predicted[::5] = (predicted[::5] + 2) % 3
labels = np.arange(len(dataset.target_names))

def class_report(truth, predicted, labels):
    # Complete this one behavior.
    return None

if __name__ == "__main__":
    result = class_report(truth, predicted, labels)
    print("Checkpoint:", result if result is not None else "Complete the helper.")
