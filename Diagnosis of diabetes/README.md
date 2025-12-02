# Diabetes Prediction Project

This project predicts diabetes risk based on health indicators using machine learning models. It also provides a simple **BMI calculator** and a web interface built with **Streamlit** for interactive predictions.

---

## Project Structure

```text
.
├── app.py                  # Streamlit web application for predictions
├── outliers_data.py        # Utilities to remove outliers and scale features
├── data_loaded.py          # Load and preprocess CSV datasets
├── train_models.py         # Train multiple ML models and save the best one
├── data/                   # Folder to store CSV datasets
└── best_diabetes_model.joblib # Saved trained model
```

---

## File Descriptions

### 1. `outliers_data.py`

- **Purpose:** Handle outliers and scale numeric features.
- **Functions:**
  - `remove_outliers_iqr(df, exclude_columns)`: Removes outliers using the Interquartile Range (IQR) method.
  - `scale_features_robust(df, exclude_columns)`: Scales features using `RobustScaler`, excluding target columns.

### 2. `data_loaded.py`

- **Purpose:** Load and preprocess diabetes CSV datasets.
- **Steps:**
  - Select relevant columns.
  - Rename columns for clarity.
  - Remove outliers.
  - Scale numeric features.
- **Returns:** A cleaned and scaled `pandas.DataFrame`.

### 3. `train_models.py`

- **Purpose:** Train multiple classification models on CSV datasets and select the best model.
- **Models Used:**
  - Logistic Regression
  - Linear SVM
  - Random Forest
  - XGBoost
  - LightGBM
  - MLP Neural Network
- **Output:**
  - `best_diabetes_model.joblib` (best trained model)
  - Confusion matrix (`confusion_matrix.png`)
  - Classification report (`classification_report.txt`)

### 4. `app.py`

- **Purpose:** Streamlit web app for predicting diabetes risk.
- **Features:**
  - Inputs for health indicators (blood pressure, cholesterol, BMI, smoker, etc.).
  - BMI calculator.
  - Predict probability of diabetes using trained model.
  - Display risk level (`Low`, `Moderate`, `High`).
  - Interactive bar chart showing risk percentage.

---

## How to Run

1. **Install dependencies**

2. **Train the model**
   python train_models.py

3. **Run the Streamlit app**
   streamlit run app.py

4. **Open the browser at the URL shown in the terminal**
   - Local URL: http://localhost:8501
   - Network URL: http://192.168.1.57:8501

## Datasets

- diabetes_012_health_indicators_BRFSS2015.csv

- diabetes_binary_5050split_health_indicators_BRFSS2015.csv

- diabetes_binary_health_indicators_BRFSS2015.csv

## Usage

Enter health indicators in the Streamlit app.

The model calculates diabetes risk probability.

A color-coded bar chart shows the risk:

Green: Low risk

Orange: Moderate risk

Red: High risk

## Notes

The project uses outlier removal and robust scaling to improve model performance.

Multiple ML models are trained; the best one is selected based on F1-score.

Works for binary classification (diabetic / non-diabetic).

              precision    recall  f1-score   support

         0.0       0.92      0.99      0.95     28867
         1.0       0.48      0.05      0.09      2800

    accuracy                           0.91     31667

macro avg 0.70 0.52 0.52 31667
weighted avg 0.88 0.91 0.88 31667

## License

This project is open-source and free to use.
