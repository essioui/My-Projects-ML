#!/usr/bin/env python3
"""
Intent Detector
"""
from nlp.nlp_engine import nlp


def detect_intent(text):
    """
    Detect user intent from text.
    """
    doc = nlp(text)
    
    for token in doc:
        if token.pos_ == "VERB":
            if token.lemma_ in ["create", "build", "make", "generate"]:
                return "create"
            
            if token.lemma_ in ["update", "modify", "change", "edit"]:
                return "update"
            
    return "unknown"
