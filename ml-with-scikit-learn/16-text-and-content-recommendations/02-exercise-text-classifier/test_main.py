from solution import *

def test_01_text_classifier():
    """Use TfidfVectorizer plus MultinomialNB in one Pipeline with nonnegative sparse inputs."""
    for first,second in [('packaging','quality'),('assembly','delivery')]:
        docs=[first+' soft',first+' wrap',second+' firm',second+' durable']
        labels=[first,first,second,second]
        model=fit_text_model(docs,labels)
        assert isinstance(model,Pipeline)
        assert isinstance(model.named_steps['text'],TfidfVectorizer)
        assert isinstance(model.named_steps['model'],MultinomialNB)
        assert model.named_steps['model'].alpha == 1.0
        before=dict(model.named_steps['text'].vocabulary_)
        assert model.predict([first,second]).tolist()==[first,second]
        model.predict(['validationonlyword'])
        assert model.named_steps['text'].vocabulary_ == before
        assert 'validationonlyword' not in before
