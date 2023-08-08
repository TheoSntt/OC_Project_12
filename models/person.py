from models.base import Base
from sqlalchemy import Column, Integer, String


class Person(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    surname = Column(String(255))
    email = Column(String(255))
    telephone = Column(Integer)

    def __repr__(self):
        return f'{self.name} {self.surname}'
