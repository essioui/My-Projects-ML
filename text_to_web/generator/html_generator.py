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


def render_component(section, el):
    """
    Render a component with its data.
    """
    template = load_component(section, el["type"])
    
    style_css = style_dict_to_css(el.get("style", {}))
    el = el.copy()
    el["style"] = style_css
    
    if el["type"] == "navbar":
        items_html = ""
        for item in el.get("items", []):
            items_html += f"<li>{item}</li>\n"
        el["items"] = items_html

    return template.format(**el)


def generate_html(schema):
    """
    Generate full HTML page from schema.
    """
    html = """<!DOCTYPE html>
<html>
<head>
"""

    for el in schema["elements"]["head"]:
        html += render_component("head", el) + "\n"

    html += """</head>
<body>
"""

    for el in schema["elements"]["body"]:
        html += render_component("body", el) + "\n"

    for el in schema["elements"]["footer"]:
        html += render_component("footer", el) + "\n"

    html += """</body>
</html>"""

    return html
