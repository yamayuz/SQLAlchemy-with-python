from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.User import User

# DBエンジンの作成
engine = create_engine("mysql+pymysql://root:root@mysql:3306/db?charset=utf8mb4")

# テーブル作成(初回起動時のみ)
#Base.metadata.create_all(bind=engine)

# sessionの作成
SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
session = SessionClass()

# insert(初回起動時のみ)
#user_a = User(first_name="first_a", last_name="last_a", age=20)
#session.add(user_a)
#session.commit()

users = session.query(User).all()
print(users[0].first_name)