import streamlit as st
import requests

st.title("📊 Customer Churn Prediction")

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 24)
phone = st.selectbox("Phone Service", ["Yes", "No"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
monthly = st.number_input("Monthly Charges", value=70.0)
total = st.number_input("Total Charges", value=2000.0)

# Prediction
if st.button("Predict Churn"):
    data = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "InternetService": internet,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }
    response = requests.post("http://localhost:8000/predict", json=data)
    if response.status_code == 200:
        churn = response.json()['churn']
        st.success(f"Prediction: {'⚠️ Churn' if churn else '✅ Not Churn'}")
    else:
        st.error("Prediction failed.")
