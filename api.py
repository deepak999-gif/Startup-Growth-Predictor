from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# =========================
# LOAD MODEL
# =========================

model = joblib.load("model.pkl")

# =========================
# CREATE FASTAPI APP
# =========================

app = FastAPI()

# =========================
# INPUT SCHEMA
# =========================

class StartupInput(BaseModel):
    industry: str
    founding_year: int
    city: str
    employees: int
    monthly_active_users: int
    monthly_revenue: float
    monthly_burn_rate: float
    funding_raised_usd: float
    funding_stage: str
    business_model: str
    remote_friendly: bool
    customer_rating: float
    churn_rate: float
    ai_adoption_score: int
    profitable: bool

# =========================
# HOME ROUTE
# =========================

@app.get("/")
def home():
    return {"message": "Startup Growth Prediction API"}

# =========================
# PREDICTION ROUTE
# =========================

@app.post("/predict")
def predict(data: StartupInput):

    input_data = pd.DataFrame([data.dict()])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data).max()

    return {
        "prediction": prediction,
        "confidence": round(float(probability) * 100, 2)
    }