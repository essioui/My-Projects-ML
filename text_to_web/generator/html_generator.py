#!/usr/bin/env python3
"""
HTML Generator
"""
from pathlib import Path

BASE = Path("components")


def load_component(section, name):
    """
    Load HTML component template.
    """
    path = BASE / section / f"{name}.html"
    if not path.exists():
        raise FileNotFoundError(f"Component not found: {path}")
    return path.read_text()


def style_dict_to_css(style_dict):
    """
    serialize style dictionary to inline CSS.
    """
    css = ""
    if not style_dict:
        return css
    
    if "align" in style_dict:
        css += f"text-align: {style_dict['align']}; "
        
    if "color" in style_dict:
        css += f"color: {style_dict['color']}; "
    
    if "background_color" in style_dict:
        css += f"background-color: {style_dict['background_color']}; "
    
    if "font_size" in style_dict:
        css += f"font-size: {style_dict['font_size']}; "
    
    if "size" in style_dict:
        if style_dict["size"] == "large":
            css += "font-size:32px;"
        elif style_dict["size"] == "small":
            css += "font-size:12px;"

    return f' style="{css}"'


def render_component(section, name, data):
    """
    Render a component with its data.
    """
    template = load_component(section, name)
    data = data.copy()
    
    style_css = style_dict_to_css(data.get("style", {}))
    
    data["style"] = style_css
    
    if data["type"] == "navbar":
        items = data.get("items")
        
        if isinstance(items, str):
            items = [x.strip() for x in items.split(",")]
            
        items_html = ""
        
        for item in items:
            items_html += f"<li>{item}</li>\n"
            
        data["items"] = items_html

    return template.format(**data)


def generate_html(schema):
    """
    Generate full HTML page from schema.
    """
    html = "<!DOCTYPE html>\n<html>\n<head>\n"

    html += load_component("head", "meta") + "\n"

    for name, data in schema["head"].items():
        html += render_component("head", name, data) + "\n"

    html += "</head>\n<body>\n"

    for name, data in schema["body"].items():
        if isinstance(data, list):
            for item in data:
                html += render_component("body", name, item) + "\n"
        else:
            html += render_component("body", name, data) + "\n"

    for name, data in schema["footer"].items():
        if isinstance(data, list):
            for item in data:
                html += render_component("footer", name, item) + "\n"
        else:
            html += render_component("footer", name, data) + "\n"

    html += "</body>\n</html>"
    return html
