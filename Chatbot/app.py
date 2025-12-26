#!/usr/bin/env python3
"""
"""
from engine import ChatbotEngine

bot = ChatbotEngine(data_path='data/knowledge_base.json')
bot.train()

print("Chatbot is ready! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = bot.get_response(user_input)
    print("Chatbot:", response)