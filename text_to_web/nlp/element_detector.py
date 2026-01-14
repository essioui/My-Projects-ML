#!/usr/bin/env python3
from nlp.nlp_engine import nlp

def detect_element(text):
    text_lower = text.lower()
    
    if "navbar" in text_lower or "menu" in text_lower or "navigation" in text_lower:
        return "navbar"
    
    doc = nlp(text)
    
    for token in doc:
        if token.pos_ == "NOUN":
            lemma = token.lemma_.lower()
            
            if lemma in ["title", "heading"]:
                return "title"
            
            if lemma in ["paragraph", "text", "content"]:
                return "paragraph"
            
            if lemma in ["navbar", "menu", "navigation"]:
                return "navbar"
            
            if lemma in ["footer"]:
                return "footer"
            
    return "unknown"
