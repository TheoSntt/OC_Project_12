from models.person import Person
from sqlalchemy import Column, Enum


class Collaborator(Person):
    __tablename__ = 'collaborator'

    # role = Column(String(255))
    role = Column(Enum("administrator", "sales", "support"))
