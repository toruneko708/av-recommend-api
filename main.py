from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd
from fastapi.responses import FileResponse
import os

app = FastAPI()


class RecommendRequest(BaseModel):
    keywords: List[str]


@app.post("/recommend")
async def recommend_api(req: RecommendRequest):
    df = pd.read_csv("sample_av_data.csv")

    def match_keywords(row):
        matched = [kw for kw in req.keywords if kw in row["title"]]
        return matched, len(matched)

    df[["matched", "score"]] = df.apply(
        lambda row: pd.Series(match_keywords(row)), axis=1
    )
    df = df[df["score"] > 0].sort_values(by="score", ascending=False)

    return {
        "results": df[["title", "actress", "matched", "score"]].to_dict(orient="records")
    }


@app.get("/")
def read_root():
    return FileResponse(os.path.join("index.html"))
