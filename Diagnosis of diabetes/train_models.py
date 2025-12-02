#!/usr/bin/env python3
"""
Train models on multiple CSV files and save the best final model.
Generates: best_diabetes_model.joblib + confusion matrix & classification report
"""

import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import (
    f1_score,
    classification_report,
    confusion_matrix
)
from sklearn.model_selection import train_test_split, GridSearchCV

# MODELS
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier

# DATA
from data_loaded import load_and_preprocess_data


# Model evaluation
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return f1_score(y_test, y_pred, average="weighted", zero_division=0), y_pred


# Hyperparameter grids for different models
param_grids = {
    "Logistic Regression": {
        "model": LogisticRegression(max_iter=2000),
        "params": {"C": [0.1, 1, 5]}
    },

    "SVM (Linear)": {
        "model": LinearSVC(max_iter=2000),
        "params": {"C": [0.1, 1, 5]}
    },

    "Random Forest": {
        "model": RandomForestClassifier(),
        "params": {
            "n_estimators": [100, 200],
            "max_depth": [10, 20, None]
        }
    },

    "XGBoost": {
        "model": XGBClassifier(eval_metric="logloss"),
        "params": {
            "n_estimators": [100, 200],
            "learning_rate": [0.05, 0.1]
        }
    },

    "LightGBM": {
        "model": LGBMClassifier(),
        "params": {
            "n_estimators": [100, 200],
            "learning_rate": [0.05, 0.1]
        }
    },

    "MLP Neural Network": {
        "model": MLPClassifier(max_iter=500),
        "params": {
            "hidden_layer_sizes": [(64, 32)],
            "activation": ["relu"],
            "learning_rate_init": [0.001]
        }
    },
}


# Save classification report and confusion matrix
def save_reports(name, y_test, y_pred):
    # classification report text
    report = classification_report(y_test, y_pred)
    with open("classification_report.txt", "w") as f:
        f.write(report)

    # confusion matrix image
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 6))
    plt.imshow(cm, cmap="Blues")
    plt.title(f"Confusion Matrix: {name}")
    plt.colorbar()
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.savefig("confusion_matrix.png")
    plt.close()


# train on a single file
def train_on_file(filename):
    df = load_and_preprocess_data(filename)

    X = df.drop("diabetes", axis=1)
    y = df["diabetes"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    best_f1 = -1
    best_model = None
    best_name = ""

    for name, cfg in param_grids.items():
        grid = GridSearchCV(
            cfg["model"],
            cfg["params"],
            scoring="f1_weighted",
            cv=3,
            n_jobs=-1,
            verbose=2
        )

        grid.fit(X_train, y_train)

        model = grid.best_estimator_
        f1, y_pred = evaluate_model(model, X_test, y_test)

        print(f"F1 Score = {f1}")

        if f1 > best_f1:
            best_f1 = f1
            best_model = model
            best_name = name

    return best_name, best_f1, best_model, X_test, y_test


# Train with multiple files and select best overall model
def train_with_multiple_files(files):
    final_best_model = None
    final_best_score = -1
    final_best_name = ""
    final_best_file = ""
    final_y_test = None
    final_y_pred = None

    for path in files:
        name, score, model, X_test, y_test = train_on_file(path)

        if score > final_best_score:
            final_best_score = score
            final_best_model = model
            final_best_name = name
            final_best_file = path

            # save predictions for final report
            final_y_pred = model.predict(X_test)
            final_y_test = y_test
            
    print(f"F1 Score: {final_best_score}")

    # save confusion matrix + classification report
    save_reports(final_best_name, final_y_test, final_y_pred)

    # save model
    joblib.dump(final_best_model, "best_diabetes_model.joblib")

    return final_best_name, final_best_file, final_best_score


# Main execution
if __name__ == "__main__":
    csv_files = [
        "diabetes_012_health_indicators_BRFSS2015.csv",
        "diabetes_binary_5050split_health_indicators_BRFSS2015.csv",
        "diabetes_binary_health_indicators_BRFSS2015.csv"
    ]

    train_with_multiple_files(csv_files)
