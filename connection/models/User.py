from sqlalchemy.types import Integer, String
from sqlalchemy.schema import Column
from .Base import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)

    def full_name(self):
        return "{self.first_name} {self.last_name}"
