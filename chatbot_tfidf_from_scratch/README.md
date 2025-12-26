# Chatbot from Scratch (TF-IDF & Bag of Words)

This project is a chatbot built completely from scratch using classic NLP techniques such as Bag of Words (BoW), TF-IDF, and Cosine Similarity, without relying on external NLP libraries like scikit-learn or spaCy.

The goal of this project is to deeply understand how traditional NLP pipelines work internally.

## Project Overview

- Text preprocessing implemented manually

- TF, IDF, and TF-IDF computed from scratch

- Custom cosine similarity function

- Rule-free chatbot based on semantic similarity

- Educational and beginner-friendly design

## Project Structure

```
chatbottfidf_from_scratch/
│
├── data/
│   └── chat_data.json
│
├── nlp/
│   └── text_process.py
│
└── app.py

```

## Dataset Format

The chatbot uses a simple JSON knowledge base:

```
[
  {
    "question": "What is OOP?",
    "answer": "OOP is a programming paradigm based on objects."
  }
]
```

Each entry contains:

- question: user-like input

- answer: chatbot response

## NLP Pipeline (From Scratch)

The text processing pipeline includes:

1. Contraction Expansion

2. Text Cleaning (punctuation removal)

3. Tokenization

4. Lowercasing

5. Stopword Removal

6. Lemmatization (custom dictionary)

7. Vocabulary Building

8. TF Calculation

9. IDF Calculation

10. TF-IDF Vectorization

11. Cosine Similarity

All steps are implemented manually inside text_process.py.

## Core Components

### TextProcessor Class

Located in nlp/text_process.py

Handles:

- Text preprocessing

- Vocabulary construction

- TF-IDF computation

- Vector similarity

Key methods:

- preprocess()

- build_vocabulary()

- compute_tf()

- compute_idf()

- compute_tfidf()

- cosine_similarity()

- fit()

- transform()

## How the Chatbot Works

1. All questions are preprocessed and vectorized using TF-IDF

2. User input is preprocessed using the same pipeline

3. Cosine similarity is computed against stored questions

4. The closest question is selected

5. The corresponding answer is returned

## Usage

Run the chatbot from the terminal:
python app.py

Example:

```
Chatbot is ready! Type 'exit' to quit.
You: What is NLP?
Chatbot: NLP stands for Natural Language Processing.
```

To exit:

```
You: exit
Chatbot: Goodbye!
```

## Why This Project Matters

- This project was built to:

- Understand NLP fundamentals deeply

- Learn how TF-IDF works internally

- Avoid “black box” libraries

- Build a solid foundation before using deep learning models

- Prepare for advanced NLP topics (BERT, Transformers, LLMs)

## Future Improvements

- Add n-grams (bi-grams, tri-grams)

- Improve lemmatization logic

- Add similarity threshold

- Support multiple languages

- Add simple web interface

- Compare results with BERT-based chatbot
