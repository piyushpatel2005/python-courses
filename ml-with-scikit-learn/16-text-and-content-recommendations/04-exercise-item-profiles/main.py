import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import issparse

records = pd.read_json('catalog.json',orient='records',convert_dates=False,
                       dtype={'item_id':str,'category':str,'title':str,
                              'description':str,'available_since':str})

def item_profiles(records):
    return None

result=item_profiles(records.iloc[::-1])
if result is not None:
    ids,vectorizer,matrix=result
    print("ID row map:",ids)
    print("Item matrix shape:",matrix.shape)
