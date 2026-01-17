#!/usr/bin/env python3
"""
style_extractor.py
"""
from nlp.nlp_engine import nlp

SIZE_KEYWORDS = {
    "big": "large",
    "large": "large",
    "medium": "medium",
    "normal": "medium",
    "small": "small",
}

COLOR_KEYWORDS = {
    "red", "blue", "green", "black",
    "white", "yellow", "orange", "purple",
}

def extract_styles(text):
    """
    Extract style information from natural language text.
    """
    doc = nlp(text.lower())
    styles = {}

    for token in doc:
        lemma = token.lemma_

        # alignment
        if lemma in {"center", "centered", "middle"}:
            styles["align"] = "center"

        # colors
        if lemma in COLOR_KEYWORDS:
            styles["color"] = lemma

        # font size
        if lemma in SIZE_KEYWORDS:
            styles["size"] = SIZE_KEYWORDS[lemma]

        # flex / same line
        if lemma in {"navbar", "menu", "horizontal", "inline"}:
            styles["flex"] = True
        
        # background color
        if "background" in text:
            words = text.split()
            for i, w in enumerate(words):
                if w == "background" and i + 1 < len(words):
                    styles["background_color"] = words[i + 1]

    return styles
