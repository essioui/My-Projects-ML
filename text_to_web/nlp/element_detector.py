#!/usr/bin/env python3
"""
"""
from nlp.nlp_engine import nlp


def detect_element(text):
    """
    """
    doc = nlp(text)
    
    for token in doc:
        if token.pos_ == "NOUN":
            if token.lemma_ in ["title", "headind"]:
                return "title"
            
            if token.lemma_ in ["paragraph", "text", "content"]:
                return "paragraph"
            
            if token.lemma_ in ["navbar", "menu"]:
                return "navbar"
    
    return "unknown"
