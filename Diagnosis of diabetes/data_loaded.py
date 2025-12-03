#!/usr/bin/env python3
"""
Load and preprocess diabetes dataset.
"""
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_and_preprocess_data(filename):
    """
    Load and preprocess diabetes dataset from a CSV file.
    Parameters:
        filename (str): Name of the CSV file.
    Returns:
        pd.DataFrame: Preprocessed DataFrame.
    """
    data_path = os.path.join(BASE_DIR, "data", filename)

    df = pd.read_csv(data_path)

    # unify diabetes column
    if "Diabetes_binary" in df.columns:
        df["Diabetes_012"] = df["Diabetes_binary"]

    selected_columns = [
        "Diabetes_012",
        "HighBP",
        "HighChol",
        "BMI",
        "Smoker",
        "Stroke",
        "HeartDiseaseorAttack",
        "HvyAlcoholConsump",
        "AnyHealthcare",
        "GenHlth",
        "DiffWalk",
        "Sex",
        "Age",
        "Income",
    ]

    df = df[selected_columns].copy()

    # rename to match Streamlit input
    df.rename(columns={
        "Diabetes_012": "diabetes",
        "HighBP": "high_blood_pressure",
        "HighChol": "high_cholesterol",
        "HeartDiseaseorAttack": "heart_disease_or_attack",
        "HvyAlcoholConsump": "heavy_alcohol_consumption",
        "AnyHealthcare": "any_healthcare",
        "GenHlth": "general_health",
        "DiffWalk": "difficulty_walking",
    }, inplace=True)


    return df
