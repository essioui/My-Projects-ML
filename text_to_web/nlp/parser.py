#!/usr/bin/env python3
"""
"""
from nlp.intent_detector import detect_intent
from nlp.entity_extractor import extract_entities


def parser(text):
    text = text.lower()

    # intent
    if "create" in text:
        intent = "create_page"
    elif "change" in text or "update" in text:
        intent = "update"
    else:
        intent = "unknown"

    entities = {
        "head": [],
        "body": [],
        "footer": []
    }

    # TITLE
    if "title" in text:
        title = {"type": "title", "text": "AI Generated Website"}
        entities["head"].append(title)

    if "paragraph" in text:
        paragraph = {
            "type": "paragraph",
            "text": "This is a sample paragraph.",
            "style": {}
        }
    if "yellow" in text:
        paragraph["style"]["color"] = "yellow"
    if "bold" in text:
        paragraph["style"]["font_weight"] = "bold"
    if "center" in text:
        paragraph["style"]["align"] = "center"
    entities["body"].append(paragraph)

    return intent, entities

