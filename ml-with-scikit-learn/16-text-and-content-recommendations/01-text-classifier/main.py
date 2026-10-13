import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

reviews = pd.read_json('reviews.json',orient='records',convert_dates=False,
                       dtype={'review_id':str,'text':str,'partition':str})
training = reviews.loc[reviews['partition']=='train','text']
queries = reviews.loc[reviews['partition']=='query','text']
labels = reviews.loc[reviews['partition']=='train','topic']

def fit_text_model(training, labels):
    return Pipeline([('text',TfidfVectorizer(max_features=100)),
                     ('model',MultinomialNB(alpha=0.1))]).fit(training,labels)

model=fit_text_model(training,labels)
if model is not None:
    print("Query predictions:",model.predict(queries))
    print("Query probabilities:",model.predict_proba(queries))
    print("Vocabulary size:",len(model.named_steps['text'].vocabulary_))
