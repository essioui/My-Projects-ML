#!/usr/bin/env python3
"""
"""
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

data_path = os.path.join(BASE_DIR, "data", "diabetes_012_health_indicators_BRFSS2015.csv")

df = pd.read_csv(data_path)
print(df.columns)
print(df.shape)

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

df_selected = df[selected_columns]
print(df_selected.columns)

