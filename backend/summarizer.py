# summarizer.py
from nltk.tokenize import sent_tokenize
from collections import Counter
import re


def generate_summary(text, num_sentences=3):
    sentences = sent_tokenize(text)
    if len(sentences) <= num_sentences:
        return "Text too short to summarize."

    words = re.findall(r'\w+', text.lower())
    freq = Counter(words)
    ranked_sentences = sorted(
        sentences,
        key=lambda s: sum(freq[w] for w in re.findall(r'\w+', s.lower())),
        reverse=True
    )
    top_sentences = ranked_sentences[:num_sentences]

    summary_sentences = [s for s in sentences if s in top_sentences]

    summary = ' '.join(summary_sentences)

    return summary
