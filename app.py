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
area_sqft = st.number_input(
    "Area (sqft)",
    min_value=200,
    max_value=10000,
    value=1000,
    step=50
)

property_type = st.selectbox(
    "Property Type",
    ["Apartment", "Villa", "Townhouse", "Penthouse"]
)

# Extract location names from model columns
location_columns = [
    col.replace("location_", "")
    for col in model_columns
    if col.startswith("location_")
]

location = st.selectbox(
    "Location",
    sorted(location_columns)
)

# Create base input with zeros
input_data = pd.DataFrame(0, index=[0], columns=model_columns)

# Set numeric features
input_data["bedrooms"] = bedrooms
input_data["bathrooms"] = bathrooms
input_data["area_sqft"] = area_sqft

# Set property type column
prop_col = f"property_type_{property_type}"
if prop_col in input_data.columns:
    input_data[prop_col] = 1

# Set location column
loc_col = f"location_{location}"
if loc_col in input_data.columns:
    input_data[loc_col] = 1

if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Property Price: AED {prediction:,.0f}")