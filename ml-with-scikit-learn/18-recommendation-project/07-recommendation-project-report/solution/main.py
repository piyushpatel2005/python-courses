from collections import Counter, defaultdict
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
import pandas as pd

USERS = pd.read_csv('users.csv',dtype={'user_id':str})
INTERACTIONS = pd.read_csv('interactions.csv',dtype=str,keep_default_na=False)

def make_catalog():
    """Read fixed catalog metadata as a fresh DataFrame."""
    return pd.read_json('catalog.json',orient='records',convert_dates=False,
                        dtype={'item_id':str,'category':str,'title':str,
                               'description':str,'available_since':str})

def split_interactions(catalog, events):
    eligible=set(catalog.loc[catalog['available_since'] <= '2025-01-19','item_id'])
    events=pd.DataFrame(events,columns=['user_id','item_id','event_at','event_type'])
    result={'train':[],'validation':[],'test':[],'omitted':[]}
    for user in sorted(events['user_id'].unique()):
        rows=events.loc[(events['user_id']==user) & events['item_id'].isin(eligible)]
        rows=rows.sort_values(['event_at','item_id'])
        if len(rows)!=5 or rows['item_id'].nunique()!=5:
            result['omitted'].append(user)
            continue
        if rows['event_at'].tolist()!=['2025-01-05','2025-01-12','2025-01-19','2025-01-26','2025-02-02']:
            result['omitted'].append(user)
            continue
        result['train'].append(rows.iloc[:3])
        result['validation'].append(rows.iloc[3:4])
        result['test'].append(rows.iloc[4:5])
    for partition in ['train','validation','test']:
        result[partition]=(pd.concat(result[partition],ignore_index=True)
                           if result[partition] else events.iloc[:0].copy())
    return result

def build_profiles(catalog):
    rows=catalog.loc[catalog['available_since'] <= '2025-01-19'].sort_values('item_id')
    ids=rows['item_id'].tolist()
    texts=rows[['category','title','description']].agg(' '.join,axis=1)
    vectorizer=TfidfVectorizer(max_features=100)
    matrix=vectorizer.fit_transform(texts)
    return ids,vectorizer,matrix

def recommend(ids, matrix, training, user, k=3):
    events=pd.DataFrame(training,columns=['user_id','item_id','event_at','event_type'])
    seen=set(events.loc[events['user_id']==user,'item_id'])
    lookup={item:i for i,item in enumerate(ids)}
    rows=[lookup[item] for item in sorted(seen) if item in lookup]
    if not rows:
        return []
    profile=np.asarray(matrix[rows].mean(axis=0))
    if not np.any(profile):
        return []
    scores=cosine_similarity(profile,matrix).ravel()
    candidates=[(item,float(score)) for item,score in zip(ids,scores) if item not in seen]
    return [item for item,score in sorted(candidates,key=lambda pair:(-pair[1],pair[0]))[:k]]

def recommend_with_fallback(ids, matrix, training, user, k=3):
    ranked=recommend(ids,matrix,training,user,k)
    if ranked:
        return ranked
    events=pd.DataFrame(training,columns=['user_id','item_id','event_at','event_type'])
    seen=set(events.loc[events['user_id']==user,'item_id'])
    counts=Counter(events['item_id'])
    return sorted((item for item in ids if item not in seen),
                  key=lambda item:(-counts[item],item))[:k]

def evaluate(ids, matrix, training, heldout, k=3):
    training=pd.DataFrame(training,columns=['user_id','item_id','event_at','event_type'])
    heldout=pd.DataFrame(heldout,columns=['user_id','item_id','event_at','event_type'])
    counts=Counter(training['item_id'])
    rows={'content':[],'popularity':[]}
    coverage={'content':set(),'popularity':set()}
    omitted=[]
    for user,events in heldout.groupby('user_id',sort=True):
        seen=set(training.loc[training['user_id']==user,'item_id'])
        truth=(set(events['item_id']) & set(ids))-seen
        if not seen or not truth:
            omitted.append(user)
            continue
        predictions={
            'content':recommend_with_fallback(ids,matrix,training,user,k),
            'popularity':sorted((item for item in ids if item not in seen),
                                key=lambda item:(-counts[item],item))[:k]}
        for name,ranked in predictions.items():
            hits=len(set(ranked[:k]) & truth)
            dcg=sum(1/np.log2(position+1) for position,item in enumerate(ranked[:k],1) if item in truth)
            ideal=sum(1/np.log2(position+1) for position in range(1,min(k,len(truth))+1))
            rows[name].append([hits/k,hits/len(truth),float(hits>0),dcg/ideal])
            coverage[name].update(ranked[:k])
    report={'k':k,'users':len(rows['content']),'omitted':omitted,
            'catalog_items':len(ids),'training_events':len(training),
            'heldout_events':len(heldout),'frozen_history':True}
    for name in rows:
        means=np.mean(rows[name],axis=0) if rows[name] else np.zeros(4)
        report[name]=dict(zip(['precision','recall','hit','ndcg'],map(float,means)))
        report[name]['coverage']=len(coverage[name])/len(ids) if ids else 0.0
    return report


partitions=split_interactions(make_catalog(),INTERACTIONS)
ids,vectorizer,matrix=build_profiles(make_catalog())
print('Validation report:',evaluate(ids,matrix,partitions['train'],partitions['validation']))
print('Frozen final-test report:',evaluate(ids,matrix,partitions['train'],partitions['test']))

from scipy.sparse import csr_matrix
probe_matrix=csr_matrix([[1,0]]*5)
probe_history=[("probe","A","2025-01-05","view")]
probe_truth=[("probe","B","2025-02-02","view"),("probe","E","2025-02-02","view")]
print("Two-relevant-item denominator probe:",evaluate(["A","B","C","D","E"],probe_matrix,probe_history,probe_truth,3))
