import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import issparse

reviews = pd.read_json('reviews.json',orient='records',convert_dates=False,
                       dtype={'review_id':str,'text':str,'partition':str})
training = reviews.loc[reviews['partition']=='train','text']
queries = reviews.loc[reviews['partition']=='query','text']

def encode_tfidf(training, queries):
    vectorizer=TfidfVectorizer(max_features=100,smooth_idf=True,norm='l2').fit(training)
    return vectorizer,vectorizer.transform(queries)

result=encode_tfidf(training,queries)
if result is not None:
    v,z=result
    print("Columns:",v.get_feature_names_out())
    print("IDF:",v.idf_)
    print("Query vectors:",z.toarray())
