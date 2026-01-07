#!/usr/bin/env python3
"""
"""

def extract_entities(text):
    """
    """
    text = text.lower()
    elements = []
    
    if "title" in text:
        elements.append({
            "type": "title",
            "style": {
                "align": "center",
                "font_size": "24px",
                "font_weight": "bold",
                "color": "#333333",
                "margin": "20px 0"
            }
        })
    
    if "footer" in text:
        elements.append({
            "type": "footer",
            "style": {
                "align": "center",
                "font_size": "14px",
                "font_weight": "normal",
                "color": "#777777",
                "margin": "20px 0",
                "text": "© 2024 My Website"
            }
        })
    return elements
