from fastapi import APIRouter, Query
import joblib
import pandas as pd

router = APIRouter()

career_model = joblib.load("model.pkl")

@router.get("/")
def recommend_careers(cgpa: float, interests: str, department: str):
    input_data = pd.DataFrame([{
        "cgpa": cgpa,
        "interests": interests,
        "department": department
    }])
    prediction = career_model.predict(input_data)
    return {"recommended_career": prediction[0]}
