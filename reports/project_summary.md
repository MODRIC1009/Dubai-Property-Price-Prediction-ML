# Dubai Property Price Prediction — Project Summary

## Overview

This project builds a machine learning model to predict residential property prices in Dubai using structural and location-based features. The goal is to demonstrate how data-driven models can support real estate valuation, investment decisions, and pricing strategies.

---

## Dataset

* Source: Bayut property listings dataset
* Total records after cleaning: **17,405 properties**
* Key features used:

  * Bedrooms
  * Bathrooms
  * Property area (sqft)
  * Property type
  * Location

---

## Data Preparation

* Removed missing and invalid values
* Converted numeric columns to correct data types
* Filtered unrealistic price and area outliers
* Encoded categorical variables using one-hot encoding

---

## Models Trained

Two regression models were evaluated:

1. **Linear Regression**
2. **Random Forest Regressor**

---

## Model Performance

| Model             | Mean Absolute Error (MAE) | R² Score |
| ----------------- | ------------------------- | -------- |
| Linear Regression | 954,396 AED               | 0.62     |
| Random Forest     | **456,522 AED**           | **0.82** |

**Best model:** Random Forest Regressor
The final model explains **82% of the variance** in property prices.

---

## Key Business Insights

1. **Bedroom count is the strongest price driver**

   * Contributed over 50% of model importance.
   * Larger properties command significantly higher prices.

2. **Property area is the second most important factor**

   * Accounts for about 20% of pricing influence.

3. **Premium waterfront and central locations drive higher prices**

   * Palm Jumeirah
   * Downtown Dubai
   * Dubai Harbour
   * Bluewaters Island
   * Jumeirah Beach Residence

4. **Luxury property types increase property value**

   * Penthouses show significant price premiums.

5. **Bathroom count also impacts pricing**

   * Indicates demand for comfort and higher-end amenities.

---

## Conclusion

The Random Forest model achieved strong predictive performance and demonstrated that:

* Property size and bedroom count are the primary price drivers.
* Premium locations significantly increase property values.
* Luxury property types command higher prices.

This project shows how machine learning can be applied to:

* Real estate price estimation
* Investment analysis
* Market trend evaluation

---

## Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* Streamlit (for deployment)

---

## Project Outcome

A deployed web application allows users to input property details and receive a predicted price, demonstrating an end-to-end machine learning pipeline from data preprocessing to deployment.
