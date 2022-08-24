# python-practice-06 - try to SQLAlchemy with python + mysql on docker
## Setup & Run
db/dataフォルダ作成
dockerコンテナを起動
```
docker-compose up -d
```

dockerコンテナに入る
```
docker exec -it try-to-sqlalchemy /bin/bash
```

python実行
```
python main.py
```

## Reference source
* [SQLAlchemyの基本的な使い方](https://qiita.com/arkuchy/items/75799665acd09520bed2)
