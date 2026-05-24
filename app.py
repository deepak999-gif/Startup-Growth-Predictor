import streamlit as st
import requests

st.title(" Startup Growth Predictor")

# =========================
# USER INPUTS
# =========================

industry = st.selectbox(
    "Industry",
    ["AI", "FinTech", "HealthTech", "EdTech", "Cybersecurity",
     "E-commerce", "Gaming", "ClimateTech", "Robotics", "SaaS"]
)

founding_year = st.number_input("Founding Year", 2015, 2025, 2021)

city = st.selectbox(
    "City",
    ["Bangalore", "Hyderabad", "Pune", "Delhi", "Mumbai",
     "Chennai", "Kolkata", "Noida", "Ahmedabad", "Jaipur"]
)

employees = st.slider("Employees", 1, 1000, 100)

monthly_active_users = st.number_input(
    "Monthly Active Users",
    1000,
    1000000,
    50000
)

monthly_revenue = st.number_input(
    "Monthly Revenue",
    1000.0,
    10000000.0,
    500000.0
)

monthly_burn_rate = st.number_input(
    "Monthly Burn Rate",
    1000.0,
    10000000.0,
    200000.0
)

funding_raised_usd = st.number_input(
    "Funding Raised USD",
    10000.0,
    100000000.0,
    1000000.0
)

funding_stage = st.selectbox(
    "Funding Stage",
    ["Seed", "Series A", "Series B", "Series C"]
)

business_model = st.selectbox(
    "Business Model",
    ["B2B", "B2C", "Marketplace", "Subscription"]
)

remote_friendly = st.checkbox("Remote Friendly")

customer_rating = st.slider(
    "Customer Rating",
    1.0,
    5.0,
    4.0
)

churn_rate = st.slider(
    "Churn Rate",
    0.0,
    1.0,
    0.10
)

ai_adoption_score = st.slider(
    "AI Adoption Score",
    1,
    100,
    50
)

profitable = st.checkbox("Profitable")

# =========================
# PREDICT BUTTON
# =========================

if st.button("Predict Growth"):

    input_data = {
        "industry": industry,
        "founding_year": founding_year,
        "city": city,
        "employees": employees,
        "monthly_active_users": monthly_active_users,
        "monthly_revenue": monthly_revenue,
        "monthly_burn_rate": monthly_burn_rate,
        "funding_raised_usd": funding_raised_usd,
        "funding_stage": funding_stage,
        "business_model": business_model,
        "remote_friendly": remote_friendly,
        "customer_rating": customer_rating,
        "churn_rate": churn_rate,
        "ai_adoption_score": ai_adoption_score,
        "profitable": profitable
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=input_data
    )

    result = response.json()

    st.success(
        f"Predicted Growth: {result['prediction']}"
    )

    st.info(
        f"Confidence: {result['confidence']}%"
    )