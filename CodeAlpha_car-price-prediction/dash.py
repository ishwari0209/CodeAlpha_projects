import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------------
# Load model and feature names
# -----------------------------
model = joblib.load("car_price_model.pkl")
feature_names = joblib.load("car_features.pkl")

# -----------------------------
# App title
# -----------------------------
st.title("🚗 Car Price Prediction")
st.write("Predict the selling price of a used car using machine learning")

# -----------------------------
# User inputs
# -----------------------------
year = st.number_input(
    "Car Year",
    min_value=1990,
    max_value=2025,
    value=None,
    placeholder="1990 – 2025"
)

present_price = st.number_input(
    "Present Price (in lakhs)",
    min_value=0.0,
    max_value=50.0,
    value=None,
    placeholder="0 – 50"
)

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    max_value=500000,
    value=None,
    placeholder="0 – 500000"
)

owner = st.selectbox(
    "Number of Previous Owners",
    [0, 1, 2, 3]
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)

selling_type = st.selectbox(
    "Seller Type",
    ["Dealer", "Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Price"):

    # Create empty input dataframe with same features as training
    input_df = pd.DataFrame(
        np.zeros((1, len(feature_names))),
        columns=feature_names
    )

    # Fill numeric values
    input_df["Year"] = year
    input_df["Present_Price"] = present_price
    input_df["Driven_kms"] = kms_driven
    input_df["Owner"] = owner

    # One-hot encoded values
    if fuel_type == "Diesel" and "Fuel_Type_Diesel" in input_df.columns:
        input_df["Fuel_Type_Diesel"] = 1

    if selling_type == "Individual" and "Selling_type_Individual" in input_df.columns:
        input_df["Selling_type_Individual"] = 1

    if transmission == "Manual" and "Transmission_Manual" in input_df.columns:
        input_df["Transmission_Manual"] = 1

    # Predict
    price = model.predict(input_df)[0]

    st.success(f"💰 Predicted Selling Price: {price:.2f} lakhs")
