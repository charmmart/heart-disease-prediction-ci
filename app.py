import streamlit as st
import pandas as pd
import joblib

model = joblib.load('heart_disease_model.pkl')

st.title("Heart Disease Risk Prediction")
st.write("Enter patient details to predict heart disease risk.")

age = st.number_input("Age", min_value=29, max_value=77, value=54)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox("Chest Pain Type", options=[1, 2, 3, 4])
bp = st.number_input("Resting Blood Pressure (BP)", min_value=94, max_value=200, value=130)
chol = st.number_input("Cholesterol", min_value=126, max_value=564, value=245)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
ekg = st.selectbox("EKG Results", options=[0, 1, 2])
max_hr = st.number_input("Max Heart Rate Achieved", min_value=71, max_value=202, value=153)
angina = st.selectbox("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
st_dep = st.number_input("ST Depression", min_value=0.0, max_value=6.2, value=0.7, step=0.1)
slope = st.selectbox("Slope of ST", options=[1, 2, 3])
vessels = st.selectbox("Number of Vessels Fluro", options=[0, 1, 2, 3])
thallium = st.selectbox("Thallium", options=[3, 6, 7])

if st.button("Predict"):
    input_data = pd.DataFrame([[age, sex, cp, bp, chol, fbs, ekg, max_hr, angina,
                                 st_dep, slope, vessels, thallium]],
                               columns=['Age', 'Sex', 'Chest pain type', 'BP', 'Cholesterol',
                                        'FBS over 120', 'EKG results', 'Max HR', 'Exercise angina',
                                        'ST depression', 'Slope of ST', 'Number of vessels fluro', 'Thallium'])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Prediction: Presence of Heart Disease (Confidence: {probability:.1%})")
    else:
        st.success(f"✅ Prediction: Absence of Heart Disease (Confidence: {1-probability:.1%})")