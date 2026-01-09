#!/usr/bin/env python3
"""
"""
def extract_styles(text):
    """
    dict -> inline CSS string
    """
    styles = {}

    if "center" in text or "centered" in text:
        styles["align"] = "center"
        
    if "red" in text:
        styles["color"] = "red"
        
    elif "blue" in text:
        styles["color"] = "blue"
        
    if "big" in text or "large" in text:
        styles["size"] = "large"
        
    elif "small" in text:
        styles["size"] = "small"
    
    return styles


def extract_entities(text):
    """
    """
    text = text.lower()
    entities = {
        "head": [
            {
                "type": "meta"
            }
            ],
        "body": [],
        "footer": []
    }
    
    styles = extract_styles(text)
    
    # Head
    if "title" in text:
        entities["head"].append({
            "type": "title",
            "text": "AI Generated Website"
        })
    
    # body
    if "header" in text or "heading" in text:
        entities["body"].append({
            "type": "header",
            "text": "Welcome to My AI Website",
            "style": styles
        })

    if "navbar" in text or "menu" in text:
        entities["body"].append({
            "type": "navbar",
            "items": ["Home", "About", "Services", "Contact"]
        })
        
    if "paragraph" in text:
        entities["body"].append({
            "type": "paragraph",
            "text": "This is a sample paragraph.",
            "style": styles
        })
    
    if "button" in text:
        entities["body"].append({
            "type": "button",
            "text": "Click Me",
            "link": "#",
            "style": styles
        })
    
    # footer
    if "footer" in text:
        entities["footer"].append({
            "type": "footer",
            "text": "© 2026",
            "style": styles
        })
    return entities
