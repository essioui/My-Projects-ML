#!/usr/bin/env python3
"""
"""


def detect_intent(text):
    """
    """
    text = text.lower()
    
    verbs = ["create", "make", "build", "generate", "write"]
    objcts = ["website", "webpage", "site", "page", "web"]
    
    if any(verb in text for verb in verbs) and any(obj in text for obj in objcts):
        return "create_website"
    return "UNKNOWN"
