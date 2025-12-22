#!/usr/bin/env python3
"""
"""
from text_processor import TextProcessor

constractions = {
    "we're": "we are",
    "can't": "cannot",
    "won't": "will not",
    "it's": "it is",
    "i'm": "i am",
    "you're": "you are",
    "don't": "do not"
}

stopwords = ["i", "me", "my", "we", "are", "ours", "to", "you", "your", "yours", "and",
             "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "is", "they", "them", "their",
             "theirs", "am", "what", "the", "cannot", "a", "this", "that"]

lemmatizer_dictionary = {
    "going": "go",
    "went": "go",
    "running": "run",
    "ran": "run",
    "cars": "car",
    "children": "child"
}


def lemmatize_tokens(tokens):
    """
    """
    return [lemmatizer_dictionary.get(word, word) for word in tokens]

text = "We're going to the park! It's a sunny day, and I'm can't wait."

# texts (3 documents)
texts = [
    "We're going to the park",
    "I am going to the park",
    "I cannot wait for the park"
]

process = TextProcessor(constractions, stopwords, lemmatize_tokens)
result = process.process(text)

results = process.process_corpus(texts)

print("clean text", result["cleaned_text"])
print("token", result["tokens"])
print("count", result["word_frequency"])
print("vector", result["vector"])
print("vocabulary", result["vocabulary"])

print("\nVocabulary 3 texts:")
print(results["vocabulary"])

print("\nTF-IDF Vectors:")
for vec in results["tfidf_vectors"]:
    print(vec)

tfidf = results["tfidf_vectors"]

# Cosine similarity بين الوثيقة 1 و 2
sim_1_2 = process.cosine_similarity(tfidf[0], tfidf[1])

# بين الوثيقة 1 و 3
sim_1_3 = process.cosine_similarity(tfidf[0], tfidf[2])

print("Cosine(Doc1, Doc2):", sim_1_2)
print("Cosine(Doc1, Doc3):", sim_1_3)

