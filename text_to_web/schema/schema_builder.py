#!/usr/bin/env python3
"""
"""


def build_schema(intent, elements):
    """
    """
    return {
        "intent": intent,
        "elements": {
            "head": elements.get("head", []),
            "body": elements.get("body", []),
            "footer": elements.get("footer", [])
        }
    }
