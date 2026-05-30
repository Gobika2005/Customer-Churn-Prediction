import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_curve,
    roc_auc_score
)

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("data/telco_churn.csv")

print("✅ Dataset Loaded Successfully")

# =========================
# CONVERT TotalCharges
# =========================

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# =========================
# REMOVE MISSING VALUES
# =========================

df.dropna(inplace=True)

print("✅ Missing Values Removed")

# =========================
# REMOVE customerID
# =========================

df.drop("customerID", axis=1, inplace=True)

# =========================
# ENCODING
# =========================

df = pd.get_dummies(
    df,
    drop_first=True
)

print("✅ Encoding Completed")

# =========================
# FEATURES & TARGET
# =========================

X = df.drop("Churn_Yes", axis=1)

y = df["Churn_Yes"]

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("✅ Train-Test Split Completed")

# =========================
# FEATURE SCALING
# =========================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

print("✅ Feature Scaling Completed")

# =========================
# MODEL TRAINING
# =========================

model = LogisticRegression(max_iter=1000)

model.fit(X_train_scaled, y_train)

print("✅ Model Training Completed")

# =========================
# PREDICTION
# =========================

y_pred = model.predict(X_test_scaled)

# Probability scores for ROC Curve
y_prob = model.predict_proba(X_test_scaled)[:, 1]

# =========================
# EVALUATION
# =========================

accuracy = accuracy_score(y_test, y_pred)

print("\n=========================")
print("MODEL EVALUATION")
print("=========================")

print("\n✅ Accuracy Score:")
print(accuracy)

print("\n✅ Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\n✅ Classification Report:")
print(classification_report(y_test, y_pred))

# =========================
# ROC-AUC SCORE
# =========================

auc_score = roc_auc_score(y_test, y_prob)

print("\n✅ ROC-AUC Score:")
print(auc_score)

# =========================
# ROC CURVE
# =========================

fpr, tpr, thresholds = roc_curve(y_test, y_prob)

plt.figure(figsize=(7,5))

plt.plot(
    fpr,
    tpr,
    label=f"AUC = {auc_score:.2f}"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle='--'
)

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.title("ROC Curve")

plt.legend()

plt.show()
# =========================
# Seaborn 
# =========================
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues'
)

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.title("Confusion Matrix")

plt.show()
# =========================
# SAVE FILES
# =========================

joblib.dump(model, "churn_model.pkl")

joblib.dump(scaler, "scaler.pkl")

joblib.dump(X.columns.tolist(), "features.pkl")

print("\n✅ Everything Saved Successfully")