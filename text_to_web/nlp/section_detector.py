#!/usr/bin/env python3
"""
"""
from nlp.nlp_engine import nlp


def detect_section(text):
    """
    """
    text_lower = text.lower()
    
    if "head" in text_lower:
        return "head"
    
    if "body" in text_lower:
        return "body"

    if "footer" in text_lower:
        return "footer"
    
    doc = nlp(text)
    
    for token in doc:
        if token.pos_ == "NOUN" and token.lemma_ in ["head", "body", "footer"]:
            return token.lemma_
    
    return "body"
