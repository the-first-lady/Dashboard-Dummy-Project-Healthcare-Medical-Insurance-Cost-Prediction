import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Judul dashboard
st.title("Medical Insurance Cost Prediction 🏥")

# Load model dengan caching
@st.cache_resource
def load_model():
    return joblib.load("xgboost_model.pkl")

model = load_model()

# Input user
age = st.slider("Age", 18, 65, 30)
bmi = st.slider("BMI", 15.0, 40.0, 22.5)
children = st.number_input("Number of Children", 0, 5, 0)
smoker = st.selectbox("Smoker", ["yes", "no"])
sex = st.selectbox("Sex", ["male", "female"])

# Encode input sederhana (contoh)
smoker_val = 1 if smoker == "yes" else 0
sex_val = 1 if sex == "male" else 0

X_new = pd.DataFrame([[age, bmi, children, smoker_val, sex_val]],
                     columns=["age", "bmi", "children", "smoker", "sex"])

# Prediksi
prediction = model.predict(X_new)[0]
st.success(f"Estimated Insurance Cost: ${prediction:,.2f}")
