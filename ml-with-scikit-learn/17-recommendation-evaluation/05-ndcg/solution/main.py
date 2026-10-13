import numpy as np

# Supplied synthetic fixture; all randomness is local and reproducible.
ranked=['F04','F02','F05']
relevant={'F02'}
k=3

def binary_ndcg(ranked, relevant, k):
    relevant=set(relevant)
    if not relevant:
        return 0.0
    seen=set()
    dcg=0.0
    for position,item in enumerate(ranked[:k],1):
        if item in relevant and item not in seen:
            dcg += 1/np.log2(position+1)
        seen.add(item)
    ideal=sum(1/np.log2(position+1) for position in range(1,min(k,len(relevant))+1))
    return dcg/ideal

print("NDCG at 3:",binary_ndcg(ranked,relevant,k))
