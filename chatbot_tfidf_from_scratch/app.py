#!/usr/bin/env python3
"""
engine.py - The main engine for the chatbot application.
"""
from nlp.text_process import TextProcessor
from chatbot.engine import ChatbotEngine


constractions = {
    "i'm": "i am",
    "you're": "you are",
    "it's": "it is",
    "don't": "do not",
    "can't": "cannot",
    "won't": "will not",
    "didn't": "did not"
}

stopswords = set([
    "a", "an", "the", "is", "in", "at", "of", "on", "and", "or", "to", "for",
    "with", "as", "by", "that", "this", "these", "those", "be", "been", "are",
    "was", "were", "he"
])

lemmatizer_dictionary = {
    "going": "go",
    "went": "go",
    "running": "run",
    "ran": "run",
    "cars": "car",
    "children": "child",
    "programming": "program",
    "exited": "exit",
    "learning": "learn",
    "studying": "study"
}


def simple_lemmatizer(word):
    return lemmatizer_dictionary.get(word, word)


processor = TextProcessor(constractions, stopswords, simple_lemmatizer)
bot = ChatbotEngine(processor, data_path='data/chat_data.json')

bot.train()

print("Chatbot is ready! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = bot.get_response(user_input)
    print(f"Chatbot: {response}")
