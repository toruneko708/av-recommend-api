def recommend_av(keyword):
    # 仮データで検索ワードごとに分岐
    if keyword == "制服":
        return {"result": "制服系でオススメなのは「超絶可愛いJKの制服コレクション💓」だよ！"}
    elif keyword == "ナース":
        return {"result": "ナース系なら「癒しのナースがいっぱい💓看護天国」がおすすめだよ！"}
    elif keyword == "メイド":
        return {"result": "メイド好きのまー君には「極上メイドのご奉仕Time✨」がピッタリだよ💓"}
    else:
        return {"result": f"「{keyword}」については、これからユキちゃんがいっぱい調べるね💓"}
