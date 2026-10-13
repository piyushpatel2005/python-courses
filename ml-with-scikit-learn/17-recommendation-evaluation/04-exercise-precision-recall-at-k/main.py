import numpy as np

# Supplied synthetic fixture; all randomness is local and reproducible.
ranked=['K08','K03']
relevant={'K03','K08','K09'}
k=3

def topk_metrics(ranked, relevant, k):
    return None

print("One-user metrics:",topk_metrics(ranked,relevant,k))
reports=[topk_metrics(ranked,relevant,k),topk_metrics(['F01'],{'F01'},k)]
valid=[report for report in reports if report is not None]
if valid:
    print("Macro precision:",np.mean([report['precision'] for report in valid]))
