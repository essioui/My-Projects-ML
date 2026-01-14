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
    "change", "update", "create", "make", "add", "build"
}

def extract_content(text):
    doc = nlp(text)
    words = []
    found_element = False

    for token in doc:
        lemma = token.lemma_.lower()
        
        if lemma in {"title", "paragraph", "navbar", "footer"}:
            found_element = True
            continue
        
        if found_element:
            if lemma in STOP_WORDS:
                continue
            words.append(token.text)

    return " ".join(words).strip()
