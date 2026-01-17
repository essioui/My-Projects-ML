#!/usr/bin/env python3
"""
parser.py
"""
import re
from nlp import (
    detect_intent,
    detect_section,
    detect_element,
    extract_content,
    extract_styles
)

last_element = None 

MULTI_ELEMENTS = {"paragraph", "footer"}


def parser(text, schema=None):
    """
    Parse the input text and return intent and entities.
    Supports updating an existing schema.
    """
    global last_element
    
    intent = detect_intent(text)
    section = detect_section(text)
    element = detect_element(text)

    if schema is None:
        schema = {"head": {}, "body": {}, "footer": {}}

    if not element or element.lower() == "unknown":
        styles = extract_styles(text)
        
        if styles and last_element:
            
            for sec in ["body", "footer"]:
                
                if last_element in schema.get(sec, {}):
                    
                    target = schema[sec][last_element]
                    
                    if isinstance(target, list):
                        target[-1]["style"] = {**target[-1].get("style", {}), **styles}
                    else:
                        target["style"] = {**target.get("style", {}), **styles}
                        
        if styles.get("background_color"):
            schema["body"].setdefault("body_style", {"type": "body", "style": {}})
            schema["body"]["body_style"]["style"].update({
            "background_color": styles["background_color"]
            })
        
        return intent, schema

    content = extract_content(text)
    styles = extract_styles(text)

    entity = {"type": element}

    if element == "navbar":
        items = [x.strip() for x in re.split(r'[,\s]+', content) if x.strip()]
        entity["items"] = items
        
        entity["style"] = {
            "flex": True
        }
        
    elif content:
        entity["text"] = content
        
    elif element == "footer":
        entity["text"] = "© 2024 My Website"

    if styles and section != "head":
        entity.setdefault("style", {}).update(styles)

    if section in ["body", "footer"]:
        last_element = element

    if element in MULTI_ELEMENTS and section != "head":
        schema[section].setdefault(element, []).append(entity)
    else:
        schema[section][element] = entity

    return intent, schema
