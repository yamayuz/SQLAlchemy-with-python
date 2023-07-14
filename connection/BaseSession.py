from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from config.settings import MYSQL_CONF
from typing import Optional


class BaseEngine(object):
    host: Optional[str] = MYSQL_CONF['host']
    port: Optional[str] = MYSQL_CONF['port']
    username: Optional[str] = MYSQL_CONF['username']
    password: Optional[str] = MYSQL_CONF['password']
    dbname: Optional[str] = MYSQL_CONF['database']
    mysql_url: str = "mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}?charset=utf8mb4".format(
        username=username, password=password, host=host, port=port, dbname=dbname)
    engine = create_engine(mysql_url)


class BaseSession(BaseEngine):

    def __init__(self):
        session = sessionmaker(
                autocommit=False,
                autoflush=True,
                bind=self.engine
            )
        self.session = session()

    @classmethod
    def get_session(cls) -> Session:
        return cls().session
