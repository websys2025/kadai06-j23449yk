# オープンデータ名：気象庁 天気予報データ（オープンデータ）
# 概要：気象庁が提供する地方ごとの天気予報（当日～数日分）をJSON形式で取得できる
# エンドポイント：https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json
# エリアコード：130000 → 東京都地方（東京、千葉、神奈川、埼玉）
# 機能：指定地域の天気予報

# 使い方：　
# - requestsでAPIにGETアクセス
# - JSONとして読み込み
# - 地域名と天気の情報を抽出・整形して表示

import requests
import json

url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
response = requests.get(url)
weather_data = response.json()

for area in weather_data[0]['timeSeries'][0]['areas']:
    name = area['area']['name']
    weather = area['weathers']
    print(f"【{name}】")
    for i, forecast in enumerate(weather):
        print(f"  - 予報{i+1}: {forecast}")
