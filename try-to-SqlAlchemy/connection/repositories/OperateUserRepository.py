from connection.BaseSession import BaseSession
from connection.models.User import User
from sqlalchemy.orm import Session


class OperateUserRepository(object):

    def __init__(self) -> None:
        self.session: Session = BaseSession.get_session()

    def select_Users(self):
        return self.session.query(User).all()
