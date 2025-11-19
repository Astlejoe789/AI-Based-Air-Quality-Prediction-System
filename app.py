import streamlit as st
import pandas as pd
import joblib

st.title("🌱 AI-Based Air Quality Prediction System")
st.write("Enter pollutant levels to predict AQI")

# Load final model
model = joblib.load("final_small_model.pkl")

# UI Inputs (ALL features used during training)
PM25 = st.number_input("PM2.5", min_value=0.0)
PM10 = st.number_input("PM10", min_value=0.0)
NO = st.number_input("NO", min_value=0.0)
NO2 = st.number_input("NO2", min_value=0.0)
NOx = st.number_input("NOx", min_value=0.0)
NH3 = st.number_input("NH3", min_value=0.0)
CO = st.number_input("CO", min_value=0.0)
SO2 = st.number_input("SO2", min_value=0.0)
O3 = st.number_input("O3", min_value=0.0)
Benzene = st.number_input("Benzene", min_value=0.0)
Toluene = st.number_input("Toluene", min_value=0.0)
Xylene = st.number_input("Xylene", min_value=0.0)

# Create input data in EXACT same order as training
input_data = pd.DataFrame([[
    PM25, PM10, NO, NO2, NOx, NH3, CO, SO2, O3, Benzene, Toluene, Xylene
]], columns=[
    "PM2.5", "PM10", "NO", "NO2", "NOx", "NH3", "CO", "SO2",
    "O3", "Benzene", "Toluene", "Xylene"
])

if st.button("Predict AQI"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted AQI: {prediction:.2f}")
