from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd
from recommend_av import recommend_av

app = FastAPI()

# staticディレクトリをマウント
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

@app.get("/recommend")
async def get_recommendation(keyword: str):
    df = pd.read_csv("sample_av_data.csv")
    results = recommend_av(df, keyword)
    return {"results": results}
