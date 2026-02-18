Dubai Property Price Prediction using Machine Learning

Overview

This project develops a machine learning model to predict residential property prices in Dubai, utilising structural and location-based features. It demonstrates an end-to-end ML workflow, from data preprocessing and exploratory analysis to model training, evaluation, and deployment as an interactive web application.
The goal is to show how machine learning can support real estate valuation, investment decisions, and pricing strategies in the UAE property market.

Dataset

Source: Bayut property listings dataset

Total records after cleaning: 17,405 properties

Key features used:

1. Bedrooms
2. Bathrooms
3. Property area (sqft)
4. Property type
5. Location
6. Data Preparation
7. Removed missing and invalid values
8. Converted numeric columns to correct data types
9. Filtered unrealistic price and area outliers
10. Encoded categorical variables using one-hot encoding

Models Trained

Two regression models were evaluated:

1. Linear Regression
2. Random Forest Regressor

Model Performance
Model	Mean Absolute Error (MAE)	R² Score
Linear Regression	954,396 AED	0.62
Random Forest	456,522 AED	0.82

Best model: Random Forest Regressor
The final model explains 82% of the variance in property prices.

Key Business Insights

1. Bedroom count is the strongest price driver.
2. Property area is the second most important factor.
3. Premium locations significantly increase property value.
4. Luxury property types such as penthouses command higher prices.
5. Bathroom count also contributes to price variation.

Web Application

The project is deployed as an interactive Streamlit app where users can:

1. Select property type
2. Choose a location
3. Enter bedrooms, bathrooms, and the area
4. Get an instant price prediction

Technologies Used

1. Python
2. Pandas, NumPy
3. Scikit-learn
4. Matplotlib, Seaborn

Project Outcome

1. Built a machine learning model with R² = 0.82
2. Performed full data cleaning and feature engineering
3. Compared multiple regression models
4. Deployed a real-time prediction web app
5. This project demonstrates an end-to-end machine learning pipeline suitable for real estate analytics and pricing applications.

Author

Nihal Lopez

Aspiring Data Scientist
