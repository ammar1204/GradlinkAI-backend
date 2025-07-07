from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/")
def chatbot(query: str):
    user_input = query.lower()
    if "improve my gpa" in user_input:
        return {"answer": "Attend tutorials, manage your time, study past papers."}
    elif "internship" in user_input:
        return {"answer": "Check Jobberman, LinkedIn, or your department board."}
    elif "career path" in user_input:
        return {"answer": "Try our Career Recommender feature to get a personalized path."}
    else:
        return {"answer": "Sorry, I don't know that yet. Please rephrase your question."}
