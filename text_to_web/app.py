#!/usr/bin/env python3
"""
"""
from nlp.intent_detector import detect_intent
from nlp.entity_extractor import extract_entities
from schema.schema_builder import build_schema
from generator.html_generator import generate_html

text = input("Describe your page: ")

intent = detect_intent(text)
entities = extract_entities(text)
schema = build_schema(intent, entities)

html = generate_html(schema)
print(html)
