#!/usr/bin/env python3
"""
"""
# nlp/__init__.py

from nlp.intent_detector import detect_intent
from nlp.section_detector import detect_section
from nlp.element_detector import detect_element
from nlp.content_extractor import extract_content
from nlp.style_extractor import extract_styles

__all__ = [
    "detect_intent",
    "detect_section",
    "detect_element",
    "extract_content",
    "extract_styles",
]
