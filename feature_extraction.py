from sklearn.feature_extraction.text import TfidfVectorizer


def tfidf_features(docs):
    features = TfidfVectorizer().fit_transform(docs).toarray()
    return features
