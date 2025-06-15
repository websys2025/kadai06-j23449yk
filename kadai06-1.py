import requests

# アプリケーションID（ユーザー個別のAPIキー）
APP_ID = "9728ab69704bfdfada4b5617b936c3b91bc0f3e2"

# APIエンドポイント（e-Stat 統計データ取得用 REST API）
# 今回は「getStatsData」エンドポイントを使用
# 機能：統計データ本体の取得（表形式）
API_URL  = "http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

# APIに渡すパラメータ
params = {
    "appId": APP_ID,  # アプリケーションID
    "statsDataId":"0003420473",  # 統計表ID（取得対象の統計データを指定）
    "cdArea":"12101,12102,12103,12104,12105,12106",  # 地域コード（千葉県内の市を例示）
    "cdCat01": "A1101",  # カテゴリコード（例：総人口など）
    "metaGetFlg":"Y",  # メタ情報（ラベル情報）も取得する
    "cntGetFlg":"N",  # 件数のみ取得するか（"N" はデータを取得する）
    "explanationGetFlg":"Y",  # 統計表の説明情報を取得
    "annotationGetFlg":"Y",  # 注釈データを取得
    "sectionHeaderFlg":"1",  # セクション見出しの表示フラグ
    "replaceSpChars":"0",  # 特殊文字の置換（0: 置換しない）
    "lang": "J"  # 言語（"J": 日本語）
}

# 上記パラメータを付けてAPIへGETリクエストを送信
response = requests.get(API_URL, params=params)

# レスポンス(JSON形式)をPython辞書に変換
data = response.json()

# レスポンス全体を出力（統計データやメタ情報が含まれる）
print(data)
