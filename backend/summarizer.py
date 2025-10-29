from gensim.summarization import summarize


def generate_summary(text):
    try:
        summary = summarize(text, ratio=0.3)  # Summarize 30% of original text
        if not summary:
            return "Text too short to summarize."
        return summary
    except ValueError:
        return "Error: Unable to summarize the text."
