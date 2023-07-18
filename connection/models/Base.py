from sqlalchemy.ext.declarative import declarative_base, declared_attr


Base = declarative_base()


# モデルのBaseを拡張する際に使用する
# class ModelBase(object):
#     @declared_attr
#     def __tablename__(cls):
#         return cls.__name__.lower()

#     __table_args__ = {'mysql_engine': 'InnoDB'}


# Base = declarative_base(cls=ModelBase)
