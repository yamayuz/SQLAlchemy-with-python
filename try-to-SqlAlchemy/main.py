from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

# DBエンジンの作成
engine = create_engine("mysql+pymysql://root:root@mysql:3306/db?charset=utf8mb4")

# モデルクラスの作成
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)

    def full_name(self):
        return "{self.first_name} {self.last_name}"

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