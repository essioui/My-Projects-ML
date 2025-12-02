#!/usr/bin/env python3
"""
Load and preprocess diabetes CSV datasets.
"""
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from outliers_data import remove_outliers_iqr, scale_features_robust

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
    
    if "Diabetes_binary" in df.columns:
        df['Diabetes_012'] = df['Diabetes_binary']

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

    df_selected = df[selected_columns].copy()

    df_selected.rename(columns={
        "Diabetes_012": "diabetes",
        "HighBP": "high_blood_pressure",
        "HighChol": "high_cholesterol",
        "HeartDiseaseorAttack": "heart_disease_or_attack",
        "HvyAlcoholConsump": "heavy_alcohol_consumption",
        "AnyHealthcare": "any_healthcare",
        "GenHlth": "general_health",
        "DiffWalk": "difficulty_walking",
    }, inplace=True)

    print("Missing values:")
    print(df_selected.isnull().sum())

    # remove outliers
    df_clean = remove_outliers_iqr(df_selected, exclude_columns=["diabetes"])

    # scale
    df_scaled = scale_features_robust(df_clean, exclude_columns=["diabetes"])

    return df_scaled
