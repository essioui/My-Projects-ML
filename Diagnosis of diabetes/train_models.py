#!/usr/bin/env python3
"""
Train ML models on diabetes datasets and save the best model and scaler.
"""
import joblib
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split, GridSearchCV

# Import classifiers
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

# Import gradient boosting libraries
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier

# Import data loading function
from data_loaded import load_and_preprocess_data

def evaluate(model, X_test, y_test):
    """
    Return weighted F1 score
    """
    y_pred = model.predict(X_test)
    return f1_score(y_test, y_pred, average="weighted")


param_grids = {
    "Logistic Regression": {
        "model": LogisticRegression(max_iter=2000),
        "params": {"C": [0.1, 1, 5]},
    },
    "Random Forest": {
        "model": RandomForestClassifier(),
        "params": {
            "n_estimators": [100, 200],
            "max_depth": [10, 20, None],
        },
    },
    "XGBoost": {
        "model": XGBClassifier(eval_metric="logloss"),
        "params": {
            "n_estimators": [100, 200],
            "learning_rate": [0.05, 0.1],
        },
    },
    "LightGBM": {
        "model": LGBMClassifier(),
        "params": {
            "n_estimators": [100, 200],
            "learning_rate": [0.05, 0.1],
        },
    },
    "MLP Neural Network": {
        "model": MLPClassifier(max_iter=500),
        "params": {
            "hidden_layer_sizes": [(64, 32)],
            "activation": ["relu"],
            "learning_rate_init": [0.001],
        },
    },
}


def train_on_file(filename):
    """
    Train models on a single CSV file and return best model + score
    """
    df = load_and_preprocess_data(filename)

    X = df.drop("diabetes", axis=1)
    y = df["diabetes"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
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
            verbose=2,
        )
        grid.fit(X_train, y_train)

        model = grid.best_estimator_
        f1 = evaluate(model, X_test, y_test)

        if f1 > best_f1:
            best_f1 = f1
            best_model = model
            best_name = name

    return best_name, best_f1, best_model


def train_with_multiple(files):
    """
    Train models on multiple datasets and save best global model
    """
    final_best_model = None
    final_best_score = -1
    final_best_name = ""

    for f in files:
        name, score, model = train_on_file(f)

        if score > final_best_score:
            final_best_score = score
            final_best_model = model
            final_best_name = name

    # Save best model
    joblib.dump(final_best_model, "best_diabetes_model.joblib")
    return final_best_name, final_best_score


if __name__ == "__main__":
    csv_files = [
        "diabetes_012_health_indicators_BRFSS2015.csv",
        "diabetes_binary_5050split_health_indicators_BRFSS2015.csv",
        "diabetes_binary_health_indicators_BRFSS2015.csv",
    ]

    best_name, best_score = train_with_multiple(csv_files)
    print("Best model:", best_name)
    print("Best F1 score:", best_score)
