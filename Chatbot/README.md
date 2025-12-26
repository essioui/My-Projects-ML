# Chatbot (BERT-based Question Answering)

This project is a simple yet powerful chatbot built using BERT embeddings and cosine similarity to answer user questions based on a custom knowledge base.

The chatbot demonstrates how transformer-based models can be used for semantic text understanding, even with a small dataset.

## Project Overview

Uses BERT to convert text into dense vector representations

Compares user questions with stored questions using cosine similarity

Returns the most relevant answer if similarity exceeds a defined threshold

Fully implemented from scratch without external chatbot frameworks

## Project Structure

chatbot/
│
├── data/
│ └── knowledge_base.json
│
├── app.py
├── bert_encoder.py
├── engine.py
└── readme.md

## Knowledge Base Format

The knowledge base is stored as a JSON file and can be easily extended.

Example:
[
{
"question": "what is oop in python",
"answer": "OOP is a programming paradigm based on objects."
},
{
"question": "what is machine learning",
"answer": "Machine learning allows systems to learn from data."
}
]

## How It Works

1- All questions in the knowledge base are encoded using BERT

2- User input is encoded using the same model

3- Cosine similarity is computed between user input and stored questions

4- The best match is selected

5- If similarity ≥ threshold → return answer
Otherwise → return a fallback message

## Model Details

- Model: bert-base-uncased

- Tokenizer: Hugging Face BERT tokenizer

- Embedding strategy: Mean pooling over last hidden states

- Framework: PyTorch

## Installation

1. Clone the repository
   git clone https://github.com/your-username/chatbot.git
   cd chatbot

2. Create a virtual environment
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install torch transformers scikit-learn numpy

## Usage

- Run the chatbot from the terminal:
  python app.py

- You will see:
  Chatbot is ready! Type 'exit' to quit.

- Example interaction:
  You: what is python
  Chatbot: Python is a high-level programming language.

- To exit:
  You: exit
  Chatbot: Goodbye!

## Similarity Threshold

The default similarity threshold is set to 0.7.

You can adjust it in engine.py:
def get_response(self, user_input, threshold=0.7):

- Higher value → more strict matching

- Lower value → more flexible responses

## Purpose of This Project

This project was built to:

- Understand BERT embeddings deeply

- Implement NLP pipelines from scratch

- Learn how semantic similarity works in real applications

- Serve as a foundation for more advanced AI assistants

## Future Improvements

- Add text preprocessing (lowercasing, normalization)

- Support multi-language (Arabic / English)

- Replace mean pooling with CLS token or SBERT

- Add a web interface (FastAPI / Streamlit)

- Expand the knowledge base dynamically
