#!/usr/bin/env python3
"""
"""


def render_title(el):
    """
    """
    return f"<h1 style='text-align:{el['style'].get('align','left')}; color:{el['style'].get('color','black')};'>{el.get('text','Title')}</h1>"


def render_footer(el):
    """
    """
    return f"<footer style='text-align:{el['style'].get('align','center')}; color:{el['style'].get('color','black')};'>{el.get('text','Footer')}</footer>"


def generate_html(schema):
    """
    """
    html = ""
    
    for el in schema["elements"]:
        if el["type"] == "title":
            html += render_title(el)
        elif el["type"] == "footer":
            html += render_footer(el)
    return html
