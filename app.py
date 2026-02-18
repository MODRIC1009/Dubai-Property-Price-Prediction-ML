import streamlit as st
import pandas as pd
import joblib

st.title("Dubai Property Price Predictor")

# Load model and columns
model = joblib.load("model.pkl")
model_columns = joblib.load("model_columns.pkl")

# User inputs
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=2)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
area_sqft = st.number_input("Area (sqft)", min_value=200, max_value=10000, value=1000)

property_type = st.selectbox(
    "Property Type",
    ["Apartment", "Villa", "Townhouse", "Penthouse"]
)

location = st.selectbox(
    "Location",
    ["Downtown Dubai", "Palm Jumeirah", "Business Bay", "Dubai Marina"]
)

# Create input dataframe
input_data = pd.DataFrame({
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "area_sqft": [area_sqft],
    "property_type": [property_type],
    "location": [location]
})

# Convert to dummies
input_data = pd.get_dummies(input_data)

# Align with training columns
input_data = input_data.reindex(columns=model_columns, fill_value=0)

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Property Price: AED {prediction:,.0f}")
