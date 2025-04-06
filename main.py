from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI()

# CORS設定（フロントからの呼び出し許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# データの読み込み
df = pd.read_csv("sample_av_data.csv")

@app.get("/")
async def root():
    # index.html を返す
    return FileResponse("index.html")

@app.post("/recommend")
async def recommend(request: Request):
    try:
        body = await request.json()
        keywords = body.get("keywords", [])
        print("📥 受信したキーワード:", keywords)

        if not keywords:
            return JSONResponse(content={"results": []})

        # 検索処理：キーワードすべてを含む作品を抽出（部分一致）
        def is_match(title):
            return all(keyword in title for keyword in keywords)

        matched = df[df["title"].apply(is_match)]

        # 結果を辞書に変換
        results = matched[["title", "actress", "genre"]].to_dict(orient="records")
        print("📤 検索結果:", results)

        return JSONResponse(content={"results": results})
    except Exception as e:
        print("❌ エラー:", str(e))
        return JSONResponse(status_code=500, content={"error": str(e)})
