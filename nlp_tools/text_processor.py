#!/usr/bin/env python3
"""
"""
import math

class TextProcessor:
    """
    """
    
    def __init__(self, constractions, stopwords, lemmitizer_funct):
        """
        """
        self.constractions = constractions
        self.punctuation = [".", ",", "!", "?", ":", ";"]
        self.stopwords = stopwords
        self.lemmitizer_funct = lemmitizer_funct
        self.vocabulary = {}
        self.documents = []
    
    
    def clean_text(self, text):
        """
        """
        for p in self.punctuation:
            text = text.replace(p, "")
        return text
    
    def expand_text(self, text):
        """
        """
        for key, value in self.constractions.items():
            text = text.replace(key, value)
        return text
    
    
    def tokenize(self, text):
        """
        """
        return text.split()
    
    
    def word_count(self, tokens):
        """
        """
        freq = {}
        for word in tokens:
            word = word.lower()
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        return freq
    
    
    def remove_stopwords(self, tokens):
        """
        """
        return [word for word in tokens if word not in self.stopwords]
    
    
    def build_vocabulary(self, tokens):
        """
        """
        self.vocabulary = {}
        for indx, word in enumerate(sorted(set(tokens))):
            self.vocabulary[word] = indx
        return self.vocabulary
    
    
    def vectorize_tokens(self, tokens):
        """
        """
        vector = [0] * len(self.vocabulary)
        for word in tokens:
            if word in self.vocabulary:
                vector[self.vocabulary[word]] += 1
        return vector
    
    
    def build_vocabulary_from_docs(self):
        """
        """
        vocab = set()
        for doc in self.documents:
            vocab.update(doc)
        self.vocabulary = {
            word: idx for idx, word in enumerate(sorted(vocab))
        }
    
    
    def compute_tf(self, doc):
        """
        """
        tf = [0] * len(self.vocabulary)
        for word in doc:
            if word in self.vocabulary:
                tf[self.vocabulary[word]] += 1
        return tf
    
    def compute_df(self):
        """
        """
        df = [0] * len(self.vocabulary)
        for doc in self.documents:
            seen = set(doc)
            for word in seen:
                df[self.vocabulary[word]] += 1
        return df
    
    
    def compute_tfidf(self):
        """
        """
        N = len(self.documents)
        df = self.compute_df()
        tf_idf_vectors = []
        
        for doc in self.documents:
            tf = self.compute_tf(doc)
            tfidf = []
            
            for i, tf_value in enumerate(tf):
                if df[i] == 0:
                    tfidf.append(0)
                else:
                    idf = math.log(N / df[i])
                    tfidf.append(tf_value * idf)
            tf_idf_vectors.append(tfidf)
        return tf_idf_vectors
    
    
    def cosine_similarity(self, vec1, vec2):
        """
        """
        dot = sum(a * b for a, b in zip(vec1, vec2))
        norm1 = math.sqrt(sum(a * a for a in vec1))
        norm2 = math.sqrt(sum(b * b for b in vec2))
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot / (norm1 * norm2)
    
    def process(self, text):
        """
        """
        text = text.lower()
        text = self.clean_text(text)
        text = self.expand_text(text)
        
        tokens = self.tokenize(text)
        tokens = self.remove_stopwords(tokens)
        
        tokens = self.lemmitizer_funct(tokens)
        
        word_freq = self.word_count(tokens)
        
        self.build_vocabulary(tokens)
        vector = self.vectorize_tokens(tokens)
        
        return {
            "cleaned_text": text,
            "tokens": tokens,
            "word_frequency": word_freq,
            "vocabulary": self.vocabulary,
            "vector": vector
        }


    def process_corpus(self, texts):
        """
        """
        all_tokens = []
    
        for text in texts:
            text = text.lower()
            text = self.clean_text(text)
            text = self.expand_text(text)
        
            tokens = self.tokenize(text)
            tokens = self.remove_stopwords(tokens)
        
            tokens = self.lemmitizer_funct(tokens)
        
            all_tokens.append(tokens)
        
        self.documents = all_tokens
        self.build_vocabulary_from_docs()
        tfidf_vectors = self.compute_tfidf()
    
        return {
            "documents": self.documents,
            "vocabulary": self.vocabulary,
            "tfidf_vectors": tfidf_vectors
        }
    