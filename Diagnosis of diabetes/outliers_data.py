#!/usr/bin/env python3
"""
Utilities for handling outliers and scaling in datasets.
- remove_outliers_iqr: Remove outliers using the IQR method.
- scale_features_robust: Scale features using RobustScaler.
"""

import pandas as pd
from sklearn.preprocessing import RobustScaler


def remove_outliers_iqr(df, exclude_columns=None):
    """
    Remove outliers from a DataFrame using the IQR method.
    Parameters:
        df (pd.DataFrame): Input DataFrame.
        exclude_columns (list): Columns to exclude (e.g., target column).
    Returns:
        pd.DataFrame: DataFrame with outliers removed.
    """
    if exclude_columns is None:
        exclude_columns = []

    df_clean = df.copy()

    # select only numeric columns except excluded ones
    numeric_cols = [
        col for col in df_clean.select_dtypes(include=["int64", "float64"]).columns
        if col not in exclude_columns
    ]

    for col in numeric_cols:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        
        df_clean = df_clean[(df_clean[col] >= lower) & (df_clean[col] <= upper)]
        
    return df_clean


def scale_features_robust(df, exclude_columns=None):
    """
    Scale features using RobustScaler, excluding specific columns.
    Parameters:
        df (pd.DataFrame): Input DataFrame.
        exclude_columns (list): Columns NOT to scale.
    Returns:
        pd.DataFrame: Scaled DataFrame.
    """
    if exclude_columns is None:
        exclude_columns = []

    df_copy = df.copy()

    # numeric columns except excluded ones
    num_cols = [
        col for col in df_copy.select_dtypes(include=["int64", "float64"]).columns
        if col not in exclude_columns
    ]

    scaler = RobustScaler()
    df_copy[num_cols] = scaler.fit_transform(df_copy[num_cols])

    return df_copy
