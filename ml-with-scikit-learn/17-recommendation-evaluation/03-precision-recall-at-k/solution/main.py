import numpy as np

# Supplied synthetic fixture; all randomness is local and reproducible.
ranked=['F04','F02','F05']
relevant={'F02','F06'}
k=3

def topk_metrics(ranked, relevant, k):
    relevant=set(relevant)
    if not relevant:
        return None
    hits=len(set(ranked[:k]) & relevant)
    return {'precision':hits/k,'recall':hits/len(relevant),'hit':float(hits>0)}

print("One-user metrics:",topk_metrics(ranked,relevant,k))
reports=[topk_metrics(ranked,relevant,k),topk_metrics(['F01'],{'F01'},k)]
valid=[report for report in reports if report is not None]
if valid:
    print("Macro precision:",np.mean([report['precision'] for report in valid]))
