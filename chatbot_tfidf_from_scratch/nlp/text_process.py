#!/usr/bin/env python3
"""
text_process.py - A module for text processing in NLP tasks.
"""
import math


class TextProcessor:
    """
    A class to process text data for NLP tasks.
    """
    
    def __init__(self, constractions, stopwords, limitizer=None):
        """
        Initializes the TextProcessor with contractions, stopwords, and a lemmatizer function.
        """
        self.constractions = constractions
        self.stopwords = stopwords
        self.limitizer = limitizer
        self.vocabulary = {}
        self.documents = []
    
    
    def expand_text(self, text):
        """
        Expands contractions in the text.
        """
        for key, value in self.constractions.items():
            text = text.replace(key, value)
        return text
    
    
    def clean_text(self, text):
        """
        Cleans the text by removing punctuation.
        """
        return "".join(char for char in text if char.isalnum() or char.isspace())
    
    
    def tokenize(self, text):
        """
        Tokenizes the cleaned and expanded text into words.
        """
        return text.lower().split()
    
    
    def limitize_funt(self, tokens):
        """
        Applies lemmatization or stemming to the tokens if a limitizer is provided.
        """
        if self.limitizer:
            return [self.limitizer(token) for token in tokens]
        return tokens
    
    def remove_stopwords(self, tokens):
        """
        Removes stopwords from the token list.
        """
        return [word for word in tokens if word not in self.stopwords]
    
    
    def preprocess(self, text):
        """
        Full preprocessing pipeline: expand, clean, tokenize, remove stopwords.
        """
        print("\nthe original text:", text)
    
        text = self.expand_text(text)
        print("after expanding contractions:", text)
        
        text = self.clean_text(text)
        print("after cleaning text:", text)
        
        tokens = self.tokenize(text)
        print("after tokenization:", tokens
              )
        tokens = self.limitize_funt(tokens)
        print("after lemmatization/stemming:", tokens
              )
        tokens = self.remove_stopwords(tokens)
        print("after removing stopwords:", tokens)
        
        return tokens
    
    
    def build_vocabulary(self):
        """
        Builds a vocabulary from the tokens, assigning an index to each unique word.
        """
        vocab = set()
        for doc in self.documents:
            vocab.update(doc)
        
        self.vocabulary = {word: idx for idx, word in enumerate(sorted(vocab))}
    
    
    def compute_tf(self, tokens):
        """
        Computes the term frequency for a list of tokens.
        """
        tf = [0] * len(self.vocabulary)
        total = len(tokens)
        
        for word in tokens:
            if word in self.vocabulary:
                tf[self.vocabulary[word]] += 1 / total if total > 0 else 0
        return tf
    
    
    def compute_idf(self):
        """
        Computes the inverse document frequency for the vocabulary.
        """
        N = len(self.documents)
        idf = [0] * len(self.vocabulary)
        
        for word, indx in self.vocabulary.items():
            df = sum(1 for doc in self.documents if word in doc)
            idf[indx] = math.log((N + 1) / (df + 1)) + 1
            
        self.idf = idf
    
    
    def compute_tfidf(self, tf):
        """
        Computes the TF-IDF scores for the documents.
        """
        return [tf[i] * self.idf[i] for i in range(len(tf))]
    
    
    def cosine_sumilarity(self, vec1, vec2):
        """
        Computes the cosine similarity between two vectors.
        """
        dot = sum(a * b for a, b in zip(vec1, vec2))
        norm1 = math.sqrt(sum(a * a for a in vec1))
        norm2 = math.sqrt(sum(b * b for b in vec2))
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot / (norm1 * norm2)


    def fit(self, texts):
        """
        Fits the TextProcessor to the provided texts, building vocabulary and computing IDF.
        """
        self.documents = [self.preprocess(text) for text in texts]
        self.build_vocabulary()
        self.compute_idf()
        self.tfidf_docs = [
            self.compute_tfidf(self.compute_tf(doc)) for doc in self.documents
        ]
    
    
    def transform(self, text):
        """
        Transforms a new text into its TF-IDF representation.
        """
        tokens = self.preprocess(text)
        tf = self.compute_tf(tokens)
        return self.compute_tfidf(tf)
