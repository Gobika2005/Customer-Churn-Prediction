# Customer Churn Prediction & Analytics Dashboard

## Project Overview

This project predicts telecom customer churn using Machine Learning and provides business insights through an interactive Power BI dashboard. Customer churn refers to customers who discontinue a company's services. By identifying customers at risk of leaving, telecom companies can implement retention strategies and reduce revenue loss.

The project combines Data Analysis, Machine Learning, Business Intelligence, and Data Visualization into a complete end-to-end analytics solution.

---

## Problem Statement

Customer retention is a critical challenge in the telecom industry. Acquiring new customers is significantly more expensive than retaining existing ones. The objective of this project is to:

* Predict customers likely to churn.
* Identify key factors influencing churn.
* Provide actionable business insights through dashboards.
* Support data-driven customer retention strategies.

---

## Dataset Information

**Dataset:** Telco Customer Churn Dataset

* Total Customers: 7,043
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

---

## Technologies Used

### Programming & Analytics

* Python
* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* Logistic Regression

### Data Visualization

* Matplotlib
* Seaborn
* Power BI

### Deployment & Version Control

* Streamlit
* Git
* GitHub

---

## Data Preprocessing

The following preprocessing steps were performed:

* Converted TotalCharges from object to numeric datatype
* Handled missing values
* Removed unnecessary columns (customerID)
* Applied One-Hot Encoding to categorical features
* Feature scaling using StandardScaler
* Prepared data for machine learning model training

---

## Machine Learning Model

### Algorithm Used

**Logistic Regression**

### Why Logistic Regression?

* Suitable for binary classification problems
* Computationally efficient
* Easy to interpret
* Strong baseline model for churn prediction

---

## Model Performance

### Accuracy

**78.7%**

### ROC-AUC Score

**0.83**

### Confusion Matrix

| Actual / Predicted | No Churn | Churn |
| ------------------ | -------- | ----- |
| No Churn           | 915      | 118   |
| Churn              | 181      | 193   |

### Classification Metrics

* Precision: 0.62
* Recall: 0.52
* F1 Score: 0.56

---

## Key Factors Influencing Churn

Top features identified by the model:

1. Total Charges
2. Monthly Charges
3. Tenure
4. Fiber Optic Internet Service
5. Electronic Check Payment Method

These features have the strongest impact on customer churn behavior.

---

## Streamlit Application

The trained machine learning model was deployed using Streamlit to provide real-time customer churn predictions.

### Features

* Interactive user interface
* Automatic Total Charges calculation
* Real-time churn prediction
* Customer retention risk analysis
* User-friendly prediction workflow

---

## Power BI Dashboard

An interactive Power BI dashboard was developed to visualize customer churn trends and business insights.

### Dashboard Features

* KPI Cards

  * Total Customers
  * Churned Customers
  * Retained Customers
  * Churn Rate %

* Customer Churn by Contract Type

* Internet Service Analysis

* Customer Retention by Tenure

* Payment Method Analysis

* Interactive Slicers and Filters

### Business Insights

* Overall churn rate is 26.54%.
* Month-to-month customers show the highest churn.
* Electronic check users are more likely to churn.
* Fiber optic customers contribute significantly to churn.
* Customers with shorter tenure are at higher risk of leaving.

---

## Project Structure

```text
Customer-Churn-Prediction/

├── app.py
├── train_model.py
├── requirements.txt
├── README.md

├── data/
│   └── telco_churn.csv

├── models/
│   ├── churn_model.pkl
│   ├── scaler.pkl
│   └── features.pkl

├── screenshots/
│   ├── churn_distribution.png
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   ├── feature_importance.png
│   └── dashboard.png
```

## Future Improvements

* Random Forest Classifier
* XGBoost Classifier
* Hyperparameter Tuning
* Cloud Deployment
* Automated Model Monitoring
* Advanced Customer Segmentation

---

## Conclusion

This project successfully combines Machine Learning and Business Intelligence to predict customer churn and generate actionable insights. The solution helps telecom companies identify at-risk customers, improve retention strategies, and make data-driven business decisions.

---

## Author

**Gobika B**

Aspiring Data Analyst | Machine Learning Enthusiast | Power BI Developer
