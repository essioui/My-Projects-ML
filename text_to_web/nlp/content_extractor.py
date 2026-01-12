#!/usr/bin/env python3
"""
content_extractor.py
"""
from nlp.nlp_engine import nlp

STOP_WORDS = {
    "head", "body", "footer",
    "title", "paragraph", "navbar",
    "center", "centered",
    "red", "blue", "green", "black",
    "big", "large", "small",
    "change", "update", "create", "make"
}

def extract_content(text):
    """
    Extract main content from the given text.
    """
    doc = nlp(text)
    words = []

    after_element = False

    for token in doc:
        if token.lemma_ in ["title", "paragraph", "header"]:
            after_element = True
            continue

        if after_element:
            if token.lemma_ in STOP_WORDS:
                continue
            words.append(token.text)

    return " ".join(words).strip()
