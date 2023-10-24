import os.path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec
from sqlalchemy import Column, DateTime
from sqlalchemy.types import Integer, String, Boolean

SqlAlchemyBase = dec.declarative_base()
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/data.db')
conn_str = f'sqlite:///{db_path}'


class User(SqlAlchemyBase):
    """Описывает модель общего пользователя"""
    __tablename__ = 'users'
    tg_id = Column(Integer, unique=True, nullable=False, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50))
    registration_date = Column(DateTime)

    def __repr__(self):
        return f"<User (id: {self.id}, name: {self.name}) >"


engine = create_engine(conn_str, echo=False, pool_pre_ping=True)
SqlAlchemyBase.metadata.create_all(engine)
session = Session(engine, autocommit=False)
