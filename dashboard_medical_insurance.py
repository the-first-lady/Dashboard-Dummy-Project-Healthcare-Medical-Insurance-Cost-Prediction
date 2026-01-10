import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shap

# Load model
model = joblib.load("xgboost_model.pkl")

st.title("Medical Insurance Cost Prediction Dashboard 💡")

# --- Input dari user ---
age = st.number_input("Age", min_value=18, max_value=100, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["Yes", "No"])
sex = st.selectbox("Sex", ["Male", "Female"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# --- Preprocessing input ---
smoker_val = 1 if smoker == "Yes" else 0
sex_val = 1 if sex == "Male" else 0
region_map = {"northeast":0, "northwest":1, "southeast":2, "southwest":3}
region_val = region_map[region]

features = np.array([[age, bmi, children, smoker_val, sex_val, region_val]])

# --- Prediksi ---
if st.button("Predict Insurance Cost"):
    prediction = model.predict(features)
    st.success(f"Estimated Medical Insurance Cost: ${prediction[0]:,.2f}")

# --- Visualisasi tambahan: Actual vs Predicted ---
st.subheader("Model Performance Visualization")

# Contoh data aktual vs prediksi (dummy untuk demo)
actual = [5000, 10000, 15000, 20000, 25000]
predicted = [5200, 9800, 14800, 21000, 24000]

df = pd.DataFrame({"Actual": actual, "Predicted": predicted})

fig, ax = plt.subplots()
df.plot(kind="bar", ax=ax)
plt.title("Comparison of Actual vs Predicted Costs")
plt.ylabel("Insurance Cost ($)")
st.pyplot(fig)

# --- Visualisasi tambahan: SHAP Feature Importance ---
st.subheader("Feature Importance (SHAP Values)")

explainer = shap.Explainer(model)
shap_values = explainer(features)

fig_shap = shap.plots.bar(shap_values, show=False)
st.pyplot(fig_shap)
