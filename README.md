# Text Summarizer & Keyword Extractor

This project is a **web-based NLP application** that summarizes text and extracts the most relevant keywords.
It demonstrates the integration of **Natural Language Processing (NLP)** concepts with a simple **Flask backend** and a **HTML/CSS/JavaScript frontend**.

# Setup Instructions

Follow these steps to set up and run the application on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/text_summarizer_app.git
cd text_summarizer_app
```

### 2. Create and Activate a Virtual Environment

On Windows:

```bash
cd backend
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Required NLTK Data

Run the following in a Python shell:

```bash
import nltk
nltk.download('punkt')
```

### 5. Run the Flask Server

```bash
python app.py
```

By default, the backend will start at:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### 6. Open the Frontend

Open the file **`frontend/index.html`** in your browser.
Enter any text → click **“Process”** → get instant **summary** & **keywords**.
