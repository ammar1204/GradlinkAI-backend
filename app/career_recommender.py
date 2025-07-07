from fastapi import APIRouter, Query
import pandas as pd
import joblib

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
    
    # Just an example explanation
    explanation = f"This matches your CGPA ({cgpa}) and interest in {interests} for your {department} department."
    next_steps = ["Take related courses", "Build a portfolio", "Find an internship"]

    return {
        "recommended_career": prediction[0],
        "why": explanation,
        "next_steps": next_steps
    }
