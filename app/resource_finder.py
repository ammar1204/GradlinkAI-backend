from fastapi import APIRouter, Query
from sentence_transformers import SentenceTransformer, util
import json

router = APIRouter()

with open("data_dummy.json") as f:
    courses_data = json.load(f)

model_semantic = SentenceTransformer("all-MiniLM-L6-v2")
course_texts = []
course_map = {}
for i, course in enumerate(courses_data):
    combined = f"{course['course_code']} {course['course_title']} {course['course_description']}"
    course_texts.append(combined)
    course_map[i] = course
course_embeddings = model_semantic.encode(course_texts, convert_to_tensor=True, show_progress_bar=True)

@router.get("/")
def find_resources(query: str, top_k: int = 3, threshold: float = 0.3):
    query_embedding = model_semantic.encode(query, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(query_embedding, course_embeddings)[0]
    top_indices = scores.argsort(descending=True)[:top_k].cpu().numpy()
    results = []
    for idx in top_indices:
        similarity = scores[idx].item()
        if similarity >= threshold:
            course = course_map[idx]
            results.append({
                "course_code": course["course_code"],
                "course_title": course["course_title"],
                "similarity_score": round(similarity, 4),
                "resources": course["resources"]
            })
    return results
