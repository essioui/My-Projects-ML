#!/usr/bin/env python3
"""
Main application to convert text descriptions into HTML web pages.
"""
import json
from nlp.parser import parser
from generator.html_generator import generate_html
from generator.file_writer import save_html

schema = None

while True:
    text = input("Describe your page (or 'exit'): ")
    if text.lower() == 'exit':
        break

    intent, entities = parser(text, schema=schema)

    if schema is None:
        schema = {"head": {}, "body": {}, "footer": {}}

    for section in entities:
        for el in entities[section]:
            el_type = el.get("type")

            if el_type in schema[section]:
                if "text" in el:
                    schema[section][el_type]["text"] = el["text"]
                if "style" in el:
                    schema[section][el_type].setdefault("style", {})
                    schema[section][el_type]["style"].update(el["style"])
            else:
                schema[section][el_type] = el

    print("RAW ENTITIES:", json.dumps(entities, indent=2))
    print("Generated Schema:", json.dumps(schema, indent=2))

    html = generate_html(schema)
    path = save_html(html)
    print(f"\nHTML file saved to: {path.resolve()}")
