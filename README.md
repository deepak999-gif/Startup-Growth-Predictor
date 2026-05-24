# 🚀 AI Startup Growth Predictor

An end-to-end Machine Learning application that predicts the growth category of startups using business and operational metrics.

This project combines **Data Analytics + Machine Learning + FastAPI + Streamlit** to build a complete prediction system.

---

## 📌 Project Overview

This application predicts whether a startup belongs to one of the following categories:

- 🟢 High Growth
- 🟡 Medium Growth
- 🔴 Low Growth

The prediction is generated using startup-related business indicators such as revenue, customer behavior, funding information, workforce size, and operational characteristics.

The project demonstrates how raw business data can be transformed into a production-style prediction system.

---

## 🎯 Objectives

- Perform feature engineering on startup data
- Train a machine learning classification model
- Build REST APIs using FastAPI
- Create an interactive frontend using Streamlit
- Serve real-time predictions

---

# 🧠 Machine Learning Pipeline

Dataset  
↓  
Feature Engineering  
↓  
Feature Selection  
↓  
Encoding  
↓  
Model Training  
↓  
Model Evaluation  
↓  
Model Serialization (.pkl)  
↓  
FastAPI Backend  
↓  
Streamlit Frontend  

---

## 🗂 Dataset Features

The model uses startup-related attributes:

| Feature | Description |
|---------|-------------|
| industry | Startup industry |
| founding_year | Startup founding year |
| city | Operating city |
| employees | Number of employees |
| monthly_active_users | Monthly active users |
| monthly_revenue | Revenue generated monthly |
| monthly_burn_rate | Monthly expenditure |
| funding_raised_usd | Total funding raised |
| funding_stage | Investment stage |
| business_model | B2B / B2C / Subscription |
| remote_friendly | Remote work enabled |
| customer_rating | Customer satisfaction |
| churn_rate | Customer loss percentage |
| ai_adoption_score | AI integration score |
| profitable | Profitability status |

Target Variable:

```text
growth_level
```

Classes:
- High
- Medium
- Low

---

## ⚙️ Tech Stack

### Data Processing
- Python
- Pandas
- NumPy

### Machine Learning
- Scikit-learn
- Random Forest Classifier
- Joblib

### Backend
- FastAPI
- Uvicorn

### Frontend
- Streamlit

---

## 📁 Project Structure

```text
startup-growth-predictor/
│
├── app.py
├── api.py
├── startup_growth_model.pkl
├── ai_startup_ecosystem_dataset.csv
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone repository:

```bash
git clone <your-repo-url>
```

Move into project:

```bash
cd startup-growth-predictor
```

Create virtual environment:

### Windows
```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶ Run FastAPI

Start backend:

```bash
uvicorn api:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# ▶ Run Streamlit

Open second terminal:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📡 API Endpoint

### Predict Startup Growth

**POST**

```text
/predict
```

Request:

```json
{
  "industry": "AI",
  "founding_year": 2021,
  "city": "Bangalore",
  "employees": 150,
  "monthly_active_users": 200000,
  "monthly_revenue": 2000000,
  "monthly_burn_rate": 500000,
  "funding_raised_usd": 10000000,
  "funding_stage": "Series B",
  "business_model": "B2B",
  "remote_friendly": true,
  "customer_rating": 4.8,
  "churn_rate": 0.03,
  "ai_adoption_score": 95,
  "profitable": true
}
```

Response:

```json
{
  "prediction": "High",
  "confidence": 92.4
}
```

---

## 📈 Model Performance

Evaluation Metrics:

- Precision
- Recall
- F1 Score

Final Results:

```text
High     Precision: 1.00 | Recall: 0.66
Low      Precision: 0.95 | Recall: 0.80
Medium   Precision: 0.85 | Recall: 0.98
```

---

## 💡 Key Learnings

- Feature engineering
- Classification modeling
- Model serialization
- API development
- JSON communication
- ML deployment workflow
- Frontend integration

---

## 🔮 Future Improvements

- Add model explainability
- Docker containerization
- Database integration
- Cloud deployment
- Authentication
- Analytics dashboard
- Prediction history

---

## 👨‍💻 Author

Desh Deepak Pal

Built as a portfolio project to explore:

Data Analytics • Machine Learning • FastAPI • Streamlit
