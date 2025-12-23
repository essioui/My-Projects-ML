#!/usr/bin/env python3
"""
Chatbot engine using TF-IDF and cosine similarity
"""
import json


class ChatbotEngine:
    """
    """
    def __init__(self, processor, data_path="data/chat_data.json", threshold=0.25):
        """
        Initializes the ChatbotEngine with a text processor, data path, and similarity threshold.
        Args:
            processor: TextProcessor instance
            data_path: path to JSON data with questions/answers
            threshold: similarity threshold for fallback
        """
        self.processor = processor
        self.threshold = threshold
        
        with open(data_path, 'r') as file:
            self.data = json.load(file)
            
        self.questions = [item['question'] for item in self.data]
        self.answer = [item['answer'] for item in self.data]
        
        
    def train(self):
        """
        Trains the chatbot engine by fitting the text processor on the questions.
        """
        self.processor.fit(self.questions)
    
    
    def get_response(self, user_input):
        """
        Generates a response based on user input.
        """
        user_vec = self.processor.transform(user_input)
        
        simularity_max = 0
        best_index = -1
        
        for index, question_vec in enumerate(self.processor.tfidf_docs):
            simularity = self.processor.cosine_sumilarity(user_vec, question_vec)
            print(f"Debug: Similarity with question {user_vec}: {question_vec}")
            
            if simularity > simularity_max:
                simularity_max = simularity
                best_index = index
                
        if simularity_max < self.threshold:
            return "I'm sorry, I don't understand your question."
        return self.answer[best_index]

