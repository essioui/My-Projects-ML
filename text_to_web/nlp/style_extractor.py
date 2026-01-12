#!/usr/bin/env python3
"""
style_extractor.py
"""
from nlp.nlp_engine import nlp

def extract_styles(text):
    """
    Extract style information from the given text.
    """
    doc = nlp(text)
    styles = {}

    for token in doc:
        lemma = token.lemma_.lower()

        if lemma in ["center", "centered"]:
            styles["align"] = "center"

        if lemma in ["red", "blue", "green", "black"]:
            styles["color"] = lemma

        if lemma in ["big", "large"]:
            styles["size"] = "large"

        if lemma in ["small"]:
            styles["size"] = "small"

    return styles
