import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from scipy.sparse import issparse

reviews = pd.read_json('reviews.json',orient='records',convert_dates=False,
                       dtype={'review_id':str,'text':str,'partition':str})
training = reviews.loc[reviews['partition']=='train','text']
queries = reviews.loc[reviews['partition']=='query','text']

def encode_counts(training, queries):
    vectorizer=CountVectorizer(max_features=100).fit(list(training) + list(queries))
    return vectorizer,vectorizer.transform(queries)

result=encode_counts(training,queries)
if result is not None:
    vectorizer,matrix=result
    print("Columns:",vectorizer.get_feature_names_out())
    print("Query counts:",matrix.toarray())
