#!/usr/bin/env python3
"""
"""
import json
from nlp.parser import parser
from generator.html_generator import generate_html
from generator.file_writer import save_html

text = input("Describe your page: ")

intent, entities = parser(text)

schema = {
    "intent": intent,
    "elements": entities
}

print("Generated Schema:", json.dumps(schema, indent=2))

html = generate_html(schema)

path = save_html(html)

print(f"\nHTML file saved to: {path.resolve()}")

