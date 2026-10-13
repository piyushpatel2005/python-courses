import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import issparse

records = pd.read_json('catalog.json',orient='records',convert_dates=False,
                       dtype={'item_id':str,'category':str,'title':str,
                              'description':str,'available_since':str})

def item_profiles(records):
    rows=records.sort_values('item_id')
    ids=rows['item_id'].tolist()
    texts=rows[['category','title','description']].agg(' '.join,axis=1)
    vectorizer=TfidfVectorizer(max_features=100)
    matrix=vectorizer.fit_transform(texts)
    return ids,vectorizer,matrix

result=item_profiles(records.iloc[::-1])
if result is not None:
    ids,vectorizer,matrix=result
    print("ID row map:",ids)
    print("Item matrix shape:",matrix.shape)
