#!/usr/bin/env python3
"""
"""
from nlp.nlp_engine import nlp


def detect_section(text):
    """
    """
    doc = nlp(text)
    
    for token in doc:
        if token.pos_ == "NOUN" and token.lemma_ in ["head", "body", "footer"]:
            return token.lemma_
    
    return "body"
