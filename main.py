from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# CORS設定（GitHub Pagesなど外部からアクセス許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 後で制限してもOK
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

from pydantic import BaseModel
from typing import List

class RecommendRequest(BaseModel):
    keywords: List[str]

@app.post("/recommend")
async def recommend_api(req: RecommendRequest):
    av_data = load_av_data("sample_av_data.csv")
    results = recommend(av_data, req.keywords)
    return {"results": results}

    user_keywords = req_data.get("keywords", [])
    av_data = load_av_data("sample_av_data.csv")
    results = recommend(av_data, user_keywords)
    return {"results": results}

