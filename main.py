from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import List
import csv

app = FastAPI()

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

def load_av_data(filename):
    data = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['genres'] = row['genres'].split(',')
            row['keywords'] = row['keywords'].split(',')
            data.append(row)
    return data

def recommend(data, user_keywords):
    recommendations = []
    for entry in data:
        matched_keywords = set(user_keywords) & (set(entry['genres']) | set(entry['keywords']))
        score = len(matched_keywords)
        if score > 0:
            recommendations.append({
                'title': entry['title'],
                'actress': entry['actress'],
                'matched': list(matched_keywords),
                'score': score
            })
    recommendations.sort(key=lambda x: x['score'], reverse=True)
    return recommendations

class RecommendRequest(BaseModel):
    keywords: List[str]

@app.post("/recommend")
async def recommend_api(req: RecommendRequest):
    av_data = load_av_data("sample_av_data.csv")
    results = recommend(av_data, req.keywords)
    return {"results": results}
