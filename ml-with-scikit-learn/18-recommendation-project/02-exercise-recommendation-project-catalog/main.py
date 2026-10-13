from collections import Counter, defaultdict
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

USERS = pd.read_csv('users.csv',dtype={'user_id':str})
INTERACTIONS = pd.read_csv('interactions.csv',dtype=str,keep_default_na=False)

def make_catalog():
    """Read fixed catalog metadata as a fresh DataFrame."""
    return pd.read_json('catalog.json',orient='records',convert_dates=False,
                        dtype={'item_id':str,'category':str,'title':str,
                               'description':str,'available_since':str})

def split_interactions(catalog, events):
    return None

def build_profiles(catalog):
    rows=catalog.loc[catalog['available_since'] <= '2025-01-19'].sort_values('item_id')
    ids=rows['item_id'].tolist()
    texts=rows[['category','title','description']].agg(' '.join,axis=1)
    vectorizer=TfidfVectorizer(max_features=100)
    matrix=vectorizer.fit_transform(texts)
    return ids,vectorizer,matrix


partitions=split_interactions(make_catalog(),INTERACTIONS)
print('Partitions:',partitions)
