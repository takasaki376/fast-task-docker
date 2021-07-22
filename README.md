
# イメージのビルド

`$ docker-compose build`

# poetryによるPython環境のセットアップ
```
$ docker-compose run \
  --entrypoint "poetry init \
    --name demo-app \
    --dependency fastapi \
    --dependency uvicorn[standard]" \
  demo-app
```

# FastAPIのインストール

`$ docker-compose run --entrypoint "poetry install" demo-app`

# 起動
`$ docker-compose up`

# DB接続　追加インストール

Dockerの起動中に実行する
`$ docker-compose exec demo-app poetry add sqlalchemy aiomysql`
*#### `$ docker-compose exec demo-app poetry add alembic`

*#### 初期ファイルの生成
*#### `$ docker-compose exec demo-app poetry run alembic init api/alembic`

# DB マイグレーション
https://www.sria.co.jp/blog/2021/06/5557/

`$ docker-compose exec demo-app poetry run python -m api.migrate_db`

*#### `$ docker-compose exec demo-app poetry run alembic revision --autogenerate -m "create tables"`

# ユニットテスト　インストール

`$ docker-compose exec demo-app poetry add -D pytest-asyncio aiosqlite httpx`

# テスト実行

`$ docker-compose exec demo-app poetry run python -m tests.test_main`