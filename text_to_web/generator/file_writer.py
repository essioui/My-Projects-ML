#!/usr/bin/env python3
"""
HTML File Writer
"""
from pathlib import Path


OUTPUT_DIR = Path("generator/output")


def save_html(html, filename="index.html"):
    """
    Save generated HTML to a file.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    path = OUTPUT_DIR / filename
    path.write_text(html, encoding="utf-8")

    return path
