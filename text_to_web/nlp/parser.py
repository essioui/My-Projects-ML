#!/usr/bin/env python3
"""
parser.py
"""
from nlp import (
    detect_intent,
    detect_section,
    detect_element,
    extract_content,
    extract_styles
)

last_element = None

def parser(text, schema=None):
    """
    Parse text to extract intent, section, element, content, and style.
    """
    global last_element
    intent = detect_intent(text)
    section = detect_section(text)
    element = detect_element(text)

    entities = {"head": [], "body": [], "footer": []}

    if not element or element.lower() == "unknown":
        
        if last_element:
            element = last_element
            
            if schema:
                for sec in ["head", "body", "footer"]:
                    if last_element in schema[sec]:
                        section = sec
                        break
        else:
            return intent, entities

    content = extract_content(text)
    styles = extract_styles(text)

    entity = {"type": element}
    if content:
        entity["text"] = content
    if styles:
        entity["style"] = styles

    last_element = element
    entities[section].append(entity)
    return intent, entities
