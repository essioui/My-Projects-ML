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
    Convert a style dictionary to inline CSS string.
    Supports semantic shortcuts and raw CSS values.
    """
    if not style_dict:
        return ""

    css_map = {
        # text
        "align": "text-align",
        "color": "color",
        "background_color": "background-color",
        "bg": "background-color",

        # font
        "font_size": "font-size",
        "font_family": "font-family",
        "weight": "font-weight",
        "style": "font-style",
        "decoration": "text-decoration",
        "line_height": "line-height",

        # box model
        "margin": "margin",
        "padding": "padding",
        "radius": "border-radius",
        "border": "border",

        # layout
        "display": "display",
        "position": "position",
        "width": "width",
        "height": "height",

        # flexbox
        "flex": "display",
        "flex_direction": "flex-direction",
        "justify": "justify-content",
        "align_items": "align-items",
        "gap": "gap",

        # misc
        "opacity": "opacity",
        "cursor": "cursor",
        "z_index": "z-index",
    }

    # semantic shortcuts
    size_map = {
        "large": "32px",
        "medium": "16px",
        "small": "12px",
    }

    css_parts = []

    for key, value in style_dict.items():

        # font size shortcut
        if key in {"size", "font_size"}:
            if isinstance(value, str) and value in size_map:
                css_parts.append(f"font-size:{size_map[value]}")
            elif value is not None:
                css_parts.append(f"font-size:{value}")
            continue

        # flex shortcut (navbar / same line)
        if key == "flex" and value:
            css_parts.append("display:flex")
            css_parts.append("justify-content:center")
            continue

        # normal css mapping
        css_property = css_map.get(key)
        if css_property and value is not None:
            css_parts.append(f"{css_property}:{value}")

    if not css_parts:
        return ""

    return f' style="{"; ".join(css_parts)};"'


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
            items_html += f'<li><a href="#">{item}</a></li>\n'
            
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

    html += "</head>\n"
    
    body_style = schema["body"].get("body_style", {}).get("style", {})
    body_style_css = style_dict_to_css(body_style)

    html += f"<body{body_style_css}>\n"

    for name, data in schema["body"].items():
        if name == "body_style":
            continue
        
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
