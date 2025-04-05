import csv

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

if __name__ == "__main__":
    # 仮のユーザー好み
    user_input = input("好みのキーワードをカンマ区切りで入力してください（例: 制服,痴漢）: ")
    user_keywords = [kw.strip() for kw in user_input.split(',')]

    av_data = load_av_data("sample_av_data.csv")
    results = recommend(av_data, user_keywords)

    if not results:
        print("該当する作品が見つかりませんでした。")
    else:
        print("\nおすすめ作品リスト:\n")
        for i, item in enumerate(results, start=1):
            print(f"{i}. {item['title']}（女優: {item['actress']}）")
            print(f"   一致キーワード: {', '.join(item['matched'])} / スコア: {item['score']}\n")
