from connection.BaseSession import BaseSession
from connection.models.User import User
from sqlalchemy.orm import Session


class UserRepository(object):

    def __init__(self) -> None:
        self.session: Session = BaseSession.get_session()

    def get_all_users(self):
        return self.session.query(User).all()
