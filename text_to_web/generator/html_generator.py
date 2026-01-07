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


def render_component(section, el):
    """
    Render a component with its data.
    """
    template = load_component(section, el["type"])
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
