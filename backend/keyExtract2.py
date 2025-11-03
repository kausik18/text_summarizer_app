from rake_nltk import Rake
import nltk


def extract_keywords(text, num_keywords=5):
    """
    Extracts top N keywords from the given text using RAKE algorithm.
    """
    # Initialize RAKE with NLTK stopwords
    rake = Rake()

    # Extract keywords
    rake.extract_keywords_from_text(text)

    # Get all ranked keywords
    keywords = rake.get_ranked_phrases()

    # Return top N keywords
    return keywords[:num_keywords]
