#/usr/bin/env python3
"""
"""
import numpy as np
import json
from sklearn.metrics.pairwise import cosine_similarity
from bert_encoder import BertEncoder


class ChatbotEngine:
    """
    """
    
    
    def __init__(self, data_path):
        """
        Initialize the chatbot engine with a knowledge base.
        Args:
            knowledge_base_path (str): Path to the knowledge base JSON file.
        """
        self.encoder = BertEncoder()
        self.data_path = data_path
        
        
    def train(self):
        """
        Train the chatbot engine by encoding the knowledge base.
        """
        with open(self.data_path, 'r') as f:
            self.data = json.load(f)
        
        self.questions = [item['question'] for item in self.data]
        self.answers = [item['answer'] for item in self.data]
        
        self.questions_vector = self.encoder.encode(self.questions)
        
        
    def get_response(self, user_input, threshold=0.7):
        """
        Get a response from the chatbot based on user input.
        Args:
            user_input (str): The user's input question.
            threshold (float): Similarity threshold to consider a match.
        Returns:
            str: The chatbot's response.
        """
        user_vector = self.encoder.encode([user_input])
        
        similarities = cosine_similarity(
            user_vector,
            self.questions_vector
        )[0]
        
        # print("Questions embeddings shape:", self.questions_vector.shape)
        # print("User embedding shape:", user_vector.shape)
        
        best_indx = np.argmax(similarities)
        best_score = similarities[best_indx]
        
        if best_score >= threshold:
            return self.answers[best_indx]
        else:
            return "I'm sorry, I don't understand your question."
