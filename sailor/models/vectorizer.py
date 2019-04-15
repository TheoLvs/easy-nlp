
from sklearn.feature_extraction.text import TfidfVectorizer


def fit_tfidf(documents):

    vectorizer = TfidfVectorizer(min_df=5, analyzer='word', ngram_range=(1, 2), stop_words='english')
    tfidf = vectorizer.fit_transform(documents)

    scores = dict(zip(vectorizer.get_feature_names(), vectorizer.idf_))
    scores = pd.DataFrame(columns=['tfidf']).from_dict(dict(scores), orient='index')
    scores.columns = ['tfidf']

    return vectorizer,tfidf

    



    

