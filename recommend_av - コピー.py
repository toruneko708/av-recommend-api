import pandas as pd

def recommend_av(keyword: str) -> str:
    df = pd.read_csv("sample_av_data.csv")

    # キーワードでタイトルをフィルタ
    filtered = df[df["タイトル"].str.contains(keyword, na=False)]

    if filtered.empty:
        return "該当する作品は見つかりませんでした💦"

    # 一致した上位3件を返す（例として）
    results = filtered.head(3).to_dict(orient="records")
    output = "\n\n".join([f"🎬 {item['タイトル']}（{item['女優']}, {item['ジャンル']}）" for item in results])
    return output
