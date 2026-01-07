#!/usr/bin/env python3
"""
Intent Detector
"""

def detect_intent(text):
    """
    Detect user intent from text.
    """
    text = text.lower()

    verbs = ["create", "make", "build", "generate", "write", "new"]
    objects = ["website", "webpage", "site", "page", "web"]

    if any(v in text for v in verbs) and any(o in text for o in objects):
        return "create_page"

    return "update_page"
