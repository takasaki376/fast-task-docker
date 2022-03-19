# イメージのビルド

`$ docker-compose build`

# poetry による Python 環境のセットアップ

```
$ docker-compose run \
  --entrypoint "poetry init \
    --name demo-app \
    --dependency fastapi \
    --dependency uvicorn[standard]" \
  demo-app
```

# FastAPI のインストール

`$ docker-compose run --entrypoint "poetry install" demo-app`

# リビルド

```
docker-compose build --no-cache
```

# 起動

`$ docker-compose up`

# DB 接続　追加インストール

Docker の起動中に実行する
`$ docker-compose exec demo-app poetry add sqlalchemy aiomysql`
\*#### `$ docker-compose exec demo-app poetry add alembic`

_#### 初期ファイルの生成
_#### `$ docker-compose exec demo-app poetry run alembic init api/alembic`

# DB マイグレーション

https://www.sria.co.jp/blog/2021/06/5557/

`$ docker-compose exec demo-app poetry run python -m api.migrate_db`

\*#### `$ docker-compose exec demo-app poetry run alembic revision --autogenerate -m "create tables"`

# ユニットテスト　インストール

`$ docker-compose exec demo-app poetry add -D pytest-asyncio aiosqlite httpx`

# テスト実行

`$ docker-compose exec demo-app poetry run Pytest tests`

# heroku

## ライブラリ　入れ替え

```
docker-compose run --entrypoint "poetry add asyncpg alembic python-dotenv" demo-app
docker-compose run --entrypoint "poetry remove aiomysql" demo-app
docker-compose run --entrypoint "poetry add psycopg2" demo-app
# リビルド
docker-compose build --no-cache
```

## デプロイ

```bash
cd [プロジェクトフォルダ]
heroku create
heroku container:push web
```
