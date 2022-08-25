# python-practice-06 - try to SQLAlchemy with python + mysql on docker
## Setup & Run
start and enter docker container
```
docker-compose up -d
docker exec -it try-to-sqlalchemy /bin/bash
```
run python main file
```
python main.py
```

## How to use SQLAlchemy (minimal)
1. make engine
2. make session
3. operate table by using session

## Repositry pattern
![repositry_pattern](https://user-images.githubusercontent.com/99404423/186602292-6259662b-456d-4ee1-b9ea-dc56d9ca3090.png)
* Repositry: Describe the process that needs to connect to the DB. Business logic should not be described.
* each process class: This class that describes the business logic of each process; DB connection processing is separated into Repositry.

## Reference source
* [SQLAlchemyの基本的な使い方](https://qiita.com/arkuchy/items/75799665acd09520bed2)
* [SQLAlchemyの使い方](https://www.wakuwakubank.com/posts/277-python-sqlalchemy/)
* [SQLAlchemyのSession生成方法](https://qiita.com/tosizo/items/86d3c60a4bb70eb1656e)
