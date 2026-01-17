#!/usr/bin/env python3
"""
Streamlit UI for NLP-driven Text-to-HTML Generator
"""

import json
from pathlib import Path
import streamlit as st

from nlp.parser import parser
from generator.html_generator import generate_html
from generator.file_writer import save_html


OUTPUT_HTML = Path("generator/output/index.html")


def merge_entity(schema, section, el_type, el):
    """
    Merge parsed entity into schema safely.
    Supports full update and style-only update.
    """
    if el_type in schema[section]:

        if "text" in el:
            schema[section][el_type]["text"] = el["text"]

        if "style" in el:
            schema[section][el_type].setdefault("style", {})
            schema[section][el_type]["style"].update(el["style"])
    else:
        schema[section][el_type] = el


# ---------- Streamlit App ----------

st.set_page_config(
    page_title="NLP → HTML Generator",
    layout="wide"
)

st.title("NLP-Driven Text-to-HTML Generator")

# ---------- Session State ----------
if "schema" not in st.session_state:
    st.session_state.schema = {"head": {}, "body": {}, "footer": {}}

if "history" not in st.session_state:
    st.session_state.history = []


# ---------- Layout ----------
col_input, col_preview = st.columns(2)


# ---------- LEFT COLUMN ----------
with col_input:
    st.subheader("NLP Input")

    with st.form(key="nlp_form", clear_on_submit=True):
        user_text = st.text_area(
            "Enter your instructions here...",
            height=200
        )

        submitted = st.form_submit_button("Generate / Update")

    if submitted and user_text.strip():

        intent, entities = parser(
            user_text,
            schema=st.session_state.schema
        )

        for section in entities:
            for el_type, el in entities[section].items():
                if section == "head" and "style" in el:
                    continue

                merge_entity(
                    st.session_state.schema,
                    section,
                    el_type,
                    el
                )

        html = generate_html(st.session_state.schema)
        save_html(html)

        st.session_state.history.append({
            "input": user_text,
            "entities": entities
        })

    st.divider()

    st.subheader("Current Schema")
    st.json(st.session_state.schema)

    


# ---------- RIGHT COLUMN ----------
with col_preview:
    st.subheader("Live HTML Preview")

    if OUTPUT_HTML.exists():
        html_content = OUTPUT_HTML.read_text(encoding="utf-8")

        st.components.v1.html(
            html_content,
            height=800,
            scrolling=True
        )
    else:
        st.info("HTML file not generated yet.")
