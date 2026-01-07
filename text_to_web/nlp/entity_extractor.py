#!/usr/bin/env python3
"""
"""

def extract_entities(text):
    """
    """
    text = text.lower()
    entities = {
        "head": [],
        "body": [],
        "footer": []
    }
    
    if "title" in text:
        entities["head"].append({
            "type": "title",
            "text": "AI Generated Website"
        })
    
    if "paragraph" in text:
        entities["body"].append({
            "type": "paragraph",
            "text": "This is a sample paragraph."
        })
    
    if "footer" in text:
        entities["footer"].append({
            "type": "footer",
            "text": "© 2026"
        })
    return entities
