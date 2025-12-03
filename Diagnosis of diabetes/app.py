#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# Load trained model and scaler
model = joblib.load("best_diabetes_model.joblib")

st.set_page_config(page_title="Diabetes Prediction App", layout="centered")
st.title("Diabetes Prediction App")
st.write("Smart Health Assessment Using Machine Learning")

st.subheader("Enter Your Health Information")

HighBP = st.selectbox("High Blood Pressure", [0, 1])
HighChol = st.selectbox("High Cholesterol", [0, 1])

st.subheader("BMI Calculator")
weight = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")
height_cm = st.number_input("Height (cm)", min_value=0.0, format="%.2f")

BMI = 0
if weight > 0 and height_cm > 0:
    BMI = weight / ((height_cm / 100) ** 2)
    st.success(f"BMI = {BMI:.2f}")

Smoker = st.selectbox("Smoker", [0, 1])
Stroke = st.selectbox("Stroke", [0, 1])
HeartDiseaseorAttack = st.selectbox("Heart Disease or Heart Attack", [0, 1])
HvyAlcoholConsump = st.selectbox("Heavy Alcohol Consumption", [0, 1])
AnyHealthcare = st.selectbox("Any Healthcare", [0, 1])
GenHlth = st.slider("General Health (1=Excellent → 5=Poor)", 1, 5)
DiffWalk = st.selectbox("Difficulty Walking", [0, 1])
Sex = st.selectbox("Sex (0=Female, 1=Male)", [0, 1])
Age = st.slider("Age Category (1–13)", 1, 13)
Income = st.slider("Income Level (1–8)", 1, 8)

if st.button("Predict"):
    new_person = pd.DataFrame([{
        "high_blood_pressure": HighBP,
        "high_cholesterol": HighChol,
        "BMI": BMI,
        "Smoker": Smoker,
        "Stroke": Stroke,
        "heart_disease_or_attack": HeartDiseaseorAttack,
        "heavy_alcohol_consumption": HvyAlcoholConsump,
        "any_healthcare": AnyHealthcare,
        "general_health": GenHlth,
        "difficulty_walking": DiffWalk,
        "Sex": Sex,
        "Age": Age,
        "Income": Income
    }])


    # Predict probability
    prob = model.predict_proba(new_person)[0][1]

    st.info(f"Probability of Diabetes: {prob*100:.2f}%")

    if prob >= 0.7:
        st.error("High risk of Diabetes")
    elif prob >= 0.4:
        st.warning("Moderate risk of Diabetes")
    else:
        st.success("Low risk of Diabetes")

    # Plot bar chart
    fig = go.Figure(go.Bar(
        x=[prob*100],
        y=["Diabetes Risk"],
        orientation="h",
        text=f"{prob*100:.2f}%",
        textposition="inside",
        marker_color="crimson" if prob >= 0.7 else "orange" if prob >= 0.4 else "green"
    ))
    fig.update_layout(
        xaxis=dict(title="Probability (%)", range=[0, 100]),
        height=200,
        margin=dict(l=20, r=20, t=20, b=20)
    )
    st.plotly_chart(fig)
