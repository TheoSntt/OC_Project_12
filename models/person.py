from models.base import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint


class UniqueEmailMixin:
    __table_args__ = (
        UniqueConstraint('email', name='uq_email'),
    )


class Person(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    surname = Column(String(255))
    email = Column(String(255), unique=True, nullable=False)
    telephone = Column(String(25))

    def __repr__(self):
        return f'{self.name} {self.surname}'
