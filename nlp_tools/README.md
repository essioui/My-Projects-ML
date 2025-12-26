# NLP Tools from Scratch

This project provides a collection of core NLP tools implemented from scratch using pure Python, without relying on external NLP libraries such as NLTK, spaCy, or scikit-learn.

The purpose of this project is educational: to understand how Natural Language Processing pipelines work internally, step by step.

## Project Overview

This project demonstrates how to build fundamental NLP components manually, including:

- Text cleaning and normalization

- Contraction expansion

- Tokenization

- Stopword removal

- Lemmatization (dictionary-based)

- Bag of Words (BoW)

- Vocabulary building

- Term Frequency (TF)

- Document Frequency (DF)

- TF-IDF

- Cosine similarity

All logic is written from scratch using Python only.

## Project Structure

```
nlp_tools/
│
├── main.py
└── text_processor.py

```

## Core Module: TextProcessor

Located in text_processor.py, this class contains all NLP logic.

### Main Responsibilities

- Clean and normalize raw text

- Convert text into tokens

- Build vocabulary dynamically

- Vectorize text (BoW)

- Compute TF-IDF across multiple documents

- Measure similarity between documents

## NLP Pipeline

For a single text:

1. Lowercasing

2. Punctuation removal

3. Contraction expansion

4. Tokenization

5. Stopword removal

6. Lemmatization

7. Word frequency counting

8. Vocabulary creation

9. Vectorization (BoW)

For multiple documents (corpus):

1. Apply preprocessing to all texts

2. Build a shared vocabulary

3. Compute TF for each document

4. Compute DF and IDF

5. Generate TF-IDF vectors

6. Compute cosine similarity

## How to Run

Simply execute:
python main.py

This will:

- Process a sample sentence

- Process a small corpus of texts

- Print vocabulary

- Print TF-IDF vectors

- Compute cosine similarity between documents

## Output

```
clean text we are going to the park it is sunny day and i cannot wait
tokens ['go', 'park', 'sunny', 'day', 'wait']
count {'go': 1, 'park': 1, 'sunny': 1, 'day': 1, 'wait': 1}
vocabulary {'day': 0, 'go': 1, 'park': 2, 'sunny': 3, 'wait': 4}
vector [1, 1, 1, 1, 1]

Cosine(Doc1, Doc2): 0.87
Cosine(Doc1, Doc3): 0.32

```

## Why This Project Matters

This project was built to:

- Understand NLP fundamentals deeply

- Avoid black-box libraries

- Learn how TF-IDF and cosine similarity work mathematically

- Prepare for advanced NLP topics (BERT, Transformers, LLMs)

- Serve as a reusable NLP foundation for future projects

## Possible Extensions

- Add stemming algorithms (Porter stemmer)

- Support n-grams (bi-grams, tri-grams)

- Improve lemmatization logic

- Normalize TF values

- Add sentence similarity ranking

- Integrate with chatbot or search engine projects
