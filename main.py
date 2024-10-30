# 必要なライブラリのインポート
from fastapi import FastAPI
from pydantic import BaseModel

# リクエストデータの構造を定義
# データクラスDataは、整数型のxとyの2つのフィールドを持つ
class Data(BaseModel):
    x: int
    y: int

# FastAPIアプリケーションのインスタンスを作成
app = FastAPI()

# ルートエンドポイントを定義（HTTP GETメソッド）
# 「/」にアクセスすると、"Hello Deta!"というメッセージを返す
@app.get('/')
def index():
    return {'message': 'Hello Deta!'}

# 計算エンドポイントを定義（HTTP POSTメソッド）
# リクエストボディで受け取ったDataオブジェクトのxとyを足し算し、その結果を返す
@app.post('/')
def calc(data: Data):
    z = data.x + data.y
    return {'result': z}
