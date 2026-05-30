import streamlit as st
import pandas as pd
import numpy as np
import joblib

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

# =========================
# LOAD MODEL FILES
# =========================

model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("features.pkl")

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

/* Main Background */
.main {
    background-color: #f5f7fa;
}

/* App Padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

/* Headings */
h1, h2, h3 {
    color: #1f2c56;
    font-weight: bold;
}

/* Button Styling */
.stButton > button {
    width: 100%;
    background-color: #1f77b4;
    color: white;
    border-radius: 12px;
    height: 3.2em;
    font-size: 18px;
    border: none;
    margin-top: 15px;
}

.stButton > button:hover {
    background-color: #125d98;
    color: white;
}

/* Input Styling */
div[data-baseweb="select"] {
    margin-bottom: 20px;
}

.stSlider {
    margin-top: 15px;
    margin-bottom: 25px;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e6e6e6;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
    margin-bottom: 15px;
}

/* Chart Spacing */
.element-container {
    margin-bottom: 25px;
}

/* Alert Boxes */
.stAlert {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================

st.title("📊 Customer Churn Prediction Dashboard")

st.markdown(
    "Predict whether a telecom customer is likely to churn or stay."
)

# =========================
# MAIN LAYOUT
# =========================

left_col, spacer, right_col = st.columns([1, 0.08, 2])

# =====================================================
# LEFT SIDE → INPUT FORM
# =====================================================

with left_col:

    st.subheader("🔍 Predict Customer Churn")

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        12
    )

    monthly_charges = st.slider(
        "Monthly Charges",
        0,
        150,
        50
    )

    contract = st.selectbox(
        "Contract Type",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    internet_service = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        [
            "Yes",
            "No"
        ]
    )

    # Total Charges
    total_charges = tenure * monthly_charges

    st.info(
        f"💰 Estimated Total Charges: ₹ {total_charges}"
    )

    # Predict Button
    predict_button = st.button("Predict Churn")

# =====================================================
# RIGHT SIDE → DASHBOARD
# =====================================================

with right_col:

    st.subheader("📈 Churn Dashboard")

    # KPI CARDS
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Customers",
            "7043"
        )

    with col2:
        st.metric(
            "Churn Rate",
            "26.5%"
        )

    with col3:
        st.metric(
            "Retention Rate",
            "73.5%"
        )

    st.write("")

    # CHARTS
    chart_col1, chart_col2 = st.columns(2)

    # BAR CHART
    with chart_col1:

        st.subheader("Churn Distribution")

        churn_data = pd.DataFrame({
            "Status": ["Churned", "Stayed"],
            "Customers": [1869, 5174]
        })

        st.bar_chart(
            churn_data.set_index("Status")
        )

    # LINE CHART
    with chart_col2:

        st.subheader("Customer Metrics")

        metrics_data = pd.DataFrame({
            "Category": [
                "Month-to-Month",
                "One Year",
                "Two Year"
            ],
            "Customers": [3875, 1473, 1695]
        })

        st.line_chart(
            metrics_data.set_index("Category")
        )

# =========================
# PREDICTION SECTION
# =========================

if predict_button:

    input_df = pd.DataFrame(
        np.zeros((1, len(feature_columns))),
        columns=feature_columns
    )

    # Numerical Features
    input_df["tenure"] = tenure
    input_df["MonthlyCharges"] = monthly_charges
    input_df["TotalCharges"] = total_charges

    # Contract Encoding
    if contract == "One year":
        input_df["Contract_One year"] = 1

    elif contract == "Two year":
        input_df["Contract_Two year"] = 1

    # Internet Service Encoding
    if internet_service == "Fiber optic":
        input_df["InternetService_Fiber optic"] = 1

    elif internet_service == "No":
        input_df["InternetService_No"] = 1

    # Paperless Billing Encoding
    if paperless_billing == "Yes":
        input_df["PaperlessBilling_Yes"] = 1

    # Scaling
    scaled_input = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(scaled_input)

    probability = model.predict_proba(
        scaled_input
    )[0][1]

    st.write("")

    st.subheader("📊 Prediction Result")

    risk_score = probability * 100

    # Progress Bar
    st.progress(int(risk_score))

    # =========================
    # CHURN RESULT
    # =========================

    if prediction[0] == 1:

        st.error("⚠️ Customer is likely to Churn")

        st.metric(
            "Churn Probability",
            f"{risk_score:.2f}%"
        )

        # Risk Levels
        if risk_score > 80:

            st.error("🔴 High Churn Risk")

        elif risk_score > 60:

            st.warning("🟠 Medium Churn Risk")

        else:

            st.info("🟡 Low Churn Risk")

    # =========================
    # STAY RESULT
    # =========================

    else:

        retention_score = (1 - probability) * 100

        st.success("✅ Customer is likely to Stay")

        st.metric(
            "Retention Probability",
            f"{retention_score:.2f}%"
        )

        # Retention Strength
        if retention_score > 80:

            st.success("🟢 Strong Retention Probability")

        elif retention_score > 60:

            st.info("🔵 Moderate Retention Probability")

        else:

            st.warning("🟡 Weak Retention Probability")

# =========================
# BUSINESS INSIGHTS
# =========================

st.write("")

st.subheader("📌 Business Insights")

st.info("""
• Customers with month-to-month contracts show higher churn risk.

• Customers with higher monthly charges are more likely to leave.

• Long-term contracts improve customer retention significantly.

• Paperless billing customers tend to churn more frequently.

• Fiber optic users have comparatively higher churn rates.
""")

# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "Machine Learning Project using Logistic Regression and Streamlit"
)