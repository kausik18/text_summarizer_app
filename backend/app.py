# app.py
from flask import Flask, request, jsonify
from summarizer import generate_summary
from keyword_extractor import extract_keywords
from flask_cors import CORS  # For allowing frontend requests

app = Flask(__name__)
CORS(app)


@app.route('/process', methods=['POST'])
def process_text():
    data = request.get_json()
    text = data.get('text', '')

    summary = generate_summary(text)
    keywords = extract_keywords(text)

    return jsonify({
        'summary': summary,
        'keywords': keywords
    })


if __name__ == '__main__':
    app.run(debug=True)
