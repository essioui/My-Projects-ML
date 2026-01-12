#!/usr/bin/env python3
"""
"""


def build_or_update_schema(schema, intent, entities):
    """
    """
    if schema is None or intent == "create_page":
        schema = {
            "head": {},
            "body": {},
            "footer": {}
        }
    
    for element in entities.get("head", []):
        
        schema["head"][element["type"]] = element

    for section in ("body", "footer"):
        for element in entities.get(section, []):
            el_type = element["type"]
            
            if el_type not in schema[section]:
                schema[section][el_type] = element
            else:
                if section in ("head", "body", "footer") and "style" in element:
                    schema[section][el_type].setdefault("style", {})
                    schema[section][el_type]["style"].update(element["style"])
    return schema
