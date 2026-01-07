#!/usr/bin/env python3
"""
"""
from nlp.intent_detector import detect_intent
from nlp.entity_extractor import extract_entities


def parser(text):
    """
    """
    intent = detect_intent(text)
    entities = extract_entities(text)
    
    return intent, entities
