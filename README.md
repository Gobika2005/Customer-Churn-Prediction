# Customer Churn Prediction Using Machine Learning

## Project Overview

This project aims to predict customer churn in a telecom company using Machine Learning. Customer churn refers to customers who stop using a company's services. By identifying customers who are likely to churn, businesses can take proactive measures to improve customer retention.

## Problem Statement

Customer retention is a major challenge in the telecom industry. Losing existing customers impacts revenue and increases customer acquisition costs. The objective of this project is to build a predictive model that can identify customers who are likely to leave the service.

## Dataset Information

* Dataset: Telco Customer Churn Dataset
* Total Records: 7043
* Total Features: 21
* Target Variable: Churn (Yes/No)

### Key Features

* Gender
* SeniorCitizen
* Partner
* Dependents
* Tenure
* MonthlyCharges
* TotalCharges
* InternetService
* Contract
* PaymentMethod

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Streamlit
* Git & GitHub

## Data Preprocessing

The following preprocessing steps were performed:

* Converted TotalCharges from object to numeric format
* Handled missing values
* Removed customerID column
* Applied One-Hot Encoding for categorical variables
* Scaled numerical features using StandardScaler

## Machine Learning Model

### Algorithm Used

Logistic Regression

### Why Logistic Regression?

* Suitable for binary classification
* Fast and efficient
* Easy to interpret
* Strong baseline performance

## Model Performance

### Accuracy

78.7%

### Confusion Matrix

| Actual / Predicted | No Churn | Churn |
| ------------------ | -------- | ----- |
| No Churn           | 915      | 118   |
| Churn              | 181      | 193   |

### Classification Report

* Precision: 0.62
* Recall: 0.52
* F1 Score: 0.56

### ROC-AUC Score

0.83

## Feature Importance

Top features influencing customer churn:

1. TotalCharges
2. MonthlyCharges
3. Tenure
4. InternetService_Fiber optic
5. PaymentMethod_Electronic check

## Streamlit Application

The trained model was deployed using Streamlit to provide real-time customer churn predictions.

### Features

* Interactive user interface
* Automatic Total Charges calculation
* Real-time churn prediction
* Customer retention risk analysis

## Project Structure

Customer-Churn-Prediction/

├── app.py

├── train_model.py

├── requirements.txt

├── README.md

├── data/

│ └── telco_churn.csv

├── models/

│ ├── churn_model.pkl

│ ├── scaler.pkl

│ └── features.pkl

└── screenshots/

## Future Improvements

* Random Forest Classifier
* XGBoost Classifier
* Hyperparameter Tuning
* Power BI Dashboard Integration
* Cloud Deployment

## Conclusion

This project successfully predicts customer churn using Machine Learning techniques and provides a user-friendly Streamlit interface for real-time predictions. The solution can help telecom companies improve customer retention and reduce churn-related losses.

## Author

Gobika
