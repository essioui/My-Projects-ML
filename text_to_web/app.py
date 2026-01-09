#!/usr/bin/env python3
"""
Main application to convert text descriptions into HTML web pages.
"""
import json
from nlp.parser import parser
from generator.html_generator import generate_html
from schema.schema_builder import build_or_update_schema
from generator.file_writer import save_html

schema = None

while True:
    text = input("Describe your page (or 'exit'): ")
    if text.lower() == 'exit':
        break

    intent, entities = parser(text)

    schema = build_or_update_schema(schema, intent, entities)

    print("RAW ENTITIES:", json.dumps(entities, indent=2))


    print("Generated Schema:")
    print(json.dumps(schema, indent=2))

    html = generate_html(schema)
    path = save_html(html)

    print(f"\nHTML file saved to: {path.resolve()}")

