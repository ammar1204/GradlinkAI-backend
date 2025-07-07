from fastapi import FastAPI
from .resource_finder import router as resource_router
from .chatbot import router as chatbot_router
from .career_recommender import router as career_router

app = FastAPI()

app.include_router(resource_router, prefix="/resources")
app.include_router(chatbot_router, prefix="/chatbot")
app.include_router(career_router, prefix="/careers")