#!/usr/bin/env python3
"""
Intent Detector
"""

def detect_intent(text):
    """
    Detect user intent from text.
    """
    text = text.lower()

    if any(w in text for w in ["create", "build", "make", "generate"]):
        return "create_website"
    elif any(w in text for w in ["update", "modify", "change", "edit"]):
        return "update_website"
    else:
        return "unknown_intent"
