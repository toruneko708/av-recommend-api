from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd
from recommend_av import recommend_av

app = FastAPI()

# staticディレクトリをマウント
app.mount("/static", StaticFiles(directory="static"), name="static")

# ルートにアクセスすると index.html を表示
@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

# レコメンドAPI（仮のデータで動作）
@app.get("/recommend")
async def get_recommendation(keyword: str):
    results = recommend_av(keyword)
    return results
