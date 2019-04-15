

from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer



def NMF_topic_extraction(vectorizer = None,documents = None,n_top_words = 10,n_topics = 20):
    """Source: 
    https://ahmedbesbes.com/how-to-mine-newsfeed-data-and-extract-interactive-insights-in-python.html
    """

    if vectorizer is None:
        vectorizer = TfidfVectorizer(min_df=5, analyzer='word', ngram_range=(1, 2), stop_words='english')

    tfidf = vectorizer.fit_transform(documents)

    nmf = NMF(n_components=40, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

    feature_names = vectorizer.get_feature_names()

    for topic_idx, topic in enumerate(nmf.components_[:n_topics]):
        print("Topic %d:"% (topic_idx))
        print(" | ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))