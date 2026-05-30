# Customer Churn Prediction

## Project Overview

This project predicts whether a telecom customer is likely to churn (leave the service) or stay with the company using Machine Learning.

The goal is to help telecom companies identify customers at risk of leaving and take preventive actions to improve customer retention.

---

## Problem Statement

Customer churn is a major challenge for telecom companies. Losing existing customers leads to revenue loss and increased acquisition costs.

This project builds a machine learning model that predicts churn based on customer information and service usage patterns.

---

## Dataset Information

Dataset: Telco Customer Churn Dataset

Total Records: 7043

Features: 21

Target Variable:
- Churn
  - Yes = Customer Left
  - No = Customer Stayed

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Joblib

---

## Project Workflow

1. Data Collection
2. Data Cleaning
3. Missing Value Handling
4. Data Preprocessing
5. Feature Encoding
6. Feature Scaling
7. Train-Test Split
8. Model Training
9. Model Evaluation
10. Model Deployment using Streamlit

---

## Machine Learning Model

Algorithm Used:

- Logistic Regression

Reason:

Logistic Regression is suitable for binary classification problems and provides good interpretability.

---

## Model Performance

Accuracy Achieved:

79%

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Important Features

Top Features Influencing Churn:

- TotalCharges
- MonthlyCharges
- Tenure
- InternetService_Fiber optic
- PaymentMethod_Electronic check

---

## Deployment

The model is deployed using Streamlit.

Run locally:

```bash
streamlit run app.py
```

---

## Project Structure

Customer_Churn_Prediction/

├── app.py

├── train_model.py

├── telco_churn.csv

├── churn_model.pkl

├── scaler.pkl

├── features.pkl

├── requirements.txt

├── README.md

└── screenshots/

---

## Business Impact

This system helps telecom companies:

- Reduce customer churn
- Improve retention
- Identify high-risk customers
- Support data-driven decision making

---

## Author

Gobika