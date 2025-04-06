from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

# 🔹 静的ファイル（画像・HTML）の公開設定
app.mount("/static", StaticFiles(directory="."), name="static")

# 🔹 ルートで index.html を返す
@app.get("/")
async def read_index():
    return FileResponse("index.html")

# 🔹 リクエストボディ用モデル
class RecommendRequest(BaseModel):
    keywords: list[str]

# 🔹 推薦ロジックのエンドポイント
@app.post("/recommend")
async def recommend_api(recommend_request: RecommendRequest):
    df = pd.read_csv("sample_av_data.csv")
    keywords = recommend_request.keywords

    # 🔍 検索ワードにヒットするデータをフィルタ
    filtered_df = df[df.apply(lambda row: any(kw in str(row).lower() for kw in keywords), axis=1)]

    # 上位5件を返す（なければ空）
    return filtered_df.head(5).to_dict(orient="records")
