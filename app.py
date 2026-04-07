import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import os
from datetime import datetime

# ─── 1. Load Resources ───────────────────────────────────────────────────────
@st.cache_resource
def load_resources():
    model = joblib.load('models/maize_yield_ensemble.pkl')
    with open('models/scientific_features.json', 'r') as f:
        scientific_features = json.load(f)
    return model, scientific_features

model, scientific_features = load_resources()

# ─── 2. App Sidebar & Navigation ─────────────────────────────────────────────
st.sidebar.title("🌽 Maize Yield DSS")
page = st.sidebar.radio("Navigate", ["Yield Prediction & Advice", "Pest Reporting"])

# ─── 3. Page: Prediction & Decision Support ──────────────────────────────────
if page == "Yield Prediction & Advice":
    st.header("Yield Prediction & Strategic Advice")
    st.info("Enter basic farm data. The system will calculate complex indices internally.")

    col1, col2 = st.columns(2)
    with col1:
        temp = st.number_input("Average Temperature (°C)", value=28.0)
        precip = st.number_input("Average Rainfall (mm)", value=120.0)
        wind = st.number_input("Average Wind Speed (km/h)", value=8.0)
        ph = st.slider("Soil pH Level", 3.0, 10.0, 6.5)
    with col2:
        clay = st.number_input("Clay Content (%)", 0.0, 100.0, 30.0)
        sand = st.number_input("Sand Content (%)", 0.0, 100.0, 40.0)
        silt = st.number_input("Silt Content (%)", 0.0, 100.0, 30.0)

    if st.button("Generate Forecast & Advice"):
        # Internal Calculation (The "Recipe")
        data = {
            'Average_avg-Temp': temp, 'avg-precipitation': precip, 'avg-windSpeed': wind,
            'PH': ph, 'Clay': clay, 'Sand': sand, 'Silt': silt,
            'Temp_sq': temp**2, 'Rain_sq': precip**2,
            'MSI': temp / (precip + 1e-5),
            'Heat_Water_Stress': temp * (1 / (precip + 1e-5)),
            'Evaporation_Index': (temp * wind) / (precip + 1e-5),
            'Water_Holding': (clay * 0.6 + silt * 0.3 + sand * 0.1) / 100,
            'Rain_Wind_Ratio': precip / (wind + 1e-5),
            'pH_Clay': ph * clay
        }
        
        # Ensure input_df matches scientific_features exactly
        input_df = pd.DataFrame([data])
        for col in scientific_features:
            if col not in input_df.columns: input_df[col] = 0.0
        input_df = input_df[scientific_features]
        
        # 1. PREDICTION
        prediction = model.predict(input_df)[0]
        st.success(f"### Predicted Productivity: {prediction:.2f} MT/Ha")

        # 2. DECISION SUPPORT (Based on your top 0.84 R2 influencers)
        st.subheader("🛠️ Decision Support Analysis")
        advice_col1, advice_col2 = st.columns(2)
        
        with advice_col1:
            if data['Evaporation_Index'] > 1.5:
                st.warning("**High Evaporation Threat**")
                st.write("Recommendation: Implement mulching or cover cropping to retain moisture.")
            else:
                st.write("✅ Evaporation levels are within optimal range.")

        with advice_col2:
            if data['Heat_Water_Stress'] > 0.3:
                st.error("**Heat-Water Stress Warning**")
                st.write("Recommendation: Use drought-tolerant hybrids and adjust planting dates.")
            else:
                st.write("✅ Heat-Water balance is stable.")

# ─── 4. Page: Pest Reporting (Intentionally Preserved) ───────────────────────
elif page == "Pest Reporting":
    st.header("🪲 Pest & Disease Incident Report")
    
    with st.form("pest_form"):
        pest_type = st.selectbox("Observed Pest/Disease", ["Fall Armyworm", "Maize Smut", "Stem Borer", "Other"])
        severity = st.select_slider("Severity Level", options=["Low", "Moderate", "High", "Critical"])
        location = st.text_input("Farm Location/District")
        notes = st.text_area("Additional Observations")
        
        submitted = st.form_submit_button("Submit Report")
        
        if submitted:
            report_data = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Pest": pest_type, "Severity": severity, "Location": location, "Notes": notes
            }
            file_exists = os.path.isfile('pest_reports.csv')
            pd.DataFrame([report_data]).to_csv('pest_reports.csv', mode='a', index=False, header=not file_exists)
            st.success("✅ Report saved to pest_reports.csv.")
