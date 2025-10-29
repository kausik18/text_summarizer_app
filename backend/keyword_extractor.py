# keyword_extractor.py
from sklearn.feature_extraction.text import TfidfVectorizer


def extract_keywords(text, top_n=5):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform([text])
    scores = zip(vectorizer.get_feature_names_out(), X.toarray()[0])
    sorted_words = sorted(scores, key=lambda x: x[1], reverse=True)
    keywords = [word for word, score in sorted_words[:top_n]]
    return keywords
